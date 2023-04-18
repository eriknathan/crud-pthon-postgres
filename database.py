import psycopg2

# INFORMAÇÕES PARA CONECÇÃO NO BANCO DE DADOS
connection = psycopg2.connect(
    host="localhost",
    port=5432,
    database="pessoas",
    user="admin",
    password="admin"
)


def cadastrar(nome, idade, cpf):
    """Função para cadastrar uma pessoa no banco de dados"""
    cursor = connection.cursor()
    cursor.execute("INSERT INTO pessoas (nome, idade, cpf) VALUES (%s, %s, %s)", (nome, idade, cpf))
    connection.commit()
    cursor.close()


def listar():
    """Função para listar todas as pessoas cadastradas no banco de dados"""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pessoas")
    pessoas = cursor.fetchall()
    cursor.close()
    return pessoas


def excluir(id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM pessoas WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
