from flask import Flask, render_template, jsonify, request
import json
from jabuticaba_functions import *
from os import environ, listdir
import requests
import json
from PyPDF2 import PdfReader

app = Flask(__name__)

@app.route('/main')
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html');

@app.route('/PaginaDeUpload', methods=['GET'])
def PaginaDeUpload():
    return render_template('PaginaDeUpload.html');

@app.route('/listar_arquivos', methods=['POST'])
def listar_arquivos():
    path = request.form.get('path', '');

    print("path: ",path);
    diretorio = listdir(path);

    for arquivo in diretorio:
        #print("arquivo: ",arquivo[-4:]);
        if arquivo[-4:] != '.pdf':
            diretorio.remove(arquivo);
    print("diretorio: ",diretorio);
    return jsonify(diretorio), 200, {'Content-Type': 'application/json; charset=utf-8'};

@app.route('/enviarAnalise', methods=['POST'])
def enviarAnalise():
    arquivos = request.get_json('arquivos');
    vaga = arquivos.get('vaga', []);
    arquivos = arquivos.get('arquivos', []);
    print("vaga: ",vaga);
    string_arquivo = vaga + "\n-------\nCurrículo 1\n";

    for arquivo in arquivos:
        print("----------------------------------------------------------------");
        print("arquivo: ",arquivo);
        print("----------------------------------------------------------------");
        reader = PdfReader(arquivo)
        number_of_pages = len(reader.pages)

        for i in range(0,number_of_pages):
            page = reader.pages[0]
            text = page.extract_text();
            text = text.replace('\n', ' ').replace('\r', ' ');
            temp = i + 2;
            string_arquivo = string_arquivo + "\n-----\n Currículo " + str(temp) + "\n-----\n" + text;

    print("Enviando para análise");

    result = send_openai_request(environ['OPENAI_API_KEY'], string_arquivo, requests)

    return result['output'][0]['content'][0]['text'], 200, {'Content-Type': 'application/json; charset=utf-8'};

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