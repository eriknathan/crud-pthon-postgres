import os
from lib.interface import linha, cabecalho
import database


def listar_pessoa():
    pessoas = database.listar()
    cabecalho("PESSOAS CADASTRADAS")
    for pessoa in pessoas:
        print(f"\033[34mID:\033[m {pessoa[0]}{os.linesep}"
              f"\033[34mNome:\033[m {pessoa[1]}{os.linesep}"
              f"\033[34mIdade:\033[m {pessoa[2]}{os.linesep}"
              f"\033[34mCPF:\033[m {pessoa[3]}{os.linesep}{linha()}")

