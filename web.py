from flask import Flask, request
from flask import url_for, redirect
from flask import render_template

#Flast entry point
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('under_construction.html')
   #return "Hello World! {0}".format(request.remote_addr)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello1(name=None):
    return render_template('name_template.html', name=name)

#MAIN
if __name__ == "__main__":
    app.run()


