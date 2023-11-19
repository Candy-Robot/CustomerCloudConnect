# views.py
from flask import request, jsonify, Blueprint
from models import  db, test_excel
import pandas as pd
from flask import render_template
import datetime
import traceback
from sqlalchemy.exc import SQLAlchemyError

# 目前引入的db没有关联app 需要解决

mod = Blueprint('test',__name__)
@mod.route('/')
def home():
    return 'Welcome to the home page!'


@mod.route('/upload', methods=['GET', 'POST'])
def upload():
    # GET方法调用如下函数
    if request.method == 'GET':
        return render_template('upload.html')  
        
    # POST方法调用下面的函数
    if request.method == 'POST':
        # 返回文件中是否有excelFile
        if 'excelFile' not in request.files:
            return jsonify({'error': 'No file part'})
        # 获取文件
        file = request.files['excelFile']

        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        if file.filename.endswith('.xls') or file.filename.endswith('.xlsx'):
            try:
                df = pd.read_excel(file)
                # 将数据存储到数据库
                for index, row in df.iterrows():
                    customer_code = str(row.to_dict().get('客户编码')) # 遍历到每条的客户编码
                    # 查找数据库中是否有该条编码
                    existing_data = db.session.query(test_excel).filter(test_excel.customer_code==customer_code).first()
                    
                    if existing_data:
                        # 更改最近上传时间
                        existing_data.last_upload_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
                        if existing_data.data_score != row.to_dict()['数采分']: # 数采分不一致的情况
                            # 更改最近数采分变化时间
                            existing_data.last_modified_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        if existing_data.data_score > row.to_dict()['数采分']:
                            # 更改恢复时间 增加90天
                            existing_data.restore_time = (datetime.datetime.now()
                                                          +datetime.timedelta(days=90)).strftime("%Y-%m-%d %H:%M:%S")
                        # 更新数采分
                        existing_data.data_score = row.to_dict()['数采分']
                        db.session.add(existing_data)
                    else:   # 数据库中不存在则新增数据
                        excel_data = test_excel(
                            customer_code = row.to_dict()['客户编码'], 
                            # market_department =  row.to_dict()['市场部'],
                            customer_manager = row.to_dict()['客户经理'],
                            company_name = row.to_dict()['企业名称'],
                            data_score = row.to_dict()['数采分'],
                            # 最近上传时间
                            last_upload_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            # 第一次上传数据时，最近修改时间和恢复时间为空
                            # last_modified_time =      # 最近修改时间
                            # restore_time = db.Column(db.DateTime)   # 恢复时间
                        )   
                        db.session.add(excel_data)
                    db.session.commit()
                return jsonify({'success': True, 'message': '文件成功上传并存储在数据库中'})
            except SQLAlchemyError as e:
                db.session.rollback()
                print(traceback.format_exc())  # 添加这行来打印异常堆栈信息
                return jsonify({'error': str(e)})
            except Exception as e:
                db.session.rollback()
                print(traceback.format_exc())  # 添加这行来打印异常堆栈信息
                return jsonify({'error': str(e)})
        else:
            return jsonify({'error': 'Invalid file type'})
        

