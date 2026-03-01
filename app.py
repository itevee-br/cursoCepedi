from flask import Flask, request, jsonify, render_template_string
import logging

app = Flask(__name__)

# Configuração de logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

USUARIO = "admin"
SENHA = "1234"
TOKEN_VALIDO = "token123"

# -------------------------
# Página inicial
# -------------------------
@app.route('/')
def home():
    return '''
    <h2>API de WebServices</h2>
    <ul>
        <li><a href="/login">Login (Autenticação)</a></li>
        <li><a href="/dados">Acessar Dados (Autorização)</a></li>
    </ul>
    '''

# -------------------------
# LOGIN – Autenticação
# -------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
        <h2>Login</h2>
        <form method="post">
            Usuário: <input type="text" name="usuario"><br><br>
            Senha: <input type="password" name="senha"><br><br>
            <button type="submit">Entrar</button>
        </form>
        '''

    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    if usuario == USUARIO and senha == SENHA:
        logging.info("Usuário autenticado com sucesso")
        return f'''
        <h3>Autenticação realizada com sucesso!</h3>
        <p>Seu token é: <b>{TOKEN_VALIDO}</b></p>
        <a href="/dados">Ir para autorização</a>
        '''
    else:
        logging.warning("Falha na autenticação")
        return '''
        <h3>Credenciais inválidas</h3>
        <a href="/login">Tentar novamente</a>
        '''

# -------------------------
# DADOS – Autorização
# -------------------------
@app.route('/dados', methods=['GET', 'POST'])
def dados():
    if request.method == 'GET':
        return '''
        <h2>Acesso aos Dados</h2>
        <form method="post">
            Token: <input type="text" name="token"><br><br>
            <button type="submit">Acessar</button>
        </form>
        '''

    token = request.form.get('token')

    if token == TOKEN_VALIDO:
        logging.info("Acesso autorizado")
        return '''
        <h3>Acesso autorizado!</h3>
        <p>Dados: [10, 20, 30, 40]</p>
        '''
    else:
        logging.warning("Token inválido")
        return '''
        <h3>Acesso negado</h3>
        <p>Token inválido</p>
        <a href="/dados">Tentar novamente</a>
        '''

# -------------------------
# Execução
# -------------------------
if __name__ == '__main__':
    logging.info("API iniciada")
    app.run(debug=True)
    