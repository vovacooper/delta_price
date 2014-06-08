from flask import Flask, request,Response, send_from_directory
from flask import url_for, redirect
from flask import render_template

from classes import logger

########################################################################################################################
from modules.data_module import data_module
from modules.subscription_module import subscription_module
from modules.deltaprice_module import deltaprice_module

app = Flask(__name__)

########################################################################################################################

app.register_blueprint(data_module)
app.register_blueprint(subscription_module)
app.register_blueprint(deltaprice_module)


########################################################################################################################
@app.route("/")
def hello():
    return render_template('under_construction.html')

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


