FROM python:3.12-slim

# Actualiza e instala paquetes necesarios 
 
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    build-essential \  
    git \
    curl \
    nano \
    unzip \
    libzip-dev \
    libpng-dev \
    libonig-dev \ 
    && apt-get clean 
    


# Instala herramientas adicionales de Python
RUN pip install --no-cache-dir pipenv 

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["uvicorn","src.main:app","--host","0.0.0.0","--port","80"]
