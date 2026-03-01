
from flask import Flask, render_template_string
from flask_socketio import SocketIO, send
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    return render_template_string('''
    <h2>Chat em Tempo Real</h2>
    <input id="msg" placeholder="Digite sua mensagem">
    <button onclick="enviar()">Enviar</button>
    <ul id="mensagens"></ul>

    <script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>
    <script>
        var socket = io();
        socket.on('message', function(msg) {
            var li = document.createElement("li");
            li.innerText = msg;
            document.getElementById("mensagens").appendChild(li);
        });
        function enviar() {
            var msg = document.getElementById("msg").value;
            socket.send(msg);
        }
    </script>
    ''')

@socketio.on('message')
def handle_message(msg):
    logging.info(f"Mensagem recebida: {msg}")
    send(msg, broadcast=True)

if __name__ == '__main__':
    logging.info("Servidor WebSocket iniciado")
    socketio.run(app, 
                 debug=True,
                 host='10.70.60.73', 
                 port=8080)