## Índice
- [Manual Tecnico](manual-tecnico)

## MANUAL TECNICO

# TYTUS TB
# ADMINISTRADOR DE ALMACENAMIENTO
# <center> INTEGRANTES </center>

## <center> CARLOS EMILIO CAMPO MORAN </center>

## <center> JOSE RAFAEL SOLIS FRANCO </center>

## <center> MADELYN ZUSETH PEREZ ROSALES </center>

## <center> JOSE FRANCISCO DE JESUS SANTOS SALAZAR </center>

# UNIVERSIDAD DE SAN CARLOS DE GUATEMALA
# FACULTAD DE INGENIERIA
# ESCUELA DE CIENCIAS Y SISTEMAS
# ESTRUCTURA DE DATOS
# 2020

### <center>**INTRODUCCION**</center>

<p align= "justify" > TYTUS TB es un administrador de base de datos que facilita al usuario ingresar información de manera ordenada y precisa, teniendo así un mejor manejo de datos. El manual que se presenta a continuación es una guía  de ayuda al usuario para tener un mejor soporte al momento de manejar el administrador de base de datos. Tener en cuenta el lenguaje que utiliza el administrador es lenguaje Python. </p>


---


### <center> **OBJETIVOS** </center>

#### **OBJETIVOS GENERALES** 

* OBJETIVO GENERAL
    * •	Tener un mejor manejo de administración de datos, para facilitar al usuario la inserción y extracción de datos.

* OBJETIVOS ESPECIFICOS
    * •	Garantizar una mejor seguridad en el manejo de datos
    * •	Recopilar datos para la realización de tablas y consultas

---
### <center> **HERRAMIENTAS UTILIZADAS PARA EL PROCESO**  </center>

Para poder ejecutar el siguiente proyecto debe tener en cuenta estas herramientas

* Tener instalado Python version 3.0 en el computador
* Tener un IDE que ejecute programas de lenguaje Python( más recomendable Visual Code)
* Tener instalado graphviz 

---
### <center> **CODIGO TYTUSTB** </center>

<p align= "justify"> El administrador de la base de datos TYTUSDB está compuesta por archivos y carpetas que hacen que el programa funcione de forma eficiente. </p>

## 1. Archivos Extension .py

Los archivos .py  son archivos escritos en el lenguaje de programación python. En estos incluyen las clases creadas que son utilizadas para la realización de cada funcion. Los archivos .py contenidos son:

### 1.1. NamesStructure.py

<p align = "justify"> Este archivo contiene dos clases: </p>

### 1.1.1. Clase NombreEstructuras:

<p align = "justify"> La clase NombreEstructuras maneja todos los ingresos de datos, asi como el manejo de tablas y almacenamiento de datos. Se divide de los siguientes modulos: </p>

### 1.1.1.1. __init__(self):

<p align = "justify"> Es el constructor de la clase NombreEstructuras donde se inicializan los atributos a utilizar en la clase </p>

``` Python 

    def __init__(self):
        data_dir="data"
        images_dir="images"
        tables_dir="data/tables"

        try:
            self.database=self.deserialize("data/database")
        except:
            print("Base de datos vacia")
            self.database={}
        else:
            pass

        try:
            os.mkdir(data_dir)
        except:
            pass
        try:
            os.mkdir(images_dir)
        except:
            pass
        try:
            os.mkdir(tables_dir)
        except:
            pass
```
donde:

> En este codigo se crean los ficheros si no han sido creado antes, y son utilizados en todo el proyecto 
```Python
        data_dir="data"
        images_dir="images"
        tables_dir="data/tables"
```
> Serializa y deserializa los objetos
``` Python
 try:
            self.database=self.deserialize("data/database")
        except:
            print("Base de datos vacia")
            self.database={}
        else:
            pass

        try:
            os.mkdir(data_dir)
        except:
            pass
        try:
            os.mkdir(images_dir)
        except:
            pass
        try:
            os.mkdir(tables_dir)
        except:
            pass
```
### 1.1.1.2. ComprobarNombre(self, nombre: str):
<p align = "Justify">   Para poder evaluar este metodo se necesita ingresar el nombre del identificador. En este metodo se comprueban los nombres del identificador, si sigue la norma de la expresion regular.</p>

```Python
def ComprobarNombre(self, nombre: str):
        expresionRegular = "[A-Za-z]{1}([0-9]|[A-Za-z]|\\$|@|_)*"
        
        if re.fullmatch(expresionRegular, str(nombre)) != None:
            return True
        else:
            return False
```

donde:
> Es la expresion regular del identificador donde debe empezar con una letra seguido de otra letra o numeros o cualquier caracter una o varias veces
```Python
        expresionRegular = "[A-Za-z]{1}([0-9]|[A-Za-z]|\\$|@|_)*"
```
> Recorre toda la expresion, si coincide devuelve un objeto coincidente correspondiente, de lo contrario devuelve nulo(None). Si la expresión es nula devuelve True, de lo contrario devuelve false.
```Python
    if re.fullmatch(expresionRegular, str(nombre)) != None:
            return True
        else:
            return False
```
### 1.1.1.3. searchDatabase(self, name: str):
<p align = "Justify"> El siguiente metodo busca si la base de datos ha sido creada. Para evaluar este metodo se requiere el nombre de la base de datos. Si retorna Nulo(None) retornara False, significa que la base de datos no ha sido encontrada, de lo contrario retornara True, entonces la base de datos ha sido encontrada </p>

```Python
    if self.database.get(name) == None:
            return False
        else:
            return True
```
### 1.1.1.4. createDatabase(self, database: str):

<p align = "Justify">El siguiente método crea una base de datos. Para evaluar este metodo se requiere el nombre de la base de datos. </p>

```Python
    def createDatabase(self, database: str):
        try:
            if self.ComprobarNombre(database) == True:  #Verificamos el identificador sea correcto
                
                if self.searchDatabase(database) == False: #Si la base no existe se crea
                    tablas = {} #inicializamos una estructura tipo diccionario para los nombres de tablas
                    self.database.setdefault(database, tablas)
                    ne.serialize("data/database",self.database)
                    return 0
                else:
                    return 2
            else:
                return 1
        except:
            return 1
```
donde:
>Se verifica si el identificador es correto, si es correcto sigue con el siguiente codigo, de lo contrario retorna 1. Try ... except es utilizado por si se da un error al verificar el nombre 
```Python
    try:
        if self.ComprobarNombre(database) == True:    
        ...
        return 1
    except:
            return 1
```
>Si el identificador es correcto, verifica si la base de Datos esta creada, ya que no se pueden agregar dos bases de datos con el mismo identificador. Si la base de datos no ha sido creada, se inicializa un diccionario para guardar los nombres de las tablas que se van almacenar en la base de datos. El diccionario se inicializa con la clave donde se puede utiliza para buscar los datos.

```Python
        if self.searchDatabase(database) == False:
            tablas = {} 
            self.database.setdefault(database, tablas)
            ne.serialize("data/database",self.database)
        else:
            return 2
```
### 1.1.1.5. showDatabases(self):

<p align = "Justify">Este método muestra un arreglo donde estan almacenados todas las bases de datos</p>

```Python
    def showDatabases(self):
        arreglotmp = []
        for x in self.database:
            arreglotmp.append(str(x))
        
        return arreglotmp
```
### 1.1.1.6. alterDatabase(self, databaseOld, databaseNew):
<p align = "Justify">Este método realiza el cambio de nombre de una base de datos que ha sido almacenada anteriormente. Para evaluar este método se necesita el nombre de la base de datos almacenada, y el nuevo nombre de la base de datos que desea uno reemplazar</p>

```Python
    def alterDatabase(self, databaseOld, databaseNew):
        try:
            if self.ComprobarNombre(databaseOld) == True and self.ComprobarNombre(databaseNew) == True:
                if self.searchDatabase(databaseOld) == True: 
                    if self.searchDatabase(databaseNew) == False: 
                        self.database[databaseNew] = self.database[databaseOld]
                        del self.database[databaseOld]
                 
                        directorio='data/tables/'
                        with os.scandir(directorio) as ficheros:
                            for f in ficheros:
                                if f.name.startswith(str(databaseOld)):
                                    print(str(f.path))
                                    get_path=f.path.split("/")
                                    tmp_name=get_path[2].split("-")
                                    new_name=str(databaseNew)+"-"+tmp_name[1]
                                    final_string="data/tables/"+str(new_name)
                                    os.rename(f.path,final_string)
                        ne.serialize("data/database",self.database)            
                        return 0
                    else:
                        return 3
                    
                else:
                    return 2
            else:
                return 1
        except:
            return 1
```
Donde:
>Primero comprueba si el nombre cumple con la regla de identificador de lo contrario retorna 1
```Python
        try:
            if self.ComprobarNombre(databaseOld) == True and self.ComprobarNombre(databaseNew) == True:
                ...
            else:
                return 1
```

>Despues busca si la base de datos que se desea modificar este creada, de lo contrario retorna 2
```Python

        if self.searchDatabase(databaseOld) == True:
            ...
        else:
            return 2
```

>y de ultimo determina si el nombre nuevo de la base de datos exista, retorna 3. Si acerta todas las condiciones anteriores, recorre todos los archivos que corresponden con la base anterior y coloca el nuevo nombre
```Python
     if self.searchDatabase(databaseNew) == False: 
                        self.database[databaseNew] = self.database[databaseOld]
                        del self.database[databaseOld]

                        directorio='data/tables/'
                        with os.scandir(directorio) as ficheros:
                            for f in ficheros:
                                if f.name.startswith(str(databaseOld)):
                                    print(str(f.path))
                                    get_path=f.path.split("/")
                                    tmp_name=get_path[2].split("-")
                                    new_name=str(databaseNew)+"-"+tmp_name[1]
                                    final_string="data/tables/"+str(new_name)
                                    os.rename(f.path,final_string)
                        ne.serialize("data/database",self.database)            
                        return 0
                    else:
                        return 3
```
### 1.1.1.7. dropDatabase(self, database: str):
<p align = "Justify">Este método elimina una base de datos. Para evaluar este método se asigna se necesita el nombre de la base de datos a eliminar </p>

```Python
    def dropDatabase(self, database: str):
        try:
            if self.ComprobarNombre(database) == True: #Comprobamos el nombre
                if self.searchDatabase(database) == True: #Buscamos la db
                    del self.database[database]
                    ne.serialize("data/database",self.database)
                    directorio='data/tables/'
                    with os.scandir(directorio) as ficheros:
                        for f in ficheros:
                            if f.name.startswith(str(database)):
                                os.remove(f.path)
                    return 0
                else:
                    return 2
            else:
                return 1
        except:
            return 1
```
donde:
>Primero se comprueba si el nombre de la base de datos es un identificador
```Python
        try:
            if self.ComprobarNombre(database) == True:  
                ...
        else:
                return 1
        except:
            return 1       
```
>Despues se busca si la base de datos ha sido creado. Si devuelve True(que ha sido creada), entonces se elimina la base de datos 
```Python
                if self.searchDatabase(database) == True:
                    del self.database[database]
                        ne.serialize("data/database",self.database)
                        directorio='data/tables/'
                        with os.scandir(directorio) as ficheros:
                            for f in ficheros:
                                if f.name.startswith(str(database)):
                                    os.remove(f.path)
                        return 0
                else:
                    return 2
```
### 1.1.1.8. buscarTabla(self, nombre, tablas):
<p align="Justify">Este método realiza la busqueda de tablas, si estan agregadas en un diccionario, si no se encuentra retorna nula(None). Cuando se obtiene nulo(None) retorna false de lo contrario retorna True(significa que la tabla esta almacenada en el diccionario). Para evaluar este método requiere el nombre del diccionario, donde se encuentran almacenadas las tablas creadas</p>

