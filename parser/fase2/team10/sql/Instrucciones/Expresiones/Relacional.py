from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from sql.Instrucciones.Excepcion import Excepcion
from sql.Instrucciones.Sql_select.SelectLista import Alias
 
import time
import numpy as np

class Relacional(Instruccion):
    def __init__(self, opIzq, opDer, operador, strGram,linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.BOOLEAN),linea,columna,strGram)
        self.opIzq = opIzq
        self.opDer = opDer
        self.operador = operador


    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        # Si existe algún error en el operador izquierdo, retorno el error.
        #Aqui vamos a verificar si hay un alias
        if isinstance(self.opIzq, Alias):
            nombreColumna = self.opIzq.expresion
            nombreTabla = tabla.getVariable(self.opIzq.id)
            #obtener la posicion
            posicion = arbol.devolverOrdenDeColumna(nombreTabla.valor,nombreColumna)
            resultadoIzq = posicion
        else:
            resultadoIzq = self.opIzq.ejecutar(tabla, arbol)
        if isinstance(resultadoIzq, Excepcion):
            return resultadoIzq
        # Si existe algún error en el operador derecho, retorno el error.
        if isinstance(self.opDer, Alias):
            nombreColumna = self.opDer.expresion
            nombreTabla = tabla.getVariable(self.opDer.id)
            #obtener la posicion
            posicion = arbol.devolverOrdenDeColumna(nombreTabla.valor,nombreColumna)
            resultadoDer = posicion
        else:
            resultadoDer=""
            if self.opDer.tipo.tipo== Tipo_Dato.QUERY:
                pass
                #print("ES UN QUERY")
            else:
                resultadoDer = self.opDer.ejecutar(tabla, arbol)
        if isinstance(resultadoDer, Excepcion):
            return resultadoDer
        # Comprobamos el tipo de operador
        if self.operador == '>':
            
            if(arbol.getWhere() or arbol.getUpdate()):
                fila = []
                tabla = []
                tablaRes = []
                #devolver columna
                tabla = arbol.getTablaActual()
                #aqui vamos a dividir por columnas
                data = np.array((tabla))
                #recorrer columna y ver si es == la posicion
                nueva_Columna = data[:, resultadoIzq]
                
                for x in range(0, len(nueva_Columna)):
                    variableNC = nueva_Columna[x]
                    variableComp = None

                    if (str.isdigit(variableNC)):
                        variableComp = int(variableNC)
                    elif str.isdecimal(variableNC) :
                        variableComp = float(variableNC)
                    else:
                        variableComp = nueva_Columna[x]

                    if(variableComp > resultadoDer):
                        #agregar a filas
                        fila.append(x)
                
                #Recorrer la tabla Completa y devolver el numero de filas
                for x in range(0, len(fila)):
                    fil = tabla[fila[x]]
                    tablaRes.append(fil)

                #agregar la tabla al arbol
                arbol.setTablaActual(tablaRes)                  
                return tablaRes
            else:
                if (self.opIzq.tipo.tipo == Tipo_Dato.SMALLINT or self.opIzq.tipo.tipo == Tipo_Dato.INTEGER or self.opIzq.tipo.tipo == Tipo_Dato.BIGINT or self.opIzq.tipo.tipo == Tipo_Dato.DECIMAL or self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC or self.opIzq.tipo.tipo == Tipo_Dato.REAL or self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opIzq.tipo.tipo == Tipo_Dato.MONEY) and (self.opDer.tipo.tipo == Tipo_Dato.SMALLINT or self.opDer.tipo.tipo == Tipo_Dato.INTEGER or self.opDer.tipo.tipo == Tipo_Dato.BIGINT or self.opDer.tipo.tipo == Tipo_Dato.DECIMAL or self.opDer.tipo.tipo == Tipo_Dato.NUMERIC or self.opDer.tipo.tipo == Tipo_Dato.REAL or self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opDer.tipo.tipo == Tipo_Dato.MONEY):
                    return resultadoIzq > resultadoDer
                elif (self.opIzq.tipo.tipo == Tipo_Dato.DATE or self.opIzq.tipo.tipo == Tipo_Dato.TIME or self.opIzq.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opIzq.tipo.tipo == Tipo_Dato.CHAR) and (self.opDer.tipo.tipo == Tipo_Dato.DATE or self.opDer.tipo.tipo == Tipo_Dato.TIME or self.opDer.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opDer.tipo.tipo == Tipo_Dato.CHAR):
                    formats = ("%d-%m-%Y", "%Y-%m-%d","%d-%M-%Y", "%Y-%M-%d","%Y-%b-%d", "%d-%b-%Y")
                    val1 = None
                    val2 = None
                    for fmt in formats:
                        valid_date=""
                        try:
                            valid_date = time.strptime(resultadoIzq, fmt)
                            if isinstance(valid_date, time.struct_time):
                                val1 = time.strftime('%Y-%m-%d',valid_date)
                        except ValueError as e:
                            pass
                    for fmt in formats:
                        valid_date=""
                        try:
                            valid_date = time.strptime(resultadoDer, fmt)
                            if isinstance(valid_date, time.struct_time):
                                val2 = time.strftime('%Y-%m-%d',valid_date)
                        except ValueError as e:
                            pass
                    if val1 != None and val2 != None:
                        return resultadoIzq > resultadoDer
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" > "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
                else:
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" > "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
        elif self.operador == '<':
            if(arbol.getWhere() or arbol.getUpdate()):
                fila = []
                tabla = []
                tablaRes = []
                #devolver columna
                tabla = arbol.getTablaActual()
                #aqui vamos a dividir por columnas
                data = np.array((tabla))
                #recorrer columna y ver si es == la posicion
                nueva_Columna = data[:, resultadoIzq]
                
                for x in range(0, len(nueva_Columna)):
                    variableNC = nueva_Columna[x]
                    variableComp = None

                    if (str.isdigit(variableNC)):
                        variableComp = int(variableNC)
                    elif str.isdecimal(variableNC):
                        variableComp = float(variableNC)
                    else:
                        variableComp = nueva_Columna[x]

                    if(variableComp < resultadoDer):
                        #agregar a filas
                        fila.append(x)
                
                #Recorrer la tabla Completa y devolver el numero de filas
                for x in range(0, len(fila)):
                    fil = tabla[fila[x]]
                    tablaRes.append(fil)

                #agregar la tabla al arbol
                arbol.setTablaActual(tablaRes)                  
                return tablaRes
            else:
                if (self.opIzq.tipo.tipo == Tipo_Dato.SMALLINT or self.opIzq.tipo.tipo == Tipo_Dato.INTEGER or self.opIzq.tipo.tipo == Tipo_Dato.BIGINT or self.opIzq.tipo.tipo == Tipo_Dato.DECIMAL or self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC or self.opIzq.tipo.tipo == Tipo_Dato.REAL or self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opIzq.tipo.tipo == Tipo_Dato.MONEY) and (self.opDer.tipo.tipo == Tipo_Dato.SMALLINT or self.opDer.tipo.tipo == Tipo_Dato.INTEGER or self.opDer.tipo.tipo == Tipo_Dato.BIGINT or self.opDer.tipo.tipo == Tipo_Dato.DECIMAL or self.opDer.tipo.tipo == Tipo_Dato.NUMERIC or self.opDer.tipo.tipo == Tipo_Dato.REAL or self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opDer.tipo.tipo == Tipo_Dato.MONEY):
                    return resultadoIzq < resultadoDer
                elif (self.opIzq.tipo.tipo == Tipo_Dato.DATE or self.opIzq.tipo.tipo == Tipo_Dato.TIME or self.opIzq.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opIzq.tipo.tipo == Tipo_Dato.CHAR) and (self.opDer.tipo.tipo == Tipo_Dato.DATE or self.opDer.tipo.tipo == Tipo_Dato.TIME or self.opDer.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opDer.tipo.tipo == Tipo_Dato.CHAR):
                    formats = ("%d-%m-%Y", "%Y-%m-%d","%d-%M-%Y", "%Y-%M-%d","%Y-%b-%d", "%d-%b-%Y")
                    val1 = None
                    val2 = None
                    for fmt in formats:
                        valid_date=""
                        try:
                            valid_date = time.strptime(resultadoIzq, fmt)
                            if isinstance(valid_date, time.struct_time):
                                val1 = time.strftime('%Y-%m-%d',valid_date)
                        except ValueError as e:
                            pass
                    for fmt in formats:
                        valid_date=""
                        try:
                            valid_date = time.strptime(resultadoDer, fmt)
                            if isinstance(valid_date, time.struct_time):
                                val2 = time.strftime('%Y-%m-%d',valid_date)
                        except ValueError as e:
                            pass
                    if val1 != None and val2 != None:
                        return resultadoIzq < resultadoDer
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" < "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
                else:
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" < "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
        elif self.operador == '>=':
            if(arbol.getWhere() or arbol.getUpdate()):
                fila = []
                tabla = []
                tablaRes = []
                #devolver columna
                tabla = arbol.getTablaActual()
                #aqui vamos a dividir por columnas
                data = np.array((tabla))
                #recorrer columna y ver si es == la posicion
                nueva_Columna = data[:, resultadoIzq]
                
                for x in range(0, len(nueva_Columna)):
                    variableNC = nueva_Columna[x]
                    variableComp = None

                    if (str.isdigit(variableNC)):
                        variableComp = int(variableNC)
                    elif str.isdecimal(variableNC):
                        variableComp = float(variableNC)
                    else:
                        variableComp = nueva_Columna[x]


                    if(variableComp >= resultadoDer):
                        #agregar a filas
                        fila.append(x)
                
                #Recorrer la tabla Completa y devolver el numero de filas
                for x in range(0, len(fila)):
                    fil = tabla[fila[x]]
                    tablaRes.append(fil)

                #agregar la tabla al arbol
                arbol.setTablaActual(tablaRes)                  
                return tablaRes
            else:
                if (self.opIzq.tipo.tipo == Tipo_Dato.SMALLINT or self.opIzq.tipo.tipo == Tipo_Dato.INTEGER or self.opIzq.tipo.tipo == Tipo_Dato.BIGINT or self.opIzq.tipo.tipo == Tipo_Dato.DECIMAL or self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC or self.opIzq.tipo.tipo == Tipo_Dato.REAL or self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opIzq.tipo.tipo == Tipo_Dato.MONEY) and (self.opDer.tipo.tipo == Tipo_Dato.SMALLINT or self.opDer.tipo.tipo == Tipo_Dato.INTEGER or self.opDer.tipo.tipo == Tipo_Dato.BIGINT or self.opDer.tipo.tipo == Tipo_Dato.DECIMAL or self.opDer.tipo.tipo == Tipo_Dato.NUMERIC or self.opDer.tipo.tipo == Tipo_Dato.REAL or self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opDer.tipo.tipo == Tipo_Dato.MONEY):
                    return resultadoIzq >= resultadoDer
                elif (self.opIzq.tipo.tipo == Tipo_Dato.DATE or self.opIzq.tipo.tipo == Tipo_Dato.TIME or self.opIzq.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opIzq.tipo.tipo == Tipo_Dato.CHAR) and (self.opDer.tipo.tipo == Tipo_Dato.DATE or self.opDer.tipo.tipo == Tipo_Dato.TIME or self.opDer.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opDer.tipo.tipo == Tipo_Dato.CHAR):
                    formats = ("%d-%m-%Y", "%Y-%m-%d","%d-%M-%Y", "%Y-%M-%d","%Y-%b-%d", "%d-%b-%Y")
                    val1 = None
                    val2 = None
                    for fmt in formats:
                        valid_date=""
                        try:
                            valid_date = time.strptime(resultadoIzq, fmt)
                            if isinstance(valid_date, time.struct_time):
                                val1 = time.strftime('%Y-%m-%d',valid_date)
                        except ValueError as e:
                            pass
                    for fmt in formats:
                        valid_date=""
                        try:
                            valid_date = time.strptime(resultadoDer, fmt)
                            if isinstance(valid_date, time.struct_time):
                                val2 = time.strftime('%Y-%m-%d',valid_date)
                        except ValueError as e:
                            pass
                    if val1 != None and val2 != None:
                        return resultadoIzq >= resultadoDer
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" >= "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
                else:
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" >= "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
        elif self.operador == '<=':
            if(arbol.getWhere() or arbol.getUpdate()):
                fila = []
                tabla = []
                tablaRes = []
                #devolver columna
                tabla = arbol.getTablaActual()
                #aqui vamos a dividir por columnas
                data = np.array((tabla))
                #recorrer columna y ver si es == la posicion
                nueva_Columna = data[:, resultadoIzq]
                
                for x in range(0, len(nueva_Columna)):
                    variableNC = nueva_Columna[x]
                    variableComp = None

                    if (str.isdigit(variableNC)):
                        variableComp = int(variableNC)
                    elif str.isdecimal(variableNC):
                        variableComp = float(variableNC)
                    else:
                        variableComp = nueva_Columna[x]

                    if(variableComp <= resultadoDer):
                        #agregar a filas
                        fila.append(x)
                
                #Recorrer la tabla Completa y devolver el numero de filas
                for x in range(0, len(fila)):
                    fil = tabla[fila[x]]
                    tablaRes.append(fil)

                #agregar la tabla al arbol
                arbol.setTablaActual(tablaRes)                  
                return tablaRes
            else:
                if (self.opIzq.tipo.tipo == Tipo_Dato.SMALLINT or self.opIzq.tipo.tipo == Tipo_Dato.INTEGER or self.opIzq.tipo.tipo == Tipo_Dato.BIGINT or self.opIzq.tipo.tipo == Tipo_Dato.DECIMAL or self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC or self.opIzq.tipo.tipo == Tipo_Dato.REAL or self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opIzq.tipo.tipo == Tipo_Dato.MONEY) and (self.opDer.tipo.tipo == Tipo_Dato.SMALLINT or self.opDer.tipo.tipo == Tipo_Dato.INTEGER or self.opDer.tipo.tipo == Tipo_Dato.BIGINT or self.opDer.tipo.tipo == Tipo_Dato.DECIMAL or self.opDer.tipo.tipo == Tipo_Dato.NUMERIC or self.opDer.tipo.tipo == Tipo_Dato.REAL or self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opDer.tipo.tipo == Tipo_Dato.MONEY):
                    return resultadoIzq <= resultadoDer
                elif (self.opIzq.tipo.tipo == Tipo_Dato.DATE or self.opIzq.tipo.tipo == Tipo_Dato.TIME or self.opIzq.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opIzq.tipo.tipo == Tipo_Dato.CHAR) and (self.opDer.tipo.tipo == Tipo_Dato.DATE or self.opDer.tipo.tipo == Tipo_Dato.TIME or self.opDer.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opDer.tipo.tipo == Tipo_Dato.CHAR):
                    formats = ("%d-%m-%Y", "%Y-%m-%d","%d-%M-%Y", "%Y-%M-%d","%Y-%b-%d", "%d-%b-%Y")
                    val1 = None
                    val2 = None
                    for fmt in formats:
                        valid_date=""
                        try:
                            valid_date = time.strptime(resultadoIzq, fmt)
                            if isinstance(valid_date, time.struct_time):
                                val1 = time.strftime('%Y-%m-%d',valid_date)
                        except ValueError as e:
                            pass
                    for fmt in formats:
                        valid_date=""
                        try:
                            valid_date = time.strptime(resultadoDer, fmt)
                            if isinstance(valid_date, time.struct_time):
                                val2 = time.strftime('%Y-%m-%d',valid_date)
                        except ValueError as e:
                            pass
                    if val1 != None and val2 != None:
                        return resultadoIzq <= resultadoDer
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" <= "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
                else:
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" <= "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
        elif self.operador == '=':
            if(arbol.getWhere()):
                fila = []
                tabla = []
                tablaRes = []
                #devolver columna
                tabla = arbol.getTablaActual()
                #aqui vamos a dividir por columnas
                data = np.array((tabla))
                #recorrer columna y ver si es == la posicion
                nueva_Columna = data[:, resultadoIzq]
                
                for x in range(0, len(nueva_Columna)):
                    variableNC = str(nueva_Columna[x])
                    variableComp = None
                    if (str.isdigit(variableNC)):
                        variableComp = int(variableNC)
                    elif str.isdecimal(variableNC):
                        variableComp = float(variableNC)
                    else:
                        variableComp = nueva_Columna[x]

                    if(variableComp == resultadoDer):
                        #agregar a filas
                        fila.append(x)
                
                #Recorrer la tabla Completa y devolver el numero de filas
                for x in range(0, len(fila)):
                    fil = tabla[fila[x]]
                    tablaRes.append(fil)

                #agregar la tabla al arbol
                #arbol.setTablaActual(tablaRes)                  
                return tablaRes
            elif arbol.getUpdate():
                #aqui va un comparador para update como en update el igual es para asignacion
                if(self.opIzq.tipo.tipo == Tipo_Dato.ID and (not self.opDer.tipo.tipo == Tipo_Dato.ID)):
                    # aqui va el procedimiento para devolver un id con su valor
                    a = Alias(resultadoIzq, resultadoDer)
                    a.tipo = self.opDer.tipo
                    return a
                else:
                    # este es el error por el momento
                    error = Excepcion('42883', "Semántico", "el operador no existe "+self.opIzq.tipo.toString()+" = "+self.opDer.tipo.toString(), self.linea, self.columna )
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())

            else:
                if (self.opIzq.tipo.tipo == Tipo_Dato.SMALLINT or self.opIzq.tipo.tipo == Tipo_Dato.INTEGER or self.opIzq.tipo.tipo == Tipo_Dato.BIGINT or self.opIzq.tipo.tipo == Tipo_Dato.DECIMAL or self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC or self.opIzq.tipo.tipo == Tipo_Dato.REAL or self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opIzq.tipo.tipo == Tipo_Dato.MONEY) and (self.opDer.tipo.tipo == Tipo_Dato.SMALLINT or self.opDer.tipo.tipo == Tipo_Dato.INTEGER or self.opDer.tipo.tipo == Tipo_Dato.BIGINT or self.opDer.tipo.tipo == Tipo_Dato.DECIMAL or self.opDer.tipo.tipo == Tipo_Dato.NUMERIC or self.opDer.tipo.tipo == Tipo_Dato.REAL or self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opDer.tipo.tipo == Tipo_Dato.MONEY):
                    return resultadoIzq == resultadoDer
                elif (self.opIzq.tipo.tipo == Tipo_Dato.DATE or self.opIzq.tipo.tipo == Tipo_Dato.TIME or self.opIzq.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opIzq.tipo.tipo == Tipo_Dato.CHAR) and (self.opDer.tipo.tipo == Tipo_Dato.DATE or self.opDer.tipo.tipo == Tipo_Dato.TIME or self.opDer.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opDer.tipo.tipo == Tipo_Dato.CHAR):
                    formats = ("%d-%m-%Y", "%Y-%m-%d","%d-%M-%Y", "%Y-%M-%d","%Y-%b-%d", "%d-%b-%Y")
                    val1 = None
                    val2 = None
                    for fmt in formats:
                        valid_date=""
                        try:
                            valid_date = time.strptime(resultadoIzq, fmt)
                            if isinstance(valid_date, time.struct_time):
                                val1 = time.strftime('%Y-%m-%d',valid_date)
                        except ValueError as e:
                            pass
                    for fmt in formats:
                        valid_date=""
                        try:
                            valid_date = time.strptime(resultadoDer, fmt)
                            if isinstance(valid_date, time.struct_time):
                                val2 = time.strftime('%Y-%m-%d',valid_date)
                        except ValueError as e:
                            pass
                    if val1 != None and val2 != None:
                        return resultadoIzq == resultadoDer
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" = "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
                else:
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" = "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
        elif self.operador == '<>':
            if(arbol.getWhere() or arbol.getUpdate()):
                fila = []
                tabla = []
                tablaRes = []
                #devolver columna
                tabla = arbol.getTablaActual()
                #aqui vamos a dividir por columnas
                data = np.array((tabla))
                #recorrer columna y ver si es == la posicion
                nueva_Columna = data[:, resultadoIzq]
                
                for x in range(0, len(nueva_Columna)):
                    variableNC = nueva_Columna[x]
                    variableComp = None

                    if (str.isdigit(variableNC)):
                        variableComp = int(variableNC)

                    elif str.isdecimal(variableNC):
                        variableComp = float(variableNC)

                    else:
                        variableComp = nueva_Columna[x]


                    if(variableComp != resultadoDer):
                        #agregar a filas
                        fila.append(x)
                
                #Recorrer la tabla Completa y devolver el numero de filas
                for x in range(0, len(fila)):
                    fil = tabla[fila[x]]
                    tablaRes.append(fil)

                #agregar la tabla al arbol
                arbol.setTablaActual(tablaRes)                  
                return tablaRes
            else:
                if (self.opIzq.tipo.tipo == Tipo_Dato.SMALLINT or self.opIzq.tipo.tipo == Tipo_Dato.INTEGER or self.opIzq.tipo.tipo == Tipo_Dato.BIGINT or self.opIzq.tipo.tipo == Tipo_Dato.DECIMAL or self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC or self.opIzq.tipo.tipo == Tipo_Dato.REAL or self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opIzq.tipo.tipo == Tipo_Dato.MONEY) and (self.opDer.tipo.tipo == Tipo_Dato.SMALLINT or self.opDer.tipo.tipo == Tipo_Dato.INTEGER or self.opDer.tipo.tipo == Tipo_Dato.BIGINT or self.opDer.tipo.tipo == Tipo_Dato.DECIMAL or self.opDer.tipo.tipo == Tipo_Dato.NUMERIC or self.opDer.tipo.tipo == Tipo_Dato.REAL or self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opDer.tipo.tipo == Tipo_Dato.MONEY):
                    return resultadoIzq != resultadoDer
                elif (self.opIzq.tipo.tipo == Tipo_Dato.DATE or self.opIzq.tipo.tipo == Tipo_Dato.TIME or self.opIzq.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opIzq.tipo.tipo == Tipo_Dato.CHAR) and (self.opDer.tipo.tipo == Tipo_Dato.DATE or self.opDer.tipo.tipo == Tipo_Dato.TIME or self.opDer.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opDer.tipo.tipo == Tipo_Dato.CHAR):
                    formats = ("%d-%m-%Y", "%Y-%m-%d","%d-%M-%Y", "%Y-%M-%d","%Y-%b-%d", "%d-%b-%Y")
                    val1 = None
                    val2 = None
                    for fmt in formats:
                        valid_date=""
                        try:
                            valid_date = time.strptime(resultadoIzq, fmt)
                            if isinstance(valid_date, time.struct_time):
                                val1 = time.strftime('%Y-%m-%d',valid_date)
                        except ValueError as e:
                            pass
                    for fmt in formats:
                        valid_date=""
                        try:
                            valid_date = time.strptime(resultadoDer, fmt)
                            if isinstance(valid_date, time.struct_time):
                                val2 = time.strftime('%Y-%m-%d',valid_date)
                        except ValueError as e:
                            pass
                    if val1 != None and val2 != None:
                        return resultadoIzq != resultadoDer
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" <> "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
                else:
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" <> "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
        elif self.operador == "LIKE":
            if(arbol.getWhere()):
                fila = []
                tabla = []
                tablaRes = []
                #devolver columna
                tabla = arbol.getTablaActual()
                #aqui vamos a dividir por columnas
                data = np.array((tabla))
                #recorrer columna y ver si es == la posicion
                nueva_Columna = data[:, resultadoIzq]
                if not(self.opIzq.tipo.tipo == Tipo_Dato.ID) : 
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" = "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
                if not (self.opDer.tipo.tipo == Tipo_Dato.VARCHAR or self.opDer.tipo.tipo == Tipo_Dato.CHAR or self.opDer.tipo.tipo == Tipo_Dato.CHARACTER or self.opDer.tipo.tipo == Tipo_Dato.VARCHAR or self.opDer.tipo.tipo == Tipo_Dato.VARYING or self.opDer.tipo.tipo == Tipo_Dato.TEXT):
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" = "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error


                for x in range(0, len(nueva_Columna)):
                    variableNC = str(nueva_Columna[x])

                    if(resultadoDer in variableNC):
                        #agregar a filas
                        fila.append(x)
                
                #Recorrer la tabla Completa y devolver el numero de filas
                for x in range(0, len(fila)):
                    fil = tabla[fila[x]]
                    tablaRes.append(fil)

                #agregar la tabla al arbol
                #arbol.setTablaActual(tablaRes)                  
                return tablaRes
            
            else:
                if (self.opIzq.tipo.tipo == Tipo_Dato.VARCHAR or self.opIzq.tipo.tipo == Tipo_Dato.CHAR or self.opIzq.tipo.tipo == Tipo_Dato.CHARACTER or self.opIzq.tipo.tipo == Tipo_Dato.VARCHAR or self.opIzq.tipo.tipo == Tipo_Dato.VARYING or self.opIzq.tipo.tipo == Tipo_Dato.TEXT ) and (self.opDer.tipo.tipo == Tipo_Dato.VARCHAR or self.opDer.tipo.tipo == Tipo_Dato.CHAR or self.opDer.tipo.tipo == Tipo_Dato.CHARACTER or self.opDer.tipo.tipo == Tipo_Dato.VARCHAR or self.opDer.tipo.tipo == Tipo_Dato.VARYING or self.opDer.tipo.tipo == Tipo_Dato.TEXT):
                    return resultadoIzq == resultadoDer
                else:
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" = "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
                    
        elif self.operador == "NOT LIKE":
            if(arbol.getWhere()):
                fila = []
                tabla = []
                tablaRes = []
                #devolver columna
                tabla = arbol.getTablaActual()
                #aqui vamos a dividir por columnas
                data = np.array((tabla))
                nueva_Columna = data[:, resultadoIzq]
                if not(self.opIzq.tipo.tipo == Tipo_Dato.ID) : 
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" = "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
                if not (self.opDer.tipo.tipo == Tipo_Dato.VARCHAR or self.opDer.tipo.tipo == Tipo_Dato.CHAR or self.opDer.tipo.tipo == Tipo_Dato.CHARACTER or self.opDer.tipo.tipo == Tipo_Dato.VARCHAR or self.opDer.tipo.tipo == Tipo_Dato.VARYING or self.opDer.tipo.tipo == Tipo_Dato.TEXT):
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" = "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error


                for x in range(0, len(nueva_Columna)):
                    variableNC = str(nueva_Columna[x])

                    if( not (resultadoDer in variableNC )):
                        #agregar a filas
                        fila.append(x)
                
                #Recorrer la tabla Completa y devolver el numero de filas
                for x in range(0, len(fila)):
                    fil = tabla[fila[x]]
                    tablaRes.append(fil)

                #agregar la tabla al arbol
                #arbol.setTablaActual(tablaRes)                  
                return tablaRes
            
            else:
                if (self.opIzq.tipo.tipo == Tipo_Dato.VARCHAR or self.opIzq.tipo.tipo == Tipo_Dato.CHAR or self.opIzq.tipo.tipo == Tipo_Dato.CHARACTER or self.opIzq.tipo.tipo == Tipo_Dato.VARCHAR or self.opIzq.tipo.tipo == Tipo_Dato.VARYING or self.opIzq.tipo.tipo == Tipo_Dato.TEXT ) and (self.opDer.tipo.tipo == Tipo_Dato.VARCHAR or self.opDer.tipo.tipo == Tipo_Dato.CHAR or self.opDer.tipo.tipo == Tipo_Dato.CHARACTER or self.opDer.tipo.tipo == Tipo_Dato.VARCHAR or self.opDer.tipo.tipo == Tipo_Dato.VARYING or self.opDer.tipo.tipo == Tipo_Dato.TEXT):
                    return resultadoIzq == resultadoDer
                else:
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" = "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
        elif self.operador == "IN":
            if(arbol.getWhere()):
                try:
                    fila = []
                    tabla = []
                    tablaRes = []
                    #devolver columna
                    tabla = arbol.getTablaActual()
                    #aqui vamos a dividir por columnas
                    data = np.array((tabla))
                    nueva_Columna = data[:, resultadoIzq]
                    if self.opDer.lista[0].tipo.tipo == Tipo_Dato.QUERY:
                        resultadoDer= self.opDer.lista[0].ejecutar(tabla, arbol)

                    if isinstance(resultadoDer, np.ndarray):
                        for nfila in resultadoDer:
                            #if(variableComp == nfila):
                                #agregar a filas
                                #print("fila",nfila)
                                #fila.append(x)                
                            for x in range(0, len(nueva_Columna)):
                                variableNC = str(nueva_Columna[x])
                                variableComp = None
                                #print(type(variableNC))

                                if (str.isdigit(variableNC)):
                                    variableComp = int(variableNC)
                                elif str.isdecimal(variableNC):
                                    variableComp = float(variableNC)
                                else:
                                    variableComp = nueva_Columna[x]
                                if(variableComp == nfila):
                                    #agregar a filas
                                    fila.append(x)
                    elif isinstance(resultadoDer, list):
                        for nfila in resultadoDer:               
                            for x in range(0, len(nueva_Columna)):
                                variableNC = str(nueva_Columna[x])
                                variableComp = None
                                if (str.isdigit(variableNC)):
                                    variableComp = int(variableNC)
                                elif str.isdecimal(variableNC):
                                    variableComp = float(variableNC)
                                else:
                                    variableComp = nueva_Columna[x]
                                if(variableComp == nfila):
                                    fila.append(x)
                    else:
                        for x in range(0, len(nueva_Columna)):
                            variableNC = str(nueva_Columna[x])
                            variableComp = None
                            if (str.isdigit(variableNC)):
                                variableComp = int(variableNC)
                            elif str.isdecimal(variableNC):
                                variableComp = float(variableNC)
                            else:
                                variableComp = nueva_Columna[x]
                            if(variableComp == resultadoDer):
                                fila.append(x)
                    
                    #Recorrer la tabla Completa y devolver el numero de filas
                    for x in range(0, len(fila)):
                        fil = tabla[fila[x]]
                        tablaRes.append(fil)
                except:
                    error = Excepcion('XX000',"Semántico","ERROR INTERNO.",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    tablaRes=error

                #agregar la tabla al arbol
                #arbol.setTablaActual(tablaRes)                  
                return tablaRes
            else:
                print("ENTRO A ESTE ELSE")
        elif self.operador == "NOT IN":
            if(arbol.getWhere()):
                try:
                    fila = []
                    tabla = []
                    tablaRes = []
                    #devolver columna
                    tabla = arbol.getTablaActual()
                    #aqui vamos a dividir por columnas
                    data = np.array((tabla))
                    #recorrer columna y ver si es == la posicion
                    nueva_Columna = data[:, resultadoIzq]
                    if self.opDer.lista[0].tipo.tipo == Tipo_Dato.QUERY:
                        resultadoDer= self.opDer.lista[0].ejecutar(tabla, arbol)

                    if isinstance(resultadoDer, np.ndarray):             
                            for x in range(0, len(nueva_Columna)):
                                variableNC = str(nueva_Columna[x])
                                variableComp = None
                                #print(type(variableNC))

                                if (str.isdigit(variableNC)):
                                    variableComp = int(variableNC)
                                elif str.isdecimal(variableNC):
                                    variableComp = float(variableNC)
                                else:
                                    variableComp = nueva_Columna[x]
                                if not (variableComp in resultadoDer):
                                    fila.append(x)
                                   
                    elif isinstance(resultadoDer, list):             
                            for x in range(0, len(nueva_Columna)):
                                variableNC = str(nueva_Columna[x])
                                variableComp = None
                                if (str.isdigit(variableNC)):
                                    variableComp = int(variableNC)
                                elif str.isdecimal(variableNC):
                                    variableComp = float(variableNC)
                                else:
                                    variableComp = nueva_Columna[x]
                                if not (variableComp in resultadoDer):
                                    fila.append(x)
                    else:
                        for x in range(0, len(nueva_Columna)):
                            variableNC = str(nueva_Columna[x])
                            variableComp = None
                            if (str.isdigit(variableNC)):
                                variableComp = int(variableNC)
                            elif str.isdecimal(variableNC):
                                variableComp = float(variableNC)
                            else:
                                variableComp = nueva_Columna[x]
                            if (variableComp != resultadoDer):
                                fila.append(x)
                    
                    #Recorrer la tabla Completa y devolver el numero de filas
                    for x in range(0, len(fila)):
                        fil = tabla[fila[x]]
                        tablaRes.append(fil)
                except:
                    error = Excepcion('XX000',"Semántico","ERROR INTERNO.",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    tablaRes=error

                #agregar la tabla al arbol
                #arbol.setTablaActual(tablaRes)                  
                return tablaRes
            else:
                print("ENTRO A ESTE ELSE")
                
        else:
            error = Excepcion('42804',"Semántico","Operador desconocido.",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error

    def analizar(self, tabla, arbol):
        super().analizar(tabla,arbol)
        resultadoIzq = self.opIzq.analizar(tabla, arbol)
        if isinstance(resultadoIzq, Excepcion):
            return resultadoIzq
        resultadoDer = self.opDer.analizar(tabla, arbol)
        if isinstance(resultadoDer, Excepcion):
            return resultadoDer
        # Comprobamos el tipo de operador
        if self.operador == '>':
            if (self.opIzq.tipo.tipo == Tipo_Dato.SMALLINT or self.opIzq.tipo.tipo == Tipo_Dato.INTEGER or self.opIzq.tipo.tipo == Tipo_Dato.BIGINT or self.opIzq.tipo.tipo == Tipo_Dato.DECIMAL or self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC or self.opIzq.tipo.tipo == Tipo_Dato.REAL or self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opIzq.tipo.tipo == Tipo_Dato.MONEY) and (self.opDer.tipo.tipo == Tipo_Dato.SMALLINT or self.opDer.tipo.tipo == Tipo_Dato.INTEGER or self.opDer.tipo.tipo == Tipo_Dato.BIGINT or self.opDer.tipo.tipo == Tipo_Dato.DECIMAL or self.opDer.tipo.tipo == Tipo_Dato.NUMERIC or self.opDer.tipo.tipo == Tipo_Dato.REAL or self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opDer.tipo.tipo == Tipo_Dato.MONEY):
                return self.tipo
            elif (self.opIzq.tipo.tipo == Tipo_Dato.DATE or self.opIzq.tipo.tipo == Tipo_Dato.TIME or self.opIzq.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opIzq.tipo.tipo == Tipo_Dato.CHAR) and (self.opDer.tipo.tipo == Tipo_Dato.DATE or self.opDer.tipo.tipo == Tipo_Dato.TIME or self.opDer.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opDer.tipo.tipo == Tipo_Dato.CHAR):
                return self.tipo
            else:
                error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" > "+self.opDer.tipo.toString(),self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        elif self.operador == '<':
            if (self.opIzq.tipo.tipo == Tipo_Dato.SMALLINT or self.opIzq.tipo.tipo == Tipo_Dato.INTEGER or self.opIzq.tipo.tipo == Tipo_Dato.BIGINT or self.opIzq.tipo.tipo == Tipo_Dato.DECIMAL or self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC or self.opIzq.tipo.tipo == Tipo_Dato.REAL or self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opIzq.tipo.tipo == Tipo_Dato.MONEY) and (self.opDer.tipo.tipo == Tipo_Dato.SMALLINT or self.opDer.tipo.tipo == Tipo_Dato.INTEGER or self.opDer.tipo.tipo == Tipo_Dato.BIGINT or self.opDer.tipo.tipo == Tipo_Dato.DECIMAL or self.opDer.tipo.tipo == Tipo_Dato.NUMERIC or self.opDer.tipo.tipo == Tipo_Dato.REAL or self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opDer.tipo.tipo == Tipo_Dato.MONEY):
                return self.tipo
            elif (self.opIzq.tipo.tipo == Tipo_Dato.DATE or self.opIzq.tipo.tipo == Tipo_Dato.TIME or self.opIzq.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opIzq.tipo.tipo == Tipo_Dato.CHAR) and (self.opDer.tipo.tipo == Tipo_Dato.DATE or self.opDer.tipo.tipo == Tipo_Dato.TIME or self.opDer.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opDer.tipo.tipo == Tipo_Dato.CHAR):
                return self.tipo
            else:
                error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" < "+self.opDer.tipo.toString(),self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        elif self.operador == '>=':
            if (self.opIzq.tipo.tipo == Tipo_Dato.SMALLINT or self.opIzq.tipo.tipo == Tipo_Dato.INTEGER or self.opIzq.tipo.tipo == Tipo_Dato.BIGINT or self.opIzq.tipo.tipo == Tipo_Dato.DECIMAL or self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC or self.opIzq.tipo.tipo == Tipo_Dato.REAL or self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opIzq.tipo.tipo == Tipo_Dato.MONEY) and (self.opDer.tipo.tipo == Tipo_Dato.SMALLINT or self.opDer.tipo.tipo == Tipo_Dato.INTEGER or self.opDer.tipo.tipo == Tipo_Dato.BIGINT or self.opDer.tipo.tipo == Tipo_Dato.DECIMAL or self.opDer.tipo.tipo == Tipo_Dato.NUMERIC or self.opDer.tipo.tipo == Tipo_Dato.REAL or self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opDer.tipo.tipo == Tipo_Dato.MONEY):
                return self.tipo
            elif (self.opIzq.tipo.tipo == Tipo_Dato.DATE or self.opIzq.tipo.tipo == Tipo_Dato.TIME or self.opIzq.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opIzq.tipo.tipo == Tipo_Dato.CHAR) and (self.opDer.tipo.tipo == Tipo_Dato.DATE or self.opDer.tipo.tipo == Tipo_Dato.TIME or self.opDer.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opDer.tipo.tipo == Tipo_Dato.CHAR):
                return self.tipo
            else:
                error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" >= "+self.opDer.tipo.toString(),self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        elif self.operador == '<=':
            if (self.opIzq.tipo.tipo == Tipo_Dato.SMALLINT or self.opIzq.tipo.tipo == Tipo_Dato.INTEGER or self.opIzq.tipo.tipo == Tipo_Dato.BIGINT or self.opIzq.tipo.tipo == Tipo_Dato.DECIMAL or self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC or self.opIzq.tipo.tipo == Tipo_Dato.REAL or self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opIzq.tipo.tipo == Tipo_Dato.MONEY) and (self.opDer.tipo.tipo == Tipo_Dato.SMALLINT or self.opDer.tipo.tipo == Tipo_Dato.INTEGER or self.opDer.tipo.tipo == Tipo_Dato.BIGINT or self.opDer.tipo.tipo == Tipo_Dato.DECIMAL or self.opDer.tipo.tipo == Tipo_Dato.NUMERIC or self.opDer.tipo.tipo == Tipo_Dato.REAL or self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opDer.tipo.tipo == Tipo_Dato.MONEY):
                return self.tipo
            elif (self.opIzq.tipo.tipo == Tipo_Dato.DATE or self.opIzq.tipo.tipo == Tipo_Dato.TIME or self.opIzq.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opIzq.tipo.tipo == Tipo_Dato.CHAR) and (self.opDer.tipo.tipo == Tipo_Dato.DATE or self.opDer.tipo.tipo == Tipo_Dato.TIME or self.opDer.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opDer.tipo.tipo == Tipo_Dato.CHAR):
                return self.tipo
            else:
                error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" <= "+self.opDer.tipo.toString(),self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        elif self.operador == '=':            
            if (self.opIzq.tipo.tipo == Tipo_Dato.SMALLINT or self.opIzq.tipo.tipo == Tipo_Dato.INTEGER or self.opIzq.tipo.tipo == Tipo_Dato.BIGINT or self.opIzq.tipo.tipo == Tipo_Dato.DECIMAL or self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC or self.opIzq.tipo.tipo == Tipo_Dato.REAL or self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opIzq.tipo.tipo == Tipo_Dato.MONEY) and (self.opDer.tipo.tipo == Tipo_Dato.SMALLINT or self.opDer.tipo.tipo == Tipo_Dato.INTEGER or self.opDer.tipo.tipo == Tipo_Dato.BIGINT or self.opDer.tipo.tipo == Tipo_Dato.DECIMAL or self.opDer.tipo.tipo == Tipo_Dato.NUMERIC or self.opDer.tipo.tipo == Tipo_Dato.REAL or self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opDer.tipo.tipo == Tipo_Dato.MONEY):
                return self.tipo
            elif (self.opIzq.tipo.tipo == Tipo_Dato.DATE or self.opIzq.tipo.tipo == Tipo_Dato.TIME or self.opIzq.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opIzq.tipo.tipo == Tipo_Dato.CHAR) and (self.opDer.tipo.tipo == Tipo_Dato.DATE or self.opDer.tipo.tipo == Tipo_Dato.TIME or self.opDer.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opDer.tipo.tipo == Tipo_Dato.CHAR):
                return self.tipo
            else:
                error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" = "+self.opDer.tipo.toString(),self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        elif self.operador == '<>':
            if (self.opIzq.tipo.tipo == Tipo_Dato.SMALLINT or self.opIzq.tipo.tipo == Tipo_Dato.INTEGER or self.opIzq.tipo.tipo == Tipo_Dato.BIGINT or self.opIzq.tipo.tipo == Tipo_Dato.DECIMAL or self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC or self.opIzq.tipo.tipo == Tipo_Dato.REAL or self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opIzq.tipo.tipo == Tipo_Dato.MONEY) and (self.opDer.tipo.tipo == Tipo_Dato.SMALLINT or self.opDer.tipo.tipo == Tipo_Dato.INTEGER or self.opDer.tipo.tipo == Tipo_Dato.BIGINT or self.opDer.tipo.tipo == Tipo_Dato.DECIMAL or self.opDer.tipo.tipo == Tipo_Dato.NUMERIC or self.opDer.tipo.tipo == Tipo_Dato.REAL or self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opDer.tipo.tipo == Tipo_Dato.MONEY):
                return self.tipo
            elif (self.opIzq.tipo.tipo == Tipo_Dato.DATE or self.opIzq.tipo.tipo == Tipo_Dato.TIME or self.opIzq.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opIzq.tipo.tipo == Tipo_Dato.CHAR) and (self.opDer.tipo.tipo == Tipo_Dato.DATE or self.opDer.tipo.tipo == Tipo_Dato.TIME or self.opDer.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opDer.tipo.tipo == Tipo_Dato.CHAR):
                return self.tipo
            else:
                error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" <> "+self.opDer.tipo.toString(),self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        elif self.operador == "LIKE":
            if (self.opIzq.tipo.tipo == Tipo_Dato.VARCHAR or self.opIzq.tipo.tipo == Tipo_Dato.CHAR or self.opIzq.tipo.tipo == Tipo_Dato.CHARACTER or self.opIzq.tipo.tipo == Tipo_Dato.VARCHAR or self.opIzq.tipo.tipo == Tipo_Dato.VARYING or self.opIzq.tipo.tipo == Tipo_Dato.TEXT ) and (self.opDer.tipo.tipo == Tipo_Dato.VARCHAR or self.opDer.tipo.tipo == Tipo_Dato.CHAR or self.opDer.tipo.tipo == Tipo_Dato.CHARACTER or self.opDer.tipo.tipo == Tipo_Dato.VARCHAR or self.opDer.tipo.tipo == Tipo_Dato.VARYING or self.opDer.tipo.tipo == Tipo_Dato.TEXT):
                return self.tipo
            else:
                error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" = "+self.opDer.tipo.toString(),self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error                    
        elif self.operador == "NOT LIKE":
            if (self.opIzq.tipo.tipo == Tipo_Dato.VARCHAR or self.opIzq.tipo.tipo == Tipo_Dato.CHAR or self.opIzq.tipo.tipo == Tipo_Dato.CHARACTER or self.opIzq.tipo.tipo == Tipo_Dato.VARCHAR or self.opIzq.tipo.tipo == Tipo_Dato.VARYING or self.opIzq.tipo.tipo == Tipo_Dato.TEXT ) and (self.opDer.tipo.tipo == Tipo_Dato.VARCHAR or self.opDer.tipo.tipo == Tipo_Dato.CHAR or self.opDer.tipo.tipo == Tipo_Dato.CHARACTER or self.opDer.tipo.tipo == Tipo_Dato.VARCHAR or self.opDer.tipo.tipo == Tipo_Dato.VARYING or self.opDer.tipo.tipo == Tipo_Dato.TEXT):
                return self.tipo
            else:
                error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" = "+self.opDer.tipo.toString(),self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        elif self.operador == "IN":
            print("ENTRO A ESTE ELSE")
        elif self.operador == "NOT IN":
            print("ENTRO A ESTE ELSE")    
        else:
            error = Excepcion('42804',"Semántico","Operador desconocido.",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error

    def traducir(self, tabla, arbol):
        super().traducir(tabla,arbol)
       
        resultadoIzq = self.opIzq.traducir(tabla, arbol)
        resultadoDer = self.opDer.traducir(tabla, arbol)

        retorno.etiquetaTrue = tabla.getEtiqueta()
        retorno.etiquetaFalse = tabla.getEtiqueta()
        arbol.addc3d(f"if({resultadoIzq.temporalAnterior} {self.operador} {resultadoDer.temporalAnterior}):\n\t\tgoto .{retorno.etiquetaTrue}")
        arbol.addc3d(f"goto .{retorno.etiquetaFalse}")
        return retorno
    