###### UNIVERSIDAD DE SAN CARLOS DE GUATEMALA
###### FACULTAD DE INGENIERÍA
###### INGENIERÍA EN CIENCIAS Y SISTEMAS
###### ESTRUCTURAS DE DATOS
###### SECCIÓN A
___
###### EQUIPO: 10
___
***

# **MANUAL TÉCNICO**

## **ENTORNO DE DESARROLLO**
- Versión de Python utilizada: 3.9.0
- Versión de Graphviz utilizada: 2.38.0
- Librería utilizada para la interfaz gráfica: Tkinter
- Librería utilizada para la encriptación: Cryptography.Fernet
- Biblioteca utilizada para la compresión: zlib

## **DESCRIPCIÓN DE LA SOLUCIÓN**
TytusDB es un administrador de base de datos de código, desarrollado utilizando como lenguaje de programación Python. Una de las principales características de este proyecto es que el usuario puede elegir el modo en que desea almacenar la información.

## **ESTRUCTURA DEL PAQUETE**
La estructura del paquete se rige de acuerdo a la guía PEP 8.
~~~
storage/
    __init__.py
    avl/
        __init__.py
        avl_mode.py
        otros.py
    b/
        __init__.py
        b_mode.py
        otros.py
    bplus/
        __init__.py
        bplus_mode.py
        otros.py
    dict/
        __init__.py
        dict_mode.py
        otros.py
    isam/
        __init__.py
        isam_mode.py
        otros.py
    json/
        __init__.py
        json_mode.py
        otros.py
    hash/
        __init__.py
        mode.py
        otros.py 
~~~

## **CODIFICACIÓN**
TytusDB permite tres tipos de codificaciones:
- ASCII
- ISO 8859-1
- UTF8

## **CHECKSUM**
Para calcular el Checksum deuna base de datos se utilizaron dos algoritmos:
- MD5
- SHA256

## **COMPRESIÓN DE DATOS**
Para realizar la compresión de los datos se utilizaron la funciones compress y decompresss de la biblioteca zlib de Python.

## **SEGURIDAD**

### CRIPTOGRAFÍA
Se utilizó una herramienta de cifrado simétrico. Para lo cual se utilizó la biblioteca cryptography.fernet de Python. A través de Fernet se garantiza que la información encriptada no se pueda leer ni manipular sin la clave.

### BLOCKCHAIN
Se implemento este sistema de seguridad, por su alta seguridad (siendo casi inquebrantable), para este sistema no se utilizo ninguna librería.

## **DESCRIPCIÓN DE MÉTODOS**
#### **createDatabase**
~~~
createDatabase(database: str, mode: str, encoding: str) -> int
~~~
>**DESCRIPCIÓN**
Crea una nueva base de datos, y guarda sus tablas dependiendo el modo de almacenamiento y de codificación que se escoja.
**PARÁMETROS**

| Parametro | Descripción | 
| --------- | ----------- |
| database (cadena) | Nombre que se le asignara a la base de datos al crearla |
| mode (cadena) | Indica el modo de almacenamiento (avl, b, bplus, dict, isam, json, hash).|
| encoding (cadena) | Indica el modo de codificación a utilizar (ascii, iso-8859-1, utf8). |
>**RETORNOS**

| Retorno | Descripción |
| ------- | ----------- |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos existente |
| 3 | Modo incorrecto |
| 4 | codificación incorrecta |
&nbsp;
#### **alterDatabaseMode**
~~~
alterDatabaseMode(database: str, mode: st) -> int
~~~
>**DESCRIPCIÓN**
Cambia el modo de almacenamiento de una base de datos.
**PARÁMETROS**

| Parametro | Descripción | 
| --------- | ----------- |
| database (cadena) | Nombre que se le asignara a la base de datos al crearla |
| mode (cadena) | Indica el modo de almacenamiento (avl, b, bplus, dict, isam, json, hash).
>**RETORNOS**

| Retorno | Descripción |
| ------- | ----------- |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos existente |
| 3 | Modo incorrecto |
&nbsp;
#### **alterTableMode**
~~~
alterTableMode(database: str, table: str, mode: str) -> int
~~~
>**DESCRIPCIÓN**
Cambia el modo de almacenamiento de una tabla especificada, en una base de datos especificada.
**PARÁMETROS**

