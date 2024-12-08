# Etapa 1: Construção do frontend com Node.js
FROM node:18-alpine AS build
WORKDIR /app

# Copia os arquivos de configuração e instala as dependências
COPY package.json package-lock.json ./
RUN npm install

# Copia o restante dos arquivos do frontend e gera a build
COPY . . 
RUN npm run build

# Etapa 2: Configuração do Nginx para servir os arquivos estáticos
FROM nginx:alpine

# Copia os arquivos de build para o Nginx
COPY --from=build /app/build /usr/share/nginx/html

# Copia a configuração personalizada do Nginx (se necessário)
COPY nginx.conf /etc/nginx/nginx.conf

# Expondo a porta 80
EXPOSE 80

# Inicia o Nginx
CMD ["nginx", "-g", "daemon off;"]
