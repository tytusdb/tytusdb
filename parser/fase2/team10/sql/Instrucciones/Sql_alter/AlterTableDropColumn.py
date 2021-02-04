from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.Excepcion import Excepcion
import collections
from sql.storageManager.jsonMode import *

class AlterTableDropColumn(Instruccion):
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
                listaBorrar = []
                for c in self.lista_col:
                    for columnas in objetoTabla.lista_de_campos:
                        if columnas.nombre == c.id:
                            listaMatch.append(c)
                            listaBorrar.append(columnas)
                if len(listaMatch) == 0:
                    for c in self.lista_col:
                        error = Excepcion('42703',"Semántico","No existe la columna «"+c.id+"» en la relación «"+self.tabla+"»",c.linea,c.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                    return
                elif len(listaMatch) == len(self.lista_col):
                    # Existen columnas con el mismo nombre a insertar
                    nombres = []
                    for columnas in self.lista_col:
                        nombres.append(columnas.id)
                    duplicados = [item for item, count in collections.Counter(nombres).items() if count > 1]
                    for columnas in duplicados:
                        error = Excepcion('42701',"Semántico","Ya existe la columna «"+columnas+"» en la relación «"+self.tabla+"»",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                    if len(duplicados) != 0:
                        return
                    # Las columnas se eliminarán en memoria.
                    #print("Inicia-------------->",len(objetoTabla.lista_de_campos))
                    for c in listaBorrar:     
                        indice = arbol.devolverOrdenDeColumna(self.tabla, c.nombre)
                        resultado = alterDropColumn(arbol.getBaseDatos(),self.tabla,indice)
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
                            error = Excepcion('2BP01',"Semántico","No se puede eliminar columna "+c.nombre+" de "+self.tabla+" prueba porque otros objetos dependen de él",self.linea,self.columna)
                            arbol.excepciones.append(error)
                            arbol.consola.append(error.toString())
                            return error
                        elif resultado == 5:
                            error = Excepcion('XX002',"Semántico","Columna fuera de limites."+self.tabla,self.linea,self.columna)
                            arbol.excepciones.append(error)
                            arbol.consola.append(error.toString())
                            return error
                        # Las columnas se eliminarán en disco.
                        objetoTabla.lista_de_campos.remove(c)
                        #print("Termina-------------->",len(objetoTabla.lista_de_campos))
                        # Actualizar orden
                        for c in range(0,len(objetoTabla.lista_de_campos)):
                            objetoTabla.lista_de_campos[c].orden = c
                            arbol.devolverOrdenDeColumna(self.tabla, objetoTabla.lista_de_campos[c].nombre)
                            #print(objetoTabla.lista_de_campos[c].nombre,objetoTabla.lista_de_campos[c].orden,indice)
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

        '''
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
        '''