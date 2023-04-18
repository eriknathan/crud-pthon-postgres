from lib.interface import cabecalho, linha, limpa_tela
from getpass import getpass
from lib.sistema import sistema
import time

usuario_correto = 'admin'
senha_correta = 'admin'


def fazer_login():
    cabecalho('ENTRAR NO SISETEMA')
    login = str(input('Login: '))
    password = getpass('Senha: ')

    print(linha())

    if login == usuario_correto and password == senha_correta:
        print('Acessando sistema...')
        time.sleep(1)
        limpa_tela()
        sistema()

    else:
        print('Acesso Negado!')
        time.sleep(1)
        limpa_tela()
        return fazer_login()
