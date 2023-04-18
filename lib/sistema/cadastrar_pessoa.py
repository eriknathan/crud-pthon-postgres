import database


# Função para validar o CPF
def validar_cpf(cpf):
    # Remover os pontos e traços do CPF
    cpf = cpf.replace(".", "").replace("-", "")
    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False
    # Verificar se todos os dígitos do CPF são iguais
    if cpf == cpf[0] * 11:
        return False
    # Calcular o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto
    # Calcular o segundo dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (11 - i)
    soma += digito1 * 2
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto
    # Verificar se os dígitos verificadores são válidos
    if cpf[-2:] == str(digito1) + str(digito2):
        return True
    else:
        return False


def cadastrar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    cpf = input("Digite o cpf: ")

    if validar_cpf(cpf):
        database.cadastrar(nome, idade, cpf)
        print("Pessoa cadastrada com sucesso!")
    else:
        print('CPF inválido!')
        return cadastrar_pessoa()
