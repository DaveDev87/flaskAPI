import flask
from flask import request
from fibonacci import fibo
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Saquenme de Latinoamerica</h1>"


@app.route("/fibo", methods=['GET'])
def getFibo():
    if 'number' in request.args:
        number = int(request.args['number'])
    else:
        return "Input incorrecto"
    
    return str(fibo(number))


app.run()
