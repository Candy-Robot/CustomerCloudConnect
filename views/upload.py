from models import db, CustomerInformation, InventoryPenaltyDetail, SalesPenaltyDetail, DataScoreAndUploadTime
from flask import request, jsonify, Blueprint
import pandas as pd
import numpy as np
from flask import render_template
import datetime
import traceback
from sqlalchemy.exc import SQLAlchemyError

mod = Blueprint('upload', __name__, url_prefix='/upload')

@mod.route('/')
def index():
    return 'Welcome to the upload page!'

# 初次初始化数据库 只有这里可以添加新数据
# 后续可以添加判断，只有特定的市场部可以加入到数据库中
@mod.route('/init-db', methods=['GET', 'POST'])
def upload():
    # GET方法调用如下函数
    if request.method == 'GET':
        return render_template('init-db.html')  
        
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

                # 遍历所有单元格，将包含'-'的单元格设置为None
                for column in df.columns:
                    df[column] = df[column].apply(lambda x: None if x == '-' else x)
                df.replace({np.nan: None}, inplace=True)
                # 记录新增数据个数和更新数据个数
                newRecordCount = 0
                existRecordCount = 0
                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # 将数据存储到数据库
                for index, row in df.iterrows():
                    
                    customer_code_df = row.to_dict()['客户编码']
                    existing_data = db.session.query(CustomerInformation).filter(CustomerInformation.customer_code==customer_code_df).first()
                    if existing_data is None:

                        newRecordCount += 1
                        # 创建 CustomerInformation 对象并添加到数据库会话
                        customer_info = CustomerInformation(
                            customer_code=customer_code_df,
                            market_department=row.to_dict()['市场部'],
                            customer_manager=row.to_dict()['客户经理'],
                            company_name=row.to_dict()['企业名称'],
                            operator=row.to_dict()['经营者'],
                            level=row.to_dict()['档位'],
                            terminal_hierarchy=row.to_dict()['终端层级'],
                            is_sample_customer=row.to_dict()['是否样本户'],
                            data_collection_method=row.to_dict()['数采方式'],
                            store_name=row.to_dict()['店招名称'],
                            address=row.to_dict()['地址'],
                            data_type=row.to_dict()['数采类型'],
                            location_interval=row.to_dict()['所在区间'],
                        )
                        # 创建 InventoryPenaltyDetail 对象并添加到数据库会话
                        inventory_penalty_detail = InventoryPenaltyDetail(
                            customer_code=customer_code_df,
                            inventory_accuracy = row.to_dict()['盘库准确率'],
                            inventory_count=row.to_dict()['盘库次数'],
                            inspection_accuracy=row.to_dict()['检查准确率'],
                            inspection_count=row.to_dict()['检查次数'],
                            inventory_penalty=row.to_dict()['盘库扣分'],
                            inventory_penalty_time=None,  # 初始化为空
                            inventory_penalty_recovery_time=None,  # 初始化为空
                            inventory_sales_ratio=row.to_dict()['存销比'],
                            inventory_sales_penalty=row.to_dict()['存销比扣分值'],
                            inventory_sales_penalty_time=None,  # 初始化为空
                            inventory_sales_penalty_recovery_time=None,  # 初始化为空
                            negative_inventory=row.to_dict()['负库存'],
                            negative_inventory_penalty=row.to_dict()['负库存扣分项'],
                            negative_inventory_penalty_time=None,  # 初始化为空
                            negative_inventory_penalty_recovery_time=None,  # 初始化为空
                            manual_inventory_changes_count=row.to_dict()['人为修改库存次数'],
                            manual_inventory_changes_penalty=row.to_dict()['人为修改库存次数扣分'],
                            manual_inventory_changes_penalty_time=None,  # 初始化为空
                            manual_inventory_changes_penalty_recovery_time=None  # 初始化为空
                        )

                        # 创建 SalesPenaltyDetail 对象并添加到数据库会话
                        sales_penalty_detail = SalesPenaltyDetail(
                            customer_code=customer_code_df,
                            data_score=row.to_dict()['数采分'],
                            startup_days=row.to_dict()['开机天数'],
                            effective_upload_ratio=row.to_dict()['有效上传比例'],
                            upload_ratio_penalty=row.to_dict()['有效上传比例扣分'],
                            upload_ratio_penalty_time=None,  # 初始化为NULL
                            upload_ratio_recovery_time=None,  # 初始化为NULL
                            sales_days=row.to_dict()['销售天数'],
                            average_sales_duration=row.to_dict()['日均销售时长'],
                            sales_duration_penalty=row.to_dict()['销售时长扣分'],
                            sales_duration_penalty_time=None,  # 初始化为NULL
                            sales_duration_recovery_time=None,  # 初始化为NULL
                            warning_count=row.to_dict()['预警次数'],
                            warning_penalty=row.to_dict()['预警扣分'],
                            warning_penalty_time=None,  # 初始化为NULL
                            warning_recovery_time=None,  # 初始化为NULL
                            centralized_sales_count=row.to_dict()['集中销售次数'],
                            centralized_sales_penalty=row.to_dict()['集中销售次数扣分'],
                            centralized_sales_penalty_time=None,  # 初始化为NULL
                            centralized_sales_recovery_time=None,  # 初始化为NULL
                            delayed_upload_count=row.to_dict()['延迟上传次数'],
                            delayed_upload_penalty=row.to_dict()['延迟上传次数扣分'],
                            delayed_upload_penalty_time=None,  # 初始化为NULL
                            delayed_upload_recovery_time=None,  # 初始化为NULL
                        )
                        # 数采分和最近上传时间
                        data_score_and_upload_time = DataScoreAndUploadTime(
                            customer_code = customer_code_df,    # 客户代码
                            data_score = row.to_dict()['数采分'],   # 数采分
                            last_upload_time = now_time   # 最近上传时间
                        )

                        # 加入数据
                        db.session.add(data_score_and_upload_time)
                        db.session.add(sales_penalty_detail)
                        db.session.add(customer_info)
                        db.session.add(inventory_penalty_detail)
                    else:
                        existRecordCount += 1
                db.session.commit()
                return jsonify({
                    'success': True, 
                    'message': '文件成功上传并存储在数据库中', 
                    'newRecordCount': newRecordCount,
                    'existRecordCount' : existRecordCount,
                    })
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
    