from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion
from storageManager.jsonMode import *

from Instrucciones.TablaSimbolos import Instruccion3D as c3d

class AlterTableDropConstraint(Instruccion):
    def __init__(self, tabla, col, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.tabla = tabla
        self.col = col

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if arbol.bdUsar != None:
            objetoTabla = arbol.devolviendoTablaDeBase(self.tabla)
            if objetoTabla != 0:
                existe = None
                constraintBorrar = None
                for columnas in objetoTabla.lista_de_campos:
                    if columnas.constraint != None:
                        for const in columnas.constraint:
                            if const.id == self.col:
                                existe = columnas
                                constraintBorrar = const
                if existe != None:
                    existe.constraint.remove(constraintBorrar)
                    arbol.consola.append("Consulta devuelta correctamente.")  
                else:
                    error = Excepcion('42P01',"Semántico","No existe la columna «"+self.col+"» en la llave",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            else:
                error = Excepcion('42P01',"Semántico","No existe la relación "+self.tabla,self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        else:
            error = Excepcion("100","Semantico","No ha seleccionado ninguna Base de Datos.",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())

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
        t2 = c3d.getTemporal()
        code.append(t2 + ' = "' + str(self.col) + '"')
        code.append('heap[h] = ' + t2)
        code.append('p = h')
        code.append('call_alterTable_dropConstraint()')
        
        return code

        '''
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
            error = Excepcion('2BP01',"Semántico","No se puede eliminar columna "+self.col+" de "+self.tabla+" prueba porque otros objetos dependen de él",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        elif resultado == 5:
            error = Excepcion('XX002',"Semántico","Columna fuera de limites."+self.tabla,self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        arbol.consola.append("Consulta devuelta correctamente.")
        '''