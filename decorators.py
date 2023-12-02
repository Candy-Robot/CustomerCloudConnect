
from functools import wraps
from flask import redirect, url_for, session

# 装饰器：检查用户是否已登录
def login_required(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            # 如果用户未登录，重定向到登录页面
            return redirect(url_for('user.index'))
        return view_func(*args, **kwargs)
    return wrapper