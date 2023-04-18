import time

import database
from lib.interface import cabecalho, linha, limpa_tela


def excluir_pessoa():
    cabecalho("EXCLUIR PESSOA")
    id = int(input("ID que você quer excluir: "))
    database.excluir(id)
    print(linha())
    print("Pessoa excluida com sucesso!")
    time.sleep(2)
    limpa_tela()
