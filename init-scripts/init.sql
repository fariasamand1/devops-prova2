CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    text VARCHAR(255),
    completed BOOLEAN DEFAULT FALSE
);

INSERT INTO tasks (text, completed) VALUES
('Comprar leite', FALSE),
('Estudar para a prova', TRUE),
('Lavar a roupa', FALSE);
