import time

from db.excluir import excluir
from lib.interface import cabecalho, linha, limpa_tela


def excluir_pessoa():
    cabecalho("EXCLUIR PESSOA")
    matricula = int(input("Matricula que você quer excluir: "))
    excluir(matricula)
    print(linha())
    print("Pessoa excluida com sucesso!")
    time.sleep(2)
    limpa_tela()
