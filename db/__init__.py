import psycopg2

# INFORMAÇÕES PARA CONECÇÃO NO BANCO DE DADOS
try:
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="pessoas",
        user="admin",
        password="admin"
    )
except psycopg2.Error as e:
    print("Ocorreu um erro ao tentar conectar ao banco de dados:", e)
