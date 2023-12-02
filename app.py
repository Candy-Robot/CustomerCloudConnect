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

@app.route('/')
def index():
    return render_template('login.html')

from views import upload
from views import query, user
app.register_blueprint(upload.mod)
app.register_blueprint(query.mod)
app.register_blueprint(user.mod)

if __name__ == '__main__':
    app.run(debug=True)