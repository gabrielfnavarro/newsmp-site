from flask import Flask, render_template, request
from mcstatus import JavaServer
import requests

app = Flask(__name__, static_folder='static', static_url_path='/static')
server = JavaServer.lookup("newsmpworld.jogar.io")
DISCORD_WEBHOOK_URL = 'https://ptb.discord.com/api/webhooks/1193912475620474961/Qubz2HTgLa_uzawPhwp91-Nts1x7R7XjGz0oQsXMn5ZW81V8ttpCTi842l5ScaMxJGIi'


@app.route('/')
def index():
    status = server.status()
    player_count = status.players.online
    print(status.players.sample[0])
    return render_template('index.html', player_count=player_count)

@app.route('/lores')
def lore():
    return render_template('lores.html')

@app.route('/staffs')
def staff():
    return render_template('staffs.html')

@app.route('/whitelist')
def whitelist():
    return render_template('whitelist.html')

@app.route('/processar_formulario', methods=['POST'])
def processar_formulario():
    nick = request.form['nick']
    intencoes = request.form['intencoes']
    como_chegou = request.form['como_chegou']

    # Criar o payload para enviar para o webhook do Discord com um conjunto de campos
    payload = {
        'embeds': [{
            'title': 'Novo Formulário Enviado!',
            'color': 0x9925be,  # Cor do embed (verde neste exemplo)
            'fields': [
                {'name': '`Nick`', 'value': nick, 'inline': False},
                {'name': '`Intenções`', 'value': intencoes, 'inline': False},
                {'name': '`Como chegou`', 'value': como_chegou, 'inline': False},
            ]
        }]
    }

    # Fazer a solicitação HTTP POST para o webhook do Discord
    response = requests.post(DISCORD_WEBHOOK_URL, json=payload)

    if response.status_code == 204:
        return 'Dados enviados com sucesso para o Discord!'
    else:
        return 'Erro ao enviar dados para o Discord.'

if __name__ == '__main__':
    app.run(debug=True)
