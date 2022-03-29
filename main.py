from flask import *

app = Flask(__name__)

@app.route('/')
def indx():
    return render_template('index.html')

@app.route('/home')
def ggome():
    return render_template('index.html')

@app.route('/login')
def loginiiu():
    return render_template('login.html')

if __name__ = '__main__':
   app.run()