```Python
    def buscarTabla(self, nombre, tablas):
        if tablas.get(nombre) == None:
            return False
        else:
            return True
``` 
### 1.1.1.9. buscarTablaDatabase(self, database: str, tabla: str):
<p align="Justify">Este mètodo verifica si una tabla esta en una base de datos. Para evaluar este método se requiere el nombre de la base de datos, y el nombre de la tabla que se desea encontrar. Si se encuentra retorna el nombre de la tabla, de lo contrario retorna false</p>

```Python
    def buscarTablaDatabase(self, database: str, tabla: str):
        encontrar = False
        if self.searchDatabase(database) == True:
            dictmp = self.database[database]
            encontrar = self.buscarTabla(tabla,dictmp)

        return encontrar
``` 
### 1.1.1.10. createTable(self, basedato: str, tabla: str, columna: int):
<p align="Justify"> </p>

```Python
    def createTable(self, basedato: str, tabla: str, columna: int):
        try:
            if self.ComprobarNombre(basedato) == True and self.ComprobarNombre(tabla) == True:
                if self.searchDatabase(basedato) == True:
                    aux = self.database[basedato]
                    if self.buscarTabla(tabla,aux) == False: # Si no encuentra la tabla la inserta
                        tmp = [columna, []] #variable tmp para agregar el número de columna en la pos[0] y en la pos[1] la lista de primary keys
                        aux.setdefault(tabla, tmp)
                        self.database[basedato] = aux
                        ne.serialize("data/tables/"+str(basedato)+"-"+str(tabla),self.database[basedato])
                        ne.serialize("data/database",self.database)
                        return 0
                    else:
                        return 3
                else:
                    return 2
            else:
                return 1
        except:
            return 1
```
Donde:

>Primero se comprueba si el nombre de la base de datos y el nombre de la tabla es un identificador
```Python
        try:
            if self.ComprobarNombre(basedato) == True and self.ComprobarNombre(tabla) == True:
                ... 
            else:
                return 1
        except:
            return 1
```
>Despues se busca si la base de datos esta creada, si esta creada se obtiene el arreglo de las tablas que estan almacenadas en esa base de datos.
```Python
                if self.searchDatabase(basedato) == True:
                    aux = self.database[basedato]
                    ...
                else:
                    return 2
```
>Despues se busca si existe la tabla con ese nombre, si no existe, la crea agregandole el numero de columna en la pos[0] y en la pos[1] la lista de primary keys que desea agregarle a la tabla. Si la tabla ya existe returna 3
```Python
                    if self.buscarTabla(tabla,aux) == False: # Si no encuentra la tabla la inserta
                        tmp = [columna, []] #variable tmp para agregar el número de columna en la pos[0] y en la pos[1] la lista de primary keys
                        aux.setdefault(tabla, tmp)
                        self.database[basedato] = aux
                        ne.serialize("data/tables/"+str(basedato)+"-"+str(tabla),self.database[basedato])
                        ne.serialize("data/database",self.database)
                        return 0
                    else:
                        return 3
```

### 1.1.1.12. showTables(self, database: str):
<p align="Justify">Este método nos muestra el listado de tablas que existen en la base de datos que deseamos mostrar. Para evaluar este método se necesita ingresar el nombre de la base de datos.Comprueba si el nombre de la base de datos es un identificador y comprueba si la base de datos esta creada. Si esta creada, se obtiene el diccionario de las tablas y se agregan a un arreglo </p>

```Python
    def showTables(self, database: str):
        try:
            if self.ComprobarNombre(database) == True:
                if self.searchDatabase(database) == True:
                    aux = self.database[database] 
                    arrtmp = [] 
                    for key in aux:
                        arrtmp.append(str(key))
                    return arrtmp

                else:
                    return None
            else:
                return None
        except:
            None
``` 

### 1.1.1.13. alterTable(self, database: str, tableOld: str, tableNew: str):
<p align="Justify"> Este método modifica el nombre de la tabla de una base de datos. Para evaluar este método se necesita ingresar el nombre de la base de datos donde se busca la tabla, el nombre de la tabla que se desea modificar, y el nuevo nombre que se desea asignar a la tabla.

```Python
    def alterTable(self, database: str, tableOld: str, tableNew: str):
        try:
            if self.ComprobarNombre(database) == True and self.ComprobarNombre(tableOld) == True and self.ComprobarNombre(tableNew) == True:
                if  self.searchDatabase(database) == True: 
                    aux = self.database[database]
                    if self.buscarTabla(tableOld, aux) == True: 
                        if self.buscarTabla(tableNew, aux) == False:
                            aux[tableNew] = aux[tableOld] 
                            ne.serialize("data/tables/"+str(database)+"-"+str(tableNew),aux[tableNew])
                            del aux[tableOld]
                            os.remove("data/tables/"+str(database)+"-"+str(tableOld))
                            ne.serialize("data/database",self.database)
                            return 0
                        else:
                            return 4
                    else:
                        return 3
                else:
                    return 2
            else:
                return 1
        except:
            return 1
```
donde:
>Primero comprueba que el nombre de la base de datos y el nombre de la tabla sean identificadores.
```Python
        try:
            if self.ComprobarNombre(database) == True and self.ComprobarNombre(tableOld) == True and self.ComprobarNombre(tableNew) == True:`
                ...
            else:
                return 1
        except:
            return 1    
```
>Despues busca la base de datos. Si existe toma el diccionario donde se almacenan todas las tablas que se encuentran en esa base de datos. De lo contrario retorna 3
```Python

                if  self.searchDatabase(database) == True: 
                    aux = self.database[database]
                    ...
                else:
                    return 3
```
>Si existe la base de datos, busca la tabla que se desea modificar
```Python
                    if self.buscarTabla(tableOld, aux) == True: 
                        ...
                    else:
                        return 3
```
>Al encontrar la tabla se le cambia el nombre 
```Python
                        if self.buscarTabla(tableNew, aux) == False: 
                            aux[tableNew] = aux[tableOld] 
                            ne.serialize("data/tables/"+str(database)+"-"+str(tableNew),aux[tableNew])
                            del aux[tableOld]
                            os.remove("data/tables/"+str(database)+"-"+str(tableOld))
                            ne.serialize("data/database",self.database)
                            return 0
                        else:
                            return 4
```
### 1.1.1.14. dropTable(self, database, tableName):
<p align="Justify"> Este método elimina la tabla que se le asigna en el método</p>
   
```Python
    def dropTable(self, database, tableName):
        try:
            if self.ComprobarNombre(database) == True and self.ComprobarNombre(tableName) == True: #Comprobamos nombre
                if self.searchDatabase(database) == True:  #Verificamos que exista la bd
                    aux = self.database[database] #Asignamos a una variable temporal el diccionario de tablas de la bd
                    
                    if self.buscarTabla(tableName, aux) == True:
                        del aux[tableName]
                        self.database[database] = aux
                        os.remove("data/tables/"+str(database)+"-"+str(tableName))
                        ne.serialize("data/database",self.database)
                        return 0
                    else:
                        return 3
                else:
                    return 2
            else:
                return 1
        except:
            return 1
```
Donde:
>Primero se comprueba los nombres de la base de datos y la tabla sean identificadores
```Python
        try:
            if self.ComprobarNombre(database) == True and self.ComprobarNombre(tableName) == True: 
                ...
            else:
                return 1
        except:
            return 1    
```
>Despues se verifica si existe la base de datos y si existe se le asigna a una variable temporal el diccionario de tablas de la base de datos encontrada
```Python
        
                if self.searchDatabase(database) == True:  
                    aux = self.database[database] 
                   ...
                else:
                    return 2
```
>Se busca dentro de la variable si existe la tabla, si se encuentra se elimina de la base de datos
```Python
                    
                    if self.buscarTabla(tableName, aux) == True:
                        del aux[tableName]
                        self.database[database] = aux
                        os.remove("data/tables/"+str(database)+"-"+str(tableName))
                        ne.serialize("data/database",self.database)
                        return 0
                    else:
                        return 3
```

Los métodos que se encuentran a continuacion de este archivos para que funcionen, se necesita crear una tabla hash. Para crear una tabla Hash se encuentra en la clase HashTable
    
### 1.1.1.15. alterAddPK(self, database: str, table: str, columns: list):
<p align="Justify"> Este método añade las llaves primarias a la tabla. Recordar que la tabla Hash debe ser creada antes </p>

```Python
    #Agregar primary key
    def alterAddPK(self, database: str, table: str, columns: list):
        try:
            if self.searchDatabase(database) == True: #Busca si la base de datos donde se encuentra la tabla de datos donde se desea agregar las llaves primarias existe
                dicTemp = self.database[database]
                
                if self.buscarTabla(table, dicTemp) == True:#Busca si la tabla esta creada dentro de la base de datos
                    lenColumns = len(columns) #tamaño del atributo columns
                    lenPrimaryKey = len(dicTemp[table][1]) #tamaño de la tabla creada
                    columnasTabla = int(dicTemp[table][0]) - 1 #numero de columnas de la tabla

                    if  (columnasTabla + 1) >= lenColumns: #Comparamos tamaño de columnas
                        if lenPrimaryKey == 0:

                            okPrimaryKey = True #Variable para ver que todos los indices existan en la tabla

                            for e in columns: #for para recorrer los indices de PK y que existan dichos indices en la columna
                                if int(e) >= columnasTabla:
                                    okPrimaryKey = False
                            
                            if okPrimaryKey == True:
                                dicTemp[table][1] = columns #Agregamos la lista de primary keys
                                self.database[database] = dicTemp #Actualizamos el diccionario de base de datos
                                ht.pk_redefinition(database, table) #Redefine las primary key
                                ne.serialize("data/database",self.database)
                                ne.serialize("data/tables/"+str(database)+"-"+str(table),self.database[database])
                                return 0
                            
                            elif okPrimaryKey == False:
                                return 1
                        else:
                            return 4
                    else:
                        return 5

                else:
                    return 3
            else: 
                return 2
        except:
            return 1
 ``` 
### 1.1.1.16. listaPrimaryKeyTabla(self, baseDatos: str, tabla: str):
<p align="Justify"> Este método muestra una lista de las llaves primarias que existen en la tabla, si la lista muestra vacio o nulo(None) significa que no hay llaves primarias creadas</p>
 
```Python
    def listaPrimaryKeyTabla(self, baseDatos: str, tabla: str):
        try:
            listaTemporal = [] 
            if self.searchDatabase(baseDatos) == True: #Se busca la base de datos donde se encuentra la tabla donde se encuentran las llaves primarias
                dictTemporal = self.database[baseDatos]

                if self.buscarTabla(tabla, dictTemporal) == True:#Se busca la tabla donde se agregaran las llaves primarias
                    listaTemporal = dictTemporal[tabla][1]
                    if len(listaTemporal) != 0:
                        return listaTemporal
                    else:
                        None
                else:
                    return None
        except:
            return None
```
### 1.1.1.17. BuscarPrimaryKey(self, baseDatos: str, tabla: str, pk):
<p align="Justify">Se busca la llave primaria, recorriendo el diccionario que se encuentra en la tabla, si existe retorna true, al contrario devuelve false </p>

```Python
    def BuscarPrimaryKey(self, baseDatos: str, tabla: str, pk):
        listaTemporal = self.listaPrimaryKeyTabla(baseDatos, tabla)
        encontrado = False
        if listaTemporal != None:
            for e in listaTemporal:
                if pk == e:
                    encontrado = True
        return encontrado
