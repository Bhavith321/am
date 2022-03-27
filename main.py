from flask import *
app = Flask(__name__)

@app.route('/')
def homepe():
   return render_template('index.html')

@app.route('/login')
def logiage():
   return render_template('login.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST' and
   request.form['username'] == 'admin' :
   return redirect(url_for('dashboard'))
   return redirect(url_for('index'))

@app.route('/dashboard')
def success():
   return 'logged in successfully'

if __name__ == '__main__':
   app.run()
