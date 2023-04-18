import database
import os
from lib.interface import cabecalho, linha, limpa_tela


def pesquisar_pessoa():
    cabecalho("PESQUISAR PESSOAS")
    id = int(input("ID para pesquisa: "))
    pessoas = database.pesquisar(id)
    limpa_tela()
    cabecalho("PESQUISA")
    for pessoa in pessoas:
        print(f"\033[34mID:\033[m {pessoa[0]}{os.linesep}"
              f"\033[34mNome:\033[m {pessoa[1]}{os.linesep}"
              f"\033[34mIdade:\033[m {pessoa[2]}{os.linesep}"
              f"\033[34mCPF:\033[m {pessoa[3]}{os.linesep}{linha()}")

