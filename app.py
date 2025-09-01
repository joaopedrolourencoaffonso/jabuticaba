from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/abrir-arquivo')
def abrirArquivo():
    file = open("temp.txt","r").read();
    
    return file;

if __name__ == '__main__':
    app.run(debug=True)