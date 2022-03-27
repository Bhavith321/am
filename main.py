from flask import *
app = Flask(__name__)

@app.route('/')
def indexpage():
   return redirect(url_for('index'))

@app.route('/index')
def homepage():
   return render_template('index.html')

@app.route('/login')
def loginpage():
   return render_template('login.html')

if __name__ == '__main__':
   app.run()
