from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost:3306/test'  # 你的数据库连接配置
db = SQLAlchemy(app)

class TestExcel(db.Model):
    __tablename__ = 'test_excel'    # 数据库中的表名

    customer_code = db.Column(db.String, primary_key=True)
    customer_manager = db.Column(db.String, unique=True, nullable=False)
    company_name = db.Column(db.String)
    data_score = db.Column(db.String)
    last_upload_time = db.Column(db.DateTime)
    last_modified_time = db.Column(db.DateTime)
    restore_time = db.Column(db.DateTime)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 根据客户编码和客户经理查询数据的路由
@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        # 从查询参数中获取客户编码和客户经理的信息
        customer_code = request.args.get('customer_code')
        customer_manager = request.args.get('customer_manager')

        # 在数据库中查询符合条件的数据
        query = TestExcel.query

        if customer_code:
            query = query.filter_by(customer_code=customer_code)

        if customer_manager:
            query = query.filter_by(customer_manager=customer_manager)

        data = query.all()

        # 将查询结果转换为字典列表
        result = []
        for item in data:
            result.append({
                'customer_code': item.customer_code,
                'customer_manager': item.customer_manager,
                'company_name': item.company_name,
                'data_score': item.data_score,
                'last_upload_time': item.last_upload_time.isoformat() if item.last_upload_time else None,
                'last_modified_time': item.last_modified_time.isoformat() if item.last_modified_time else None,
                'restore_time': item.restore_time.isoformat() if item.restore_time else None
            })

        return jsonify({'success': True, 'data': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
