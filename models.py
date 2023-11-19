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
