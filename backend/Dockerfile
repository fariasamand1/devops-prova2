# Usando imagem oficial do Node.js
FROM node:14-alpine

# Definindo diretório de trabalho
WORKDIR /app

# Copia os arquivos de configuração e dependências
COPY package*.json ./
RUN npm install

# Copia o restante do código
COPY . .

# Expõe a porta onde a aplicação Node.js vai rodar
EXPOSE 3000

# Comando para iniciar o servidor Express
CMD ["node", "src/app.js"]