```
### 1.1.1.18. alterDropPK(self, database: str, table: str):
<p align ="Justify">Este metodo elimina la llave primaria de la tabla. Para evaluar este metodo se llama el nombre de la base de datos, y el nombre de la tabla </P>

```Python  
    def alterDropPK(self, database: str, table: str):
        try:
            if self.searchDatabase(database) == True:#Se verifica la base de datos donde se encuentra la tabla donde se desea agregar la llave primaria
                dicTemp = self.database[database]
                
                if self.buscarTabla(table, dicTemp) == True:#Se busca la tabla donde se desea agregar la llave primaria
                    lenPrimaryKey = len(dicTemp[table][1]) #tamaño de la tabla creada

                    if lenPrimaryKey != 0:
                        dicTemp[table][1] = [] #limpiamos su valor
                        self.database[database] = dicTemp #Actualizamos el diccionario de base de datos
                        ne.serialize("data/database",self.database)
                        ne.serialize("data/database"+str(database)+"-"+str(table),self.database[database])
                        return 0
                    
                    else:
                        return 4
                else:
                    return 3 
            else:
                return 2
        except:
            return 1
```
### 1.1.1.19. alterAddColumn(self, database: str, table: str, default: any):
<p  align = "Justify"> Este metodo agrega columna a una tabla escogida. Para poder evaluar este método se le asigna el nombre de la base de datos y el nombre de la tabla </p>

```Python
    def alterAddColumn(self, database: str, table: str, default: any):
        try:
            if self.searchDatabase(database) == True:#Busca la base de datos
                dicTemp = self.database[database]
                
                if self.buscarTabla(table, dicTemp) == True:#Busca la tabla que se desea agregar columnas
                    dicTemp[table][0] = int(dicTemp[table][0]) + 1 #Columna agregada
                    self.database[database] = dicTemp #Actualizamos el diccionario de base de datos
                    ht.addColumn(default, database, table) ##agrega una columna en hash table
                    ne.serialize("data/tables/"+str(database)+"-"+str(table),self.database[database])
                    ne.serialize("data/database",self.database)
                    return 0
                else:
                    return 3 
            else:
                return 2
        except:
            return 1
```
### 1.1.1.20. alterDropColumn(self, database: str, table: str, columnNumber: int):
<p align="Justify"> Este metodo se modifica el tamaño de columnas de una tabla. Para evaluar este método se requiere el nombre de la base de datos donde se encuentra la tabla a modificar, el nombre de la tabla y el numero de columna que se desea convertir la tabla</p>

```Python
    def alterDropColumn(self, database: str, table: str, columnNumber: int):
        try:
            columnNumber=int(columnNumber)
            if self.searchDatabase(database) == True: #Se verifica si existe la base de datos
                dicTemp = self.database[database]
                
                if self.buscarTabla(table, dicTemp) == True:#Se busca si la tabla esta contenida en la base de datos
                    totalColumnaFinal = dicTemp[table][0] - 1 #Columna agregada

                    if totalColumnaFinal >= columnNumber:#Se compara el numero de columnas que posee la tabla con el numero de tablas que se desea convertir
                        
                        if totalColumnaFinal != 0 or self.BuscarPrimaryKey(database, table, columnNumber) == False: #para saber si todavía nos quedamos con columnas y si no es una llave primaria
                            dicTemp[table][0] = int(dicTemp[table][0]) - 1 #Columna Eliminada
                            self.database[database] = dicTemp #Actualizamos el diccionario de base de datos
                            ht.dropColumn(columnNumber,database, table) #Elimina un indice (columna) en la tabla hash
                            ne.serialize("data/tables/"+str(database)+"-"+str(table),self.database[database])
                            ne.serialize("data/database",self.database)
                            return 0
                        else:
                            return 4
                    else: 
                        return 5
                else:
                    return 3 
            else:
                return 2
        except:
            return 1
```
### 1.1.1.21. numeroDeColumnas(self, database: str, table: str):
<p align="Justify"> Devuelve el numero de columna de una tabla especifica, sino la tabla no existe devuelve Nulo(None)</p>
```Python
    def numeroDeColumnas(self, database: str, table: str):
        try:
            dicTemporal = self.database[database]
            numeroColumna = dicTemporal[table][0]
            return numeroColumna
        except:
            return None
```

### 1.1.1.22. serialize(self, filename, data):
<p align= "Justify"> Este método crea un archivo binario</p>

```Python
    ##serializacion
    def serialize(self, filename, data):
        objetos=data
        nombre_archivo=filename
        
        #creacion del archivo
        archivo_dat=open(nombre_archivo,'wb')
        pickle.dump(objetos,archivo_dat)
        archivo_dat.close()
        del archivo_dat
```

### 1.1.1.23. deserialize(self, filename): 
<p align= "Justify"> Este método lee un archivo binario </p>
    
```Python
    def deserialize(self, filename):
        archivo_dat=open(filename,'rb')
        recover_data={}
        recover_data=pickle.load(archivo_dat)
        archivo_dat.close()
        
        #print("recover data:",recover_data)
        return recover_data
    ##fin serializacion
``` 
### 1.1.2. Clase HashTable:  
Esta clase se almacenan los métodos para la utilizacion de la tabla Hash 

### 1.1.2.1. __init__(self):  
<p align= "Justify"> Es el constructor de la clase HashTable. Dentro de este se define el tamaño del vector al crearse la tabla </p>

```Python
    def __init__(self):
        self.DiccionarioTabla = {} #este es cambio hecho por mí
        self.__vector = [None] * 20
        self.__order_keys = []
        try:
            self.DiccionarioTabla=ne.deserialize("data/tables/table")
        except:
            print("Tablas vacias")
            self.DiccionarioTabla={}
        else:
            pass
```
### 1.1.2.2.  __hash(self, valor):
<p align = "Justify"> En este método se define la llave que identificara al dato para poder ingresar a la tabla Hash. Para poder encontrar la llave se recorre el dato caracter por caracter y se encuentra el codigo Ascci de cada caracter y se suman, despues se divide la suma total dentro del tamaño del arreglo, y el residuo es el indice que se utilizara para ingresar a la tabla Hash </p>

```Python
    def __hash(self, valor):
        llave = 0
        for i in range(0, len(valor)):
            llave += ord(valor[i]) * i
        return llave % 20
``` 
### 1.1.2.3. IniciarHashTable(self, database: str, table: str):
<p align = "Justify">Se obtienen los datos que se leen del archivo. Basado en estos datos se puede eliminar, modificar o agregar mas datos </p>

```Python
    def IniciarHashTable(self, database: str, table: str):
        nombreKeyDiccionario = database + "_" + table
        #Para comprobar que si existe la llave
        if self.DiccionarioTabla.get(nombreKeyDiccionario) != None:
            self.__vector = self.DiccionarioTabla[nombreKeyDiccionario][0]
            self.__order_keys = self.DiccionarioTabla[nombreKeyDiccionario][1]
        else: 
            self.__vector = [None] * 20
            self.__order_keys = []
```
### 1.1.2.3. RestaurarHashTable(self, database: str, table: str):     
<p align = "Justify">Restauramos el diccionario</p>

```Python
    def RestaurarHashTable(self, database, table, lista: list): #[__vector, __orderkeys]
        nombreKeyDiccionario = database + "_" + table
        self.DiccionarioTabla[nombreKeyDiccionario] = lista
        ne.serialize("data/tables/table", self.DiccionarioTabla)
``` 

### 1.1.2.4. insert(self, database: str, table: str, data: list):
<p align = "Justify">Inserta los datos que estan en la tupla a la tabla Has. Para evaluar este método se llama el nombre de la base de datos, el nombre de la tabla y el diccionario que deseas insertar</p> 

```Python
    def insert(self, database: str, table: str, data: list):     
        self.IniciarHashTable(database, table) #Iniciamos las variables de la tabla hash
        
        #Verifica si existe la base de datos especificada
        if ne.searchDatabase(database) is False:
            return 2

        #Verifica si existe la tabla especificada en la base de datos
        if ne.buscarTablaDatabase(database, table) is False:
            return 3

        #Verifica si la cantidad de datos de tupla coincide con el número de columnas
        if int(ne.numeroDeColumnas(database, table)) != len(data):
            return 5

        #Verifica si la tabla tiene llave primaria
        concat_llaves = ""
        lista_llaves = ne.listaPrimaryKeyTabla(database, table)
        if lista_llaves != None:
            
            #Concatena los datos de la columna
            for l in lista_llaves:
                concat_llaves += str(data[int(l)]) + "_"
        else:
            for d in data:
                if d is not None:
                    concat_llaves += d + "_"
        
        #Obtiene la llave que se utilizará para la tabla hash
        llave = self.__hash(concat_llaves)
        #Condiciones para verificar si la llave ya está ocupada
        if self.__vector[llave] is None:
            dic_datos = {}
            dic_datos[concat_llaves] = data
            self.__vector[llave] = dic_datos
            self.__order_keys.append(concat_llaves)

            self.RestaurarHashTable(database, table, [self.__vector, self.__order_keys]) #Restauramos el diccionario
            return 0
        else:
            dic_datos = self.__vector[llave]
            if dic_datos.get(concat_llaves) is None:
                dic_datos[concat_llaves] = data
                self.__vector[llave] = dic_datos
                self.__order_keys.append(concat_llaves)
                self.RestaurarHashTable(database, table, [self.__vector, self.__order_keys]) #Restauramos el diccionario
                return 0
            return 4
        return 1
``` 

### 1.1.2.5. extractRow(self, database: str, table: str, columns: list):
<p align = "Justify">Este método devuelve la tupla con respecto a su llave primari </p>

```Python
    #Devuelve la tupla con respecto a su llave primaria
    def extractRow(self, database: str, table: str, columns: list):
        self.IniciarHashTable(database, table) #Iniciamos las variables de la tabla hash

        #Verifica si existe la base de datos especificada
        if ne.searchDatabase(database) is False:
            return []

        #Verifica si existe la tabla especificada en la base de datos
        if ne.buscarTablaDatabase(database, table) is False:
            return []

        #Verifica si la tabla tiene llave primaria
        concat_llaves = ""
        for c in columns:
            concat_llaves = concat_llaves+ str(c) + "_"
        #Obtiene la llave hash 
        llave = self.__hash(concat_llaves)
        if self.__vector[llave] is not None:
            dic_datos = self.__vector[llave]
            if dic_datos.get(concat_llaves) is not None:
                return dic_datos.get(concat_llaves)
        return []
```
### 2.2.2.6. update(self, database: str, table: str, register: dict, columns: list):
<p align = "Justify"> Este método modifica un registro de una tupla especificada. Para evaluar este método se necesita el nombre de la base de datos donde se encuentra la tupla
</p>

```Python
    def update(self, database: str, table: str, register: dict, columns: list):
        self.IniciarHashTable(database, table) #Iniciamos las variables de la tabla hash
        #Verifica si existe la base de datos especificada
        if ne.searchDatabase(database) is False:
            return 2

        #Verifica si existe la tabla especificada en la base de datos
        if ne.buscarTablaDatabase(database, table) is False:
            return 3

        #Verifica si la tabla tiene llave primaria
        concat_llaves = ""
        for k in columns:
            concat_llaves += str(k) + "_"
        
        #Obtiene la llave hash
        llave = self.__hash(concat_llaves)
        #Verificación de llave y cambio de valores
        if self.__vector[llave] is not None:
            dic_tupla = self.__vector[llave]

            if dic_tupla.get(concat_llaves) is not None:
                listaDatos = []
                #tupla = dic_tupla.get(concat_llaves)
                for k in register.keys():
                    #tupla[k] = register.get(k)
                    listaDatos.append(register.get(k))
                #dic_tupla[concat_llaves] = tupla
                del dic_tupla[concat_llaves]
                self.insert(database, table, listaDatos)
                self.RestaurarHashTable(database, table, [self.__vector, self.__order_keys]) #Restauramos el diccionario
                return 0
            else:
                return 4
        return 1
