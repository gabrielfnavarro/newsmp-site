from flask import Flask, render_template
from mcstatus import JavaServer

app = Flask(__name__, static_folder='static', static_url_path='/static')
server = JavaServer.lookup("newsmpworld.jogar.io")

@app.route('/')
def index():
    status = server.status()
    player_count = status.players.online
    print(status.players.sample[0])
    return render_template('index.html', player_count=player_count)

if __name__ == '__main__':
    app.run(debug=True)
