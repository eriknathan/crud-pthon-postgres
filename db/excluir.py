from db import connection


def excluir(matricula):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM pessoas WHERE matricula = '%s'", (matricula,))
    connection.commit()
    cursor.close()

