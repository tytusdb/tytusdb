from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.TablaSimbolos.Simbolo import Simbolo
from Instrucciones.TablaSimbolos.Nodo3D import Nodo3D
from Instrucciones.TablaSimbolos.Tabla import Tabla
from Instrucciones.Excepcion import Excepcion

class DropProc(Instruccion):
    def __init__(self, id, parametros, if_exists, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.id = id
        self.parametros = parametros
        self.if_exists = if_exists

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        pass

    def analizar(self, tabla, arbol):
        super().analizar(tabla,arbol)
        existe = tabla.getSimboloFuncion(self.id)
        if existe != None:
            if self.parametros == None:
                if existe.funcion.activa:
                    existe.funcion.activa = False
                    return
                else:
                    error = Excepcion("42723", "Semantico", f"El procedimiento almacenado: {self.id} no existe.", self.linea, self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            else:
                listaArgumentos = []
                for i in self.parametros:
                    listaArgumentos.append(i.tipo)

                listaParametros = []
                for i in existe.funcion.parametros:
                    listaParametros.append(i.tipo.tipo)

                if (listaParametros == listaArgumentos):
                    if existe.funcion.activa:
                        existe.funcion.activa = False
                        return
                    else:
                        error = Excepcion("42723", "Semantico", f"El procedimiento almacenado: {self.id} no existe.", self.linea, self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                else:
                    error = Excepcion("42723", "Semantico", f"El procedimiento almacenado: {self.id} no existe. Los tipos de parámetros no coinciden.", self.linea, self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
        else:
            if self.if_exists == None:
                error = Excepcion("42723", "Semantico", f"La función: {self.id} no existe.", self.linea, self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
            self.ignora = True

    def traducir(self, tabla, arbol):
        super().traducir(tabla,arbol)
        if not self.ignora:
            arbol.addComen(f"Se elimina el procedimiento almacenado -> {self.id}")
            arbol.addc3d(f"del globals()[\"{self.id}\"]")
            arbol.addc3d(f"print(\"El procedimiento almacenado: {self.id} ha sido eliminado con éxito\")")