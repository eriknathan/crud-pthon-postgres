from database.crud import connection


def cadastrar_pessoa(nome, idade):
    """Função para cadastrar uma pessoa no banco de dados"""
    cursor = connection.cursor()

    cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (%s, %s)", (nome, idade))

    connection.commit()
    cursor.close()
