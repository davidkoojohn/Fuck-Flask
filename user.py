
from flask import Flask, request, render_template
from werkzeug import secure_filename

app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    searchword = request.args.get('key', '')
    print(searchword)

    if request.method == 'POST':
        print(request.form)
        # if valid_login(request.form['username'],
        #                request.form['password']):
        #     return log_the_user_in(request.form['username'])
        # else:
        #     error = 'Invalid username/password'

    return render_template('login.html', error=error)


@app.route('/upload', methods=['POST', 'PUT'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/')


    pass

"""
# test_request_context 请求上下管理器
with app.test_request_context('/hello', method='POSt'):
    assert request.path == '/hello'
    assert request.method == 'POST'
    
# 传入整个WSGI
with app.request_context(environ):
    assert request.method == 'POST'
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

