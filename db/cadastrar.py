from db import connection
import psycopg2


def cadastrar(matricula, nome, celular, email, data_nasc, sexo, cpf, data):
    """Função para cadastrar uma pessoa no banco de dados"""
    cursor = connection.cursor()
    cursor.execute("INSERT INTO pessoas (matricula, nome, celular, email, data_nasc, sexo, cpf, cep, logradouro, "
                   "bairro, localidade, uf)"
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (matricula, nome, celular, email, data_nasc, sexo, cpf, data['cep'], data['logradouro'], data['bairro'], data['localidade'], data['uf']))
    connection.commit()
    cursor.close()