```
 ### 2.2.2.7. delete(self, database: str, table: str, columns: list):     
<p align = "Justify">Elimina un registro de una tabla y base de datos especificados por la llave primaria </p>

```Python
    def delete(self, database: str, table: str, columns: list):
        self.IniciarHashTable(database, table) #Iniciamos las variables de la tabla hash
        
        #Verifica si existe la base de datos especificada
        if ne.searchDatabase(database) is False:
            return 2

        #Verifica si existe la tabla especificada en la base de datos
        if ne.buscarTablaDatabase(database, table) is False:
            return 3

        #Verifica si la tabla tiene llave primaria
        concat_llaves = ""

        lista_llaves = ne.listaPrimaryKeyTabla(database, table)

        if lista_llaves != None:
            
            #Concatena los datos de la columna
            for l in lista_llaves:
                concat_llaves += str(columns[l]) + "_"
        else:
            for c in columns:
                if c is not None:
                    concat_llaves += str(c) + "_"
        
        #Obtiene la llave hash
        llave = self.__hash(concat_llaves)
        #Verificación de llave y eliminación de valor
        if self.__vector[llave] is None:
            return 4
        
        dic_tupla = self.__vector[llave]
        if dic_tupla.get(concat_llaves) is None:
            return 4
        else:
            del dic_tupla[concat_llaves]
            self.__vector[llave] = dic_tupla
            self.RestaurarHashTable(database, table, [self.__vector, self.__order_keys]) #Restauramos el diccionario
            return 0
        return 1
```

### 2.2.2.8. truncate(self, database: str, table: str):
<p align = "Justify">Elimina todos los registros de una tabla y base de datos</p>

```Python
    def truncate(self, database: str, table: str):
        self.IniciarHashTable(database, table) #Iniciamos las variables de la tabla hash
        #Verifica si existe la base de datos especificada
        if ne.searchDatabase(database) is False:
            return 2

        #Verifica si existe la tabla especificada en la base de datos
        if ne.buscarTablaDatabase(database, table) is False:
            return 3

        self.__vector = [None] * 20
        self.RestaurarHashTable(database, table, [self.__vector, self.__order_keys]) #Restauramos el diccionario
        return 0
```

### 2.2.2.9. addColumn(self, data_default, database, table): 
<p align = "Justify">Agrega una nueva columna al final de cada tupla, esta columna no tendra nada, por los que sera de tipo nulo(None) </p>

```Python
    def addColumn(self, data_default, database, table):
        self.IniciarHashTable(database, table) #Iniciamos las variables de la tabla hash
        for r in self.__vector:
            if r is not None:
                aux_keys = r.keys()
                for k in aux_keys:
                    tup = r.get(k)
                    tup.append(data_default)
                    r[k] = tup
        
        self.RestaurarHashTable(database, table, [self.__vector, self.__order_keys]) #Restauramos el diccionario
        return 0
```

### 2.2.2.10.     def dropColumn(self, numberColum: int, database, table):
<p align = "Justify">Elimina la columna de la tupla </p>    

```Python
    def dropColumn(self, numberColum: int, database, table):
        self.IniciarHashTable(database, table) #Iniciamos las variables de la tabla hash
        for r in self.__vector:
            if r is not None:
                aux_keys = r.keys()
                for k in aux_keys:
                    tup = r.get(k)
                    tup.pop(numberColum)
                    r[k] = tup

        self.RestaurarHashTable(database, table, [self.__vector, self.__order_keys]) #Restauramos el diccionario
        return 0
```

### 2.2.2.11. pk_redefinition(self, database: str, table: str):
<p align = "Justify">Complementa el método alterAddPk </p>  

```Python
    def pk_redefinition(self, database: str, table: str):
        self.IniciarHashTable(database, table) #Iniciamos las variables de la tabla hash
        tuplas = []
        #Obtiene todos los registros que están en la tabla
        for r in self.__vector:
            if r is not None:
                aux_keys = r.keys()
                for k in aux_keys:
                    tuplas.append(r.get(k))
        #Vacía el vector
        self.__vector = [None] * 20
        del self.DiccionarioTabla[database+"_"+table] #
        #Reingresa los valores
        for t in tuplas:
            self.insert(database, table, t)
        
        self.RestaurarHashTable(database, table, [self.__vector, self.__order_keys]) #Restauramos el diccionario
```

### 2.2.2.12. extractTable(self, database: str, table: str):
<p align = "Justify">Extrae y devuelve una lista con los elementos que corresponden a cada registro de la tabla </p>

```Python
    def extractTable(self, database: str, table: str):
        self.IniciarHashTable(database, table) #Iniciamos las variables de la tabla hash
        if ne.searchDatabase(database) is False:
            return None

        if ne.buscarTablaDatabase(database, table) is False:
            return None

        tuplas = []
        #Obtiene todos los registros que están en la tabla
        for r in self.__vector:
            if r is not None:
                aux_keys = r.keys()
                for k in aux_keys:
                    tuplas.append(r.get(k))
        return tuplas
```

### 2.2.2.13. extractRangeTable(self, database: str, table: str, columnNumber: int, lower, upper):
<p align = "Justify"> Devuelve una lista con los elementos que corresponden a un rango de registros</p>  
    
```Python
    def extractRangeTable(self, database: str, table: str, columnNumber: int, lower, upper):
        self.IniciarHashTable(database, table) #Iniciamos las variables de la tabla hash
        if ne.searchDatabase(database) is False:
            return None

        if ne.buscarTablaDatabase(database, table) is False:
            return None

        if columnNumber > ne.numeroDeColumnas(database, table):
            return None

        if lower < 0 or upper > len(self.__order_keys):
            return None

        lista_datos = []

        for t in range(lower, upper):
            llave = self.__order_keys[t][:-1].split("_")
            lista_datos.append(self.extractRow(database, table, llave)[columnNumber])

        return lista_datos
```

### 2.2.2.14. imprimir(self):
<p align = "Justify">Imprime el vector de la tabla Hash, recorriendo desde la primera posicion hasta la ultima posicion del arreglo, si es nulo(None) no muestra nada</p>   

```Python
    def imprimir(self):
        for k in self.__vector:
            print(k)
``` 
### 2.2.2.15. graficar(self, database: str, table: str):  
<p align = "Justify">En este método muestra la grafica de la tabla Hash. Para evaluar este método se necesita el nombre de la base de datos, y el nombre de la tabla que esta almacenada en la tabla Hash que deseas mostrar. </p>  

```Python
    def graficar(self, database: str, table: str):
        self.IniciarHashTable(database, table)#Se inicializa la tabla Hash
        s = open('graph.dot', 'w')#Se crea un documento .dot
        s.write('digraph G{\n')#Se escribe dentro del documento el codigo de graphviz
        s.write('rankdir = \"LR\" \n')
        s.write('node[shape=record]\n')
        llave = 0
        s.write('Nodo[label =\"<f' + str(llave) + '>')
        if self.__vector[llave] is None: 
            s.write('|<f' + str(llave) + '>')
        else:
            posicion = 0
            auxiliar = self.__vector[llave]
            for key in auxiliar:
                if(posicion != 0):
                    posicion = posicion + 1
                else:
                    s.write('|<f' + str(llave) + str(auxiliar[key]) + '>')
                    posicion = posicion + 1
        llave = llave + 1
        while llave < 20 #Se empieza a recorrer el arreglo de la tabla, si es diferente de nulo(None), muestra el dato almacenado en la tabla, de lo contrario sigue graficando
            if self.__vector[llave] is None:
                s.write('|<f' + str(llave) + '>')
            else:
                posicion = 0
                auxiliar = self.__vector[llave]
                for key in auxiliar:
                    if(posicion != 0):
                        posicion = posicion + 1
                    else:
                        s.write('|<f' + str(llave) + '> ' + str(auxiliar[key]))
                        posicion = posicion + 1
            llave = llave + 1
        s.write('\"];')
        llave = 0
        
        while llave < 20 ::#Empieza a recorrer otra vez el arreglo de la tabla, pero empieza a buscar si cada arreglo contiene un diccionario, si lo contiene recorre ese diccionario y lo muestra y une los nodos
            if self.__vector[llave] is not None:
                posicion = 0
                auxiliar = self.__vector[llave]
                dato = "Nodo:<f"
                for key in auxiliar:
                    if(posicion == 0):
                        posicion = posicion + 1
                    else:
                        s.write('nodo'+ str(llave) + str(posicion) + '[label= \"' + str(auxiliar[key]) + '\"];')  
                        if(posicion == 1):
                            s.write(dato + str(llave) + "> -> nodo" + str(llave) + str(posicion) + "; ")
                            dato = "nodo" + str(llave) + str(posicion)
                            posicion = posicion + 1
                        else:
                            s.write(dato + " -> nodo" + str(llave) + str(posicion) + ";")
                            dato = "nodo" + str(llave) + str(posicion)
                            posicion = posicion  + 1
            llave = llave + 1
        s.write('}')###Cierra el documento de graphviz
        s.close()#Cierra el documento .dot
        
        path=os.getcwd()
        print('path'+path)
        
        os.system('dot -Tpdf graph.dot -o graph.pdf')#Convierte el documento .dot a documento .pdf
        os.system('graph.pdf')#Abre el documento pdf
```        

### 1.2. Archivos.py
En este documento contine una clase donde se maneja la carga de archivos tipo .csv

### 1.2.1. Clase archivoCsv:
<p align ="Justify"> Para poder utilizar esta clase primero se importo la libreria csv, que nos sirve para la realizacion de carga de tipo archivo .csv . Tambien se importo la clase de NamesStructure para poder utilizar sus metodos. </p>

En esta clase contiene los siguientes métodos:

### 1.2.1.1. __init__(self):
<p align ="Justify"> Es el constructor de la clase archivoCsv. La función que esta incluida en el constructor nos permite invocar y conservar un método o atributo de una clase padre (primaria) desde una clase hija (secundaria) sin tener que nombrarla explícitamente. Esto nos brinda la ventaja de poder cambiar el nombre de la clase padre (base) o hija (secundaria) cuando queramos y aún así mantener un código funcional, sencillo  y mantenible.</p>

```Python
    def __init__(self):
        super().__init__()
```

### 1.2.1.2. leerCSV(self, file: str, database: str, table: str):
<p align="Justify">En este metodo hace la lectura de un archivo .csv . Para poder realizar esta lectura se necesita un objeto tipo File para poder crear el archivo, el nombre de la tabla donde se almacenara los datos del archivo y la base de datos donde esta almacenada esta tabla </p>

```Python
    def leerCSV(self, file: str, database: str, table: str):
        listaValores = []
        try: 
            
            if d.searchDatabase(database) == True:#Se verifica que la base de datos exista
                if d.buscarTablaDatabase(database,table) == True:#Se busca la tabla en la base de datos y se verifica que exista
                    with open(file) as f:                     #Se realiza la lectura del archivo y se separa cada dato por medio del delimitador (,)
                        reader = csv.reader(f, delimiter=",")

                        valorError = True
                        numeroColumnas = int(d.numeroDeColumnas(database,table)) #Se obtiene el numero de columna que contiene la tabla donde se almacenara el archivo
                        for x in reader: #[2,3,4,5]
                            if numeroColumnas == len(x): #Comprobamos que el numero de columnas sea igual al de csc
                                #aqui se ingresa la funcion insertar de la tabla hash 
                                valorRetorno = h.insert(database, table, x)
                                listaValores.append(valorRetorno)
                                
                            else:
                                valorError = False
                    
                    #Si hay error en la lectura la variable valorError devuelve True
                    if valorError == True:
                        return listaValores
                    else:
                        listaValores = []
                        return listaValores
                                
            else:
                return listaValores
        except:
            return listaValores
