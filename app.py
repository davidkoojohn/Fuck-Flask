# coding: utf-8

from flask import Flask
from flask import request
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return 'browser is %s' % user_agent, 400


if __name__ == '__main__':
    manager.run()
    # app.run(debug=True)
