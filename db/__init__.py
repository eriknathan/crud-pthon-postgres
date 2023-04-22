import psycopg2

# INFORMAÇÕES PARA CONECÇÃO NO BANCO DE DADOS
connection = psycopg2.connect(
    host="localhost",
    port=5432,
    database="pessoas",
    user="admin",
    password="admin"
)