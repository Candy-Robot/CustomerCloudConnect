from flask import request, jsonify, Blueprint, render_template,session,redirect, url_for
from models import  db , User

mod = Blueprint('user', __name__, url_prefix='/user')


@mod.route('/')
def index():
    return render_template('login.html')

@mod.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        # 获取用户名和密码
        username = data['username']
        password = data['password']

        # 查询数据库中的用户
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            # 用户认证成功，将用户ID存储在会话中
            session['user_id'] = user.id
            # 假设验证成功，返回一个 JSON 响应
            response_data = {'success': True, 'message': 'Login successful'}
            return jsonify(response_data), 200
        else:
            response_data = {'success': False, 'message': '登陆失败'}
            return jsonify(response_data), 200
    except Exception as e:
        # 处理异常情况，返回错误信息
        response_data = {'success': False, 'message': str(e)}
        return jsonify(response_data), 400

# @mod.route('/logout')
# def logout():
#     # 清除会话中的用户ID
#     session.pop('user_id', None)
#     return redirect(url_for('login'))

