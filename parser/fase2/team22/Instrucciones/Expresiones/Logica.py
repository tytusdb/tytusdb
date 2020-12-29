from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion

class Logica(Instruccion):
    def __init__(self, opIzq, opDer, operador, strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.BOOLEAN),linea,columna,strGram)
        self.opIzq = opIzq
        self.opDer = opDer
        self.operador = operador

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        # Operación con dos operadores
        if(self.opDer != None):
            # Si existe algún error en el operador izquierdo, retorno el error.
            resultadoIzq = self.opIzq.ejecutar(tabla, arbol)
            if isinstance(resultadoIzq, Excepcion):
                return resultadoIzq
            # Si existe algún error en el operador derecho, retorno el error.
            resultadoDer = self.opDer.ejecutar(tabla, arbol)
            if isinstance(resultadoDer, Excepcion):
                return resultadoDer
            # Comprobamos el tipo de operador
            if self.operador == 'OR':
                if self.opIzq.tipo.tipo == Tipo_Dato.BOOLEAN and self.opDer.tipo.tipo == Tipo_Dato.BOOLEAN:
                    return resultadoIzq or resultadoDer
                else:
                    error = Excepcion('42804',"Semántico","El argumento de OR debe ser de tipo boolean",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            elif self.operador == 'AND':
                if self.opIzq.tipo.tipo == Tipo_Dato.BOOLEAN and self.opDer.tipo.tipo == Tipo_Dato.BOOLEAN:
                    return resultadoIzq and resultadoDer
                else:
                    error = Excepcion('42804',"Semántico","El argumento de AND debe ser de tipo boolean",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            else:
                error = Excepcion('42804',"Semántico","Operador desconocido.",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        # Operación unaria
        else:
            # Si existe algún error en el operador izquierdo, retorno el error.
            resultadoIzq = self.opIzq.ejecutar(tabla, arbol)
            if isinstance(resultadoIzq, Excepcion):
                return resultadoIzq
            if self.operador == 'NOT':
                if self.opIzq.tipo.tipo == Tipo_Dato.BOOLEAN:
                    return resultadoIzq and resultadoDer
                else:
                    error = Excepcion('42804',"Semántico","Tipo de datos incorrectos en la operación lógica not",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            else:
                error = Excepcion('42804',"Semántico","Operador desconocido.",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error