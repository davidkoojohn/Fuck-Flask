
from flask import Flask, request, session, escape, render_template, abort, redirect, url_for, make_response

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():

    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    # return redirect(url_for('login'))
    return 'You are not logged in'


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username></p>
            <p><input type=submit value=Login></p>
        </form>
        '''
    # abort(401)


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


app.secret_key = 'koo is a very good girl'




@app.errorhandler(404)
def page_not_found(error):
    resp = make_response(render_template('404.html', info=error), 404)
    resp.headers['X-something'] = 'a value'
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

