# Flask api
Backend para aplicación tytus para el [cliente](../../../client/fase2/team05) 'team05'

Esta es una versión más "completa" de la versión que se encuentra en el [direcotrio superior](../team05)

## Probar código:
Tener instalado:
* Python 3.8.5
* Versión más reciente de Pip
* pipenv (Explicación abajo)

Luego de clonar el repositorio y posicionarse en esta carpeta (server/team05)

### Para instalar pipenv
pipenv es un entorno virutal que Python ofrece para ejecutar una aplicación en un entorno "controlado" y apartado. De esta forma, no es necesario instalar las dependencias manualmente si no únicamente ejecutar una serie de comandos:
```cmd
$ pip install --user pipenv
$ pipenv install
$ pipenv shell
$ python app.py
```
<b>Explicación de comandos</b>

1. Instala las librerías necesarias para crear y correr un entorno virual. Se puede saltar si ya está instalado pipenv.
2. Crea el entorno virtual e instala las dependencias en ese entorno. 
3. "Abre" una consola para el entorno virutal recién creado
4. Dentro de esa consola, se ejecuta la aplicación

La aplicación deberìa estar corriendo en [localhost:5000](http://localhost:5000)

## Librerías utilizadas
Si no se desea instalar pipenv, puede instalar las librerías directamente en el sistema a través del comando ```pip install```

Las librerías utlizadas son:
- flask
- flask-cors
- numpy
- graphviz
- pandas
- ply
- prettytable

En Windows o Linux es necesario tener instalado [Graphviz](https://www.graphviz.org/download/) version 2.44.1 o superior

## Diagrama de paquetes del servidor

![Alt text](img/uml_server.png?raw=true "")

Para más información de SQL Parser, su gramática, uso, etc., [click aquí](../../../parser/team29/docs)
