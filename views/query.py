from flask import request, jsonify, Blueprint, render_template
from models import  db , CustomerInformation, InventoryPenaltyDetail, SalesPenaltyDetail
from models import DataScoreAndUploadTime
from decorators import login_required
mod = Blueprint('query', __name__, url_prefix='/query')

# 使用装饰器，确保所有路由都经过登录验证
@mod.before_request
@login_required
def before_request():
    pass

@mod.route('/', methods=['GET'])
def search():
    return render_template('search.html')

# 路由，返回客户经理选项列表
@mod.route('/get_customer_managers', methods=['GET'])
def get_customer_managers():
    try:
        # 在数据库中查询符合条件的数据
        existing_managers = db.session.query(CustomerInformation.customer_manager).distinct().all()
        customer_managers = [manager[0] for manager in existing_managers]
        return jsonify({'customer_managers': customer_managers})
    except Exception as e:
        return jsonify({'error': str(e)})
    

# 路由，查询数据
@mod.route('/get_data', methods=['GET'])
def get_data():
    try:
        # 从查询参数中获取客户编码、客户经理和店铺名称的信息的信息
        customer_code = request.args.get('customer_code')
        customer_manager = request.args.get('customer_manager')
        store_name = request.args.get('store_name')
        # 创建query实例
        query_customer_code = db.session.query(CustomerInformation)
        query_InventoryPenaltyDetail   = db.session.query(InventoryPenaltyDetail)
        query_SalesPenaltyDetail = db.session.query(SalesPenaltyDetail)
        query_DataScoreAndUploadTime = db.session.query(DataScoreAndUploadTime)
        if customer_code:
            query_customer_code = query_customer_code.filter_by(customer_code=customer_code)

        if customer_manager:
            query_customer_code = query_customer_code.filter_by(customer_manager=customer_manager)

        if store_name:
            # 使用 like 进行模糊查询，结合 % 通配符
            query_customer_code = query_customer_code.filter(CustomerInformation.company_name.like('%' + store_name + '%'))

        data = query_customer_code.all()

        # 将查询结果转换为字典列表
        result = []
        # 查询具体的扣分项目以及扣分时间
        for item in data:
            # 都应该只有一条数据
            query_Inventory = query_InventoryPenaltyDetail.filter_by(customer_code = item.customer_code).first()
            query_Sales = query_SalesPenaltyDetail.filter_by(customer_code = item.customer_code).first()
            query_data = query_DataScoreAndUploadTime.filter_by(customer_code = item.customer_code).first()

            result.append({
                'customer_code': item.customer_code,
                'company_name':item.company_name,
                'customer_manager':item.customer_manager,
                'data_score':query_data.data_score,
                'last_upload_time':query_data.last_upload_time,
                'inventory_penalty':query_Inventory.inventory_penalty,
                'inventory_penalty_time':query_Inventory.inventory_penalty_time,
                'inventory_sales_penalty':query_Inventory.inventory_sales_penalty,
                'inventory_sales_penalty_time':query_Inventory.inventory_sales_penalty_time,
                'negative_inventory_penalty' :query_Inventory.negative_inventory_penalty,
                'negative_inventory_penalty_time':query_Inventory.negative_inventory_penalty_time,
                'manual_inventory_changes_penalty':query_Inventory.manual_inventory_changes_penalty,
                'manual_inventory_changes_penalty_time':query_Inventory.manual_inventory_changes_penalty_time,
                'upload_ratio_penalty':query_Sales.upload_ratio_penalty,
                'upload_ratio_penalty_time':query_Sales.upload_ratio_penalty_time,
                'sales_duration_penalty':query_Sales.sales_duration_penalty,
                'sales_duration_penalty_time':query_Sales.sales_duration_penalty_time,
                'warning_penalty':query_Sales.warning_penalty,
                'warning_penalty_time':query_Sales.warning_penalty_time,
                'centralized_sales_penalty':query_Sales.centralized_sales_penalty,
                'centralized_sales_penalty_time':query_Sales.centralized_sales_penalty_time,
                'delayed_upload_penalty':query_Sales.delayed_upload_penalty,
                'delayed_upload_penalty_time':query_Sales.delayed_upload_penalty_time,
            })

        return jsonify({'success': True, 'data': result})
    except Exception as e:
        return jsonify({'error': str(e)})