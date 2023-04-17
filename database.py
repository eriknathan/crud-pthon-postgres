import psycopg2

# INFORMAÇÕES PARA CONECÇÃO NO BANCO DE DADOS
connection = psycopg2.connect(
    host="localhost",
    port=5432,
    database="pessoas",
    user="admin",
    password="admin"
)


def cadastrar(nome, idade):
    """Função para cadastrar uma pessoa no banco de dados"""
    cursor = connection.cursor()
    cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (%s, %s)", (nome, idade))
    connection.commit()
    cursor.close()


def listar():
    """Função para listar todas as pessoas cadastradas no banco de dados"""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pessoas")
    pessoas = cursor.fetchall()
    cursor.close()
    return pessoas
