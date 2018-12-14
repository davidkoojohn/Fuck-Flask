# coding: utf-8

from flask import Flask
from views import todos_view, landing_view

app = Flask(__name__)

app.register_blueprint(landing_view, url_prefix='/')
app.register_blueprint(todos_view, url_prefix='/todos')



