import requests
import json
from flask import Flask, render_template, request
import pprint
import base64
import pandas as pd

# instancia o meu app no servidor
app = Flask(__name__)

'''@app.route('/ibge/<cep>')
def retornaIBGE(cep):
    url = "https://viacep.com.br/ws/"+cep+"/json/"
    dados = requests.get(url)
    return dados.json()
  #dataset = pd.DataFrame(dados.json(), index=[0])
'''


@app.route('/ibge/', methods=['GET', 'POST'])
def getCEP():
    cep = request.args.get("cep")
    # cep = request.form.get("cep")
    url = "https://viacep.com.br/ws/" + cep + "/json/"
    dados = requests.get(url)
    return dados.json()
    # return cep


@app.route('/meme/')
def getMeme():
    resposta = requests.get('https://api.chucknorris.io/jokes/random')  # resquests (biblioteca externa do flask)
    chuck = resposta.json()['url']
    return render_template('chuck.html', chuckNoris=chuck)
    # return resposta.json()

@app.route('/chuck/')
def getChuck():
    resposta = requests.get('https://meme-api.herokuapp.com/gimme')  # resquests (biblioteca externa do flask)
    meme = resposta.json()['url']
    return render_template('meme.html', imagem_meme=meme)
    # return resposta.json()

@app.route('/tradutor/')
def getTrad():
    trad = request.args.get("tradutorV")
    url = 'https://api.gotit.ai/Translation/v1.1/Translate'
    data = {"T": str(trad), "SL": "EnUs", "TL": "PtBr"}
    data_json = json.dumps(data)
    userAndPass = base64.b64encode(b"2184-1eWNhD1W:KFjVctG7B1eHixhmED4IfnplwNfoZbs0").decode("ascii")
    headers = {'Content-type': 'application/json', "Authorization": "Basic %s" % userAndPass}
    response = requests.post(url, data=data_json, headers=headers)
    return response.json()
    # return resposta.json()

@app.route('/trad')
def trad():
    return render_template('tradutor.html')

@app.route('/')
def index():
    return render_template('index.html')
    # return render_template('meme.html')


if __name__ == '__main__':
    app.run()