| Parametro | Descripción | 
| --------- | ----------- |
| database (cadena) | Nombre de la base de datos que contiene la tabla. |
| table (cadena) | Nombre de la tabla de la cual se cambiara el modo de almacenamiento. |
| mode (cadena) | Indica el modo de almacenamiento (avl, b, bplus, dict, isam, json, hash).
>**RETORNOS**

| Retorno | Descripción |
| ------- | ----------- |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos no existente |
| 3 | Tabla no existente | 
| 4 | Modo incorrecto | 
&nbsp;
#### **alterTableAddFK**
~~~
alterTableAddFK(database: str, table: str, indexName: str, columns: list, tableRef: str, columnsRef: list) -> int
~~~
>**DESCRIPCIÓN**
Agrega un índice de llave foránea, creando una estructura adicional con el modo indicado para la base de datos.
**PARÁMETROS**

| Parametro | Descripción | 
| --------- | ----------- |
| database (cadena) | Nombre de la base de datos a utilizar. |
| table (cadena) | Nombre de la tabla donde estan las llaves foráneas. |
| indexName (cadena) | Es el nombre único del índice manejado como metadato de la tabla para ubicarlo fácilmente. |
| columns (lista) | Conjunto de índices de columnas que forman parte de llave foránea, como mínimo debe ser una columna. |
| tableRef (cadena) | Nombre de la tabla que hace la referencia, donde están las llaves primarias. |
| columnsRef (lista) | Conjunto de índices de columnas que forman parte de la llave primaria, mínimo debe ser una columna. |
>**RETORNOS**

| Retorno | Descripción |
| ------- | ----------- |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos no existente |
| 3 | table o tableRef no existente |
| 4 | Cantidad no exacta entre columns y columnsRef |
| 5 | No se cumple la integridad referencial (es decir, algún valor de las llaves foráneas no existe en la tabla de referencia) |
&nbsp;
#### **alterTableDropFK**
~~~
alterTableDropFK(database: str, table: str, indexName: str) -> int
~~~
>**DESCRIPCIÓN**
Destruye el índice tanto como metadato de la tabla como la estructura adicional creada.
**PARÁMETROS**

| Parametro | Descripción | 
| --------- | ----------- |
| database (cadena) | Nombre de la base de datos a utilizar. |
| table (cadena) | Nombre de la tabla donde están las llaves foráneas. |
| indexName (cadena) | Es el nombre del índice manejado como metadato de la tabla para ubicarlo fácilmente. |
>**RETORNOS**

| Retorno | Descripción |
| ------- | ----------- |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos no existente |
| 3 | Tabla no existente | 
| 4 | Nombre de índice no existente |
&nbsp;
#### **alterTableAddUnique**
~~~
alterTableMode(database: str, table: str, indexName: str, columns: list, tableRef: str, columnsRef: list) -> int
~~~
>**DESCRIPCIÓN**
Agrega un índice único, creando una estructura adicional con el modo indicado para la base de datos.
**PARÁMETROS**

| Parametro | Descripción | 
| --------- | ----------- |
| database (cadena) | Es el nombre de la base de datos a utilizar. |
| table (cadena) | Es el nombre de la tabla donde están las llaves foráneas. |
| indexName (cadena) | Es el nombre único del índice manejado como metadato de la tabla para ubicarlo fácilmente. |
| columns (lista) | Es el conjunto de índices de columnas que forman parte de la llave foránea, mínimo debe ser una columna. |
| tableRef (cadena) | Es el nombre de la tabla que hace referencia, donde están las llaves primarias. |
| columnsRef (lista) | Es el conjunto de índices de columnas que forman parte de la llave primaria, mínimo debe ser una columna. |
>**RETORNOS**

| Retorno | Descripción |
| ------- | ----------- |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos no existente |
| 3 | table o tableRef no existente |
| 4 | Cantidad no exacta entre columns y columnsRef |
| 5 | No se cumple la integridad de unicidad (es decir, algún valor de las llaves está duplicado). |
&nbsp;
#### **alterTableDropUnique**
~~~
alterTableDropUnique(database: str, table: str, indexName: str) -> int
~~~
>**DESCRIPCIÓN**
Destruye el índice tanto como metadato de la tabla como la estructura adicional creada.
**PARÁMETROS**

