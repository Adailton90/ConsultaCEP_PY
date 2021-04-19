from flask import Flask, request
from flask import jsonify 
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['get'])
def home():
    return 'API de consultar CEP!!'

@app.route('/consultaCep/<cep>', methods=['GET'])
def consultaCEP(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/xml/')
    return response.text
    



    
app.run()