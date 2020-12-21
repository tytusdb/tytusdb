from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion
#from storageManager.jsonMode import *

class AlterTableAddConstraint(Instruccion):
    def __init__(self, tabla, id, lista_col, linea, columna):
        Instruccion.__init__(self,None,linea,columna)
        self.tabla = tabla
        self.id = id
        self.lista_col = lista_col
    
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if arbol.bdUsar != None:
            objetoTabla = arbol.devolviendoTablaDeBase(self.tabla)
            if objetoTabla != None:
                listaUnique = []
                listaNombres = []
                '''
                for columnas in objetoTabla.lista_de_campos:
                    listaNombres.append(columnas.nombre)
                '''
                for c in self.lista_col:
                    for columnas in objetoTabla.lista_de_campos:
                        if columnas.nombre == c:
                            listaUnique.append(columnas)
                            listaNombres.append(columnas.nombre)
                if(len(listaUnique)==len(self.lista_col)):
                    print(len(listaUnique),self.tabla, self.id)
                    #Insertar llaves Unique
                else:
                    lista = set(self.lista_col) - set(listaNombres)
                    #print(listaNombres,self.lista_col)
                    #print(lista)
                    for i in lista:
                        error = Excepcion('42P01',"Semántico","No existe la columna «"+i+"» en la llave",self.linea,self.columna)
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
        
