from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'API de consulta CEP!!'



app.run()