```    

### 1.3. HashMode.py
En este archivo se empaquetan todos los métodos para poder utilizarlos correctamente en el proyecto

```Python
import re
from NameStructure import ne as d 
from NameStructure import ht as h
from Archivos import archivo as ar

def createDatabase(database: str):
    return d.createDatabase(database)

def showDatabases():
    return d.showDatabases()

def alterDatabase(databaseOld, databaseNew):
    return d.alterDatabase(databaseOld, databaseNew)

def dropDatabase(database: str):
    return d.dropDatabase(database)

def createTable(database: str, table: str, numberColumns: int):
    return d.createTable(database, table, numberColumns)

def showTables(database: str):
    return d.showTables(database)

def extractTable(database: str, table: str):
    return h.extractTable(database, table)

def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any):
    try:
        return h.extractRangeTable(database, table, columnNumber, lower, upper)
    except:
        return None

def alterAddPK(database: str, table: str, columns: list):
    return d.alterAddPK(database, table, columns)

def alterDropPK(database: str, table: str):
    return d.alterAddPK(database, table)

def alterTable(database: str, tableOld: str, tableNew: str):
    return d.alterTable(database, tableOld, tableNew)

def alterAddColumn(database: str, table: str, default: any):
    return d.alterAddColumn(database, table, default)

def alterDropColumn(database: str, table: str, columnNumber: int):
    return d.alterDropColumn(database, table, columnNumber)

def dropTable(database: str, table: str):
    return d.dropTable(database, table)

def insert(database: str, table: str, register: list):
    try:
        return h.insert(database, table, register)
    except:
        return 1        

def loadCSV(file: str, database: str, table: str):
    return ar.leerCSV(file, database, table)

def extractRow(database: str, table: str, columns: list):
    try:
        return h.extractRow(database, table, columns)
    except:
        return []

def update(database: str, table: str, register: dict, columns: list):
    try:
        return h.update(database, table, register, columns)
    except:
        return 1

def delete(database: str, table: str, columns: list):
    try:
        return h.delete(database, table, columns)
    except:
        return 1

def truncate(database: str, table: str):
    try: 
        return h.truncate(database, table)
    except:
        return 1
``` 
### 1.4. graphics.py
En este archivo contiene toda la parte grafica del proyecto.Para poder mostrar la forma grafica en Python se importo la libreria tkinter y se importaron los documentos NameStructure.py y Archivos.py para la utilizacion de sus métodos, newData es quien importa el paquete de NameStructures.

```Python
import tkinter as Tk

import tkinter.ttk as Ttk
from NameStructure import ne as newData
from NameStructure import ht as newHash
from Archivos import archivo as newLoad

from tkinter import messagebox
from tkinter import filedialog
from tkinter import StringVar
```

>El siguiente método es para la realizacion de las ventanas

```Python
ventana = Tk.Tk()
ventana.geometry("400x200")#Dimension de la ventana
ventana.title("TytusDB | EDD A | G5")#Titulo de la ventana
ventana.resizable(0,0)#Para poder utilizar las funciones principales de la ventana, como cerrar, maximizar y minimizar.
```

>Se declara una lista, y se configura el icono de la ventana
tablas=[]
ventana.iconbitmap('images/icon.ico')

Acontinuacion se presenta los métodos que se utilizaran en el formulario

### 1.4.1 show_acercade():
En este método se muestra la informacion de los integrantes del grupo

```Python
def show_acercade():
    messagebox.showinfo("Acerca De...","GRUPO 5:\n\nCARLOS EMILIO CAMPOS MORÁN\nJOSÉ RAFAEL SOLIS FRANCO\nMÁDELYN ZUSETH PÉREZ ROSALES\nJOSÉ FRANCISCO DE JESÚS SANTOS SALAZAR")
```
### 1.4.2 saveDatabaseFile():
En el siguiente método se guardan las bases de datos

```Python
def saveDatabaseFile():
    newData.serialize("data/database",newData.database)
```
### 1.4.3 reloadTablas():
<p align="Justify"> es para actualizar el combobox de tablas. Primero dejo vacia la selecccion del combobox tablas,  obtengo la base de datos seleccionada en el combobox de databases, luego mando a llamar la funcion de showtables, el cual devuelve un arreglo y asigno a los datos de  combobox de tablas el arreglo o lista antes devuelta, , luego evualua si tablas es None, si no, luego revisa si esta vacia, si lo esta muestra un mensaje que esta vacia de lo contrario, que la seleccion de tablas  este vacio </p>

```Python
def reloadTablas():
    #print("CB_DB_CHANGE")
    #lb_databases_tables.delete(0,'end')
    cb_databases_tables.set("")
    db_name=cb_databases.get()
    tablas=newData.showTables(db_name)
    #for data in tablas:
    #    counter=0
    #    lb_databases_tables.insert(counter,str(data))
    #    counter=counter+1

    cb_databases_tables['values']=tablas
    if tablas is not None:
        if len(tablas)==0:
            messagebox.showerror("ERROR","No hay tablas en "+str(db_name))
        else:
            cb_databases_tables.set("")
```

### 1.4.4 showContenido(db,tabla):

```python
def showContenido(db,tabla):
    print('DB:'+str(db),'TB:'+str(tabla))
    newHash.graficar(str(db),str(tabla))
```

A continuacion los siguienten métodos se relacionan con la base de datos 

### 1.4.5 ventana_createDatabase():
<p align="Justify"> En este método incluye más métodos que son parte en la creacion de una base de datos. En el metodo MostrarError(value), se evaluan los mensajes de error cuando se crea una base de datos. En el método newDataCrearDb(nombre) imprime la creacion de la base de datos, y tambien guarda el archivo y actualiza la base de datos en el sistema. El codigo despues de los métodos es la estructura de la ventana que se mostrara en la creacion de la base de datos.</p>

```Python
def ventana_createDatabase():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table no existe")
    def newDataCrearDB(nombre):
        print("nombre nuevo: ",nombre)
        retorno=newData.createDatabase(nombre)
        if retorno ==0:
            messagebox.showinfo("Exito","Base Creada con exito")
            #saveDatabaseFile()
            cb_databases.set("")
            cb_databases['values']=newData.showDatabases() #actualiza bases de datos en el sistema
        else:
            mostrarError(retorno)
    
    ventanaCreateDB=Tk.Tk()
    ventanaCreateDB.geometry("400x200")
    ventanaCreateDB.title("Create Database")
    ventanaCreateDB.iconbitmap('images/icon.ico')
    
    label_nombre=Tk.Label(ventanaCreateDB,text="Nombre",font=("Arial",14))
    label_nombre.place(x=50,y=50)

    entry_nombre=Tk.Entry(ventanaCreateDB)
    entry_nombre.place(x=50,y=100)
    
    b_crear=Tk.Button(ventanaCreateDB,text="Crear Base de Datos",command=lambda: [newDataCrearDB(entry_nombre.get()),ventanaCreateDB.destroy()])
    b_crear.place(x=225,y=100)
``` 
### 1.4.6 ventana_alterDatabase():
<p align="Justify"> En este método incluye más métodos que son parte de la modificación de una base de datos. En el metodo MostrarError(value), se evaluan los mensajes de error cuando se modifica una base de datos. En el método newDataAlterDB(nombre) guarda los cambios realizados y actualiza la base de datos en el sistema. El codigo despues de los métodos es la estructura de la ventana que se mostrara en la modificacion de la base de datos.</p>

```Python
def ventana_alterDatabase():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database OLD no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Database NEW existente")
    def newDataAlterDB(old,new):
        retorno=newData.alterDatabase(old,new)
        if retorno==0:
            messagebox.showinfo("Exito","Base de Datos Actualizada \n"+str(old)+"->"+str(new))
            #saveDatabaseFile()
            cb_databases['values']=newData.showDatabases()
        else:
            mostrarError(retorno)
    ventanaAlterDB=Tk.Tk()
    ventanaAlterDB.geometry("400x200")
    ventanaAlterDB.title("Alter Database")
    ventanaAlterDB.iconbitmap('images/icon.ico')

    label_nombreOld=Tk.Label(ventanaAlterDB,text="Nombre Actual",font=("Arial",14))
    label_nombreOld.place(x=50,y=50)
    label_nombreNew=Tk.Label(ventanaAlterDB,text="Nombre Nuevo",font=("Arial",14))
    label_nombreNew.place(x=225,y=50)

    cb_nombreOld=Ttk.Combobox(ventanaAlterDB,state="readonly")
    cb_nombreOld['values']=newData.showDatabases()
    cb_nombreOld.place(x=50, y=100)
    entry_nombreNew=Tk.Entry(ventanaAlterDB)
    entry_nombreNew.place(x=225,y=100)

    b_alter=Tk.Button(ventanaAlterDB,text="Modificar Base de Datos",command=lambda :[newDataAlterDB(cb_nombreOld.get(),entry_nombreNew.get()),ventanaAlterDB.destroy()])
    b_alter.place(x=125,y=150)
``` 

### 1.4.7 ventana_dropDataBase()
<p align="Justify"> En este método incluye más métodos que son parte de la eliminacion de una base de datos. En el metodo MostrarError(value), se evaluan los mensajes de error cuando se elimina una base de datos. En el método newDataDropDB(nombre) guarda los cambios realizados al momento de eliminar la base de datos, guarda los cambios y actualiza la base de datos en el sistema. El codigo despues de los métodos es la estructura de la ventana que se mostrara en la eliminación de la base de datos.</p>

```Python
def ventana_dropDatabase():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
    def newDataDropDB(nombre):
        retorno=newData.dropDatabase(nombre)
        if retorno==0:
            messagebox.showinfo("Exito","Base de Datos Eliminada con exito")
            #saveDatabaseFile()
            cb_databases.set("")
            cb_databases['values']=newData.showDatabases()
            reloadTablas()
        else:
            mostrarError(retorno)

    ventanaDropDB=Tk.Tk()
    ventanaDropDB.geometry("400x200")
    ventanaDropDB.title("Drop Database")
    ventanaDropDB.iconbitmap('images/icon.ico')

    label_nombre=Tk.Label(ventanaDropDB,text="Nombre",font=("Arial",14))
    label_nombre.place(x=50,y=50)

    cb_dropDatabase=Ttk.Combobox(ventanaDropDB,state="readonly")
    cb_dropDatabase['values']=newData.showDatabases()
    cb_dropDatabase.place(x=50,y=100)

    
    b_drop=Tk.Button(ventanaDropDB,text="Eliminar Base de Datos",command=lambda: [newDataDropDB(cb_dropDatabase.get()),ventanaDropDB.destroy()])
    b_drop.place(x=225,y=100)
