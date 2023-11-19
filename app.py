## 包含 Flask 应用的主入口，以及一些基本配置。

from flask import Flask, render_template,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
import pandas as pd
from models import db, test_excel
import flask_login as flask_login
import datetime


app = Flask(__name__) # 创建一个 Flask 应用实例
app.config.from_object(Config) # 从配置对象Config中加载配置项到 Flask 应用。
# db = SQLAlchemy(app) #创建一个 SQLAlchemy 实例，并将 Flask 应用与该数据库实例关联
db.init_app(app)

from view import mod 
app.register_blueprint(mod)

@app.route('/test', methods=['GET', 'POST'])
def test():
    # GET方法调用如下函数
    if request.method == 'GET':
        return render_template('new_file.html')  

        
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
                # 查询单条语句
                existing_data = db.session.query(test_excel).all()
                existing_data_2 = db.session.query(test_excel).filter_by(customer_code = '330101127658').all()

                print(existing_data)
                for index, row in df.iterrows():
                    excel_data = test_excel(
                        customer_code = row.to_dict()['客户编码'], 
                        # market_department =  row.to_dict()['市场部'],
                        customer_manager = row.to_dict()['客户经理'],
                        company_name = row.to_dict()['企业名称'],
                        data_score = row.to_dict()['数采分'],
                        last_upload_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        # 第一次上传数据时，最近修改时间和恢复时间为空
                        last_modified_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),      # 最近修改时间
                        restore_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')   # 恢复时间
                    )   

                    db.session.add(excel_data)
                    db.session.commit()
                # print(existing_data)
                # 文件存到当前目录
                return jsonify({'success': True, 'message': 'File uploaded and data stored in the database'})
            # except SQLAlchemyError as e:
            #     db.session.rollback()
            #     print(traceback.format_exc())  # 添加这行来打印异常堆栈信息
            #     return jsonify({'error': str(e)})
            except Exception as e:
                db.session.rollback()
                # print(traceback.format_exc())  # 添加这行来打印异常堆栈信息
                return jsonify({'error': str(e)})
        else:
            return jsonify({'error': 'Invalid file type'})
        
        
if __name__ == '__main__':
    app.run(debug=True)