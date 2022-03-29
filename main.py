from flask import render_template

app = flask(_name_)

@app.route('/')
def homeage():
     return render_template('index.html')

if __name__='__main__':
   app.run()
