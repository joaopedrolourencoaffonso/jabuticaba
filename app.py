from flask import Flask, render_template, jsonify
import json
from functions import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/abrir-arquivo')
def abrirArquivo():
    file = abrirArquivoSimples();
    
    return file;

@app.route('/formularioSimples')
def formularioSimples():
    return render_template('formularioSimples.html');

if __name__ == '__main__':
    app.run(debug=True)