from Instrucciones.Excepcion import Excepcion
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Sql_select.SelectLista import Alias
from storageManager.jsonMode import *
from Instrucciones.Sql_create.Tipo_Constraint import Tipo_Dato_Constraint
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
import numpy as np

class UpdateTable(Instruccion):
    def __init__(self, id, tipo, lCol, insWhere, strGram ,linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
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

        data = np.array((tablaUpdate))
        res = []
        # vamos a mostrar todos
        for x in range(0, len(columnas)):
            col = columnas[x].obtenerNombre()
            res.append(col)

        arbol.setColumnasActual(res)
        listaMods = self.insWhere.ejecutar(tabla,arbol)
        primaryKey = self.getPrimaryKeyCol(columnas)
        arbol.setUpdate()

        if self.listaDeColumnas and len( listaMods ) > 0:
            for y in range(0 , len(listaMods)):
                tupla = listaMods[y]
                lPK = self.obtenerValores(tupla, primaryKey)
                for x in range(0 , len(self.listaDeColumnas)):
                    
                    variable = self.listaDeColumnas[x].ejecutar(tabla, arbol)
                    if isinstance(variable, Alias):
                        #id es la posicione en la que se encuentra 
                        #expresion es el valor que se le asigna a la actualizacion 
                        validar = self.validacionTipos(columnas, variable.expresion, variable.id)
                        
                        if isinstance(validar, Excepcion):
                            arbol.excepciones.append(validar)
                            arbol.consola.append(validar.toString())
                            arbol.setUpdate()
                            return validar

                        resultado = update(arbol.getBaseDatos(), val, dict({variable.id:variable.expresion}), lPK)
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
                            error = Excepcion("42P01", "Semantico", "La llave "+ lPK[0] +" de la tabla "+ str(self.identificador.devolverId(tabla, arbol)) + " no existe", self.linea, self.columna)
                            arbol.excepciones.append(error)
                            arbol.consola.append(error.toString())
                            arbol.setUpdate()
                            return error
                    else:
                        print('Nel la cagaste prro :\'v')
                        arbol.setUpdate()
                        return variable
        else:
            error = Excepcion("42P12", "Semantico", "Error de operacion base de datos no existe", self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            arbol.setUpdate()
            return error

        arbol.setUpdate()

    def getPrimaryKeyCol(self, columnas):
        listaEnteros = []
        for y in range(0, len(columnas)):
            if columnas[y].constraint:
                for k in range(0, len(columnas[y].constraint)):
                    if columnas[y].constraint[k].tipo == Tipo_Dato_Constraint.PRIMARY_KEY:
                        listaEnteros.append(y)

        return listaEnteros



    def obtenerValores(self, tupla, posicionPK):
        #recorremos la lista que trae el num de columna
        listaPK = []
        for x in range(0, len(posicionPK)):
            listaPK.append(tupla[posicionPK[x]])
        return listaPK


    def validacionTipos(self, columnas, expresion, posColumna):
        if columnas[posColumna].tipo:
            print("tipo de columna")
            if str.isnumeric(expresion):
                if columnas[posColumna].tipo.tipo == Tipo_Dato.INTEGER:
                    return True
                
                if columnas[posColumna].tipo.tipo == Tipo_Dato.REAL:
                    return True

                if columnas[posColumna].tipo.tipo == Tipo_Dato.SMALLINT:
                    return True

                if columnas[posColumna].tipo.tipo == Tipo_Dato.BIGINT:
                    return True

            
            elif str.isdecimal(expresion):
                if columnas[posColumna].tipo.tipo == Tipo_Dato.DECIMAL:
                    return True

                if columnas[posColumna].tipo.tipo == Tipo_Dato.NUMERIC:
                    return True
                
                if columnas[posColumna].tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    return True
                
                if columnas[posColumna].tipo.tipo == Tipo_Dato.MONEY:
                    return True
            else:
                if columnas[posColumna].tipo.tipo == Tipo_Dato.TEXT or columnas[posColumna].tipo.tipo == Tipo_Dato.VARCHAR or columnas[posColumna].tipo.tipo == Tipo_Dato.VARYING or columnas[posColumna].tipo.tipo == Tipo_Dato.CHAR or columnas[posColumna].tipo.tipo == Tipo_Dato.CHARACTER:
                    return True
                
                if columnas[posColumna].tipo.tipo == Tipo_Dato.DATE:
                    return True

                if columnas[posColumna].tipo.tipo == Tipo_Dato.TIME:
                    return True

                if columnas[posColumna].tipo.tipo == Tipo_Dato.TIMESTAMP:
                    return True

                if columnas[posColumna].tipo.tipo == Tipo_Dato.BOOLEAN:
                    if expresion == '1' or expresion == '0' or expresion == 'true' or expresion == 'false':
                        return True
            
            error = Excepcion("22000", "Semantico", "Tipo de dato invalido", self.linea, self.columna)
            return error

            print(columnas[posColumna].tipo.toString())
        
        
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