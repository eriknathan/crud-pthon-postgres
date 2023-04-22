import psycopg2
from db import connection


def cadastrar(matricula, nome, celular, email, data_nasc, sexo, cpf, data):
    """Função para cadastrar uma pessoa no banco de dados"""
    global cursor
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO pessoas (matricula, nome, celular, email, data_nasc, sexo, cpf, cep, logradouro, "
                       "bairro, localidade, uf)"
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (matricula, nome, celular, email, data_nasc, sexo, cpf, data['cep'], data['logradouro'], data['bairro'], data['localidade'], data['uf']))
        connection.commit()
    except psycopg2.Error as e:
        print("Ocorreu um erro ao tentar inserir os dados no banco de dados:", e)
    finally:
        if cursor:
            cursor.close()

