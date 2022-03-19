from flask import *

app = Flask(__name__)  
 
@app.route('/')  
def indexpage():  
    return render_template('index.html')

@app.route('/home')  
def indexpage():  
    return render_template('home.html')
 
@app.route('/<name>')  
def indexpage():  
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
