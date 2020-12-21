from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Sql_select.SelectLista import Alias
import numpy as np

class Relacional(Instruccion):
    def __init__(self, opIzq, opDer, operador, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.BOOLEAN),linea,columna)
        self.opIzq = opIzq
        self.opDer = opDer
        self.operador = operador

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        # Si existe algún error en el operador izquierdo, retorno el error.
        resultadoIzq = self.opIzq.ejecutar(tabla, arbol)
        if isinstance(resultadoIzq, Excepcion):
            return resultadoIzq
        # Si existe algún error en el operador derecho, retorno el error.
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
                print(data)
                print(resultadoIzq)
                #obtener la posicion
                #posicion = arbol.devolverOrdenDeColumna(nombreTabla,nombreColumna)
                #res.append(posicion)
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
                print(data)
                print(resultadoIzq)
                #obtener la posicion
                #posicion = arbol.devolverOrdenDeColumna(nombreTabla,nombreColumna)
                #res.append(posicion)
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
                print(data)
                print(resultadoIzq)
                #obtener la posicion
                #posicion = arbol.devolverOrdenDeColumna(nombreTabla,nombreColumna)
                #res.append(posicion)
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
                print(data)
                print(resultadoIzq)
                #obtener la posicion
                #posicion = arbol.devolverOrdenDeColumna(nombreTabla,nombreColumna)
                #res.append(posicion)
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
                else:
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" <= "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
        elif self.operador == '=':
            if(arbol.getWhere() or arbol.getUpdate()):
                fila = []
                tabla = []
                tablaRes = []
                #devolver columna
                tabla = arbol.getTablaActual()
                #aqui vamos a dividir por columnas
                data = np.array((tabla))
                #recorrer columna y ver si es == la posicion
                print(data)
                print(resultadoIzq)
                #obtener la posicion
                #posicion = arbol.devolverOrdenDeColumna(nombreTabla,nombreColumna)
                #res.append(posicion)
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
                if(self.opIzq.tipo.tipo == Tipo_Dato.ID and (self.opDer.tipo.tipo == Tipo_Dato.CHAR or self.opDer.tipo.tipo == Tipo_Dato.INTEGER)):
                    # aqui va el procedimiento para devolver un id con su valor
                    
                    return Alias(resultadoIzq, resultadoDer)
                else:
                    # este es el error por el momento
                    error = Excepcion('42883', "Semántico", "el operador no existe "+self.opIzq.tipo.toString()+" = "+self.opDer.tipo.toString(), self.linea, self.columna )
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())

            else:
                if (self.opIzq.tipo.tipo == Tipo_Dato.SMALLINT or self.opIzq.tipo.tipo == Tipo_Dato.INTEGER or self.opIzq.tipo.tipo == Tipo_Dato.BIGINT or self.opIzq.tipo.tipo == Tipo_Dato.DECIMAL or self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC or self.opIzq.tipo.tipo == Tipo_Dato.REAL or self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opIzq.tipo.tipo == Tipo_Dato.MONEY) and (self.opDer.tipo.tipo == Tipo_Dato.SMALLINT or self.opDer.tipo.tipo == Tipo_Dato.INTEGER or self.opDer.tipo.tipo == Tipo_Dato.BIGINT or self.opDer.tipo.tipo == Tipo_Dato.DECIMAL or self.opDer.tipo.tipo == Tipo_Dato.NUMERIC or self.opDer.tipo.tipo == Tipo_Dato.REAL or self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opDer.tipo.tipo == Tipo_Dato.MONEY):
                    return resultadoIzq == resultadoDer
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
                print(data)
                print(resultadoIzq)
                #obtener la posicion
                #posicion = arbol.devolverOrdenDeColumna(nombreTabla,nombreColumna)
                #res.append(posicion)
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
                else:
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" <> "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
        else:
            error = Excepcion('42804',"Semántico","Operador desconocido.",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error