from flask import Flask, render_template, jsonify, request
import json
from jabuticaba_functions import *

app = Flask(__name__)

@app.route('/main')
@app.route('/index')
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

@app.route('/chamandoChatGPT', methods=['POST'])
def chamandoChatGPT():
    curriculos = request.form.get('curriculos', '')

    print(curriculos);
    
    return "ok",200;

if __name__ == '__main__':
    app.run(debug=True)