| Parametro | Descripción | 
| --------- | ----------- |
| database (cadena) | Nombre de la base de datos a utilizar. |
| table (cadena) | Nombre de la tabla donde están las llaves foráneas. |
| indexName (cadena) | Nombre del índice manejado como metadato de la tabla para ubicarlo fácilmente. |
>**RETORNOS**

| Retorno | Descripción |
| ------- | ----------- |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos no existente |
| 3 | Tabla no existente | 
| 4 | Nombre de índice no existente | 
&nbsp;
#### **alterTableAddIndex**
~~~
alterTableAddIndex(database: str, table: str, indexName: str, columns: list, tableRef: str, columnsRef: list) -> int
~~~
>**DESCRIPCIÓN**
Agrega un índice, creando una estructura adicional con el modo indicado para la base de datos.
**PARÁMETROS**

| Parametro | Descripción | 
| --------- | ----------- |
| database (cadena) | Nombre de la base de datos a utilizar. |
| table (cadena) | Nombre de la tabla donde están las llaves foráneas. |
| indexName (cadena) | Nombre único del índice manejado como metadato de la tabla pra ubicarlo fácilmente. |
| columns (list) | Conjunto de índices de columnas que forman parte de la llave foránea, mínimo debe ser una columna. |
| tableRef (cadena) | Nombre de la tabla que hace hace referencia, donde están las llaves primarias. |
| columnsRef (lista) | Conjunto de índices de columnas que forman parte de la llave primaria, mínimo debe ser una columna. | 
>**RETORNOS**

| Retorno | Descripción |
| ------- | ----------- |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos no existente |
| 3 | table o tableRef no existente |
| 4 | Cantidad no exacta entre columns y columnsRef |
&nbsp;
#### **alterTableDropIndex**
~~~
alterTableDropIndex(database: str, table: str, indexName: str) -> int
~~~
>**DESCRIPCIÓN**
Destruye el índice tanto como metadato de la tabla como la estructura adicional creada.
**PARÁMETROS**

| Parametro | Descripción | 
| --------- | ----------- |
| database (cadena) | Nombre de la base de datos a utilizar. |
| table (cadena) | Nombre de la tabla donde están las llaves foráneas. |
>**RETORNOS**

| Retorno | Descripción |
| ------- | ----------- |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos no existente |
| 3 | Tabla no existente | 
| 4 | Nombre de índice no existente | 
&nbsp;
#### **alterDatabaseEncoding**
~~~
alterDatabaseEncoding(database: str, encoding: str) -> int
~~~
>**DESCRIPCIÓN**
Asocia una codificación a una base de datos por completo.
**PARÁMETROS**

| Parametro | Descripción | 
| --------- | ----------- |
| database (cadena) | Nombre de la base de datos a utilizar. |
| encoding (cadena) | Es la codificación a utilizar, está puede ser, 'ASCII', 'ISO-8859.1' o 'UTF8'. |
>**RETORNOS**

| Retorno | Descripción |
| ------- | ----------- |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos no existente |
| 3 | Nombre de la codificación no existente |
&nbsp;
#### **checksumDatabase**
~~~
checksumDatabase(database: str, mode: str) -> int
~~~
>**DESCRIPCIÓN**
Calcula el checksum para la base de datos indicada en el modo especificado.
**PARÁMETROS**

| Parametro | Descripción | 
| --------- | ----------- |
| database (cadena) | Nombre de la base de datos a utilizar. |
| mode (cadena) | Es el algoritmo de hash a utilizar, puede ser 'MD5' o 'SHA256' |
>**RETORNOS**

| Retorno | Descripción |
| ------- | ----------- |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos no existente |
| 3 | Nombre de modo no existente |
&nbsp;
#### **checksumTable**
~~~
checksumTable(database: str, table: str, mode: str) -> int
~~~
>**DESCRIPCIÓN**
Calcula el checksum para la tabla indicada en el modo especificado.
**PARÁMETROS**

