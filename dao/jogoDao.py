from consts import SQL_DELETA_JOGO, SQL_JOGO_POR_ID, SQL_BUSCA_JOGOS, SQL_CRIA_JOGO, SQL_ATUALIZA_JOGO
from model.Jogo import Jogo


class JogoDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, jogo):
        cursor = self.__db.connection.cursor()

        if (jogo.id):
            cursor.execute(SQL_ATUALIZA_JOGO, (jogo.nome, jogo.categoria, jogo.console, jogo.id))
        else:
            cursor.execute(SQL_CRIA_JOGO, (jogo.nome, jogo.categoria, jogo.console))
            jogo.id = cursor.lastrowid
        self.__db.connection.commit()
        return jogo

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_JOGOS)
        jogos = traduz_jogos(cursor.fetchall())
        return jogos

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_JOGO_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Jogo(tupla[1], tupla[2], tupla[3], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_JOGO, (id,))
        self.__db.connection.commit()


def cria_jogo_com_tupla(tupla):
    return Jogo(tupla[1], tupla[2], tupla[3], id=tupla[0])


def traduz_jogos(jogos):
    return list(map(cria_jogo_com_tupla, jogos))
