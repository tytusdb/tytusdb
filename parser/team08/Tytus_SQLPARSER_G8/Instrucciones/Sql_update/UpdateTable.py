from Instrucciones.Excepcion import Excepcion
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Sql_select.SelectLista import Alias
from storageManager.jsonMode import *
from Instrucciones.Sql_create.Tipo_Constraint import Tipo_Dato_Constraint
import numpy as np

class UpdateTable(Instruccion):
    def __init__(self, id, tipo, lCol, insWhere, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.identificador = id
        self.listaDeColumnas = lCol
        self.insWhere = insWhere

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        val = self.identificador.devolverTabla(tabla, arbol)

        if(val == 0):
            error = Excepcion("42P01", "Semantico", "La tabla " + str(self.identificador.devolverId(tabla, arbol)) + " no existe", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            print('Error tabla no existe')
            return error

        tablaUpdate = extractTable(arbol.getBaseDatos(), val)
        arbol.setTablaActual(tablaUpdate)
        columnas = arbol.devolverColumnasTabla(val)
        print("------------- IMPRIMO -------------")
        indicePK = -1
        for y in range(0, len(columnas)):
            print(columnas[y].obtenerNombre())
            print(columnas[y].pk)

            if columnas[y].constraint :
                for rango in range(0, len(columnas[y].constraint)):
                    if(columnas[y].constraint[rango].tipo == Tipo_Dato_Constraint.PRIMARY_KEY):
                        print(columnas[y].constraint[rango].toString())
                        indicePK = y
                        break
            
            if  not (indicePK == -1) :
                break

            print(columnas[y].tipo)
            print("---------------------")
        print("----------- YA NO IMPRIMO ---------")


        data = np.array((tablaUpdate))
        res = []
        # vamos a mostrar todos
        for x in range(0, len(columnas)):
            col = columnas[x].obtenerNombre()
            res.append(col)

        arbol.setColumnasActual(res)
        arbol.setUpdate()
        claveValor = self.insWhere.ejecutar(tabla,arbol)
        
        
        if self.listaDeColumnas :
            for x in range(0 , len(self.listaDeColumnas)):
                variable = self.listaDeColumnas[x].ejecutar(tabla, arbol)
                if isinstance(variable, Alias):
                    #id es la posicione en la que se encuentra 
                    #expresion es el valor que se le asigna a la actualizacion 
                    resultado = update(arbol.getBaseDatos(), val, dict({variable.id:variable.expresion}), [claveValor.expresion])
                    if resultado == 0:
                        arbol.consola.append(f"Se actualizo el registro ")
                        
                    elif resultado == 1:
                        error = Excepcion("00XX", "Semantico", "Error de operacion interno", self.linea, self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        arbol.setUpdate()
                        return error

                    elif resultado == 2:
                        error = Excepcion("42P12", "Semantico", "Error de operacion base de datos no existe", self.linea, self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        arbol.setUpdate()
                        return error
                    elif resultado == 3:
                        error = Excepcion("42P01", "Semantico", "La tabla " + str(self.identificador.devolverId(tabla, arbol)) + " no existe", self.linea, self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        arbol.setUpdate()
                        return error
                    else:
                        error = Excepcion("42P01", "Semantico", "La llave "+ claveValor.expresion +" de la tabla "+ str(self.identificador.devolverId(tabla, arbol)) + " no existe", self.linea, self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        arbol.setUpdate()
                        return error
                else:
                    print('Nel la cagaste prro :\'v')


        arbol.setUpdate()
        
        
        '''if(self.identificador != None):
            if(self.listaDeColumnas != None):
                if(self.insWhere != None):
                    update(arbol.database())
        '''
        '''
        def update(database: str, table: str, register: dict, columns: list) -> int:
            '''


'''
instruccion = UpdateTable("hola mundo",None, 1,2)
instruccion.ejecutar(None,None)
'''