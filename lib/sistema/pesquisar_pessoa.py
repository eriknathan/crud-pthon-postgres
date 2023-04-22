from db.pesquisar import pesquisar
import os
from lib.interface import cabecalho, limpa_tela


def pesquisar_pessoa():
    cabecalho("PESQUISAR PESSOAS")
    matricula = int(input("Matrícula para pesquisa: "))
    pessoas = pesquisar(matricula)
    limpa_tela()
    cabecalho("PESQUISA")
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

