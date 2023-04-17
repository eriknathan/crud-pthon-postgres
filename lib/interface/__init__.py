import os

def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
