from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion

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
            if self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                return resultadoIzq > resultadoDer
            else:
                error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" > "+self.opDer.tipo.toString(),self.linea,self.columna)
                arbol.excepciones.append(error)
                return error
        elif self.operador == '<':
            if self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                return resultadoIzq < resultadoDer
            else:
                error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" < "+self.opDer.tipo.toString(),self.linea,self.columna)
                arbol.excepciones.append(error)
                return error
        elif self.operador == '>=':
            if self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                return resultadoIzq >= resultadoDer
            else:
                error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" >= "+self.opDer.tipo.toString(),self.linea,self.columna)
                arbol.excepciones.append(error)
                return error
        elif self.operador == '<=':
            if self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                return resultadoIzq <= resultadoDer
            else:
                error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" <= "+self.opDer.tipo.toString(),self.linea,self.columna)
                arbol.excepciones.append(error)
                return error
        elif self.operador == '=':
            if self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                return resultadoIzq == resultadoDer
            else:
                error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" = "+self.opDer.tipo.toString(),self.linea,self.columna)
                arbol.excepciones.append(error)
                return error
        elif self.operador == '<>':
            if self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                return resultadoIzq != resultadoDer
            else:
                error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" <> "+self.opDer.tipo.toString(),self.linea,self.columna)
                arbol.excepciones.append(error)
                return error
        else:
            error = Excepcion('42804',"Semántico","Operador desconocido.",self.linea,self.columna)
            arbol.excepciones.append(error)
            return error