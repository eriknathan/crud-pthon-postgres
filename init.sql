CREATE TABLE pessoas (
    id SERIAL PRIMARY KEY,
    matricula VARCHAR(10),
    nome VARCHAR(100),
    celular varchar(15),
    email varchar(255),
    data_nasc varchar(10),
    sexo varchar(10),
    cpf VARCHAR(11) NOT NULL,
    cep VARCHAR(8),
    logradouro VARCHAR(100),
    bairro VARCHAR(80),
    localidade VARCHAR(80),
    uf VARCHAR(2)
)