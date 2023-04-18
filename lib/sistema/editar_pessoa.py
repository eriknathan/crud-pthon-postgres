from lib.interface import cabecalho, linha, limpa_tela
from lib.interface.menu import menu
import database
import time


def editar_pessoa():
    cabecalho("EDITAR PESSOA")

    id = int(input("Digite o ID da pessoa que deseja editar: "))
    print(linha())

    print('Você deseja editar: ')
    opcao = menu([
        'Nome',
        'Idade',
        'CPF',
        'Todos'])
    print(linha())

    if opcao == 1:
        nome = str(input('Digite o novo nome: '))
        database.editar_nome(id, nome)
        time.sleep(1)
        print('Nome atualizado com sucesso! ')
        time.sleep(2)
        limpa_tela()

    elif opcao == 2:
        idade = input('Digite a nova idade: ')
        database.editar_idade(id, idade)
        time.sleep(1)
        print('Idade atualizada com sucesso! ')
        time.sleep(2)
        limpa_tela()

    elif opcao == 3:
        cpf = input('Digite o novo CPF: ')
        cpf = cpf.replace(".", "").replace("-", "")
        database.editar_cpf(id, cpf)
        time.sleep(1)
        print("CPF atualizado com sucesso!")
        time.sleep(2)
        limpa_tela()

    elif opcao == 4:
        nome = input("Digite o novo nome da pessoa: ")
        idade = int(input("Digite a nova idade da pessoa: "))
        cpf = input('Digite o novo CPF: ')
        cpf = cpf.replace(".", "").replace("-", "")
        database.editar(id, nome, idade, cpf)
        time.sleep(1)
        print('Pessoa atualizada com sucesso! ')
        time.sleep(2)
        limpa_tela()

    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')