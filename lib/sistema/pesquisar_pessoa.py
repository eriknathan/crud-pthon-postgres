import database
import os
from lib.interface import cabecalho, limpa_tela


def pesquisar_pessoa():
    cabecalho("PESQUISAR PESSOAS")
    id = int(input("ID para pesquisa: "))
    pessoas = database.pesquisar(id)
    limpa_tela()
    cabecalho("PESQUISA")
    for pessoa in pessoas:
        print(f"\033[34mID:\033[m {pessoa[0]}{os.linesep}"
              f"\033[34mMatricula:\033[m {pessoa[9]}{os.linesep}"
              f"\033[34mNome:\033[m {pessoa[1]}{os.linesep}"
              f"\033[34mIdade:\033[m {pessoa[2]}{os.linesep}"
              f"\033[34mCPF:\033[m {pessoa[3]}{os.linesep}"
              f"\033[34mCEP:\033[m {pessoa[4]}{os.linesep}"
              f"\033[34mRua:\033[m {pessoa[5]}{os.linesep}"
              f"\033[34mBairro:\033[m {pessoa[6]}{os.linesep}"
              f"\033[34mCidade:\033[m {pessoa[7]}{os.linesep}"
              f"\033[34mEstado:\033[m {pessoa[8]}{os.linesep}")