```
>A continuacion los mètodos que se presentan se relacionan con las tablas de datos

### 1.4.8 ventana_createTable():
<p align="Justify"> En este método incluye más métodos que son parte de la creacion de la tablas. En el metodo MostrarError(value), se evaluan los mensajes de error cuando se crea una tabla. En el método newDataCreateT(db,nombre,columna) realiza la creacion de tablas y guarda los cambios y actualiza la base de datos en el sistema. El codigo despues de los métodos es la estructura de la ventana que se mostrara en la creacion de tablas.</p>

```Python
def ventana_createTable():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table existe")
    def newDataCreateT(db,nombre,columna):
        print("db: "+str(db),"nombre: "+str(nombre),"col: "+str(columna))
        retorno=newData.createTable(db,nombre,columna)

        if retorno==0:
            messagebox.showinfo("Exito","Tabla "+str(nombre)+"\ncreada con exito en: "+str(db)+"\nColumna: "+str(columna))
            #saveDatabaseFile()
            reloadTablas()
        else:
            mostrarError(retorno)

    ventanaCreateTable=Tk.Tk()
    ventanaCreateTable.geometry("400x300")
    ventanaCreateTable.title("Create Table")
    ventanaCreateTable.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaCreateTable,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_createTable=Ttk.Combobox(ventanaCreateTable,state="readonly")
    cb_createTable['values']=newData.showDatabases()
    cb_createTable.place(x=225,y=50)

    label_nombre=Tk.Label(ventanaCreateTable,text="Nombre de Tabla",font=("Arial",14))
    label_nombre.place(x=50,y=100)

    entry_nombre=Tk.Entry(ventanaCreateTable)
    entry_nombre.place(x=225,y=100)

    label_columna=Tk.Label(ventanaCreateTable,text="# Columna",font=("Arial",14))
    label_columna.place(x=50,y=150)

    entry_columna=Tk.Entry(ventanaCreateTable)
    entry_columna.place(x=225,y=150)

    b_createTable=Tk.Button(ventanaCreateTable,text="Crear Tabla",command=lambda : [newDataCreateT(cb_createTable.get(),entry_nombre.get(),entry_columna.get()),ventanaCreateTable.destroy()])
    b_createTable.place(x=50,y=200)
    pass
