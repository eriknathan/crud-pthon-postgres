from database.listar import listar


def listar_pessoas():
    pessoas = listar()
    print("Lista de pessoas cadastradas:")
    for pessoa in pessoas:
        print(f"ID: {pessoa[0]} - Nome: {pessoa[1]} - Idade: {pessoa[2]}")
