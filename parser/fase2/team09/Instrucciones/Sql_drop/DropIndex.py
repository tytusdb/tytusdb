from Instrucciones.Excepcion import Excepcion
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class DropIndex(Instruccion):
    def __init__(self, existe, nombre, strGram, linea, columna):
        Instruccion.__init__(self, None, linea, columna, strGram)
        self.nombre = nombre
        self.existe = existe
        
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)
        encontrado = False
        for db in arbol.listaBd:
            for t in db.tablas:
                for i in range(len(t.lista_de_campos)):
                    c = t.lista_de_campos[i]
                    if c.tipo.toString() == "index":
                        if c.nombre == self.nombre:
                            encontrado = True
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
                    t.lista_de_campos.pop(i)
                    arbol.consola.append("\nSe ha eliminado el índice «" + self.nombre + "» correctamente.")
                    return

    def traducir(self, tabla, controlador, arbol):
        codigo = 'DropIndex.DropIndex(' + str(self.existe) + ',"' + self.nombre + '", "'
        codigo += self.strGram + '", ' + str(self.linea) + ', ' + str(self.columna) + ').ejecutar(tabla, arbol)\n'
        #print(codigo)
        return None
