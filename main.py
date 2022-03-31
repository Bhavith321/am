from flask import *
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/home')
def homep():
   return render_template('index.html')

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/dashboard')
def dashboard():
   return render_template('dashboard.html')

@app.route('/<search>')
def show_search(search):
    return redirect(url_for(('home'))

if __name__ == '__main__':
   app.run()
