import requests
from flask import Flask, render_template, request

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
    resposta = requests.get('https://meme-api.herokuapp.com/gimme')  # resquests (biblioteca externa do flask)
    meme = resposta.json()['url']
    return render_template('meme.html', imagem_meme=meme)
    # return resposta.json()


@app.route('/')
def index():
    return render_template('index.html')
    # return render_template('meme.html')


if __name__ == '__main__':
    app.run()
