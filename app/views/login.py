
from flask import Blueprint, render_template

login_view = Blueprint('login', __name__)


@login_view.route('')
def index():
    return render_template('login/index.html')




