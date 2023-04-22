from lib.interface import cabecalho, linha, limpa_tela
from lib.interface.menu import menu
from db.editar import editar, editar_nome, editar_celular, editar_email,\
    editar_data_nasc, editar_sexo, editar_cpf, editar_cep
import time
import os
from db.pesquisar import pesquisar


def editar_pessoa():
    cabecalho("EDITAR PESSOA")

    matricula = int(input("Matrícula que deseja editar: "))
    limpa_tela()
    print(linha())
    pessoas = pesquisar(matricula)
    for pessoa in pessoas:
        print(f"\033[34mID:\033[m {pessoa[0]}{os.linesep}"
              f"\033[34mMatricula:\033[m {pessoa[1]}{os.linesep}"
              f"\033[34mNome:\033[m {pessoa[2]}{os.linesep}"
              f"\033[34mCeluar:\033[m {pessoa[3]}{os.linesep}"
              f"\033[34mEmail:\033[m {pessoa[4]}{os.linesep}"
              f"\033[34mData de Nasc.:\033[m {pessoa[5]}{os.linesep}"
              f"\033[34mSexo:\033[m {pessoa[6]}{os.linesep}"
              f"\033[34mCPF:\033[m {pessoa[7]}{os.linesep}"
              f"\033[34mCEP:\033[m {pessoa[8]}{os.linesep}"
              f"\033[34mRua:\033[m {pessoa[9]}{os.linesep}"
              f"\033[34mBairro:\033[m {pessoa[10]}{os.linesep}"
              f"\033[34mCidade:\033[m {pessoa[11]}{os.linesep}"
              f"\033[34mEstado:\033[m {pessoa[12]}{os.linesep}")
    print(linha())

    print('Você deseja editar: ')
    opcao = menu([
        'Nome',
        'Celular',
        'Email',
        'Data de nasc.',
        'Sexo',
        'CPF',
        'CEP',
        'Todos'])
    print(linha())

    if opcao == 1:
        nome = str(input('Novo nome: '))
        editar_nome(matricula, nome)
        time.sleep(1)
        print('Nome atualizado com sucesso! ')
        time.sleep(2)
        limpa_tela()

    elif opcao == 2:
        celular = input('Novo celular: ')
        editar_celular(matricula, celular)
        time.sleep(1)
        print('Celualr atualizado com sucesso! ')
        time.sleep(2)
        limpa_tela()

    elif opcao == 3:
        email = input('Novo Email: ')
        editar_email(matricula, email)
        time.sleep(1)
        print("Email atualizado com sucesso!")
        time.sleep(2)
        limpa_tela()

    elif opcao == 4:
        data_nasc = input('Nova Data de Nasc.: ')
        editar_data_nasc(matricula, data_nasc)
        time.sleep(1)
        print("Data de Nasc. atualizado com sucesso!")
        time.sleep(2)
        limpa_tela()

    elif opcao == 5:
        sexo = input('Novo Sexo: ')
        editar_sexo(matricula, sexo)
        time.sleep(1)
        print("Sexo atualizado com sucesso!")
        time.sleep(2)
        limpa_tela()

    elif opcao == 6:
        cpf = input('Novo CPF: ')
        editar_cpf(matricula, cpf)
        time.sleep(1)
        print("CPF atualizado com sucesso!")
        time.sleep(2)
        limpa_tela()

    elif opcao == 7:
        cep = input('Novo CEP: ')
        editar_cep(matricula, cep)
        time.sleep(1)
        print("CEP atualizado com sucesso!")
        time.sleep(2)
        limpa_tela()

    elif opcao == 8:
        nome = input("Novo nome: ")
        celular = int(input("Novo celular: "))
        email = input('Novo Email: ')
        data_nasc = input('Nova Data de Nasc.: ')
        sexo = input('Novo Sexo: ')
        cpf = input('Digite o novo CPF: ')
        cpf = cpf.replace(".", "").replace("-", "")
        cep = input('Novo CEP: ')
        editar(matricula, nome, celular, email, data_nasc, sexo, cpf, cep)
        time.sleep(1)
        print('Pessoa atualizada com sucesso! ')
        time.sleep(2)
        limpa_tela()

    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')