CREATE DATABASE sample;

CREATE TABLE sample.transactions (
    id INT(7) PRIMARY KEY,
    name VARCHAR(64) NOT NULL,
    amount DOUBLE NOT NULL
);
INSERT INTO sample.transactions VALUES
    (1, "foo", 100),
    (2, "bar", 200);
