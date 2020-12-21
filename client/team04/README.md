# Cliente Tytus DB (FASE I)

## Información General
- SO: Linux-Ubuntu 20.04
- Lenguaje: Python
- Grupo 4
- Diciembre 2020

**Librerias necesarias**

```python
import tkinter as tk
from tkinter import *
```

**Variables Globales**
Con ellas se controlan las pestañas

```python
control = 0
notebook = None
```

**Clase Arbol**

```python
class Arbol(Frame):
    ...
```

> La clase Arbol ultiliza el treeview de Tkinter para crear el panel izquierdo del cliente, hace referencia a las imagenes de la carpeta "resources" para mostrar los iconos en el arbol.

**Clase Campo**

```python
class Campo(Frame):
    ...
```

> Aqui se maneja el campo de texto, utiliza dos clases mas para poder mostrar el numero de lineas. TextLineNumbers crea un widget que genera las lineas dependiendo del area de Texto, CustomText crea el area de texto con la que se conectara el TextLineNumbers.

**ventana.py**

```python
def CrearMenu(masterRoot):
    ...
```

```python
def abrir():
    ...
```

```python
def CrearVentana():
    ...
```
> Conecta todo en un frame para crear el cliente.

```python
def añadir(titulo):
    ...
```

## Iniciar la interfaz

Se utiliza:
```
python ventana.py
```

## Menu
Se crearon los menus Archivo, Editar, Herramientas y Ayuda. En la primera fase solo el menu ayuda tiene opciones utilizables.

## Campo de Texto
Un editor que tiene numero de linea, opcion para multiples pestañas y un scroll para su mejor manejo.

## Vista de Bases
El panel izquiero del cliente se utiliza para tener una mejor visualizacion de las bases de datos conectadas. Es un vista de arbol que se expande hasta llegar a las tablas.

