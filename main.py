from flask import *
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/user/login/')
def login():
   return render_template('login.html')

@app.route('/user/dashboard/')
def dashboard():
   return render_template('dashboard.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
   app.run()
