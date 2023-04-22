import psycopg2
from db import connection


def excluir(matricula):
    global cursor
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM pessoas WHERE matricula = '%s'", (matricula,))
        connection.commit()
    except psycopg2.Error as e:
        print("Ocorreu um erro ao tentar editar o sexo no banco de dados:", e)
    finally:
        if cursor:
            cursor.close()
