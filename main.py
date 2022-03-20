from flask import *

app = Flask(__name__)  

@app.route('/')  
def indexpage():  
    return render_template('index.html')

@app.route('/<search>')
def index(search):
    return redirect(url_for('/'))

if __name__ == '__main__':
    app.run()
