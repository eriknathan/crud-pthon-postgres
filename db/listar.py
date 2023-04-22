import psycopg2
from db import connection


def listar():
    """Função para listar todas as pessoas cadastradas no banco de dados"""
    global cursor
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM pessoas")
        pessoas = cursor.fetchall()
        return pessoas
    except psycopg2.Error as e:
        print("Ocorreu um erro ao tentar listar as pessoas:", e)
        # adicione aqui ação de recuperação do erro, se possível
    finally:
        if cursor:
            cursor.close()
