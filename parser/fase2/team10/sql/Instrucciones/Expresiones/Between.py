from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from sql.Instrucciones.Excepcion import Excepcion
from sql.Instrucciones.Sql_select.SelectLista import Alias
import time
import numpy as np

class Between(Instruccion):
    def __init__(self, opIzq, opDer, opDer2, operador, strGram,linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.BOOLEAN),linea,columna,strGram)
        self.opIzq = opIzq
        self.opDer = opDer
        self.opDer2 = opDer2
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
            resultadoDer = self.opDer.ejecutar(tabla, arbol)
        if isinstance(resultadoDer, Excepcion):
            return resultadoDer

        # Si existe algún error en el operador derecho, retorno el error.
        if isinstance(self.opDer2, Alias):
            nombreColumna = self.opDer2.expresion
            nombreTabla = tabla.getVariable(self.opDer2.id)
            #obtener la posicion
            posicion = arbol.devolverOrdenDeColumna(nombreTabla.valor,nombreColumna)
            resultadoDer2 = posicion
        else:
            resultadoDer2 = self.opDer2.ejecutar(tabla, arbol)
        if isinstance(resultadoDer2, Excepcion):
            return resultadoDer2
        # Comprobamos el tipo de operador

        if arbol.getWhere():
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

                if self.operador == "NOT":

                    if not ((variableComp >= resultadoDer) and (variableComp <= resultadoDer2)):
                        #agregar a filas
                        fila.append(x)
                else:
                    if (variableComp >= resultadoDer) and (variableComp <= resultadoDer2):
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
                if self.operador == "NOT":
                    return not ((resultadoIzq >= resultadoDer) and (resultadoIzq <= resultadoDer2))
                else:
                    return (resultadoIzq >= resultadoDer) and (resultadoIzq <= resultadoDer2)

            elif (self.opIzq.tipo.tipo == Tipo_Dato.DATE or self.opIzq.tipo.tipo == Tipo_Dato.TIME or self.opIzq.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opIzq.tipo.tipo == Tipo_Dato.CHAR) and (self.opDer.tipo.tipo == Tipo_Dato.DATE or self.opDer.tipo.tipo == Tipo_Dato.TIME or self.opDer.tipo.tipo == Tipo_Dato.TIMESTAMP or self.opDer.tipo.tipo == Tipo_Dato.CHAR):
                formats = ("%d-%m-%Y", "%Y-%m-%d","%d-%M-%Y", "%Y-%M-%d","%Y-%b-%d", "%d-%b-%Y")
                val1 = None
                val2 = None
                val3 = None
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
                
                for fmt in formats:
                    valid_date=""
                    try:
                        valid_date = time.strptime(resultadoDer2, fmt)
                        if isinstance(valid_date, time.struct_time):
                            val3 = time.strftime('%Y-%m-%d',valid_date)
                    except ValueError as e:
                        pass

                if self.operador == "NOT" :
                    if val1 != None and val2 != None and val3 != None:
                        return not((resultadoIzq >= resultadoDer) and (resultadoIzq <= resultadoDer2)) 
                else:
                    if val1 != None and val2 != None and val3 != None:
                        return (resultadoIzq >= resultadoDer) and (resultadoIzq <= resultadoDer2)
                 
                error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" > "+self.opDer.tipo.toString(),self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
            else:
                error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" > "+self.opDer.tipo.toString(),self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
