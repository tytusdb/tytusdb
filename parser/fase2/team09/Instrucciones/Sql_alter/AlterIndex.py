from Instrucciones.Excepcion import Excepcion
from Instrucciones.Sql_create.Campo import Campo
from Instrucciones.Sql_create.CreateIndex import Cons
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Undefined.Empty import Empty

class AlterIndex(Instruccion):
    def __init__(self, existe, nombre, vcolum, ncolum, strGram, linea, columna):
        Instruccion.__init__(self, None, linea, columna, strGram)
        self.nombre = nombre
        self.existe = existe
        self.vcolum = vcolum
        self.ncolum = ncolum
        
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)
        encontrado = False
        ntabla = None
        for db in arbol.listaBd:
            for t in db.tablas:
                for i in range(len(t.lista_de_campos)):
                    c = t.lista_de_campos[i]
                    if c.tipo.toString() == "index":
                        if c.nombre == self.nombre:
                            encontrado = True
                            ntabla = t.nombreDeTabla
                            break
                if not encontrado and self.existe:
                    error = Excepcion('INX03', "Semántico", "No existe un índice llamado «" + self.nombre + "»", self.linea, self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append("\n" + error.toString())
                    err = True
                    return
                elif not encontrado:
                    arbol.consola.append("\nNo se ha encontrado el índice «" + self.nombre + "».")
                    return
                else:
                    indice = t.lista_de_campos[i]
                    try:
                        int(self.ncolum)
                        self.obtenerCampo(self.ncolum, ntabla, db.tablas)
                        if isinstance(self.ncolum, Excepcion):
                            arbol.excepciones.append(self.ncolum)
                            arbol.consola.append("\n" + self.ncolum.toString())
                            return
                    except:
                        ncolum = self.ncolum
                        self.ncolum = None
                        for c in t.lista_de_campos:
                            if c.nombre == ncolum:
                                self.ncolum = c
                                break
                        if self.ncolum is None:
                            error = Excepcion("INX01", "Semántico", "No existe el campo «" + ncolum + "» en la tabla «" + ntabla + "»", self.linea, self.columna)
                            arbol.excepciones.append(error)
                            arbol.consola.append("\n" + error.toString())
                            return
                    vacio = Empty(None, None, None, None, None)
                    self.ncolum = Campo(self.ncolum.nombre, False, vacio, vacio, "", 0, 0)
                    for j in range(len(indice.campos)):
                        if indice.campos[j].nombre == self.vcolum:
                            self.ncolum.restricciones = indice.campos[j].restricciones
                            indice.campos[j] = self.ncolum
                            break
                    restricciones = ""
                    for l in indice.campos:
                        restricciones = restricciones + " " + l.nombre + l.restricciones
                    nCons = None
                    if len(indice.constraint) == 1:
                        nCons = Cons(restricciones, "campo(s)")
                    else:
                        nCons = Cons(restricciones, "<br>campos(s)")
                    indice.constraint[len(indice.constraint) - 1] = nCons
                    arbol.consola.append("\nSe ha modificado el índice «" + self.nombre + "» correctamente.")
                    return

    def obtenerCampo(self, indice, ntabla, lista):
        actual = 0
        for tabla in lista:
            if tabla.nombreDeTabla == ntabla:
                for atributo in tabla.lista_de_campos:
                    if atributo.tipo.toString() != "index":
                        actual = actual + 1
                        if actual == indice:
                            self.ncolum = atributo
                            return
                self.ncolum = Excepcion("INX04", "Semántico", "El número de columna «" + str(indice) + "» no se encuentra en el rango de campos de la tabla «" + ntabla + "».", self.linea, self.columna)
                return
