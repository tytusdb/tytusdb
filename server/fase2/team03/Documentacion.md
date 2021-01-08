# PROYECTO 1 G-8 TYTYSDB
TytusDB is an Open Source Database Management System
## Integrantes 
* Julio Roberto Garcia Escalante 201503922
* Edgar Rolando Herrera Rivas 201520498
* Ricardo Humberto Fuentes Garcia 201513747
* Christian Enrique Ramos Alvarez 201504444


# FASE II


#Angular
* Paso 1: La informacion que el usuario agregar ya sea para el nombre de la base de datos o insertar un dato a la misma.
```python
 this.publicar.codigo=this.mensaje;
```

#Servidor
* Paso 1: Con el siguiente metodo se hace la recepcion con el cliente http
```python
if request.method == 'POST':
content = request.get_json()
name = content['codigo']
```

* Paso 2: Se conecta con el metodo de analizador de compiladores 2 para verificar si esta bien 
```python
instrucciones = g.parse(name)
```