| Parametro | Descripción | 
| --------- | ----------- |
| database (cadena) | Nombre de la base de datos a utilizar. |
| table (cadena) | Nombre de la tabla de la que se desea calcular el checksum. |
| mode | Es el algoritmo hash a utilizar, puede ser 'MD5' o 'SHA256'. |
>**RETORNOS**

| Retorno | Descripción |
| ------- | ----------- |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos no existente |
| 3 | Nombre de modo no existente |
&nbsp;
#### **alterDatabaseCompress**
~~~
alterDatabaseCompress(database: str, level: int) -> int
~~~
>**DESCRIPCIÓN**
Agrega compresión utilizando la biblioteca zlib de python y las funciones compress y descompress. Se debe agregar una columna de tipo varchar o text de cada tabla de la base de datos. De igual manera, al extraer la información se debe descomprimir.
**PARÁMETROS**

| Parametro | Descripción | 
| --------- | ----------- |
| database (cadena) | Nombre de la base de datos que se desea modificar. |
| level (entero) | Nivle de compresión definido por la función compress de la biblioteca zlib de Python. |
>**RETORNOS**

| Retorno | Descripción |
| ------- | ----------- |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos no existente |
| 3 | Nivel incorrecto |
&nbsp;
#### **alterDatabaseDecompress(database: str)**
~~~
alterDatabaseDecompress(database: str) -> int
~~~
>**DESCRIPCIÓN**
Quita la compresión de una base de datos especificada.
**PARÁMETROS**

| Parametro | Descripción | 
| --------- | ----------- |
| database (cadena) | Nombre de la base de datos a utilizar. |
>**RETORNOS**

| Retorno | Descripción |
| ------- | ----------- |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos no existente |
| 3 | No había compresión |
&nbsp;
#### **alterTableCompress**
~~~
alterTableCompress(database: str, table: str, level: int) -> int
~~~
>**DESCRIPCIÓN**
Comprime una tabla.
**PARÁMETROS**

| Parametro | Descripción | 
| --------- | ----------- |
| database (cadena) | Nombre de la base de datos a utilizar. |
| table (cadena) | Nombre de la tabla a comprimir. |
| level (entero) | Nivel de compresión definido por la función compress de la biblioteca zlib de Python. |
>**RETORNOS**

| Retorno | Descripción |
| ------- | ----------- |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos no existente |
| 3 | Nivel incorrecto |
&nbsp;
#### **alterTableDecompress**
~~~
alterTableDecompress(database: int, table: int) -> int
~~~
>**DESCRIPCIÓN**
Quita la compresión de una tabla especificada.
**PARÁMETROS**

| Parametro | Descripción | 
| --------- | ----------- |
| database (cadena) | Nombre de la base de datos a utilizar. |
| table (cadena) | Nombre de la tabla a descomprimir. |
>**RETORNOS**

| Retorno | Descripción |
| ------- | ----------- |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos no existente |
| 3 | No había compresión |
&nbsp;
#### **encrypt**
~~~
encrypt(backup: str, password: str) -> int
~~~
>**DESCRIPCIÓN**
Encripta el texto backup con la llave password y devuelve el criptograma. 
**PARÁMETROS**

| Parametro | Descripción | 
| --------- | ----------- |
| backup (cadena) | Nombre de la base de datos a utilizar. |
| password (cadena) | Llave utilizada para comprimir la información. |
>**RETORNOS**

| Retorno | Descripción |
| ------- | ----------- |
| 0 | Operación exitosa |
| 1 | Error en la operación | 
&nbsp;
#### **decrypt**
~~~
decrypt(cipherBackup: cadena, password, cadena) -> int
~~~
>**DESCRIPCIÓN**
Desencripta el texto cipherBackup con la llave password y devuelve el texto plano.
**PARÁMETROS**

| Parametro | Descripción | 
| --------- | ----------- |
| cipherBackup | Texto que se desea desencriptar. |
| password (cadena) | Llave utilizada para comprimir la información. |
>**RETORNOS**

| Retorno | Descripción |
| ------- | ----------- |
| 0 | Operación exitosa |
| 1 | Error en la operación | 
&nbsp;
#### **safeModeOn**
~~~
safeModeOn(database:str, table: str) -> int
~~~
>**DESCRIPCIÓN**
Activa el modo seguro para una tabla de una base de datos, es decir activa el BlockChain para cada una de las tuplas pertenecientes a la tabla.
**PARÁMETROS**

