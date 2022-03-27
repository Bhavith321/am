from flask import *

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/login')
def logiage():
   return render_template('login.html')

@app.route('/index')
def homeage():
   return render_template('index.html')

@app.route('/')
def index():
     if 'username' in session:
           return f'Logged in as {session["username"]}.Click here to logout.'
         return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
     return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ = '__main__':
   app.run()
