import requests

cep = input("Digite o CEP: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Logradouro: {data['logradouro']}")
    print(f"Bairro: {data['bairro']}")
    print(f"Cidade: {data['localidade']}")
    print(f"Estado: {data['uf']}")
else:
    print("Não foi possível obter informações para o CEP informado.")