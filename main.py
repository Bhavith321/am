from flask import *

app = Flask(__name__)  

@app.route('/')  
def indexpage():  
    return redirect(url_for('index'))

@app.route('/index')  
def rootpage():  
    return render_template('index.html')

@app.route('/<search>')
def searchpages(search):
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
