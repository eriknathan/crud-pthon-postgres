from lib.interface import linha, leia_int


def menu(lista):
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[33m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leia_int('\033[32mSua Opção: \033[m')
    return opc
