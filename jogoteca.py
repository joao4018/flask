from flask import Flask, render_template
from flask_mysqldb import MySQL

from dao.jogoDao import JogoDao
from database import usuario1, usuario2, usuario3, jogo2, jogo1
from services import JogoService, UserService

app = Flask(__name__)
app.secret_key = 'jao'
app.config['MYSQL_HOST'] = "127.0.0.1"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "password"
app.config['MYSQL_DB'] = "jogoteca"
app.config['MYSQL_PORT'] = 3306


db = MySQL(app)

jogo_dao = JogoDao(db)

usuarios = {usuario1.id: usuario1,
            usuario2.id: usuario2,
            usuario3.id: usuario3}


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos',
                           jogos=jogo_dao.listar())

@app.route('/novo')
def novo():
    return JogoService.novo()

@app.route('/criar', methods=['POST', ])
def criar():
    return JogoService.criar(jogo_dao)

@app.route('/login')
def login():
    return UserService.login()

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    return UserService.autenticar()

@app.route('/logout')
def logout():
    return UserService.logout()

app.run(debug=True)
