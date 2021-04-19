from flask import Flask, request
from flask import jsonify 
app = Flask(__name__)

@app.route('/', methods=['get'])
def home():
    return 'API de consultar CEP!!'

@app.route('/cadastrarEndereco', methods=['POST'])
def cadatraEndereco():
    body = request.get_json()
    print(body)
    return jsonify(body)

    
app.run()