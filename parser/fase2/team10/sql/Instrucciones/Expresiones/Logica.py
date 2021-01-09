from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
 
from sql.Instrucciones.TablaSimbolos.Tabla import Tabla
from sql.Instrucciones.TablaSimbolos.Arbol import Arbol
from sql.Instrucciones.Excepcion import Excepcion

class Logica(Instruccion):
    def __init__(self, opIzq, opDer, operador, strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.BOOLEAN),linea,columna,strGram)
        self.opIzq = opIzq
        self.opDer = opDer
        self.operador = operador

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        # Operación con dos operadores
        resultadoDer=""
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
    
    def analizar(self, tabla, arbol):
        super().analizar(tabla,arbol)
        # Operación con dos operadores
        resultadoDer=""
        if(self.opDer != None):
            # Si existe algún error en el operador izquierdo, retorno el error.
            resultadoIzq = self.opIzq.analizar(tabla, arbol)
            if isinstance(resultadoIzq, Excepcion):
                return resultadoIzq
            # Si existe algún error en el operador derecho, retorno el error.
            resultadoDer = self.opDer.analizar(tabla, arbol)
            if isinstance(resultadoDer, Excepcion):
                return resultadoDer
            # Comprobamos el tipo de operador
            if self.operador == 'OR':
                if self.opIzq.tipo.tipo == Tipo_Dato.BOOLEAN and self.opDer.tipo.tipo == Tipo_Dato.BOOLEAN:
                    return self.tipo
                else:
                    error = Excepcion('42804',"Semántico","El argumento de OR debe ser de tipo boolean",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            elif self.operador == 'AND':
                if self.opIzq.tipo.tipo == Tipo_Dato.BOOLEAN and self.opDer.tipo.tipo == Tipo_Dato.BOOLEAN:
                    return self.tipo
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
            resultadoIzq = self.opIzq.analizar(tabla, arbol)
            if isinstance(resultadoIzq, Excepcion):
                return resultadoIzq
            if self.operador == 'NOT':
                if self.opIzq.tipo.tipo == Tipo_Dato.BOOLEAN:
                    return self.tipo
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
    
    def traducir(self, tabla: Tabla, arbol: Arbol):
        super().traducir(tabla,arbol)
       
        resultadoIzq = self.opIzq.traducir(tabla,arbol)
        if self.operador == 'AND':
            if resultadoIzq.temporalAnterior == "0":
                etiqueta1 = tabla.getEtiqueta()
                arbol.addc3d(f"goto .{etiqueta1}")
                resultadoDer = self.opDer.traducir(tabla,arbol)
                if resultadoDer.temporalAnterior == "0":
                    # False and False
                    etiqueta2 = tabla.getEtiqueta()
                    arbol.addc3d(f"goto .{etiqueta2}")
                    retorno.etiquetaTrue = ''
                    retorno.etiquetaFalse = f"{etiqueta1},{etiqueta2}"
                elif resultadoDer.temporalAnterior == "1":
                    # False and True
                    etiqueta2 = tabla.getEtiqueta()
                    arbol.addc3d(f"goto .{etiqueta2}")
                    arbol.addc3d(f"label .{etiqueta2}")
                    retorno.etiquetaTrue = ""
                    retorno.etiquetaFalse = f"{etiqueta1}"
                else:
                    # False and Operación Relacional
                    retorno.etiquetaTrue = resultadoDer.etiquetaTrue
                    retorno.etiquetaFalse = f"{etiqueta1},{resultadoDer.etiquetaFalse}"
                return retorno
            elif resultadoIzq.temporalAnterior == "1":
                etiqueta1 = tabla.getEtiqueta()
                arbol.addc3d(f"goto .{etiqueta1}")
                arbol.addc3d(f"label .{etiqueta1}")
                resultadoDer = self.opDer.traducir(tabla,arbol)
                if resultadoDer.temporalAnterior == "0":
                    # True and False
                    etiqueta2 = tabla.getEtiqueta()
                    arbol.addc3d(f"goto .{etiqueta2}")
                    retorno.etiquetaTrue = ''
                    retorno.etiquetaFalse = f"{etiqueta2}"
                elif resultadoDer.temporalAnterior == "1":
                    # True and True
                    etiqueta2 = tabla.getEtiqueta()
                    arbol.addc3d(f"goto .{etiqueta2}")
                    retorno.etiquetaTrue = f"{etiqueta2}"
                    retorno.etiquetaFalse = ""
                else:
                    # True and Operación Relacional
                    retorno.etiquetaTrue = resultadoDer.etiquetaTrue
                    retorno.etiquetaFalse = resultadoDer.etiquetaFalse
                return retorno
            
            retorno.imprimirEtiquetDestino(arbol, resultadoIzq.etiquetaTrue)
            resultadoDer = self.opDer.traducir(tabla, arbol)
            if resultadoDer.temporalAnterior == "0":
                # Operación Relacional and False
                etiqueta1 = tabla.getEtiqueta()
                arbol.addc3d(f"goto .{etiqueta1}")
                retorno.etiquetaTrue = ''
                retorno.etiquetaFalse = f"{resultadoIzq.etiquetaFalse},{etiqueta1}"
                return retorno
            elif resultadoDer.temporalAnterior == "1":
                # Operación Relacional and True
                etiqueta1 = tabla.getEtiqueta()
                arbol.addc3d(f"goto .{etiqueta1}")
                retorno.etiquetaTrue = f"{etiqueta1}"
                retorno.etiquetaFalse = f"{resultadoIzq.etiquetaFalse}"
                return retorno
            # Operación Relacional and Operación Relacional
            retorno.etiquetaTrue = resultadoDer.etiquetaTrue
            retorno.etiquetaFalse = f"{resultadoIzq.etiquetaFalse},{resultadoDer.etiquetaFalse}"
            return retorno
        elif self.operador == 'OR':
            if resultadoIzq.temporalAnterior == "0":
                etiqueta1 = tabla.getEtiqueta()
                arbol.addc3d(f"goto .{etiqueta1}")
                arbol.addc3d(f"label .{etiqueta1}")
                resultadoDer = self.opDer.traducir(tabla,arbol)
                if resultadoDer.temporalAnterior == "0":
                    # False or False
                    etiqueta2 = tabla.getEtiqueta()
                    arbol.addc3d(f"goto .{etiqueta2}")
                    retorno.etiquetaTrue = ""
                    retorno.etiquetaFalse = etiqueta2
                elif resultadoDer.temporalAnterior == "1":
                    # False or True
                    etiqueta2 = tabla.getEtiqueta()
                    arbol.addc3d(f"goto .{etiqueta2}")
                    retorno.etiquetaTrue = etiqueta2
                    retorno.etiquetaFalse = ""
                else:
                    # False or Operación Relacional
                    retorno.etiquetaTrue = resultadoDer.etiquetaTrue
                    retorno.etiquetaFalse = resultadoDer.etiquetaFalse
                return retorno
            elif resultadoIzq.temporalAnterior == "1":
                etiqueta1 = tabla.getEtiqueta()
                arbol.addc3d(f"goto .{etiqueta1}")
                resultadoDer = self.opDer.traducir(tabla, arbol)
                if resultadoDer.temporalAnterior == "0":
                    # True or False
                    etiqueta2 = tabla.getEtiqueta()
                    arbol.addc3d(f"goto .{etiqueta2}")
                    retorno.etiquetaTrue = etiqueta1
                    retorno.etiquetaFalse = etiqueta2
                elif resultadoDer.temporalAnterior == "1":
                    # True or True
                    etiqueta2 = tabla.getEtiqueta()
                    arbol.addc3d(f"goto .{etiqueta2}")
                    retorno.etiquetaTrue = f"{etiqueta1},{etiqueta2}"
                    retorno.etiquetaFalse = ""
                else:
                    # True or Operación Relacional
                    retorno.etiquetaTrue = f"{etiqueta1},{resultadoDer.etiquetaTrue}"
                    retorno.etiquetaFalse = resultadoDer.etiquetaFalse
                return retorno
            retorno.imprimirEtiquetDestino(arbol, resultadoIzq.etiquetaFalse)
            resultadoDer = self.opDer.traducir(tabla, arbol)
            if resultadoDer.temporalAnterior == "0":
                # Operación Relacional or False
                etiqueta1 = tabla.getEtiqueta()
                arbol.addc3d(f"goto .{etiqueta1}")
                retorno.etiquetaTrue = resultadoIzq.etiquetaTrue
                retorno.etiquetaFalse = etiqueta1
                return retorno
            elif resultadoDer.temporalAnterior == "1":
                # Operación Relacional or True
                etiqueta1 = tabla.getEtiqueta()
                arbol.addc3d(f"goto .{etiqueta1}")
                retorno.etiquetaTrue = f"{resultadoIzq.etiquetaTrue},{etiqueta1}"
                retorno.etiquetaFalse = ""
                return retorno
            # Operación Relacional or Operación Relacional
            retorno.etiquetaTrue = f"{resultadoIzq.etiquetaTrue},{resultadoDer.etiquetaTrue}"
            retorno.etiquetaFalse = resultadoDer.etiquetaFalse
            return retorno
        elif self.operador == 'NOT':
            if resultadoIzq.temporalAnterior == "0":
                # False
                retorno.temporalAnterior = "1"
            elif resultadoIzq.temporalAnterior == "1":
                # True
                retorno.temporalAnterior = "0"
            else:
                # Operación Relacional
                retorno.etiquetaTrue = resultadoIzq.etiquetaFalse
                retorno.etiquetaFalse = resultadoIzq.etiquetaTrue
            return retorno

        
