from db import connection


def editar(matricula, nome, celular, email, data_nasc, sexo, cpf, cep):
    cursor = connection.cursor()
    cursor.execute("UPDATE pessoas SET nome = %s, celular = %s, email = %s, data_nasc = %s, sexo = %s,"
                   "cpf = %s, cep = %s WHERE matricula = '%s'"
                   ,(nome, celular, email, data_nasc, sexo, cpf, cep, matricula))
    connection.commit()
    cursor.close()


def editar_nome(matricula, nome):
    cursor = connection.cursor()
    cursor.execute("UPDATE pessoas SET nome = %s WHERE matricula = '%s'", (nome, matricula))
    connection.commit()
    cursor.close()


def editar_celular(matricula, celular):
    cursor = connection.cursor()
    cursor.execute("UPDATE pessoas SET celular = %s WHERE matricula = '%s'", (celular, matricula))
    connection.commit()
    cursor.close()


def editar_email(matricula, email):
    cursor = connection.cursor()
    cursor.execute("UPDATE pessoas SET email = %s WHERE matricula = '%s'", (email, matricula))
    connection.commit()
    cursor.close()


def editar_data_nasc(matricula, data_nasc):
    cursor = connection.cursor()
    cursor.execute("UPDATE pessoas SET data_nasc = %s WHERE matricula = '%s'", (data_nasc, matricula))
    connection.commit()
    cursor.close()


def editar_sexo(matricula, sexo):
    cursor = connection.cursor()
    cursor.execute("UPDATE pessoas SET sexo = %s WHERE matricula = '%s'", (sexo, matricula))
    connection.commit()
    cursor.close()


def editar_cpf(matricula, cpf):
    cursor = connection.cursor()
    cursor.execute("UPDATE pessoas SET cpf = %s WHERE matricula = '%s'", (cpf, matricula))
    connection.commit()
    cursor.close()


def editar_cep(matricula, cep):
    cursor = connection.cursor()
    cursor.execute("UPDATE pessoas SET cep = %s WHERE matricula = '%s'", (cep, matricula))
    connection.commit()
    cursor.close()