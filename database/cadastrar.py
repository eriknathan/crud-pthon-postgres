from database import connection


def cadastrar(nome, idade):
    """Função para cadastrar uma pessoa no banco de dados"""
    cursor = connection.cursor()

    cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (%s, %s)", (nome, idade))

    connection.commit()
    cursor.close()
