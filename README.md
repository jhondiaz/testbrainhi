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



# Instalation

## Cuando se le solicite, acceda al directorio en el que desea descargar el proyecto.

 BackEnt - Python
```
https://github.com/jhondiaz/testbrainhi/tree/main/BrainHi-backEnd
```

## Create the virtual environment:
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

uvicorn src.main:app --host 0.0.0.0 --port 8081 --reload

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

[![config](config "config")](https://firebasestorage.googleapis.com/v0/b/tdriversuper.appspot.com/o/config_base.png?alt=media&token=6c54483f-996e-4b40-b6b7-3d537026c7ac "config")




#Paso 3: Ejecutar la Aplicación
Para iniciar el servidor de desarrollo, ejecuta:



```
ng serve

```
