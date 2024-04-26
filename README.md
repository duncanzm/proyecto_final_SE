[![N|Solid](https://images.credly.com/size/400x400/images/0e3e46ee-69d9-46e6-98b7-282f193e2c94/blob.png)](https://nodesource.com/products/nsolid)
# Maestría Profesional en Ingeniería del Software con énfasis en Inteligencia Artificial
## Sistemas Basados en Conocimiento

**Profesor:**
- Luis Gerardo León Vega

**Estudiantes:**
- Gino Marín
- Josue Quiros
- Duncan Zenteno

# proyecto_final_se

## Descripción
El sistema implementa una solución donde a partir de medidas obtenidas y categorizadas en marca y modelo de parlante, se pueda saber si este es lo suficientemente bueno para ser considerado un monitor.

## Requisitos Previos
Antes de ejecutar esta aplicación, asegúrate de tener instalado lo siguiente:
- **Docker**: Para instalar Docker, sigue las instrucciones en [Instalar Docker](https://docs.docker.com/get-docker/).
- **Docker Compose**: Para instalar Docker Compose, sigue las instrucciones en [Instalar Docker Compose](https://docs.docker.com/compose/install/).

## Cómo ejecutar la aplicación
Para poner en marcha la aplicación, sigue estos pasos:
1. Clona el repositorio:
   ```bash
   git clone https://github.com/duncanzm/proyecto_final_SE.git
   cd proyecto_final_SE

2. Revisa si Docker está arriba corriendo. Si no, ponlo a correr abriendo la aplicación anteriormente descargada:
   ```bash
   docker ps
   CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

3. Haz un build del docker-compose. Puede durar alrededor de 3-4 minutos y cuando esté listo verás un output como el de abajo:
   ```bash
     docker-compose up --build
     ...
     Backend-Layer  |  * Serving Flask app 'main'
     Backend-Layer  |  * Debug mode: on
     Backend-Layer  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     Backend-Layer  |  * Running on all addresses (0.0.0.0)
     Backend-Layer  |  * Running on http://127.0.0.1:8000
     Backend-Layer  |  * Running on http://172.18.0.2:8000
     Backend-Layer  | Press CTRL+C to quit
     Backend-Layer  |  * Restarting with stat
     Backend-Layer  |  * Debugger is active!
     Backend-Layer  |  * Debugger PIN: 576-110-620

5. Sin embargo, para acceder a la aplicación deberás ir a un browser y acceder a ```localhost:4200``` <img width="1417" alt="image" src="https://github.com/duncanzm/proyecto_final_SE/assets/57607997/290440ca-d47d-4c19-88fa-c52085fad21d">

6. Después de acceder a este, verás la opción de subir archivos de ```.ssa```. Estos puede encontrarse en el folder ```proyecto_final_SE/dataGeneration/ssa_files```. Depende del cuál elijas, el sistema analizará y dará su resultado de estos, que serían si el parlante es adecuado o no, si el archivo está corrupto o si no es válido.

