# TytusDb
TytusDb es un software para administracion de base de datos
, divido en partes en este manual se explicaran las funciones, 
estrategias y metodos para poder realizar la parte que corresponde 
(Administrador de almacenamiento).

La parte a desarrollar es la de Administrador de almacenamiento
por medio de estructura de datos, la estructura de dato con el que
se trabajo fue el Arbol AVL esta implemenatodo en el lenguaje de 
programacion Python. Esta parte de software administrara la base 
datos, tablas y tuplas, cada una de las antes mencionadas son 
administradas por un arbol avl, 

#Arbol Avl
los árboles AVL estan simpre equilibrados de tal modo que para todos
los nodos, la altura de la rama izquierda no difiere en más de una
unidad de la altura de la rama derecha o viceversa. Gracias a esta 
forma de equilibrio, la complejidad O(log n). El factor de equilibrio
puede ser almacenado directamente en cada nodo os ser computado a
partir de las alturas de lso subárboles.


![](https://runestone.academy/runestone/static/pythoned/_images/simpleunbalanced.png)

#Metodos Adicionales
El metodo commit nos ayudara a la creacion de archivo .bin que almacenara lo que se 
encuentra en memoria, el archivo .bin esta creado desde un inicio antes de que se ejecurte
el programa por primera vez, asi solo sobreescribimos el metodo con la nueva instruccion
que se ejecute, almacenara el objeto que hallamos creado para luego cargarlo y asi no
perder los datos introducidos, el metodo recibe como parametros objeto que es el objeto 
que deseamos guardar y nombre de tipo string que sera el nombre con que se guardara el 
archivo .bin en nuestro caso solo lo sobreescribimos.

```
def commit(objeto, nombre):
    file = open(nombre + ".bin", "wb+")
    file.write(pickle.dumps(objeto))
    file.close()
```

Metodo rollback no ayuda a volve a cargar todo los datos ejecutados al objeto.

```
def rollback(nombre):
    file = open(nombre + ".bin", "rb")
    b = file.read()
    file.close()
    return pickle.loads(b)
```


#Programacion del Arbol AVL
La programación de Arbol AVL esta contenida en un solo archivo llamado: ArbolAVL.py
junto a todas las funciones para el ingreso de base de datos, tablas y tuplas. Las 
funciones como métodos son recursivos.


##Clase Nodo
Contiene una clase Nodo que contiene atributos como valor que ayuda a la busqueda,
contiene 3 atributos que ayudan a el manejo del arbol que son izq, der y padre, 
por ultimo se tienen dos atributos que contendran el resto informacion.

```
class Nodo:
    def __init__(self, valor, dic):
        self.valor = valor
        self.campos = dic
        self.izq = self.der = None
        self.padre = None
        self.altura = 1
        self.lista = None
```

##Clase ArbolAVL:
La clase ArbolAVL contiene dos atributos llamados raiz y contador. La raiz contendra
por lo general el primer elemento introducido para poder luego realizar una busqueda
y el atributo contador que nos ayuda a contar los elementos introducidos al arbol AVL

```
    def __init__(self):
        self.raiz = None
        self.contador = 1
```

El primer método es agregar este ingresa un nuevo nodo al árbol, esta compuesto por
dos métodos el principal que solo tomara el valor del nuevo nodo y una lista, el segundo que 
se le enviara los elementos necesario para su agregación. El primer método tiene 
una sentencia if si el árbol esta vacío solo se crea el nuevo nodo si esto no se 
cumple llamara el segundo metodo que enviara el valor del nuevo nodo como la raiz.
En el segundo metodo ingresa el nodo segun las reglas del Arbol AVL.


```
    def agregar(self, valor, dic):
        valor = str(valor)
        if self.raiz == None:
            self.raiz = Nodo(valor, dic)
            self.contador += 1
        else:
            self._agregar(valor, self.raiz, dic)

    def _agregar(self, valor, tmp, dic):
        valor = str(valor)
        if valor < tmp.valor:
            if tmp.izq == None:
                tmp.izq = Nodo(valor, dic)
                self.contador += 1
                tmp.izq.padre = tmp
                self.confirmaAgre(tmp.izq)
                return 1
            else:
                self._agregar(valor, tmp.izq, dic)
        else:
            if tmp.der == None:
                tmp.der = Nodo(valor, dic)
                self.contador += 1
                tmp.der.padre = tmp
                self.confirmaAgre(tmp.der)
                return 1
            else:
                self._agregar(valor, tmp.der, dic)
```

Contiene el método buscar, que buscar el nodo con el valor que se ingrese, esta
formado por dos metodos el primero delvolvera None si el arbol esta vacio, si no
ingresa al segundo metodo, por la forma que el arbol AVL esta estructurado facilita
la busque da un nodo.

    def buscar(self, valor):
        if self.raiz != None:
            return self._buscar(valor, self.raiz)
        else:
            return None

    def _buscar(self, valor, tmp):
        valor = str(valor)
        if valor == tmp.valor:
            return tmp
        elif valor < tmp.valor and tmp.izq != None:
            return self._buscar(valor, tmp.izq)
        elif valor > tmp.valor and tmp.der != None:
            return self._buscar(valor, tmp.der)

Método eliminar hace uso del metodo buscar esta construido de dos metodos el primero
que convertimos el valor introducido por el usuario a string para luego con ayuda del
método buscar encontremos el nodo a eliminar 

    def eliminar(self, valor):
        valor = str(valor)
        return self._eliminar(self.buscar(valor))

El submetodo de eliminar tiene una condición si el método de buscar devuelve None este submetodo tambien devuelve None de lo contrario, se
buscara el nodo a reemplazar se utilizara el nodo de la derecha mas a la izquierda y este proceso lo hace el submetodo
minimValor tenemos otro submetodo numHijos que nos ayudara a contar cuantos hijos las ramas del nodo , se hace uso de variables auxiliares
para obtener el nodo padre y su numero de hijos en base a los nodos hijos se tomara la decision por la cual se 
sustituira el nodo a eliminar, si el nodo a eliminar sus hijos son None estamos en un nodo hoja a eliminar en este caso
solo se obtiene el nodoPadre y se elimina el nodo hijo, si el nodo a eliminar sus nodo hijos es 1 se debe de verificar
si su hijo izquierdo existe por el cual se sustituira de lo contrario se tomara su hijo derecho para su sustitucion
y el caso en el que tenga dos hijos en sus ramas se procede a tomar el nodo de la derecha mas a la izquierda para su 
sustitución, luego de la sustitucion se actualiza la altura de los nodos, por ultimo se hace las rotaciones si son 
necesarias con el método validaEliminacion que recibe como parametro el nodo padre

    def _eliminar(self, tmp):

        if tmp == None or self.buscar(tmp.valor) == None:
            print("No se encuentra el valor")
            return None

        def minimValor(tmp):
            actual = tmp
            while actual.izq != None:
                actual = actual.izq
            return actual

        def numHijos(tmp):
            numHijos = 0
            if tmp.izq != None:
                numHijos += 1
            if tmp.der != None:
                numHijos += 1
            return numHijos

        nodoPadre = tmp.padre

        nodoHijo = numHijos(tmp)

        if nodoHijo == 0:

            if nodoPadre != None:
                if nodoPadre.izq == tmp:
                    nodoPadre.izq = None
                else:
                    nodoPadre.der = None
            else:
                self.raiz = None

        if nodoHijo == 1:

            if tmp.izq != None:
                hijo = tmp.izq
            else:
                hijo = tmp.der

            if nodoPadre != None:
                if nodoPadre.izq == tmp:
                    nodoPadre.izq = hijo
                else:
                    nodoPadre.der = hijo
            else:
                self.raiz = hijo

            # correct the padre pointer in node
            hijo.padre = nodoPadre

        if nodoHijo == 2:
            siguiente = minimValor(tmp.der)

            tmp.valor = siguiente.valor

            self._eliminar(siguiente)

            return

        if nodoPadre != None:
            nodoPadre.altura = 1 + max(self.altura(nodoPadre.izq), self.altura(nodoPadre.der))
            self.validaEliminacion(nodoPadre)

Método graficar este metodo recorre el arbol AVL y tomando sus valores para poder colocar el
nodo en una imagen, recorriendo todo el arbol y tomando sus valores para despues poder 
mostrarlos en una imagen y poder visualizar el arbol de un mejor manera, para esto se 
utilizo la libreria graphviz el usuario podra graficar las tuplas para una mejor administracion de los datos.

    def graficar(self):
        contenido = "digraph grafica{\n    rankdir=TB;\n    node [shape = record, style=filled, fillcolor=lightcyan2];\n    "
        contenido += self._graficar(self.raiz)
        contenido += "}"

        if contenido != "":
            tabGen = open("tab.dot","w")
            tabGen.write(contenido)
            tabGen.close()
            tab = open("tab.cmd","w")
            tab.write("dot -Tpng tab.dot -o tab.png")
            tab.close()
            subprocess.call("dot -Tpng tab.dot -o tab.png")
            os.system('tab.png')

    def _graficar(self, tmp):
        contenido = ""
        if tmp.izq == None and tmp.der == None:
            contenido = "nodo" + str(tmp.valor) + " [ label =\"" + str(tmp.valor) + "\"];\n    ";
        else:
            contenido = "nodo" + str(tmp.valor) + " [ label =\"<AI>|" + str(tmp.valor) + "|<AD>\"];\n    ";
        if tmp.izq != None:
            contenido += self._graficar(tmp.izq) + "nodo" + str(tmp.valor) + ":AI->nodo" + str(
                tmp.izq.valor) + "\n    ";

        if tmp.der != None:
            contenido += self._graficar(tmp.der) + "nodo" + str(tmp.valor) + ":AD->nodo" + str(tmp.der.valor) + "\n    "

        return contenido

# Librerias Utilizadas

##Pickle
Se utilizo a utilizado para la lectura y escritura de archivos binarios este almacenara el objeto
creado que estan en memoria, se utiliza tambien para la lectura de archivos .bin no ayudara a 
volver a cargar los datos que hayamos creado, modificado o eliminado.

##CSV
Se ha utilizado para la lectura de archivos csv.

##Tkinter
Libreria dirigido al usuario con la creacion de una interfaz grafica que ayudara al usuario final facilitando el uso 
del programa, mostrando botones, cajas de texto e imagenes para una mejor visualizacio  y manejo de los datos, ayudara
al ingreso, modificaciones y eliminaciones de datos.



# Funciones

Para almacenar las base de datos utilizaremos una arbol AVL y para agregar una nueva base de datos utilizaremos
la funcion createDatabase(database).Recibe un parametro con el nombre de tipo string que es nombre de la base de datos, 
esta funcion lo que hace es introducir un nodo creando el arbol si es el 
primero en ingresar de lo contrario solo lo busca el lugar adecuado para colocarlo. Tiene un valor de retorno 
dependiendo del estado que se ingreso: 
0. Operación exitosa
1. Error en la operación
2. base de datos existente
 ```
    def createDatabase(self, valor):
        valor = str(valor)
        nodo = self.buscar(valor)
        if nodo is None:
            try:
                self.agregar(str(valor), None)
                return 0
            except:
                return 1

        else:
            return 2
 ```

Funcion showDatabases() esta función muesta los nombres de base de datos en forma de preorden retornando una lista, 
cuando el arbol se encuentra vacío devuelve una lista vacía, se hace uso de la funcion generalista que es la forma
de recorrido preorden.

    def showDatabases(self):
        lista = []
        list = self.generarlista(self.raiz, lista)
        print()
        print("Lista de elementos en arbol")
        print(list)
        return list

Funcion alterDatabase(old, nuevo) recibe dos parametros old que es la base de datos a modificar y nuevo que el valor con
el que se va a reemplazar, se utilizarn dos variables auxiliares llamadas vieja y nueva, la vieja utiliza el metodo
buscar para verificar que la base de datos a reemplazar exitas y de igual maner se hace una busqueda de valor a 
reemplazar para verificar que no se repita esta base de datos, se utiliza una condicion para verificar estas valores
para luego solo reemplazar su nombre. La funcion tiene valores de retorno dependiendo su estado:
0. Operación exitosa
1. Error en la operación
2. Old no existente
3. nuevo existente

 ```
   def alterDatabase(self, old, nuevo):
        old = str(old)
        nuevo = str(nuevo)
        vieja = self.buscar(old)
        nueva = self.buscar(nuevo)
        if vieja != None:
            if nueva is None:
                vieja.valor = nuevo
                self.validaEliminacion(vieja)
                #__________________________________________
                return 1
            else:
                return 3
        else:
            return 2
```

Funcion dropDatabase(database) recibe como parametro el nombre de una base de datos, la funcion elimina la base de datos junto a su tablas
(si las contiene), se utiliza la variable db para buscar el nodo y almacenarlo con una condición se verifica si es None no realiza ninguna
accion de lo contrario se utiliza el metodo de la clase ArbolAVL para la eliminacion del nodo este hace sus rotaciones si son necesarias
tiene un volor de retorno dependiendo de su operacion:
0. Operación exitosa
1. Error en la operación
2. base de datos no existente


 ```
    def dropDatabase(self, db):
        db = str(db)
        base = self.buscar(db)
        if base is None:
            return 2
        else:
            self.eliminar(db)
            i = self.buscar(db)
            if i is None:
                return 0
            else:
                return 1
```

Funcion createTable(database, table, numberColums) recibe tres parametros database de tipo string que sera la base de dato que 
contendra la tabla, tabla de tipo string que sera el nombre de la tabla y numbercolums de tipo int que seran las columans que se le
asignaran a la tabla. Para el almacenamiento de las tablas se utiliza un arbol AVL cada nodo almacenara las tablas que se le asignes 
a la base de datos, el nodo base de datos que contendra las tablas tiene una variable que hara referencia la Arbol de tablas.
Se utiliza una variable auxiliar que contendra el nodo de la base de datos, si la varible que contien el arbol de las tablas se 
encuentra vacio solo se crea el arbol AVL de lo contrario solo se agrega utilizando el método de la clase ArbolAVL. Tiene un valor de 
retorno dependiendo de su operacion:
0. Operación exitosa
1. Error en la operación
2. base de datos inexistente
3. tabla existente

 ```
    def createTable(self, db, tabla, dic):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        i = self.buscartabla(db, tabla)

        if i is None:
            if raiz != None:
                if raiz.lista is None:
                    try:
                        raiz.lista = ArbolAVL()
                        lista = [None, dic, raiz.lista.contador]
                        raiz.lista.agregar(tabla, lista)
                        return 1
                    except:
                        return 0
                else:
                    try:
                        lista=[None, dic, raiz.lista.contador]
                        raiz.lista.agregar(tabla, lista)
                        print("Base de datos: ", raiz.valor)
                        raiz.lista.preorden()
                        return 1
                    except:
                        return 0
            else:
                print("no existe la base de datos: ", db)
                return 2
        else:
            return 3
 ```

Funcion showTables(database) recibe como parametro databese de tipo string que es el nombre de la base de datos a buscar, 
se utilza una variable auxiliar para verificar si existe, devuelve una lista de las tablas que se encuentran en la base de datos
se realiza un recorrido en preorden si no existe tablas solo devuelve una lista vacía.

 ```
 def showTables(self, db):
        db = str(db)
        raiz = self.buscar(db)
        if raiz != None:
            lista = []
            if raiz.lista != None:
                list = raiz.lista.generarlista(raiz.lista.raiz, lista)
                print(list)
                return list
        else:
            return None
 ```

Funcion extractTable(db, tabla) ambos parametros recibidos son string utilizamos variables auxiliares para verificar si existen 
la base de datos como la tabla hace un recoorido en preorden a los datos y los agrega a una lista para luego devolver esa lista si
la lista no contiene datos devuelve una lista vacia.

    def extractTable(self, db, tabla):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i.lista != None:
                lista = []
                li = self.generarregistros(i.lista.raiz ,lista,0,0,0)
                print(li)
                return li
        else:
            return None

Funcion extractRangeTable(db, tabla, max , min ,col) recibe 5 parametros db de tipo string que es la base de datos, tabla de
tipo string es el nombre de la tabla, max de cualquier tipo , min de cualquier tipo y col es la referencia a la comluman que se 
encuentras los datos a buscar dentro del rango. Devolvera una lista con los datos que se encuente dentro de los rango hara un recorrido
en preorden añadiendolos a una lista cada vez que encuentre dentro del rango.

    def extractRangeTable(self, db, tabla, max, min,col):
        db = str(db)
        tabla = str(tabla)
        min = str(min)
        max = str(max)
        raiz = self.buscar(db)
        if raiz.lista != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                lista = []
                li = self.generarregistros(i.lista.raiz, lista, max, min,col)
                print(li)
                return li
        else:
            return None

Funcion alterAddPK(db, tabla, columnas) recibe tres parametros db de tipo string sera el nombre de la base de datos , tabal de tipo string que es el
nombre de la tabla y columnas de tipo lista contiene las columnas que queremos que sean las llaves primarias, se utilizan variables auxiliaras 
para verificar su existencia, se toman algunas consideraciones como si la tabla tiene datos repetidos esta no se podra asignar, como verificar que 
la columan que se convertira en llave primaria exista y no se encuentre fuera de rango,tiene un valor de retorno dependiendo de su operacion.
0. Operación exitosa
1. Error en la operación
2. base de datos no existe
3. tabla no existente
4. llave primaria existente
5. columan fuera de rango


 ```
    def alterAddPK(self, db, tabla, columnas):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                if i.campos[0] != None:
                    return 4
                else:
                    try:
                        if i.lista is None:
                            i.campos[0] = columnas
                        else:
                            t2 = i.lista
                            if t2.contadorRep(columnas):
                                i.campos[0] = columnas
                                print("funciono")
                                i.lista.cambiardatos(i.lista.raiz, i.campos[0])
                                i.lista.validaEliminacion(i.lista.raiz)
                                i.lista.preorden()
                            else:
                                print("llaves repetidas")
                        return 0
                    except:
                        return 1
            else:
                return 3
        else:
            return 2
 ```

Función alterDropPK(database, table) recibe como parametro dos varibales de tipl string, la base de datos y la tabla, la 
funcion es una eliminacino de llaves primarias manteniendo la estructura del arbol. Se utilizan varibales locales para 
validar su existencia, retorna un numero dependieno su operacion:
0. Operación exitosa
1. Error en la operación
2. base de datos no existe
3. tabla no existente
4. llave primaria no existente


 ```
    def alterDropPK(self, db, tabla):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                if i.campos[0] != None:
                    try:
                        i.campos[0]=None
                        return 0
                    except:
                        return 1
                else:
                    return 4
            else:
                return 3
        else:
            return 2
 ```

Función alterTable(database, tableOld, tableNew) recibe tres parametros de tipo string, el nombre de la base de datos,
el nombre de la base de datos a cambiar y el nombre de la tabla que reemplazara, el metodo hace combio de nombre a tabla
haciendo verificaciones como validar que exista la base de datos, que la tabla exista y que el nombre a reemplazar no exista
en la base de datos, devuelve un numero dependieno de su operacion:
0. Operación exitosa
1. Error en la operación
2. base de datos no existe
3. tabla no existente
4. tabla existente 

 ```
    def alterTable(self, db, tabla, tablanueva):
        tabla = str(tabla)
        db = str(db)
        tablanueva=str(tablanueva)
        raiz = self.buscar(db)
        if raiz != None:
            f = self.buscartabla(db, tablanueva)
            if f is None:
                i = self.buscartabla(db, tabla)
                if i !=None:
                    try:
                        i.valor = tablanueva
                        self.validaEliminacion(i)
                        return 0
                    except:
                        return 1
                else:
                    return 3
            else:
                return 4
        else:
            return 2
 ```

Funcion alterAddColumn(database, table, default) esta funcion agrega una nueva columna al final del registro, la funcion
recibe 2 pametros de tipo string database y table y una mas que puede ser de cualquier tipo que es indice de la nueva columna
se verifica la existencia de la base de datos como la de la tabla returan un numero dependiendo de su operacion:
0. Operación exitosa
1. Error en la operación
2. base de datos no existe
3. tabla no existente

 ```
  def alterAddColumn(self, db, tabla, valor):
        db = str(db)
        tabla = str(tabla)
        valor = str(valor)
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                try:
                    i.campos[1]=i.campos[1]+1
                    self.agregarcolumna(i.lista.raiz, valor)
                    return 0
                except:
                    return 1
            else:
                return 3
        else:
            return 2
 ```

Funcion alterDropColumn(database, table, columnNumber) elimina una n-ésima columna de cada registro de la tabla excepto si
son llaves primarias, se verifica su existencia de la base de datos y la tabla y la columan que se quiere eliminar la 
llave primaria devuelve un numero segun la operacion que realizo:
0. Operación exitosa
1. Error en la operación
2. base de datos no existe
3. tabla no existente
4. llave no puede eliminarse o tabla queda sin columanas
5. columna fuera de limite

 ```
     def alterDropColumn(self, db, tabla, Nocol):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        if raiz !=None:
            i = self.buscartabla(db, tabla)
            if i != None:
                if i.campos[1] < Nocol:
                    return 5
                else:
                    for f in i.campos[0]:
                        if f == Nocol:
                            return 4
                try:
                    self.eliminarcolumna(i.lista.raiz, Nocol)
                    return 0
                except:
                    return 1
            else:
                return 3
        else:
            return 2
  ```


Funcion  alterDropPK(database, table) reciben dos parametros de tipo string, una para la base de datos y otra para la tabla
se utilizan variables auxiliares para validar su existencia, al encontrar la tabla se utiliza el metodo de eliminar que es 
de la clase ArbolAVL y este a su vez realiza las rotaciones necesarias para su equilibrio.

 ```
    def dropTable(self, db, tabla):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        if raiz != None:
            if raiz.lista is None:
                return 3
            else:
                try:
                    raiz.lista.eliminar(tabla)
                    print("Base de datos", raiz.valor)
                    raiz.lista.preorden()
                    return 0
                except:
                    return 1

        else:
            return 2
 ```

Funcion insert(database, table, register) recibe como parametro 2 variables tipo string database y talbe, 1 una varibale
de tipo lista, la funcion inserta registro a las tablas, los datos ingresado a la tabla se alamacenan en un árbol AVL
el nodo tabla contiene una variabale para hacer referencia a estos datos, con dos variables se almacen las referencias a
la base de datos y a la tabla que se ingresaran los datos, esto es para verificar su existencia se hace uso del metodo
guardar que es del la clase ArbolAVL, retorna un numero segun su operacion:
0. Operación exitosa
1. Error en la operación
2. base de datos no existe
3. tabla no existente
4. llave primaria duplicada
5. columna fuera de limite

 ```
     def insert(self, db, tabla, lista):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                try:
                    c = 0
                    c = int(i.campos[1])
                    if c != len(lista):
                        return 5
                    else:
                        lista2 = []
                        if i.campos[0] is None:
                            lista2 = None
                        else:
                            lista2 = i.campos[0]
                        r = self.agregarregistroatabla(db, tabla, lista, lista2)
                        if r == 4:
                            return 4
                        else:
                            return 0
                except:
                    return 1
            else:
                return 3
        else:
            return 2
 ```
  
Funcion loadCSV(file, database, table) recibe dos variables de tipo string database el nombre de la base de datos y table
nombre de la tabla a la que se le introduciran los datos y file que es la ruta del archivo csv, se hace verficación de que
exista la tabla como la base de datos devuelve una lista con los datos ingresados.

    def loadCSV(self, dirfile, database, table):
        l = []
        raiz = self.buscar(database)
        i = self.buscartabla(database, table)
        if raiz is not None:
            if i is not None:

                with open(dirfile) as f:
                    reader = csv.reader(f)
                    for row in reader:
                        row = [int(i) for i in row]  # Convierte la lista de string a int
                        if i.campos[1] == len(row):
                            con = self.insert(database, table, row)
                            if con == 4:
                                l.append(4)
                            else:
                                l.append(row)
                        else:
                            return 5

            else:
                return 3
        else:
            return 2
        return l

Funcion extractRow(database, table, columns) recibe como parametro dos string database y table que serna la base de datos y la tabla
a utilizar correspondientemente, una lista con los valores que queremos mostrar, por medio de los parametros se ira a buscara 
a la base de datos ingresada y la tabla, devuelve una lista con los coincidencias.

    def extractRow(self, db, tabla, columnas):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                lista = i.campos[0]
                try:
                    self.extraercolumna(i.lista.raiz, lista, columnas)
                    return 0
                except:
                    return 1
            else:
                return 3
        else:
            return 2

Funcion update(database, table, register, columns) actualiza un registro de una tabla, recibe como parametros la base de 
datos y la tabla de tipo string, una variabla register que es un diccionario que tiene el formato {llave:valor} y la 
variable columns de tipo lista que contendra las llavas primarias de la tabla, se verifica la existencia de la base de datos
como de la tabla y dependiendo de su operacion tiene un valor de retorno:
0. Operación exitosa
1. Error en la operación
2. base de datos no existe
3. tabla no existente
4. llave primaria no existe

 ```
    def extractRow(self, db, tabla, columnas):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                lista = i.campos[0]
                try:
                    self.extraercolumna(i.lista.raiz, lista, columnas)
                    return 0
                except:
                    return 1
            else:
                return 3
        else:
            return 2
 ```

Funcion delete(database, table, columns) elimina registro de la tabla, recibe como parametro database que es el nombre
de la base de datos y tabla que es el nombre de la tabla a eliminar los registro ambas variables de tipo string y una tercer
varibale de tipo column de tipo lista que contendra las llaves primarias de los registros a eliminar, la funcion tiene un valor
de retorno segun su operacion:
0. Operación exitosa
1. Error en la operación
2. base de datos no existe
3. tabla no existente
4. llave primaria no existe

 ```
     def deletet(self, db, tabla, columnas):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                lista = i.campos[0]
                try:
                    if lista is None:
                        i.lista.eliminar(columnas[0])
                        print("eliminado", columnas)
                        i.lista.preorden()
                    else:
                        cadena = ""
                        for i in columnas:
                            cadena += str(i) +","
                        cadena = cadena[0:len(cadena)-1]
                        print("eliminado", cadena)
                        eliminado=self.buscarreistro(db, tabla, cadena)
                        if eliminado != None:
                            i.lista.eliminar(eliminado.valor)
                        else:
                            return 4
                    return 0
                except:
                    return 1
            else:
                return 3
        else:
            return 2
 ```

Función truncate(database, table) eliminara todas los registro que contendra la tabla recibe como 
parametros la base de datos y el nombre de la tabla ambos de tipo string, se verifica su existencia
y devuleve un valor de retorno segun su operacion:
0. Operación exitosa
1. Error en la operación
2. base de datos no existe
3. tabla no existente

 ```
    def truncate(self, db, tabla):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                try:
                    i.lista = None
                    return 0
                except:
                    return 1
            else:
                return 3
        else:
            return 2
 ```

#Interfaz grafica
Para mayor facilidad de manejo de datos se a credo una interfaz grafica que ayudara al usuario al ingresar, 
modifica o eliminar solo presionando botones, cuando quiera visualizar los datos estos se mostran en un cuadro 
de texto con todos los elemento que tendra el nodo, se puede mostra base de datos, tablas o los datos que se 
han ingresado, los botones llamaran a las funciones(antes descritos) como creardatabase , showdatabse, 
createtable , etc.

