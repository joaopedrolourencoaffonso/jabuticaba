from flask import Flask, render_template, jsonify, request
import json
from jabuticaba_functions import *
from os import environ
import requests
import json

app = Flask(__name__)

@app.route('/main')
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html');

@app.route('/PaginaDeUpload', methods=['GET'])
def PaginaDeUpload():
    return render_template('PaginaDeUpload.html');

@app.route('/formularioSimples')
def formularioSimples():
    return render_template('formularioSimples.html');

@app.route('/chamandoChatGPT', methods=['POST'])
def chamandoChatGPT():
    curriculos = request.form.get('curriculos', '');

    prompt = "Análise os currículos abaixo, crie um ranking de candidatos mais apropriados a vaga descrita. Explique sua lógica: " + "\n" + curriculos

    result = send_openai_request(environ['OPENAI_API_KEY'], prompt, requests)

    print("curriculos: ",curriculos);
    print("result: ", result['output'][0]['content'][0]['text']);
    
    return result['output'][0]['content'][0]['text'], 200;

if __name__ == '__main__':
    app.run(debug=True)