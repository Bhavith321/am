from flask import *
app = Flask(__name__)

@app.route('/')
def index():
   return redirect(url_for('home'))

@app.route('/home/')
def home():
   return render_template('index.html')

@app.route('/login/')
def login():
   return render_template('login.html')

@app.route('/dashboard/')
def dashboard():
   return render_template('dashboard.html')

@app.route('/verification/')
def verification():
   return render_template('verification.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
   app.run()
