from flask import Flask, request
from flask import url_for, redirect
from flask import render_template

#Flast entry point
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! {0}".format(request.remote_addr)

#MAIN
if __name__ == "__main__":
    app.run()


