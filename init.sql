CREATE TABLE pessoas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    idade INTEGER,
    cpf VARCHAR(11) NOT NULL
);
