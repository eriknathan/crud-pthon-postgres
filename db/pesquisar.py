import psycopg2
from db import connection


def pesquisar(matricula):
    global cursor
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM pessoas WHERE matricula = '%s'", (matricula,))
        pessoas = cursor.fetchall()
        return pessoas
    except psycopg2.Error as e:
        print("Ocorreu um erro ao tentar pesquisar as pessoas:", e)
    finally:
        if cursor:
            cursor.close()
