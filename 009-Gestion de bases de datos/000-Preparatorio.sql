-- sudo mysql -u root -p

CREATE DATABASE empresadam2026;
USE empresadam2026;

CREATE TABLE clientes(
    nombre VARCHAR (255),
    apellidos VARCHAR(255),
    email VARCHAR(255)
);

INSERT INTO clientes VALUES(
    'Ruth',
    'Sainz Santos-Olmo',
    'rutsaisan@gmail.com'
);

SELECT * FROM clientes;