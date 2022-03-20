from flask import *

app = Flask(__name__)  

@app.route('/')  
def indexpage():  
    return render_template('index.html')

@app.route('/index/')  
def indexpage():  
    return render_template('index.html')

@app.route('/<search>')
def termsearch(search):
    return redirect(url_for('/index/'))

if __name__ == '__main__':
    app.run()
