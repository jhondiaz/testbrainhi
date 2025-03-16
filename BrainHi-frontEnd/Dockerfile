# Etapa 1: Construcción de la aplicación Angular
FROM node:18 AS build

WORKDIR /app

# Copiar package.json e instalar dependencias
COPY package.json package-lock.json ./
RUN npm install

# Copiar el resto del código y compilar la app
COPY . .

RUN npm run build --configuration=production

# Etapa 2: Servir con NGINX
FROM nginx:latest

WORKDIR /usr/share/nginx/html

# Copiar la aplicación compilada a la carpeta de NGINX
COPY --from=build /app/dist/fuse ./

COPY nginx.conf /etc/nginx/conf.d/default.conf

#COPY nginx.conf /etc/nginx/conf.d/default.conf

# Exponer el puerto 80
EXPOSE 80

# Iniciar NGINX
CMD ["nginx", "-g", "daemon off;"]

