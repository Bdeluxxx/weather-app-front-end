from flask import Flask, jsonify
import requests
from flask_cors import CORS

# Inicializa o servidor Flask
app = Flask(__name__)
CORS(app)

# Sua chave da API e URL
api_key = "abd2dba3225f441da0b193416252908"
link_api = "http://api.weatherapi.com/v1/current.json"

# Cria uma "rota" para que o seu Front End possa pedir os dados
@app.route('/clima')
def get_clima():
    parametros = {
        "key": api_key,
        "q": "Horizontina",
        "lang": "pt"
    }
    
    # Executa a sua lógica original para obter os dados da API
    resposta = requests.get(link_api, params=parametros)
    
    # Este bloco precisa estar dentro da função
    if resposta.status_code == 200:
        dados_requisicao = resposta.json()
        print(dados_requisicao)
        temp = dados_requisicao["current"]["temp_c"]
        descricao = dados_requisicao["current"]["condition"]["text"]
        
        # Retorna os dados como um JSON para o Front End
        return jsonify({"temperatura": temp, "descricao": descricao})
    else:
        # Retorna um erro caso a requisição falhe
        return jsonify({"erro": "Nao foi possivel obter os dados do clima"}), 500

# Inicia o servidor
if __name__ == '__main__':
    app.run(debug=True)