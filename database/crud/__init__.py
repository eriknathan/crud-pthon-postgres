import psycopg2

# Define as informações para conexão com o banco de dados
connection = psycopg2.connect(
    host="localhost",
    port=5432,
    database="pessoas",
    user="admin",
    password="admin"
)
