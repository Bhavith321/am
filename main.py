from flask import *
app = Flask(__name__)
app.secret_key = '7b3yfvuydfhh55566’

@app.route('/')
def index():
   if 'username' in session:
      username = session['username']
         return 'Logged in as ' + username + '<br>' + "<b><a href = '/logout'>click here to log out</a></b>"
   return redirect(url_for('login'))

@app.route('/index')
def home():
   return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('index'))
   return redirect(url_for('login'))

@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('index'))

@app.route('/login')
def logijjn():
   return render_template('login.html')

if name == 'main':
   app.run(debug = True)
