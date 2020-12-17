from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion
from storageManager.jsonMode import *

class AlterTableDropColumn(Instruccion):
    def __init__(self, tabla, lista_col, linea, columna):
        Instruccion.__init__(self,None,linea,columna)
        self.tabla = tabla
        self.lista_col = lista_col

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        for c in self.lista_col:
            resultado = 0
            #resultado = alterDropColumn(arbol.getBaseDatos(),self.tabla,c.id)
            if resultado == 1:
                error = Excepcion('XX000',"Semántico","Error interno",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
            elif resultado == 2:
                error = Excepcion('42P00',"Semántico","La base de datos "+str(arbol.getBaseDatos())+" no existe",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
            elif resultado == 3:
                error = Excepcion('42P01',"Semántico","No existe la relación "+self.tabla,self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
            elif resultado == 4:
                error = Excepcion('2BP01',"Semántico","No se puede eliminar columna "+c.id+" de "+self.tabla+" prueba porque otros objetos dependen de él",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
            elif resultado == 5:
                error = Excepcion('XX002',"Semántico","Columna fuera de limites."+self.tabla,self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        arbol.consola.append("Consulta devuelta correctamente.")