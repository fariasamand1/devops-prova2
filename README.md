# Projeto Lista de Tarefas

Este é um projeto simples de lista de tarefas usando uma aplicação frontend com Nginx, backend com Node.js, banco de dados PostgreSQL e um mock API para simulação de dados. O projeto utiliza Docker para facilitar a configuração e execução em containers.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

devops-prova/ ├── backend/ │ ├── Dockerfile │ ├── package.json │ ├── src/ │ │ ├── app.js │ │ ├── controllers.js │ │ └── routes.js │ └── wait-for-db.sh ├── frontend/ │ ├── Dockerfile │ ├── index.html │ ├── script.js │ └── style.css ├── init-scripts/ │ ├── init.sql │ └── backup_.sql ├── mock-api/ │ ├── Dockerfile │ ├── app.py │ └── requirements.txt ├── docker-compose.yml ├── nginx.conf ├── package.json └── prod.dockerfile


## Pré-requisitos

Antes de começar, você precisa ter o Docker e o Docker Compose instalados em sua máquina.

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)


## Crie o arquivo .env

 Antes de rodar o Docker Compose, você precisa configurar algumas variáveis de ambiente. Crie um arquivo .env na raiz do projeto com as seguintes variáveis:

POSTGRES_USER=usuario
POSTGRES_PASSWORD=senha
POSTGRES_DB=meu_banco

## Inicie os containers

Agora você pode rodar os containers usando o Docker Compose:

docker-compose up --build

Esse comando irá:

- Construir as imagens Docker para o frontend, backend, mock API e banco de dados PostgreSQL.
- Criar e iniciar os containers.
- Configurar o banco de dados e carregar os dados iniciais.

## Detalhes do Projeto

Frontend: A aplicação frontend é construída com HTML, CSS e JavaScript. Ela permite ao usuário adicionar e marcar tarefas como concluídas.
Backend: O backend é construído com Node.js e Express. Ele se comunica com o banco de dados PostgreSQL e fornece dados para o frontend.
Banco de Dados: O banco de dados utilizado é o PostgreSQL, que armazena informações sobre as tarefas.
Mock API: A API mock fornece dados falsos para testar a comunicação entre o backend e a API externa.

## Estrutura do Dockerfile

O Dockerfile do frontend é dividido em três partes:

1 - Configuração do Nginx para servir arquivos estáticos (index.html e style.css).

2 - Construção do Frontend com Node.js (instalação de dependências e execução do build).

3 - Configuração do Nginx para servir a build gerada na etapa anterior.

## Scripts de Inicialização

O script init.sql cria a tabela tasks no banco de dados PostgreSQL com alguns dados iniciais, como tarefas de exemplo.
O script wait-for-db.sh é utilizado pelo backend para aguardar o banco de dados estar disponível antes de iniciar o servidor.

## Comandos Docker

Subir os containers: docker-compose up --build
Parar os containers: docker-compose down
Visualizar os logs: docker-compose logs -f




