CREATE TABLE pessoas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    idade INTEGER,
    cpf VARCHAR(11) NOT NULL,
    cep VARCHAR(8),
    logradouro VARCHAR(100),
    bairro VARCHAR(80),
    localidade VARCHAR(80),
    uf VARCHAR(2)
)