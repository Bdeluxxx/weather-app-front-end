import requests 
import pprint

api_key = "abd2dba3225f441da0b193416252908"

link_api = "http://api.weatherapi.com/v1//current.json"

parametros = {
    "key": api_key,
    "q": "Horizontina",
    "lang": "pt"
}
resposta = requests .get (link_api, params=parametros) 


if resposta.status_code == 200:
    dados_requisicao = resposta. json()
    pprint.pprint (dados_requisicao)
    temp = dados_requisicao ["current"]["temp_c"]
    descricao = dados_requisicao ["current"]["condition"]["text"]
    print (temp)
    print (descricao)

# status code
# 200 deu certo a requisição
# 300 redirecionada
# 400 nao conseguiu fazer a requisição
# 500 deu um erro no sistema