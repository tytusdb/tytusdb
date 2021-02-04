# Manual Tecnico Grupo 3

Universidad de San Carlos de Guatemala  
Facultad de Ingeniería  
Cursos: 774 Sistemas de Bases de Datos 1 
Diciembre 2020

## Integrantes
Carné | Nombre Completo
-- | --
201503922 | Julio Roberto Garcia Escalante
201504444 | Christian Enrique Ramos Alvarez
201513747 | Ricardo Humberto Fuentes Garcia
201520498 | Edgar Rolando Herrera Rivas

## Descripcion del proyecto 
Este sistema de administracion de datos, esta estructurado de la siguiente manera 
* **Servidor:** Este servidor esta hecho en lenguaje de python que utiliza la herramienta flask para poder realizar peticiones y cumplir su funcionamiento como una api 
* **Cliente:** 
Esta hecho en python con ayuda de angular Cli para la interfaz grafica ya que el grupo considero que angular tienen 
muy buenas heramientas que son amigables con el usuario 

## Herramientas a utilizar
* Python
* Flask
* CORS
* Angular
* Angular-tree-control

### Python 
Es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código.
Se trata de un lenguaje de programación multiparadigma, ya que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional.
### Flask
Es un framework minimalista escrito en Python que permite crear aplicaciones web rápidamente y con un mínimo número de líneas de código.
Está basado en la especificación WSGI de Werkzeug y el motor de templates Jinja2 y tiene una licencia BSD.
### CORS
Es el intercambio de recursos de origen cruzado.
Es un mecanismo que utiliza cabeceras HTTP adicionales para permitir que un usuario obtenga permisos para acceder a recursos seleccionados desde un servidor.
### Angular
Es un framework para aplicaciones web desarrollado en TypeScript.
Es de código abierto, mantenido por Google, que se utiliza para crear y mantener aplicaciones web de una sola página.
### Angular Tree Control
Es un componente de control de árbol puro, basado en AngularJS.
Controlador para realizar arboles, el cual soporta arboles grandes con una minima sobrecarga.

## Servidor 
### Intalacion Sistema operativo Linux 
**Python3** 
* **Paso 1:** Se acualizan los repositorios 
```linux 
sudo apt update
```
* **Paso 2:** Se procede a intallar Python 3 
```linux 
sudo apt install python3.8
```
* **Paso 3:** Verificamos que la instalacion este correcta 
```linux 
python ––version
```
* **Paso 4:** Se vuelve actualizar los repositorios 
```linux 
sudo apt update
```

**Flask**
* **Paso 1:** Para la instalacion de Flask es necesario ya tener PIP3 en el ordenador, luego se coloca este comando para poder hacer la instalacion de flask 
```linux 
pip install Flask
```

### Codigo Servidor 
* **Paso 1:** Se agregan las librerias de Flask, request para poder realizar el servidor WEB
```python
from flask import Flask, request
```
* **Paso 2:** Se inicializa Flask para poder manejar una variable global 
```python
app = Flask(__name__)
```
* **Paso 3:** Se realiza los metodos para las peticiones ya sea de tipo POST, GET
```python
@app.route('/prueba',methods = ['GET'])
def prueba():
    return 'prueba'
```
* **Paso 4:** Se Levanta el servidor
```python
python3 Servidor_flask.py 
```
* **Paso 5:** Se realiza las pruebas en la Herramienta Postman para verificar que el servidor no tenga ningun error.

### Instalacion de Angular
* **Paso 1:** Se instala Nodejs en el sistema operativo
```text 
$ apt install python-software-properties
$ curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
$ sudo apt install nodejs
```
* **Paso 2:** Se instala Angular/Cli
```text 
$ npm install -g @angular/cli
```
* **Paso 3:** Se crea una nueva aplicacion angular
```text 
$ ng new hello-angular9
```
* **Paso 4:** Levantar la aplicacion, por defecto agarra el puerto 4200
```text 
$ ng serve
```

### Creacion de nuevos componentes en Angular
* **Paso 1:** Comando para crear un nuevo componente para la navegacion de la aplicacion
```text 
ng generate component nombre-del-componente
```
* **Paso 2:** Importamos el nuevo componente
```js 
import { Component, OnInit } from '@angular/core';
```
* **Paso 3:** En esta funcion se agregara el codigo a ejecutar
```js 
ngOnInit() {
	console.log('componente inicializado...');
}
```

### Instalacion de Angular tree control
* **Paso 1:** Copiar los script y css y agregarlos al proyecto
```js 
<script type="text/javascript" src="/angular-tree-control.js"></script>
 
<!-- Include context-menu module if you're going to use menu-id attribute -->
<script type="text/javascript" src="/context-menu.js"></script>
 
<!-- link for CSS when using the tree as a Dom element -->
<link rel="stylesheet" type="text/css" href="css/tree-control.css">
 
<!-- link for CSS when using the tree as an attribute -->
<link rel="stylesheet" type="text/css" href="css/tree-control-attribute.css">
```
* **Paso 2:** Agregar las dependencias en el modulo de la aplicacion
```js 
angular.module('myApp', ['treeControl']);
```
* **Paso 3:** Agregar los elementos para su arbol
```html 
<div treecontrol class="tree-classic"
   tree-model="dataForTheTree"
   options="treeOptions"
   on-selection="showSelected(node)"
   selected-node="node1">
   employee: {{node.name}} age {{node.age}}
</div>
```

# Conexion con el Parser (Compiladores 2)
Este es un metodo realiza la verificacion tanto lexico, cintatico y semantico de las instruccion que realize el usuario. 
```python
 if request.method == 'POST':
        content = request.get_json()
        name = content['codigo']
        instrucciones = g.parse(name)
        for instr in instrucciones['ast'] :
            if instr == None:
                continue
            result = instr.execute(datos)
            if isinstance(result, error.Error):
                print(result)
            elif isinstance(instr, select.Select):
                print(instr.ImprimirTabla(result))
            else:
                try:
                    #response = "hola " + name
                    response = {"codigo":str(result)}
                    return response
                except ClientError as e:
                    logging.error(e)
                    return e.response
                #print(str(result))
        try:
            response = "hola " + name
            return response
        except ClientError as e:
            logging.error(e)
            return e.response
```
