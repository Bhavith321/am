from flask import *

app = Flask(__name__)

app.secret_key = b'_5#y2L4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/index')
def indexingh():
    return render_template('index.html')

@app.route('/login')
def indexh():
    return render_template('login.html')

if __name__ = '__main__':
   app.run()
