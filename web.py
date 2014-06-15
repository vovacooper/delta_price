from flask import Flask, request,Response, send_from_directory
from flask import url_for, redirect
from flask import render_template

from classes import logger

#from flask.ext.uwsgi_websocket import WebSocket
from flask_uwsgi_websocket.websocket import WebSocket



########################################################################################################################
from modules.data_module import data_module
from modules.subscription_module import subscription_module
from modules.deltaprice_module import deltaprice_module

app = Flask(__name__)
ws = WebSocket(app)


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
@app.route("/ws")
def web_socket():
    return render_template('websocket_echo.html')


@ws.route('/websocket')
def web_socket_echo(ws):
    while True:
        msg = ws.receive()
        if msg is not None:
            ws.send(msg)
        else:
            return


########################################################################################################################
if __name__ == "__main__":
    app.run()


