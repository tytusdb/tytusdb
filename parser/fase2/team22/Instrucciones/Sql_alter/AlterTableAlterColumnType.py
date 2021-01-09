from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion
import collections
#from storageManager.jsonMode import *
# Solo reconocerlo en la gramatica y modificarlo en tu table de tipos
from Optimizador.C3D import *
from Instrucciones.TablaSimbolos import Instruccion3D as c3d

class AlterTableAlterColumnType(Instruccion):
    def __init__(self, tabla, lista_col, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.tabla = tabla
        self.lista_col = lista_col

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if arbol.bdUsar != None:
            objetoTabla = arbol.devolviendoTablaDeBase(self.tabla)
            if objetoTabla != 0:
                listaMatch = []
                listaAlterar = []
                for c in self.lista_col:
                    for columnas in objetoTabla.lista_de_campos:
                        if columnas.nombre == c.id:
                            listaMatch.append(c)
                            listaAlterar.append(columnas)
                if len(listaMatch) == 0:
                    for c in self.lista_col:
                        error = Excepcion('42703',"Semántico","No existe la columna «"+c.id+"» en la relación «"+self.tabla+"»",c.linea,c.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                    return
                elif len(listaMatch) == len(self.lista_col):
                    # Existen columnas con el mismo nombre a alterar
                    nombres = []
                    for columnas in self.lista_col:
                        nombres.append(columnas.id)
                    duplicados = [item for item, count in collections.Counter(nombres).items() if count > 1]
                    for columnas in duplicados:
                        error = Excepcion('42701',"Semántico","No se puede alterar el tipo de la columna «"+columnas+"» dos veces",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                    if len(duplicados) != 0:
                        return
                    # Las columnas se alterarán en memoria.
                    for c in self.lista_col:
                        for columnas in listaAlterar:
                            if columnas.nombre == c.id:
                                columnas.tipo = c.tipo
                    arbol.consola.append("Consulta devuelta correctamente.")
                else:
                    for c in list(set(self.lista_col) - set(listaMatch)):
                        error = Excepcion('42703',"Semántico","No existe la columna «"+c.id+"» en la relación «"+self.tabla+"»",c.linea,c.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                    return
            else:
                error = Excepcion('42P01',"Semántico","No existe la relación "+self.tabla,self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        else:
            error = Excepcion("100","Semantico","No ha seleccionado ninguna Base de Datos.",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())

    def generar3D(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append(c3d.asignacionH())
        code.append(c3d.aumentarP())
        t0 = c3d.getTemporal()
        code.append(c3d.asignacionString(t0, "ALTER TABLE " + self.tabla))
        t1 = c3d.getTemporal()
        for col in self.lista_col:
            code.append(c3d.operacion(t1, Identificador(t0), Valor(" \" ALTER COLUMN " + col.id + " TYPE " + col.tipo.toString() + "\"", "STRING"), OP_ARITMETICO.SUMA))
            t0 = t1
            t1 = c3d.getTemporal()
            if col.tipo.dimension != None:
                code.append(c3d.operacion(t1, Identificador(t0), Valor("\"(" + str(col.tipo.dimension) + ")\"", "STRING"), OP_ARITMETICO.SUMA))
                t0 = t1
                t1 = c3d.getTemporal()

        code.append(c3d.operacion(t1, Identificador(t0), Valor("\";\"", "STRING"), OP_ARITMETICO.SUMA))
        code.append(c3d.asignacionTemporalStack(t1))
        code.append(c3d.LlamFuncion('call_funcion_intermedia'))

        return code

    def generar3DV2(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append('h = p')
        code.append('h = h + 1')
        t0 = c3d.getTemporal()
        bd = arbol.getBaseDatos()
        if bd != None and bd != "":
            code.append(t0 + ' = "' + bd + '"')
        else:
            code.append(t0 + ' = ' + str(None))
        code.append('heap[h] = ' + t0)
        code.append('h = h + 1')
        t1 = c3d.getTemporal()
        code.append(t1 + ' = "' + str(self.tabla) + '"')
        code.append('heap[h] = ' + t1)
        code.append('h = h + 1')
        if self.lista_col != None:
            code.append('heap[h] = []')
            for columna in self.lista_col:
                t2 = c3d.getTemporal()
                code.append(t2 + ' = ["' + str(columna) + '"]')
                code.append('heap[h] = heap[h] + ' + t2)
        else:
            code.append('heap[h] = None')
        code.append('p = h')
        code.append('call_alterTable_columnType()')
        
        return code