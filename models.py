## 包含数据库模型的定义

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
db = SQLAlchemy()

class test_excel(db.Model):
    __tablename__ = 'test_excel'    # 数据库中的表名

    customer_code = db.Column(db.String, primary_key =True) # 客户编码
    # market_department = db.Column(db.String, unique=True, nullable=False)  # 市场部
    customer_manager = db.Column(db.String,unique=True, nullable=False) # 客户经理
    company_name = db.Column(db.String) # 企业名称
    data_score = db.Column(db.String)   # 数采分

    last_upload_time = db.Column(db.DateTime) # 最近上传时间
    last_modified_time = db.Column(db.DateTime)   # 最近数采分变动时间
    restore_time = db.Column(db.DateTime)   # 恢复时间
'''
    operator = db.Column(db.String) # 经营者
    level = db.Column(db.String) # 档位
    terminal_hierarchy = db.Column(db.String)
    is_sample_customer = db.Column(db.String)
    data_collection_method = db.Column(db.String)
    store_name  = db.Column(db.String)
    address = db.Column(db.String)
    data_type = db.Column(db.String)
    location_interval = db.Column(db.String)
    # 在这里定义数据库表的字段，根据Excel中的列名进行匹配
    '''

# 客户信息表
class CustomerInformation(db.Model):
    __tablename__ = 'customer_information'

    customer_code = db.Column(db.String(50), primary_key=True)  # 客户编码
    market_department = db.Column(db.String(50))  # 市场部
    customer_manager = db.Column(db.String(50))  # 客户经理
    company_name = db.Column(db.String(100))  # 企业名称
    operator = db.Column(db.String(50))  # 经营者
    level = db.Column(db.String(20))  # 档位
    terminal_hierarchy = db.Column(db.String(50))  # 终端层级
    is_sample_customer = db.Column(db.String(20))  # 是否样本户
    data_collection_method = db.Column(db.String(50))  # 数据采集方法
    store_name = db.Column(db.String(100))  # 客户店铺名称
    address = db.Column(db.String(255))  # 客户地址
    data_type = db.Column(db.String(50))  # 数采类型
    location_interval = db.Column(db.Integer)  # 数采户所在区间

# 库存评分相关
class InventoryPenaltyDetail(db.Model):
    __tablename__ = 'inventory_penalty_detail'

    customer_code = db.Column(db.String(50), primary_key=True)  # 客户ID主键
    inventory_accuracy = db.Column(db.Float)  # 库存准确性
    inventory_count = db.Column(db.Integer)  # 盘库次数
    inspection_accuracy = db.Column(db.Float)  # 检查准确率
    inspection_count = db.Column(db.Integer)  # 检查次数
    inventory_penalty = db.Column(db.Float)  # 盘库扣分
    inventory_penalty_time = db.Column(db.Date)  # 盘库扣分时间
    inventory_penalty_recovery_time = db.Column(db.Date)  # 盘库扣分恢复时间
    inventory_sales_ratio = db.Column(db.Float)  # 存销比
    inventory_sales_penalty = db.Column(db.Float)  # 存销比扣分
    inventory_sales_penalty_time = db.Column(db.Date)  # 存销比扣分时间
    inventory_sales_penalty_recovery_time = db.Column(db.Date)  # 存销比扣分恢复时间
    negative_inventory = db.Column(db.Integer)  # 负库存
    negative_inventory_penalty = db.Column(db.Float)  # 负库存扣分
    negative_inventory_penalty_time = db.Column(db.Date)  # 负库存扣分时间
    negative_inventory_penalty_recovery_time = db.Column(db.Date)  # 负库存扣分恢复时间
    manual_inventory_changes_count = db.Column(db.Integer)  # 人为修改库存次数
    manual_inventory_changes_penalty = db.Column(db.Float)  # 人为修改库存扣分
    manual_inventory_changes_penalty_time = db.Column(db.Date)  # 人为修改库存扣分时间
    manual_inventory_changes_penalty_recovery_time = db.Column(db.Date)  # 人为修改库存扣分恢复时间

# 销售评分相关
class SalesPenaltyDetail(db.Model):
    __tablename__ = 'sales_penalty_detail'

    customer_code = db.Column(db.String(50), primary_key=True)  # 客户代码
    data_score = db.Column(db.Float)  # 数采分
    startup_days = db.Column(db.Integer)  # 开机天数
    effective_upload_ratio = db.Column(db.Float)  # 有效上传比例
    upload_ratio_penalty = db.Column(db.Float)  # 有效上传比例扣分
    upload_ratio_penalty_time = db.Column(db.Date)  # 有效上传比扣分时间
    upload_ratio_recovery_time = db.Column(db.Date)  # 有效上传比恢复时间
    sales_days = db.Column(db.Integer)  # 销售天数
    average_sales_duration = db.Column(db.Float)  # 日均销售时长
    sales_duration_penalty = db.Column(db.Float)  # 销售时长扣分
    sales_duration_penalty_time = db.Column(db.Date)  # 销售时长扣分时间
    sales_duration_recovery_time = db.Column(db.Date)  # 销售时长恢复时间
    warning_count = db.Column(db.Integer)  # 预警次数
    warning_penalty = db.Column(db.Float)  # 预警扣分
    warning_penalty_time = db.Column(db.Date)  # 预警扣分时间
    warning_recovery_time = db.Column(db.Date)  # 预警扣分恢复时间
    centralized_sales_count = db.Column(db.Integer)  # 集中销售次数
    centralized_sales_penalty = db.Column(db.Float)  # 集中销售次数扣分
    centralized_sales_penalty_time = db.Column(db.Date)  # 集中销售扣分时间
    centralized_sales_recovery_time = db.Column(db.Date)  # 集中销售恢复时间
    delayed_upload_count = db.Column(db.Integer)  # 延迟上传次数
    delayed_upload_penalty = db.Column(db.Float)  # 延迟上传次数扣分
    delayed_upload_penalty_time = db.Column(db.Date)  # 延迟上传扣分时间
    delayed_upload_recovery_time = db.Column(db.Date)  # 延迟上传恢复时间

class DataScoreAndUploadTime(db.Model):
    __tablename__ = 'data_score_and_upload_time'    # 数据表名称

    
    customer_code = db.Column(db.String(50), primary_key=True )     # 客户代码
    data_score = db.Column(db.Float )               # 数采分
    last_upload_time = db.Column(db.DateTime)     # 最近上传时间