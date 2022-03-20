from flask import *

app = Flask(__name__)  

@app.route('/')
def index():
    return redirect(url_for('index'))
 
@app.route('/index')  
def indexpage():  
    return render_template('index.html')

@app.route('/index')
def daccess():
    abort(401)
    this_is_never_executed()
   
@app.route('/<search>')  
def userpage(search):  
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
