from flask import Flask, request
from flask import jsonify 
import requests
import xmltodict, json

app = Flask(__name__)

@app.route('/', methods=['get'])
def home():
    return 'API de consultar CEP!!'

@app.route('/consultaCep/<cep>', methods=['GET'])
def consultaCEP(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/xml/')
    jsonEndereco = xmltodict.parse(response.text)
    jsonEndereco = json.dumps(jsonEndereco['xmlcep'])
    strToList = jsonEndereco.split(",")
    
    
    for l in strToList:
        jsonAux = l.split(':')
        if(jsonAux[0]=='bairro'):
            print('-----')
            print(jsonAux[0])
            print('-----')
            jsonEndereco[jsonAux[0]] = jsonAux[1]

    return jsonEndereco



    
app.run()