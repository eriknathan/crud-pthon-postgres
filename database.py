import psycopg2

# INFORMAÇÕES PARA CONECÇÃO NO BANCO DE DADOS
connection = psycopg2.connect(
    host="localhost",
    port=5432,
    database="pessoas",
    user="admin",
    password="admin"
)


def cadastrar(matricula, nome, idade, cpf, data):
    """Função para cadastrar uma pessoa no banco de dados"""
    cursor = connection.cursor()
    cursor.execute("INSERT INTO pessoas (matricula, nome, idade, cpf, cep, logradouro, bairro, localidade, uf) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (matricula, nome, idade, cpf, data['cep'], data['logradouro'], data['bairro'], data['localidade'], data['uf']))
    connection.commit()
    cursor.close()


def listar():
    """Função para listar todas as pessoas cadastradas no banco de dados"""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pessoas")
    pessoas = cursor.fetchall()
    cursor.close()
    return pessoas


def editar(matricula, nome, idade, cpf):
    cursor = connection.cursor()
    cursor.execute("UPDATE pessoas SET nome = %s, idade = %s, cpf = %s WHERE matricula = '%s'", (nome, idade, cpf, id))
    connection.commit()
    cursor.close()


def editar_nome(matricula, nome):
    cursor = connection.cursor()
    cursor.execute("UPDATE pessoas SET nome = %s WHERE matricula = '%s'", (nome, matricula))
    connection.commit()
    cursor.close()


def editar_idade(matricula, idade):
    cursor = connection.cursor()
    cursor.execute("UPDATE pessoas SET idade = %s WHERE matricula = '%s'", (idade, matricula))
    connection.commit()
    cursor.close()


def editar_cpf(matricula, cpf):
    cursor = connection.cursor()
    cursor.execute("UPDATE pessoas SET cpf = %s WHERE matricula = '%s'", (cpf, matricula))
    connection.commit()
    cursor.close()


def excluir(matricula):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM pessoas WHERE matricula = '%s'", (matricula,))
    connection.commit()
    cursor.close()


def pesquisar(matricula):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pessoas WHERE matricula = '%s'", (matricula,))
    pessoas = cursor.fetchall()
    cursor.close()
    return pessoas
