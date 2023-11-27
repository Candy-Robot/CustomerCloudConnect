import sys
import os

# 获取当前脚本所在目录的上一级目录
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# 将上一级目录添加到模块搜索路径
sys.path.append(parent_dir)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db, CustomerInformation, InventoryPenaltyDetail, SalesPenaltyDetail

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.session.query(CustomerInformation).delete()
    db.session.query(InventoryPenaltyDetail).delete()
    db.session.query(SalesPenaltyDetail).delete()

    # 提交更改
    db.session.commit()

print("Data deleted successfully.")