| Parametro | Descripción | 
| --------- | ----------- |
| database (cadena) | Nombre de la base de datos a utilizar. |
| table (cadena) | Nombre la tabla de la cual se activará el modo seguro. |
>**RETORNOS**

| Retorno | Descripción |
| ------- | ----------- |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |
| 4 | Modo seguro ya activado |
&nbsp;
#### **safeModeOff**
~~~
safeModeOff(database: str, table: str) -> int
~~~
>**DESCRIPCIÓN**
Desactiva el modo seguro de la tabla especificada, es decir desactiva el BlockChain y borra el arhcivo JSON generado.
**PARÁMETROS**

| Parametro | Descripción | 
| --------- | ----------- |
| database (cadena) | Nombre de la base de datos a utilizar. |
| table (cadena) | Nombre de la tabla de la cual se desactivará el modo seguro. |
>**RETORNOS**

| Retorno | Descripción |
| ------- | ----------- |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Talba inexistente |
| 4 | Modo seguro no existente |
&nbsp;
#### **graphDSD**
~~~
graphDSD(database: str) -> str
~~~
>**DESCRIPCIÓN**
Genera un grafo mediante Graphviz acerca de la base de datos especificada.
**PARÁMETROS**

| Parametro | Descripción | 
| --------- | ----------- |
| database (cadena) | Nombre de la base de datos a graficar. |
>**RETORNOS**

| Retorno | Descripción |
| ------- | ----------- |
| Archivo formato Graphviz | Gráfica realizada con Graphviz |
| None | Retorno en caso de un error |
&nbsp;
#### **graphDF**
~~~
graphDF(database, table) -> str
~~~
>**DESCRIPCIÓN**
Genera un grafo mediante Graphviz acerca de las dependencias funcionales de una tabla especificada de una base de datos.
**PARÁMETROS**

| Parametro | Descripción | 
| --------- | ----------- |
| database (cadena) | Es el nombre de la base de datos a utilizar. |
| table (cadena) | Nombre de la Tabla a utilizar.
>**RETORNOS**

| Retorno | Descripción |
| ------- | ----------- |
| Archivo formato Graphviz | Gráfica realizada con Graphviz |
| None | Retorno en caso de un error |

## **PRINCIPALES MÉTODOS**

- Genera un archivo JSON de acuerdo al BlockChain aplicado a una tabla, este muestra las tuplas pertenecientes a la tabla y sus respectivas llaves.
~~~
def generateJsonSafeMode(self):
        try:
            data = {}
            data[self.name] = []
            for node in self.listNodes:
                data[self.name].append(
                    {
                        "PreviousKey": node.getPreviousKey(),
                        "Tuple" : node.getValue(),
                        "NextKey": node.getNextKey()
                    }
                )
            with open('BlockChain\\'+str(self.name)+'.json', 'w') as file:
                Json.dump(data, file, indent=4)
        except Exception as e:
            print("Error al generar JSON")
            print(e)
~~~
- Agrega un nodo a la cadena de bloques (BlockChain), este método se ejecuta cuando se realiza una inserción a la tabla con el modo seguro activado y la inserción no es autorizada.
~~~
    def addNodeNoSecure(self, value):
        if len(self.listNodes) == 0:
            node = Node(None, value)
            self.listNodes.append(node)
        else:
            if len(self.listNodes) > 1:
                previousNode = self.listNodes[len(self.listNodes) - 1]
            else:
                previousNode = self.listNodes[0]
            node = Node(previousNode.generateKey(value), value)
            self.listNodes.append(node)
~~~
- Genera una llave que será asignada a un nodo perteneciente a un nodo de la cadena de bloques (BlockChain).
~~~
    def generateKey(self, value):
        chars = ''.join(random.sample(string.ascii_letters, 15))
        return chars + str(len(value)) + str(time.strftime("%j")) + str(random.choice(string.ascii_letters)) + str(random.randint(0, 100)) + time.strftime("%M") + time.strftime("%S") + str(value[0])
~~~
