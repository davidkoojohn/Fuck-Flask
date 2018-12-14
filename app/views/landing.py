
from flask import Blueprint, render_template

landing_view = Blueprint('landing', __name__,
                         template_folder='templates',
                         static_folder='static')


@landing_view.route('')
def index():
    return render_template('landing/index.html')




