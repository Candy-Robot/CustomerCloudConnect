from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

from flask import request

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = request.args.get('name', 'Guest')
    return 'Hello, ' + name + '!'
from flask import render_template

@app.route('/welcome')
def welcome():
    message = 'Hello, Flask!'
    return render_template('new_file.html', message=message)

# from flask import Flask, render_template, request


# @app.route('/new_file', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['file']
#         file.save(file.filename)
#         return '文件上传成功！'
#     return render_template('new_file.html')

if __name__ == '__main__':
    app.run(debug=True)
