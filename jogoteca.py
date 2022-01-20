from flask import Flask, render_template, request, redirect, flash, session, url_for

from database import usuario1, usuario2, usuario3, jogo2, jogo1
from model.Jogo import Jogo
from services import JogoService, UserService

app = Flask(__name__)
app.secret_key = 'jao'

usuarios = {usuario1.id: usuario1,
            usuario2.id: usuario2,
            usuario3.id: usuario3}
lista = [jogo1, jogo2]


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos',
                           jogos=lista)
@app.route('/novo')
def novo():
    return JogoService.novo()

@app.route('/criar', methods=['POST', ])
def criar():
    return JogoService.criar(lista)

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
