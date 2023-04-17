import database


def cadastrar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    database.cadastrar(nome, idade)
    print("Pessoa cadastrada com sucesso!")
