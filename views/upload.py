from models import db, CustomerInformation, InventoryPenaltyDetail, SalesPenaltyDetail, DataScoreAndUploadTime
from flask import request, jsonify, Blueprint
import pandas as pd
import numpy as np
from flask import render_template
import datetime
import traceback
from sqlalchemy.exc import SQLAlchemyError
from decorators import login_required

mod = Blueprint('upload', __name__, url_prefix='/upload')

# 使用装饰器，确保所有路由都经过登录验证
@mod.before_request
@login_required
def before_request():
    pass

@mod.route('/')
def index():
    return 'Welcome to the upload page!'

# 初次初始化数据库 只有这里可以添加新数据
# 后续可以添加判断，只有特定的市场部可以加入到数据库中
@mod.route('/init-db', methods=['GET', 'POST'])
def init_db():
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


@mod.route('/upload-db', methods=['GET', 'POST'])
def upload_db():
    # GET方法调用如下函数
    if request.method == 'GET':
        return render_template('upload-db.html')  
        
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
                unExistRecordCount = 0
                existRecordCount = 0
                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                now_time_add_90 = (datetime.datetime.now()+datetime.timedelta(days=90)).strftime("%Y-%m-%d %H:%M:%S")
                now_time_add_30 = (datetime.datetime.now()+datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")
                # 将数据存储到数据库
                for index, row in df.iterrows():
                    customer_code_df = row.to_dict()['客户编码']
                    existing_data = db.session.query(CustomerInformation).filter(CustomerInformation.customer_code==customer_code_df).first()
                    # 库存数据表的数据
                    inventory_data = db.session.query(InventoryPenaltyDetail).filter(InventoryPenaltyDetail.customer_code==customer_code_df).first()
                    # 销售数据表的数据
                    sales_data = db.session.query(SalesPenaltyDetail).filter(SalesPenaltyDetail.customer_code==customer_code_df).first()
                    # 数采分和最近上传时间
                    score_data = db.session.query(DataScoreAndUploadTime).filter(DataScoreAndUploadTime.customer_code==customer_code_df).first()
                    if existing_data: # 存在数据即可以进行对比
                        existRecordCount += 1
                        # 修改数采分和最近上传时间的表
                        # 更改最近上传时间
                        score_data.last_upload_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
                        score_data.data_score = row.to_dict()['数采分']
                        # 加入数采分和最近上传时间表
                        db.session.add(score_data)
                        
                        # 扣分的逻辑，如果发生了扣分的情况，那么一定会产生当天的分数大于数据库内的分数,
                        # 记录改天为操作发生的时间，并且将恢复日期修改为当天+恢复的时间
                        # 修改库存数据表
                        # 盘库扣分 恢复时间为3个月
                        if inventory_data.inventory_penalty < row.to_dict()['盘库扣分']: 
                            inventory_data.inventory_penalty_time = now_time
                            inventory_data.inventory_penalty_recovery_time = now_time_add_90
                        inventory_data.inventory_accuracy = row.to_dict()['盘库准确率']
                        inventory_data.inventory_count = row.to_dict()['盘库次数']
                        inventory_data.inspection_accuracy = row.to_dict()['检查准确率']
                        inventory_data.inspection_count = row.to_dict()['检查次数']
                        inventory_data.inventory_penalty = row.to_dict()['盘库扣分']
                        # 存销比扣分 恢复时间为一个月
                        if inventory_data.inventory_sales_penalty < row.to_dict()['存销比扣分值']: 
                            inventory_data.inventory_sales_penalty_time = now_time
                            inventory_data.inventory_sales_penalty_recovery_time = now_time_add_30
                        inventory_data.inventory_sales_ratio = row.to_dict()['存销比']
                        inventory_data.inventory_sales_penalty=row.to_dict()['存销比扣分值']
                        # 负库存扣分项 隔天恢复 
                        if inventory_data.negative_inventory_penalty < row.to_dict()['负库存扣分项']:
                            inventory_data.negative_inventory_penalty_time = now_time
                            inventory_data.negative_inventory_penalty_recovery_time = now_time
                        inventory_data.negative_inventory=row.to_dict()['负库存']
                        inventory_data.negative_inventory_penalty=row.to_dict()['负库存扣分项']
                        # 人为修改库存 恢复时间为3个月
                        if inventory_data.manual_inventory_changes_penalty < row.to_dict()['人为修改库存次数扣分']:
                            inventory_data.manual_inventory_changes_penalty_time = now_time
                            inventory_data.manual_inventory_changes_penalty_recovery_time = now_time_add_90
                        inventory_data.manual_inventory_changes_count = row.to_dict()['人为修改库存次数']
                        inventory_data.manual_inventory_changes_penalty=row.to_dict()['人为修改库存次数扣分']
                        # 加入库存数据表
                        db.session.add(inventory_data)

                        # 有效上传比 恢复时间3个月
                        if sales_data.upload_ratio_penalty < row.to_dict()['有效上传比例扣分']:
                            sales_data.upload_ratio_penalty_time = now_time
                            sales_data.upload_ratio_recovery_time = now_time_add_90
                        sales_data.data_score=row.to_dict()['数采分']
                        sales_data.startup_days=row.to_dict()['开机天数']
                        sales_data.effective_upload_ratio=row.to_dict()['有效上传比例']
                        sales_data.upload_ratio_penalty=row.to_dict()['有效上传比例扣分']
                        # 销售时长扣分 恢复时间3个月
                        if sales_data.sales_duration_penalty < row.to_dict()['销售时长扣分']:
                            sales_data.sales_duration_penalty_time = now_time
                            sales_data.sales_duration_recovery_time = now_time_add_90
                        sales_data.sales_days=row.to_dict()['销售天数']
                        sales_data.average_sales_duration=row.to_dict()['日均销售时长']
                        sales_data.sales_duration_penalty=row.to_dict()['销售时长扣分']
                        # 预警扣分 恢复时间3个月
                        if sales_data.warning_penalty < row.to_dict()['预警扣分']:
                            sales_data.warning_penalty_time = now_time
                            sales_data.warning_recovery_time = now_time_add_90
                        sales_data.warning_count=row.to_dict()['预警次数']
                        sales_data.warning_penalty=row.to_dict()['预警扣分']
                        # 集中销售 恢复时间3个月
                        if sales_data.centralized_sales_penalty < row.to_dict()['集中销售次数扣分']:
                            sales_data.centralized_sales_penalty_time = now_time
                            sales_data.centralized_sales_recovery_time = now_time_add_90
                        sales_data.centralized_sales_count=row.to_dict()['集中销售次数']
                        sales_data.centralized_sales_penalty=row.to_dict()['集中销售次数扣分']
                        # 延迟上传扣分 恢复时间3个月
                        if sales_data.delayed_upload_penalty<row.to_dict()['延迟上传次数扣分']:
                            sales_data.delayed_upload_penalty_time = now_time
                            sales_data.delayed_upload_recovery_time = now_time_add_90
                        sales_data.delayed_upload_count=row.to_dict()['延迟上传次数']
                        sales_data.delayed_upload_penalty=row.to_dict()['延迟上传次数扣分']
                        # 加入数据
                        db.session.add(sales_data)

                    else:
                        unExistRecordCount += 1
                    db.session.commit()
                return jsonify({
                    'success': True, 
                    'message': '文件成功上传并存储在数据库中', 
                    'existRecordCount' : existRecordCount,
                    'unExistRecordCount' :unExistRecordCount,
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

