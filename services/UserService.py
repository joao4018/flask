from flask import render_template, request, session, flash, redirect, url_for

from jogoteca import usuarios


def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)

    else:
        flash('Não logado, tente de novo!')
        return redirect(url_for('login'))

def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('index'))