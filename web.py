from flask import Flask, request, send_from_directory
from flask import url_for, redirect
from flask import render_template

########################################################################################################################
from modules.data_module import data_module

#Flast entry point
app = Flask(__name__)

app.register_blueprint(data_module)

########################################################################################################################
@app.route("/")
def hello():
    return render_template('under_construction.html')
   #return "Hello World! {0}".format(request.remote_addr)

#example
@app.route('/hello/')
@app.route('/hello/<name>')
def hello1(name=None):
    return render_template('name_template.html', name=name)


#return main JS
@app.route('/js/')
def mainjs():
    return send_from_directory(app.static_folder + '/javascripts', 'main.js')

########################################################################################################################
if __name__ == "__main__":
    app.run()


