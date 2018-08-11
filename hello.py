from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/user')
def user():
    return 'user index'


# 变量标记
@app.route('/user/<username>')
def user_show(username):
    return 'username is %s' % username


# 变量转换为特定类型 int, float, path
@app.route('/post/<int:post_id>')
def post_show(post_id):
    return 'post id is %d' % post_id


if __name__ == '__main__':
    # 开启调试模式的两种方法，可以修改代码重启服务
    # app.debug = True
    app.run(host='0.0.0.0', debug=True)









