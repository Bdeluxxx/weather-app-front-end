from flask import Flask, jsonify
import requests
from flask_cors import CORS


app = Flask(__name__)

api_key = "abd2dba3225f441da0b193416252908"
link_api = "http://api.weatherapi.com/v1/current.json"


@app.route('/clima')
def get_clima():
    parametros = {
        "key": api_key,
        "q": "Horizontina",
        "lang": "pt"
    }
    
    resposta = requests.get(link_api, params=parametros)
    
    
    if resposta.status_code == 200:
        dados_requisicao = resposta.json()
        print(dados_requisicao)
        temp = dados_requisicao["current"]["temp_c"]
        descricao = dados_requisicao["current"]["condition"]["text"]
        
    
        return jsonify({"temperatura": temp, "descricao": descricao})
    else:
        
        return jsonify({"erro": "Nao foi possivel obter os dados do clima"}), 500


if __name__ == '__main__':
    app.run(debug=True)