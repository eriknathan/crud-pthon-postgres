from db import connection


def pesquisar(matricula):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pessoas WHERE matricula = '%s'", (matricula,))
    pessoas = cursor.fetchall()
    cursor.close()
    return pessoas