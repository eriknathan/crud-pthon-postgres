from database.crud import connection


def listar_pessoas():
    """Função para listar todas as pessoas cadastradas no banco de dados"""
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM pessoas")

    pessoas = cursor.fetchall()
    cursor.close()

    return pessoas
