import psycopg2
from db import connection


def editar(matricula, nome, celular, email, data_nasc, sexo, cpf, cep):
    global cursor
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE pessoas SET nome = %s, celular = %s, email = %s, data_nasc = %s, sexo = %s,"
                       "cpf = %s, cep = %s WHERE matricula = '%s'"
                       ,(nome, celular, email, data_nasc, sexo, cpf, cep, matricula))
        connection.commit()
    except psycopg2.Error as e:
        print("Ocorreu um erro ao tentar editar os dados no banco de dados:", e)
    finally:
        if cursor:
            cursor.close()


def editar_nome(matricula, nome):
    global cursor
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE pessoas SET nome = %s WHERE matricula = '%s'", (nome, matricula))
        connection.commit()
    except psycopg2.Error as e:
        print("Ocorreu um erro ao tentar editar o nome no banco de dados:", e)
    finally:
        if cursor:
            cursor.close()


def editar_celular(matricula, celular):
    global cursor
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE pessoas SET celular = %s WHERE matricula = '%s'", (celular, matricula))
        connection.commit()
    except psycopg2.Error as e:
        print("Ocorreu um erro ao tentar editar o celular no banco de dados:", e)
    finally:
        if cursor:
            cursor.close()


def editar_email(matricula, email):
    global cursor
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE pessoas SET email = %s WHERE matricula = '%s'", (email, matricula))
        connection.commit()
    except psycopg2.Error as e:
        print("Ocorreu um erro ao tentar editar o email no banco de dados:", e)
    finally:
        if cursor:
            cursor.close()


def editar_data_nasc(matricula, data_nasc):
    global cursor
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE pessoas SET data_nasc = %s WHERE matricula = '%s'", (data_nasc, matricula))
        connection.commit()
    except psycopg2.Error as e:
        print("Ocorreu um erro ao tentar editar a data de nascimento no banco de dados:", e)
    finally:
        if cursor:
            cursor.close()


def editar_sexo(matricula, sexo):
    global cursor
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE pessoas SET sexo = %s WHERE matricula = '%s'", (sexo, matricula))
        connection.commit()
    except psycopg2.Error as e:
        print("Ocorreu um erro ao tentar editar o sexo no banco de dados:", e)
    finally:
        if cursor:
            cursor.close()


def editar_cpf(matricula, cpf):
    global cursor
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE pessoas SET cpf = %s WHERE matricula = '%s'", (cpf, matricula))
        connection.commit()
    except psycopg2.Error as e:
        print("Ocorreu um erro ao tentar editar o cpf no banco de dados:", e)
    finally:
        if cursor:
            cursor.close()


def editar_cep(matricula, cep):
    global cursor
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE pessoas SET cep = %s WHERE matricula = '%s'", (cep, matricula))
        connection.commit()
    except psycopg2.Error as e:
        print("Ocorreu um erro ao tentar editar o cep no banco de dados:", e)
    finally:
        if cursor:
            cursor.close()