```

### 1.4.9 ventana_AlterTable():
<p align="Justify"> En este método incluye más métodos que son parte de la modificacion de tablas. En el metodo MostrarError(value), se evaluan los mensajes de error cuando se modifica una tabla. En el método updateAlterCB(nombre) muestra el listado de tablas y el método de alterTable(db,old,new) realiza la modificacion de la tabla, guarda los cambios y actualiza la base de datos en el sistema. El codigo despues de los métodos es la estructura de la ventana que se mostrara en la modificacion de tablas.</p>

```Python
def ventana_alterTable():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table OLD no existe")
        if value==4:
            messagebox.showerror("Error: "+str(value),"Tabla NEW existente")
    def updateAlterCB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    def alterTable(db,old,new):
        retorno=newData.alterTable(db,old,new)
        if retorno==0:
            print(db,old,new)
            messagebox.showinfo("Exito","Se ha renombrado la tabla:\n"+str(old)+"->"+str(new))
            #saveDatabaseFile()
            reloadTablas()
        else:
            mostrarError(retorno)
    ventanaAlterTable=Tk.Tk()
    ventanaAlterTable.geometry("600x300")
    ventanaAlterTable.title("Alter Table")
    ventanaAlterTable.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaAlterTable,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaAlterTable,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaAlterTable,text="Mostrar Tablas",command=lambda:[updateAlterCB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaAlterTable,text="Tabla a Modificar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaAlterTable,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)
    
    label_table=Tk.Label(ventanaAlterTable,text="Nuevo Nombre",font=("Arial",14))
    label_table.place(x=50,y=150)

    entry_newName=Tk.Entry(ventanaAlterTable)
    entry_newName.place(x=225,y=150)

    b_alter=Tk.Button(ventanaAlterTable,text="Modificar Tabla",command=lambda:[alterTable(cb_showdb.get(),cb_showtable.get(),entry_newName.get()),ventanaAlterTable.destroy()])
    b_alter.place(x=400,y=150)
``` 
### 1.4.10 ventana_delTable():
<p align="Justify"> En este método incluye más métodos que son parte de la eliminacion de tablas. En el metodo MostrarError(value), se evaluan los mensajes de error cuando se elimina una tabla. En el método updateDropDB(nombre) muestra el listado de las tablas donde se hara la eliminacion y en el método dropTable(db,name) realiza la eliminacion de tablas y guarda los cambios y actualiza la base de datos en el sistema. El codigo despues de los métodos es la estructura de la ventana que se mostrara en la eliminacion de tablas.</p>

```Python
def ventana_delTable():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table existe")
    def updateDropDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)
    def dropTable(db,name):
        retorno=newData.dropTable(db,name)
        if retorno==0:
            messagebox.showinfo("Exito","Se ha eliminado la tabla \'"+str(name)+"\' de "+str(db))
            #saveDatabaseFile()
            reloadTablas()
        else:
            mostrarError(retorno)
    
    ventanaDropTable=Tk.Tk()
    ventanaDropTable.geometry("600x200")
    ventanaDropTable.title("Drop Table")
    ventanaDropTable.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaDropTable,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaDropTable,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaDropTable,text="Mostrar Tablas",command=lambda:[updateDropDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaDropTable,text="Tabla a Eliminar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaDropTable,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    b_dropTable=Tk.Button(ventanaDropTable,text="Eliminar Tabla",command=lambda:[dropTable(cb_showdb.get(),cb_showtable.get()),ventanaDropTable.destroy()])
    b_dropTable.place(x=400,y=100)
```

### 1.4.11 ventana_alterAddColumn():
<p align="Justify"> En este método incluye más métodos que son parte de la agregacion de columnas en una tabla. En el metodo MostrarError(value), se evaluan los mensajes de error cuando se agregan columnas a una tabla. En el método updateAlColDB(nombre) muestra el listado de las columnas que contiene la tabla a modificar y en el método AlterAddCol(db,table,any_one) realiza agregacion de columnas a la tabla y guarda los cambios y actualiza la base de datos en el sistema. El codigo despues de los métodos es la estructura de la ventana que se mostrara en la añadidura de columnas de tablas.</p>

def ventana_alterAddColumn():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table no existe")
    def updateAlColDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)
    def alterAddCol(db,table,any_one):
        retorno=newData.alterAddColumn(db,table,any_one)
        if retorno==0:
            messagebox.showinfo("Exito","Se ha agregado columna \'"+str(any_one)+"\' en tabla "+str(table)+" de DB: "+str(db))
            #saveDatabaseFile()
            reloadTablas()
        else:
            mostrarError(retorno)
    
    ventanaAlterAddCol=Tk.Tk()
    ventanaAlterAddCol.geometry("600x200")
    ventanaAlterAddCol.title("Alter Add Column")
    ventanaAlterAddCol.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaAlterAddCol,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaAlterAddCol,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaAlterAddCol,text="Mostrar Tablas",command=lambda:[updateAlColDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaAlterAddCol,text="Tabla a Modificar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaAlterAddCol,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    label_column=Tk.Label(ventanaAlterAddCol,text="Default Columna",font=("Arial",14))
    label_column.place(x=50,y=150)

    entry_col=Tk.Entry(ventanaAlterAddCol)
    entry_col.place(x=225,y=150)

    b_addcol=Tk.Button(ventanaAlterAddCol,text="Agregar Columna",command=lambda:[alterAddCol(cb_showdb.get(),cb_showtable.get(),entry_col.get()),ventanaAlterAddCol.destroy()])
    b_addcol.place(x=400,y=150)


### 1.4.12 ventana_AlterDropColumn():
<p align="Justify"> En este método incluye más métodos que son parte de la eliminacion de columnas en una tabla. En el metodo MostrarError(value), se evaluan los mensajes de error cuando se eliminan columnas a una tabla. En el método updateAlColDB(nombre) muestra el listado de las columnas que contiene la tabla a modificar y en el método AlterDropCol(db,table,col) realiza la eliminación de columnas a la tabla y guarda los cambios y actualiza la base de datos en el sistema. El codigo despues de los métodos es la estructura de la ventana que se mostrara en la eliminacion de columnas de una tabla.</p>

```Python
def ventana_AlterDropColumn():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table no existe")
        if value==4:
            messagebox.showerror("Error: "+str(value),"Llave no puede eliminarse o tabla quedarse sin columnas")
        if value==5:
            messagebox.showerror("Error: "+str(value),"Columna fuera de limites")
    def updateAlColDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    def alterDropCol(db,table,col):
        retorno=newData.alterDropColumn(db,table,col)
        if retorno==0:
            messagebox.showinfo("Exito","Se ha Eliminado la columna: \'"+str(col)+"\' de tabla "+str(table)+" en DB: "+str(db))
            #saveDatabaseFile()
            reloadTablas()
        else:
            mostrarError(retorno)
    ventanaAlterDropCol=Tk.Tk()
    ventanaAlterDropCol.geometry("600x200")
    ventanaAlterDropCol.title("Alter Drop Column")
    ventanaAlterDropCol.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaAlterDropCol,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaAlterDropCol,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaAlterDropCol,text="Mostrar Tablas",command=lambda:[updateAlColDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaAlterDropCol,text="Tabla a Modificar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaAlterDropCol,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    label_col=Tk.Label(ventanaAlterDropCol,text="# Columna",font=("Arial",14))
    label_col.place(x=50,y=150)

    entry_col=Tk.Entry(ventanaAlterDropCol)
    entry_col.place(x=225,y=150)

    b_dropcol=Tk.Button(ventanaAlterDropCol,text="Eliminar Columna",command=lambda:[alterDropCol(cb_showdb.get(),cb_showtable.get(),entry_col.get()),ventanaAlterDropCol.destroy()])
    b_dropcol.place(x=400,y=150)
``` 

### 1.4.13 ventana_AlterAddPk():
<p align="Justify"> En este método incluye más métodos que son parte de la agregacion de llaves primaria a la tabla. En el metodo MostrarError(value), se evaluan los mensajes de error cuando se hace la agregacion de llaves primarias. En el método showColNumber(db,table) muestra la cantidad de columnas que contiene la tabla  y en el método updateAlColDB(nombre) muestra el listado de tablas, y en el método addPk(db,table,colist) añade las llaves primarias a la tabla, guarda los cambios y actualiza la base de datos en el sistema. El codigo despues de los métodos es la estructura de la ventana que se mostrara en la agregacion de llaves primarias de una tabla.</p>

```Python
def ventana_AlterAddPK():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table no existe")
        if value==4:
            messagebox.showerror("Error: "+str(value),"Llave primaria existente")
        if value==5:
            messagebox.showerror("Error: "+str(value),"Columna fuera de limites")
        else:
            messagebox.showerror("Error:", "Error desconocido")

    def showColNumber(db,table):
        messagebox.showinfo("Cantidad de Columnas","La tabla contiene: "+str(newData.numeroDeColumnas(db,table))+" columnas")

    def updateAlColDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    def addPk(db,table,colist):
        colList=colist.split(",")
        retorno=newData.alterAddPK(db,table,colList)
        print("RetornoPK",retorno)
        if retorno==0:
            messagebox.showinfo("Exito","Operacion Exitosa")
        else:
            mostrarError(retorno)

    ventanaAlterAddPk=Tk.Tk()
    ventanaAlterAddPk.geometry("600x200")
    ventanaAlterAddPk.title("Alter Add Primary Key")
    ventanaAlterAddPk.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaAlterAddPk,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaAlterAddPk,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaAlterAddPk,text="Mostrar Tablas",command=lambda:[updateAlColDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaAlterAddPk,text="Tabla a Modificar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaAlterAddPk,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    b_showcolnum=Tk.Button(ventanaAlterAddPk,text="Mostrar Cantidad de Columnas",command=lambda : [showColNumber(cb_showdb.get(),cb_showtable.get())])
    b_showcolnum.place(x=400,y=100)


    label_columnas=Tk.Label(ventanaAlterAddPk,text="Columnas \nEj: 0,1,2",font=("Arial",14))
    label_columnas.place(x=50,y=135)

    entry_columnas=Tk.Entry(ventanaAlterAddPk)
    entry_columnas.place_configure(x=225,y=150)

    b_AddPk=Tk.Button(ventanaAlterAddPk,text="Agregar PK",command=lambda:[addPk(cb_showdb.get(),cb_showtable.get(),entry_columnas.get()),ventanaAlterAddPk.destroy()])
    b_AddPk.place(x=400,y=150)
```

### 1.4.14 ventana_AlterDropPK()):
<p align="Justify"> En este método incluye más métodos que son parte de la agregacion de llaves primaria a la tabla. En el metodo MostrarError(value), se evaluan los mensajes de error cuando se hace la agregacion de llaves primarias. En el método showColNumber(db,table) muestra la cantidad de columnas que contiene la tabla  y en el método updateAlColDB(nombre) muestra el listado de tablas, y en el método addPk(db,table,colist) añade las llaves primarias a la tabla, guarda los cambios y actualiza la base de datos en el sistema. El codigo despues de los métodos es la estructura de la ventana que se mostrara en la agregacion de llaves primarias de una tabla.</p>

```Python
def ventana_AlterDropPK():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table no existe")
        if value==4:
            messagebox.showerror("Error: "+str(value),"Llave primaria no existente")
        else:
            messagebox.showerror("Error:", "Error desconocido")

    def updateAlColDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    def dropPK(db,tabla):
        retorno=newData.alterDropPK(str(db),str(tabla))
        if retorno==0:
            messagebox.showinfo("Exito","Operacion Exitosa")
        else:
            mostrarError(retorno)

    ventanaAlterDropPk=Tk.Tk()
    ventanaAlterDropPk.geometry("600x200")
    ventanaAlterDropPk.title("Alter Drop Primary Key")
    ventanaAlterDropPk.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaAlterDropPk,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaAlterDropPk,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaAlterDropPk,text="Mostrar Tablas",command=lambda:[updateAlColDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaAlterDropPk,text="Tabla a Modificar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaAlterDropPk,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    b_dropPK=Tk.Button(ventanaAlterDropPk,text="Drop Primary Key",command=lambda:[dropPK(cb_showdb.get(),cb_showtable.get()),ventanaAlterDropPk.destroy()])
    b_dropPK.place(x=400,y=100)
```
### 1.4.15 ventana_ExtractTable():
<p align="Justify"> </p>

```Python
def ventana_ExtractTable():
    def updateAlColDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    def loadTable(db,tabla):
        retorno=newHash.extractTable(db,tabla)
        lb_tabla.delete('0',Tk.END)
        if retorno==None:
            messagebox.showerror("Error","Ha ocurrido un error")
        elif retorno is not None:
            if len(retorno)!=0:
                for r in retorno:
                    contador=1
                    lb_tabla.insert(contador,str(r))
                    contador=contador+1
            else:
                messagebox.showerror("Error","Lista Vacia")

    ventanaExtractTable=Tk.Tk()
    ventanaExtractTable.geometry("600x400")
    ventanaExtractTable.title("Extract Table")
    ventanaExtractTable.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaExtractTable,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaExtractTable,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaExtractTable,text="Mostrar Tablas",command=lambda:[updateAlColDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaExtractTable,text="Tabla a Extraer",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaExtractTable,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    b_extract=Tk.Button(ventanaExtractTable,text="Extract Table",command=lambda:[loadTable(cb_showdb.get(),cb_showtable.get())])
    b_extract.place(x=400,y=100)

    sb=Tk.Scrollbar(ventanaExtractTable)
    sb.pack(side=Tk.RIGHT,fill=Tk.Y)

    lb_tabla=Tk.Listbox(ventanaExtractTable,width=82,yscrollcommand=sb.set)
    lb_tabla.place(x=50,y=150)
    sb.config(command=lb_tabla.yview)

def ventana_ExtractRT():
    def showColNumber(db,table):
        cantidad=newData.numeroDeColumnas(db,table)
        messagebox.showinfo("Cantidad de Columnas","La tabla contiene: "+str(cantidad)+" columnas")
        valores=[]
        contador=0
        while contador<int(cantidad):
            valores.append(contador)
            contador=contador+1
        sb_colnumber['values']=valores
        sb_colnumber.update()
    def updateAlColDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    def extractRT(db,tabla,colnum,low,up):
        retorno=newHash.extractRangeTable(db,tabla,colnum,low,up)
        lb_tabla.delete('0',Tk.END)
        if retorno==None:
            messagebox.showerror("Error","Ha ocurrido un error")
        elif retorno is not None:
            if len(retorno)!=0:
                for r in retorno:
                    contador=1
                    lb_tabla.insert(contador,str(r))
                    contador=contador+1
            else:
                messagebox.showerror("Error","Lista Vacia")
    
    ventanaExtractRTable=Tk.Tk()
    ventanaExtractRTable.geometry("600x800")
    ventanaExtractRTable.title("Extract Range Table")
    ventanaExtractRTable.iconbitmap("images/icon.ico")
    
    label_db=Tk.Label(ventanaExtractRTable,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaExtractRTable,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaExtractRTable,text="Mostrar Tablas",command=lambda:[updateAlColDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaExtractRTable,text="Tabla a Modificar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaExtractRTable,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    b_showcolnum=Tk.Button(ventanaExtractRTable,text="Mostrar Cantidad de Columnas",command=lambda : [showColNumber(cb_showdb.get(),cb_showtable.get())])
    b_showcolnum.place(x=400,y=100)

    label_colNum=Tk.Label(ventanaExtractRTable,text="Columna #: ",font=("Arial",14))
    label_colNum.place(x=50,y=150)
    
    sb_colnumber=Tk.Spinbox(ventanaExtractRTable)
    sb_colnumber.place(x=225,y=150)
    
    label_lower=Tk.Label(ventanaExtractRTable,text="Lower",font=("Arial",14))
    label_lower.place(x=50,y=200)

    entry_lower=Tk.Entry(ventanaExtractRTable)
    entry_lower.place(x=225,y=200)

    label_upper=Tk.Label(ventanaExtractRTable,text="Upper",font=("Arial",14))
    label_upper.place(x=50,y=250)

    entry_upper=Tk.Entry(ventanaExtractRTable)
    entry_upper.place(x=225,y=250)

    b_extract=Tk.Button(ventanaExtractRTable,text="Extract Range Table",command=lambda:[extractRT(cb_showdb.get(),cb_showtable.get(),sb_colnumber.get(),entry_lower.get(),entry_upper.get())])
    b_extract.place(x=400,y=250)

    sb=Tk.Scrollbar(ventanaExtractRTable)
    sb.pack(side=Tk.RIGHT,fill=Tk.Y)

    lb_tabla=Tk.Listbox(ventanaExtractRTable,width=82,yscrollcommand=sb.set)
    lb_tabla.place(x=50,y=300)
    sb.config(command=lb_tabla.yview)

``` 
>A continuacion los métodos que se presentan se relacionan con las tuplas

### 1.4.16 ventana_Insert():
<p align="Justify"> </p>

```Python
def ventana_Insert():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table no existe")
        if value==4:
            messagebox.showerror("Error: "+str(value),"Llave primaria duplicada")
        if value==5:
            messagebox.showerror("Error: "+str(value),"Columna fuera de limites")
        else:
            messagebox.showerror("Error:", "Error desconocido")
    def updateAlColDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    def insertRegister(db,tabla,registro):
        print("db"+str(db),"table:"+str(tabla),"reg: "+str(registro))
        retorno=newHash.insert(db,tabla,registro.split(","))
        if retorno==0:
            messagebox.showinfo("Exito","Se ha ingresado el registro a la tabla")
        else:
            mostrarError(retorno)
    ventanaInsert=Tk.Tk()
    ventanaInsert.geometry("600x400")
    ventanaInsert.title("Insert")
    ventanaInsert.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaInsert,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaInsert,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaInsert,text="Mostrar Tablas",command=lambda:[updateAlColDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaInsert,text="Tabla a Insertar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaInsert,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    l_registro=Tk.Label(ventanaInsert,text="Registro",font=("Arial",14))
    l_registro.place(x=50,y=150)

    entry_registro=Tk.Entry(ventanaInsert,width=50)
    entry_registro.place(x=225,y=150)

    b_cargar=Tk.Button(ventanaInsert,text="Insert",command=lambda: [insertRegister(cb_showdb.get(),cb_showtable.get(),entry_registro.get()),ventanaInsert.destroy()])
    b_cargar.place(x=50,y=200)

```
### 1.4.17 ventana_ExtraerRow():
<p align="Justify"> </p>

```Python
def ventana_ExtraerRow():
    def updateAlColDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    def extractRow(db,table,columns):
        retorno=newHash.extractRow(db,table,columns.split(","))
        lb_tabla.delete('0',Tk.END)
        if retorno==None:
            messagebox.showerror("Error","Ha ocurrido un error")
        elif retorno is not None:
            if len(retorno)!=0:
                for r in retorno:
                    contador=1
                    lb_tabla.insert(contador,str(r))
                    contador=contador+1
            else:
                messagebox.showerror("Error","Lista Vacia")


    ventanaExtractRow=Tk.Tk()
    ventanaExtractRow.geometry("600x500")
    ventanaExtractRow.title("Extract Row")
    ventanaExtractRow.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaExtractRow,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaExtractRow,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaExtractRow,text="Mostrar Tablas",command=lambda:[updateAlColDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaExtractRow,text="Tabla a Extraer",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaExtractRow,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)
    
    label_columns=Tk.Label(ventanaExtractRow,text="Columnas",font=("Arial",14))
    label_columns.place(x=50,y=150)

    entry_columns=Tk.Entry(ventanaExtractRow,width=50)
    entry_columns.place(x=225,y=150)

    b_extract=Tk.Button(ventanaExtractRow,text="Extract Row",command=lambda:[extractRow(cb_showdb.get(),cb_showtable.get(),entry_columns.get())])
    b_extract.place(x=50,y=200)

    sb=Tk.Scrollbar(ventanaExtractRow)
    sb.pack(side=Tk.RIGHT,fill=Tk.Y)

    lb_tabla=Tk.Listbox(ventanaExtractRow,width=82,yscrollcommand=sb.set)
    lb_tabla.place(x=50,y=250)
    sb.config(command=lb_tabla.yview)
``` 
### 1.4.18 ventana_Update():
<p align="Justify"> </p>

```Python
def ventana_Update():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table no existe")
        if value==4:
            messagebox.showerror("Error: "+str(value),"Llave primaria no existe")
        else:
            messagebox.showerror("Error:", "Error desconocido")
    def updateAlColDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    def updateRegister(db,table,register,col):
        #diccionario=dict(zip(range(len(register)),register))
        diccionario={}
        one_step=register.replace("\"","").split(",")
        for c in one_step:
            reg_temp=c.split(":")
            diccionario[reg_temp[0]]=reg_temp[1]

        retorno=newHash.update(db,table,diccionario,col.split(","))
        if retorno==0:
            messagebox.showinfo("Exito","Se ha realizado un Update a la tabla")
        else:
            mostrarError(retorno)

    ventanaUpdate=Tk.Tk()
    ventanaUpdate.geometry("600x400")
    ventanaUpdate.title("Update")
    ventanaUpdate.iconbitmap("images/icon.ico")
    
    label_db=Tk.Label(ventanaUpdate,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaUpdate,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaUpdate,text="Mostrar Tablas",command=lambda:[updateAlColDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaUpdate,text="Tabla a Actualizar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaUpdate,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    l_register=Tk.Label(ventanaUpdate,text="Registro",font=("Arial",14))
    l_register.place(x=50,y=150)

    entry_register=Tk.Entry(ventanaUpdate,width=50)
    entry_register.place(x=225,y=150)

    l_columns=Tk.Label(ventanaUpdate,text="Columns",font=("Arial",14))
    l_columns.place(x=50,y=200)

    entry_columns=Tk.Entry(ventanaUpdate,width=50)
    entry_columns.place(x=225,y=200)

    b_update=Tk.Button(ventanaUpdate,text="Update",command=lambda:[updateRegister(cb_showdb.get(),cb_showtable.get(),entry_register.get(),entry_columns.get())])
    b_update.place(x=50,y=250)
```

### 1.4.19 ventana_Delete():
<p align="Justify"> </p>

```Python
def ventana_Delete():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table no existe")
        if value==4:
            messagebox.showerror("Error: "+str(value),"Llave primaria no existe")
        else:
            messagebox.showerror("Error:", "Error desconocido")

    def updateAlColDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    def deleteEntry(db,table,columns):
        retorno=newHash.delete(db,table,columns.split(","))
        if retorno==0:
            messagebox.showinfo("Exito","Se ha eliminado el registro de la tabla")
        else:
            mostrarError(retorno)
    ventanaDelete=Tk.Tk()
    ventanaDelete.geometry("600x400")
    ventanaDelete.title("Delete")
    ventanaDelete.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaDelete,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaDelete,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaDelete,text="Mostrar Tablas",command=lambda:[updateAlColDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaDelete,text="Tabla a Modificar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaDelete,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    l_columns=Tk.Label(ventanaDelete,text="Columns",font=("Arial",14))
    l_columns.place(x=50,y=150)

    entry_columns=Tk.Entry(ventanaDelete,width=50)
    entry_columns.place(x=225,y=150)

    b_delete=Tk.Button(ventanaDelete,text="Delete",command=lambda:[deleteEntry(cb_showdb.get(),cb_showtable.get(),entry_columns.get()),ventanaDelete.destroy()])
    b_delete.place(x=50,y=200)
```

### 1.4.20 ventana_Truncate():
<p align="Justify"> </p>

```Python
def ventana_Truncate():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table no existe")
        if value==4:
            messagebox.showerror("Error: "+str(value),"Llave primaria no existe")
        else:
            messagebox.showerror("Error:", "Error desconocido")
    def updateAlColDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    def truncateDB(db,table):
        retorno=newHash.truncate(db,table)
        if retorno==0:
            messagebox.showinfo("Exito","Registros de tabla han sido eliminados")
        else:
            mostrarError(retorno)

    ventanaTruncate=Tk.Tk()
    ventanaTruncate.geometry("600x200")
    ventanaTruncate.title("Truncate")
    ventanaTruncate.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaTruncate,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaTruncate,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaTruncate,text="Mostrar Tablas",command=lambda:[updateAlColDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaTruncate,text="Tabla a Truncar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaTruncate,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    b_truncate=Tk.Button(ventanaTruncate,text="Truncate",command=lambda:[truncateDB(cb_showdb.get(),cb_showtable.get()),ventanaTruncate.destroy()])
    b_truncate.place(x=400,y=100)

```

### 1.4.21 ventana_arbirCSV():
<p align="Justify">En este método lee un documento .csv y sube los datos a las tablas respectivas y guarda los datos en el sistema, y tambien incluye el codigo de diseño de la ventana que se muestra al momento de leer un documento</p>

```Python
def ventana_abrirCSV():
    def loadData(file_path,db,table):
        if file_path!="":
            if db !="":
                if table !="":
                    errorCode=newLoad.leerCSV(file_path,db,table)
                    contador_exitoso=0
                    contador_errorOP=0
                    contador_dbNE=0
                    contador_tNE=0
                    contador_llDup=0
                    contador_colOut=0
                    contador_desconocido=0
                    for e in errorCode:
                        if e==0:
                            contador_exitoso=contador_exitoso+1
                        if e==1:
                            contador_errorOP=contador_errorOP+1
                        if e==2:
                            contador_dbNE=contador_dbNE+1
                        if e==3:
                            contador_tNE=contador_tNE+1
                        if e==4:
                            contador_llDup=contador_llDup+1
                        if e==5:
                            contador_colOut=contador_colOut+1
                        else:
                            contador_desconocido=contador_desconocido+1
                    messagebox.showinfo("Archivo Cargado","Operaciones Exitosas: "+str(contador_exitoso)+"\nErrores en Operacion: "+str(contador_errorOP)+"\nDatabase no Existente: "+str(contador_dbNE)+"\nLlave Primaria Duplicada: "+str(contador_llDup)+"\nColumnas Fuera de Limites: "+str(contador_colOut))
            if db=="":
                messagebox.showerror("Error", "No ha seleccionado una Base de Datos")
            else:
                if table=="":
                    messagebox.showerror("Error","No ha seleccionado una Tabla")
        elif file_path=="":
            messagebox.showerror("Error","No se ha seleccionado un archivo")

    def updateCSVDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    archivo_csv =filedialog.askopenfilename(filetypes=[("Archivo de Carga","*.csv")])
    print("File",archivo_csv)
    ventanaCSV=Tk.Tk()
    ventanaCSV.geometry("600x400")
    ventanaCSV.title("Abrir CSV")
    ventanaCSV.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaCSV,text="Base de Datos",font=(("Arial",14)))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaCSV,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaCSV,text="Mostrar Tablas",command=lambda:[updateCSVDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaCSV,text="Tabla a Cargar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaCSV,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    label_path=Tk.Label(ventanaCSV,text="Path",font=("Arial",14))
    label_path.place(x=50,y=150)

    entry_path=Tk.Entry(ventanaCSV,width=44)
    entry_path.place(x=100,y=155)
    entry_path.insert(0,str(archivo_csv))
    entry_path.update()
    entry_path.config(state="readonly")

    b_loadData=Tk.Button(ventanaCSV,text="Carga Informacion",command=lambda:[loadData(archivo_csv,cb_showdb.get(),cb_showtable.get()),ventanaCSV.destroy()])
    b_loadData.place(x=400,y=150)
    
```
> A continuacion se muestra un listado de todos los menus que contiene el formulario, asi como los métodos que contienen al momento de su funcion 

```Python
#objetos de menu
bar_menu=Tk.Menu(ventana)

#cascada Archivo
archivo=Tk.Menu(bar_menu,tearoff=0)
archivo.add_command(label="Guardar",command=saveDatabaseFile)
archivo.add_separator()
archivo.add_command(label="Salir...",command=ventana.quit)

#Cascada ayuda
ayuda=Tk.Menu(bar_menu,tearoff=0)
ayuda.add_command(label="Ayuda")
ayuda.add_command(label="Acerca de...",command=show_acercade)

#cascada Database
database=Tk.Menu(bar_menu,tearoff=0)
database.add_command(label="Create Database",command=ventana_createDatabase)
database.add_command(label="Alter Database",command=ventana_alterDatabase)
database.add_command(label="Drop Database",command=ventana_dropDatabase)

#cascada Tablas
tables=Tk.Menu(bar_menu,tearoff=0)
tables.add_command(label="Create Table",command=ventana_createTable)
tables.add_command(label="Alter Table",command=ventana_alterTable)
tables.add_command(label="Drop Table",command=ventana_delTable)
tables.add_separator()
tables.add_command(label="Add Column",command=ventana_alterAddColumn)
tables.add_command(label="Drop Column",command=ventana_AlterDropColumn)
tables.add_separator()
tables.add_command(label="Alter Add Primary Key",command=ventana_AlterAddPK)
tables.add_command(label="Alter Drop Primary Key",command=ventana_AlterDropPK)
tables.add_command(label="Alter Add Foreign Key",state=Tk.DISABLED)
tables.add_command(label="Alter Add Index",state=Tk.DISABLED)
tables.add_separator()
tables.add_command(label="Extract Table",command=ventana_ExtractTable)
tables.add_command(label="Extract Range Table",command=ventana_ExtractRT)

#cascada Tuplas
tuplas=Tk.Menu(bar_menu,tearoff=0)
tuplas.add_command(label="Insert",command=ventana_Insert)
tuplas.add_command(label="Load CSV",command=ventana_abrirCSV)
tuplas.add_command(label="Extract Row",command=ventana_ExtraerRow)
tuplas.add_command(label="Update",command=ventana_Update)
tuplas.add_command(label="Delete",command=ventana_Delete)
tuplas.add_command(label="Truncate",command=ventana_Truncate)

#--Cargar al menu las cascadas
bar_menu.add_cascade(label="Archivo",menu=archivo)
bar_menu.add_cascade(label="Base De Datos",menu=database)
bar_menu.add_cascade(label="Tablas",menu=tables)
bar_menu.add_cascade(label="Tuplas",menu=tuplas)
bar_menu.add_cascade(label="Ayuda",menu=ayuda)

```
>Es la variable que se utiliza en todo el formulario

```python
#variables
tablas=[]
```

>A continuación se muestra un listado de los objetos que se agregaron en el formulario

```Python
#objetos en la ventana
label_db = Tk.Label(ventana,text="Bases de Datos")
label_db_tables=Tk.Label(ventana,text="Tablas en\n Base de Datos")

cb_databases=Ttk.Combobox(ventana,state="readonly")
cb_databases['values']=newData.showDatabases()
#cb_databases.current(1)

cb_databases_tables=Ttk.Combobox(ventana,state="readonly")
cb_databases_tables['values']=newData.showTables(cb_databases.get())
#lb_databases_tables=Tk.Listbox(ventana)
```
>A continuacion se muestra la creacion de frames, el codigo utilizado para su diseño

```Python
b_mostrarTablas=Tk.Button(ventana,text="Mostrar Tablas",command=reloadTablas)
b_mostrarinfo=Tk.Button(ventana,text="Mostrar Contenido",command=lambda:[showContenido(cb_databases.get(),cb_databases_tables.get())])
#posicion de objetos
#labels
label_db.place(x=25,y=25)
label_db_tables.place(x=25,y=65)
```
>A continuacion se muestra la creacion de combobox, asi como el codigo utilizado para su diseño

```Python
cb_databases.place(x=125,y=25)
cb_databases_tables.place(x=125,y=75)

#lb_databases_tables.grid(column=1,row=1)
```
>Acontinuacion se muestra la creacion de botones, asi como el codigo utilizado para su diseño

```Python
b_mostrarTablas.place(x=275,y=25)
b_mostrarinfo.place(x=275,y=75)

#image_viewer=Tk.Canvas(ventana,height=475,width=750)
#image_viewer.place(x=25,y=100)
#img = Tk.PhotoImage(file="images/descarga.gif")
#image_viewer.create_image(20,20,anchor=Tk.NW,image=img)
``` 

>A continuacion  se muestra los widgets condicionales

```Python
#conditionals widgets
tmp_showDB=[]
tmp_showDB=newData.showDatabases()
```

>Acontinuacion se muestra para la ejecucion de las ventanas, asi como la configuracion para la funcion de los menus

```Python
ventana.config(menu=bar_menu)
ventana.mainloop()
#coocio
```
### 1.4. __init__.py

Este archivo se utiliza para la configuracion de importaciones. Puede estar vacio.


## 2. Carpetas

En el proyecto siguiente contiene dos carpetas que se utilizan para el manejo del proyecto

### 2.1. Carpeta Images
En esta carpeta se almacena todas las imagenes que se utilizan en el diseño del formulario

### 2.2. Carpeta data
En esta carpeta se almacenan todos los archivos que se generan durante la ejecución del proyecto

---


