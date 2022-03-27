from flask import *
app = Flask(__name__)
app.secret_key = '7b3yfvuydfhh55566’

@app.route('/')
def indexpage():
   return redirect(url_for('index'))

@app.route('/index')
def homepage():
   return render_template('index.html')

@app.route('/login', methods = ['POST'])
def loginproc():
   if request.method == 'POST':
      uname = request.form['username']
      return redirect(url_for('index'))
   return redirect(url_for('login'))

@app.route('/login')
def loginpage():
   return render_template('login.html')

if '__name__' == '__main__':
   app.run()
