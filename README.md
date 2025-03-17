[![Ar](Ar "Ar")](https://firebasestorage.googleapis.com/v0/b/tdriversuper.appspot.com/o/ar.png?alt=media&token=b6be5ae4-6c61-47a5-bfdc-a2950d4d8623 "Ar")

# About
Proyecto  de JHON HAROLD  DIAZ

# Test BrainHi
Plataforma  de registro de  pacientes  en  formato Hl7 .

# Tencologia
* FastAPI - Python 
* .Net Core
* MongoDb
* Angular 19
* RabbiMq
* Hapi-fhir

# Demo
FrontEnd

http://130.131.161.243/

BackEnd

http://135.233.78.208/

Hapi - fhir

http://hapi.fhir.org/baseR4

Video

https://drive.google.com/file/d/1gxHD7bpxp1usZSxCL1uwsVGlLMHpBp8s/view?usp=sharing

# Instalation

## Cuando se le solicite, acceda al directorio en el que desea descargar el proyecto.

 BackEnt - Python
```
https://github.com/jhondiaz/testbrainhi/tree/main/BrainHi-backEnd
```

## Create the virtual environment:

Creat un archivo .env dentro de la carpeta app  y  agragar  estas  claves
```
secret = "use your secret code with secrets.token_hex(10)"
algorithm = HS256
```

```
python -m venv venv

```

## Ejecute el entorno virtual:
### Windows
```
venv\Scripts\activate

```
### Linux/MacOS
```
source venv/bin/activate
```

## Instale los paquetes de Python necesarios::
```
pip install -r requirements.txt
pre-commit install

uvicorn main:app --host 0.0.0.0 --port 80 --reload

http://localhost:8081/docs

```
## Cuando se le solicite, acceda al directorio en el que desea descargar el proyecto.

FrontEnd- Angular 19

##Requisitos Previos
Antes de instalar Angular 19, asegúrate de contar con los siguientes requisitos:

✅ Node.js (versión 18.x o superior)
✅ npm (gestor de paquetes de Node.js)
✅ Angular CLI (interfaz de línea de comandos de Angular)
✅ Git (opcional, pero recomendado)

##Paso 1: Verificar Instalación de Node.js y npm
Abre una terminal y ejecuta los siguientes comandos para verificar las versiones instaladas:

```
node -v
npm -v

```
##Paso 2: Instalar Angular CLI
Ejecuta el siguiente comando para instalar Angular CLI globalmente:

```
npm install

npm install -g @angular/cli

```
Verifica la instalación con:

```
ng version

```

Asegúrate de que aparece Angular CLI: 19.x.x en la salida.

#Paso 3: Configuracion

Entra a las  carpeta   src/app/core/controllers

edita  el  archivo urlControllers.ts

[![config](config "config")](https://github.com/jhondiaz/testbrainhi/blob/main/config_base.png "config")




#Paso 3: Ejecutar la Aplicación
Para iniciar el servidor de desarrollo, ejecuta:



```
ng serve

```
