
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
@app.route('/hello/<name>')
def hello_world(name = None):
    return render_template('index.html',person=name)
if __name__ =="__main__":

    app.run(debug = True)
