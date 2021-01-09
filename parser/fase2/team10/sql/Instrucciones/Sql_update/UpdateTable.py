from sql.Instrucciones.Excepcion import Excepcion
from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.Sql_select.SelectLista import Alias
from sql.storageManager.jsonMode import *
from sql.Instrucciones.Sql_create.Tipo_Constraint import Tipo_Dato_Constraint
from sql.Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
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
        listaMods = []
        if self.insWhere != None:
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
                        validar = self.validacionTipos(columnas[variable.id].tipo, variable.tipo, variable.expresion, arbol)
                        
                        if isinstance(validar, Excepcion):
                            arbol.excepciones.append(validar)
                            arbol.consola.append(validar.toString())
                            arbol.setUpdate()
                            return validar

                        if not validar:
                            error = Excepcion('42804',"Semántico","La columna «"+columnas[variable.id].nombre+"» es de tipo "+columnas[variable.id].tipo.toString()+" pero la expresión es de tipo "+variable.tipo.toString(),self.linea,self.columna)
                            arbol.excepciones.append(error)
                            arbol.consola.append(error.toString())
                            arbol.setUpdate()
                            return

                        resultado = update(arbol.getBaseDatos(), val, dict({variable.id:variable.expresion}), lPK)
                            
                        if resultado == 1:
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
                        elif resultado == 4:
                            error = Excepcion("42P01", "Semantico", "La llave "+ str(lPK[0]) +" de la tabla "+ str(self.identificador.devolverId(tabla, arbol)) + " no existe", self.linea, self.columna)
                            arbol.excepciones.append(error)
                            arbol.consola.append(error.toString())
                            arbol.setUpdate()
                            return error
                    else:
                        print('Nel la cagaste prro :\'v')
                        arbol.setUpdate()
                        return variable
        elif self.listaDeColumnas and self.insWhere == None:
            for x in range(0 , len(self.listaDeColumnas)):    
                variable = self.listaDeColumnas[x].ejecutar(tabla, arbol)
                if isinstance(variable, Alias):
                    validar = self.validacionTipos(columnas[variable.id].tipo, variable.tipo, variable.expresion, arbol)
                    if isinstance(validar, Excepcion):
                        arbol.excepciones.append(validar)
                        arbol.consola.append(validar.toString())
                        arbol.setUpdate()
                        return validar
                    if not validar:
                        error = Excepcion('42804',"Semántico","La columna «"+columnas[variable.id].nombre+"» es de tipo "+columnas[variable.id].tipo.toString()+" pero la expresión es de tipo "+variable.tipo.toString(),self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        arbol.setUpdate()
                        return
                    for tupla in arbol.getTablaActual():   
                        lPK = self.obtenerValores(tupla, primaryKey)                     
                        resultado = update(arbol.getBaseDatos(), val, dict({variable.id:variable.expresion}), lPK) 
                        if resultado == 1:
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
                        elif resultado == 4:
                            error = Excepcion("42P01", "Semantico", "La llave "+ str(lPK[0]) +" de la tabla "+ str(self.identificador.devolverId(tabla, arbol)) + " no existe", self.linea, self.columna)
                            arbol.excepciones.append(error)
                            arbol.consola.append(error.toString())
                            arbol.setUpdate()
                            return error
                else:
                    arbol.setUpdate()
                    return variable
        else:
            error = Excepcion("42P12", "Semantico", "Error de operacion base de datos no existe", self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            arbol.setUpdate()
            return error
        arbol.consola.append(f"Se actualizo el registro ")
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


    def validacionTipos(self, tipoColumna, tipoValor, val, arbol):
        if (tipoColumna.tipo == Tipo_Dato.MONEY) and (tipoValor.tipo == Tipo_Dato.CHAR):
            if ',' in val:
                val = val.replace(',','')
            try:
                val = float(val)
            except:
                error = Excepcion('22P02',"Semántico","La sintaxis de entrada no es válida para tipo money",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
            return True
        if tipoColumna.tipo == Tipo_Dato.TIPOENUM:
            existe = arbol.getEnum(tipoColumna.nombre)
            existeValor = existe.buscarTipo(val)
            if existeValor == None:
                error = Excepcion('2BP01',"Semántico","El valor "+val+" no existe dentro del TYPE ENUM "+tipoColumna.nombre,self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
            return True
        if (tipoColumna.tipo == Tipo_Dato.CHAR or tipoColumna.tipo == Tipo_Dato.VARCHAR or tipoColumna.tipo == Tipo_Dato.VARYING or tipoColumna.tipo == Tipo_Dato.CHARACTER or tipoColumna.tipo == Tipo_Dato.TEXT) and (tipoValor.tipo == Tipo_Dato.CHAR or tipoValor.tipo == Tipo_Dato.VARCHAR or tipoValor.tipo == Tipo_Dato.VARYING or tipoValor.tipo == Tipo_Dato.CHARACTER or tipoValor.tipo == Tipo_Dato.TEXT):
            if tipoColumna.dimension != None:
                if len(val) >= tipoColumna.dimension:
                    error = Excepcion('2BP01',"Semántico","el valor es demasiado largo para el tipo "+tipoColumna.toString()+"("+str(tipoColumna.dimension)+")",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            return True
        elif (tipoColumna.tipo == Tipo_Dato.SMALLINT or tipoColumna.tipo == Tipo_Dato.INTEGER or tipoColumna.tipo == Tipo_Dato.BIGINT or tipoColumna.tipo == Tipo_Dato.DECIMAL or tipoColumna.tipo == Tipo_Dato.NUMERIC or tipoColumna.tipo == Tipo_Dato.REAL or tipoColumna.tipo == Tipo_Dato.DOUBLE_PRECISION or tipoColumna.tipo == Tipo_Dato.MONEY) and (tipoValor.tipo == Tipo_Dato.SMALLINT or tipoValor.tipo == Tipo_Dato.INTEGER or tipoValor.tipo == Tipo_Dato.BIGINT or tipoValor.tipo == Tipo_Dato.DECIMAL or tipoValor.tipo == Tipo_Dato.NUMERIC or tipoValor.tipo == Tipo_Dato.REAL or tipoValor.tipo == Tipo_Dato.DOUBLE_PRECISION or tipoValor.tipo == Tipo_Dato.MONEY):
            if tipoColumna.tipo == Tipo_Dato.SMALLINT:
                if(val < -32768 or val > 32767):
                    error = Excepcion('2BP01',"Semántico",tipoColumna.toString()+" fuera de rango",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            elif tipoColumna.tipo == Tipo_Dato.INTEGER:
                if(val < -2147483648 or val > 2147483647):
                    error = Excepcion('2BP01',"Semántico",tipoColumna.toString()+" fuera de rango",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            elif tipoColumna.tipo == Tipo_Dato.BIGINT:
                if(val < -9223372036854775808 or val > 9223372036854775807):
                    error = Excepcion('2BP01',"Semántico",tipoColumna.toString()+" fuera de rango",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            return True
        elif (tipoColumna.tipo == Tipo_Dato.DATE or tipoColumna.tipo == Tipo_Dato.TIMESTAMP or tipoColumna.tipo == Tipo_Dato.TIME or tipoColumna.tipo == Tipo_Dato.INTERVAL or tipoColumna.tipo == Tipo_Dato.CHAR ) and (tipoValor.tipo == Tipo_Dato.DATE or tipoValor.tipo == Tipo_Dato.TIMESTAMP or tipoValor.tipo == Tipo_Dato.TIME or tipoValor.tipo == Tipo_Dato.INTERVAL or tipoValor.tipo == Tipo_Dato.CHAR):
            return True
        elif (tipoColumna.tipo == Tipo_Dato.BOOLEAN) and (tipoValor.tipo == Tipo_Dato.BOOLEAN):
            return True
        return False
        
        
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