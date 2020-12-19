from enum import Enum
from reporteErrores.errorReport import ErrorReport # EN EL AMBITO MAS EXTERIOR SE INGRESAN A LA LISTA , EN ESTAS SUB CLASES SOLO SE SUBE EL ERROR
# Enumeraciones para identificar expresiones que comparten clase

class TIPO_DE_DATO(Enum):
    ENTERO = 1
    DECIMAL = 2
    CADENA = 3
    TIMESTAMP = 4
    BOOLEANO = 5
    NULL = 6

class OPERACION_ARITMETICA(Enum):
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDO = 4
    MODULO = 5
    EXPONENTE = 6


class OPERACION_RELACIONAL(Enum):
    MAYORIGUAL  = 1
    MENORIGUAL  = 2
    MAYOR       = 3
    MENOR       = 4
    IGUAL       = 5
    DESIGUAL    = 6


class OPERACION_LOGICA(Enum):
    AND = 1
    OR = 2

class OPERACION_UNARIA_IS(Enum):
    IS_TRUE = "is true"
    IS_FALSE = "is false"
    IS_NOT_FALSE = "is not false"
    IS_NOT_TRUE = "is not true"
    IS_NULL = "is null"
    IS_NOT_NULL = "is not null"

class OPERACION_BINARIA_IS(Enum):
    IS_DISTINCT_FROM = "is distinct from"
    IS_NOT_DISTINCT_FROM = "is not distinct from"

# ------------------------ EXPRESIONES ----------------------------
# ------EXPRESIONES NUMERICAS

# Clase de expresion númerica (Abstracta)
class Expresion:
    def dibujar(self):
        pass

    def ejecutar(self, ts):
        pass

# Clase de expresión aritmética


class ExpresionAritmetica(Expresion):
    def __init__(self, exp1, exp2, operador, linea):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
        self.linea = linea

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"" + self.operador + "\" ];"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp1)) + ";"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp2)) + ";\n"

        nodo += self.exp1.dibujar()
        nodo += self.exp2.dibujar()

        return nodo
    def ejecutar(self, ts):
        expizq = self.exp1.ejecutar(ts)
        expder = self.exp2.ejecutar(ts)
        # por si se quiere operar un error con una expresion buena ,  retorna de una el error
        if isinstance(expizq , ErrorReport):
            return expizq
        if isinstance(expder , ErrorReport):
            return expder

        if self.operador == OPERACION_ARITMETICA.MAS:
            if expizq.tipo == TIPO_DE_DATO.ENTERO and expder.tipo == TIPO_DE_DATO.ENTERO:
                return ExpresionNumero(expizq.val + expder.val, TIPO_DE_DATO.ENTERO,self.linea) 
            elif expizq.tipo == TIPO_DE_DATO.ENTERO and expder.tipo == TIPO_DE_DATO.DECIMAL:
                return ExpresionNumero(expizq.val + expder.val, TIPO_DE_DATO.DECIMAL,self.linea) 
            elif expizq.tipo == TIPO_DE_DATO.DECIMAL and expder.tipo == TIPO_DE_DATO.ENTERO:
                return ExpresionNumero(expizq.val + expder.val, TIPO_DE_DATO.DECIMAL,self.linea) 
            elif expizq.tipo == TIPO_DE_DATO.DECIMAL and expder.tipo == TIPO_DE_DATO.DECIMAL:
                return ExpresionNumero(expizq.val + expder.val, TIPO_DE_DATO.DECIMAL,self.linea)
            else:
                return 0
        elif self.operador == OPERACION_ARITMETICA.MENOS:
            if expizq.tipo == TIPO_DE_DATO.ENTERO and expder.tipo == TIPO_DE_DATO.ENTERO:
                return ExpresionNumero(expizq.val - expder.val, TIPO_DE_DATO.ENTERO,self.linea) 
            elif expizq.tipo == TIPO_DE_DATO.ENTERO and expder.tipo == TIPO_DE_DATO.DECIMAL:
                return ExpresionNumero(expizq.val - expder.val, TIPO_DE_DATO.DECIMAL,self.linea) 
            elif expizq.tipo == TIPO_DE_DATO.DECIMAL and expder.tipo == TIPO_DE_DATO.ENTERO:
                return ExpresionNumero(expizq.val - expder.val, TIPO_DE_DATO.DECIMAL,self.linea) 
            elif expizq.tipo == TIPO_DE_DATO.DECIMAL and expder.tipo == TIPO_DE_DATO.DECIMAL:
                return ExpresionNumero(expizq.val - expder.val, TIPO_DE_DATO.DECIMAL,self.linea)
            else:
               
                return 0
        elif self.operador == OPERACION_ARITMETICA.POR:
            if expizq.tipo == TIPO_DE_DATO.ENTERO and expder.tipo == TIPO_DE_DATO.ENTERO:
                return ExpresionNumero(expizq.val * expder.val, TIPO_DE_DATO.ENTERO,self.linea) 
            elif expizq.tipo == TIPO_DE_DATO.ENTERO and expder.tipo == TIPO_DE_DATO.DECIMAL:
                return ExpresionNumero(expizq.val * expder.val, TIPO_DE_DATO.DECIMAL,self.linea) 
            elif expizq.tipo == TIPO_DE_DATO.DECIMAL and expder.tipo == TIPO_DE_DATO.ENTERO:
                return ExpresionNumero(expizq.val * expder.val, TIPO_DE_DATO.DECIMAL,self.linea) 
            elif expizq.tipo == TIPO_DE_DATO.DECIMAL and expder.tipo == TIPO_DE_DATO.DECIMAL:
                return ExpresionNumero(expizq.val * expder.val, TIPO_DE_DATO.DECIMAL,self.linea)
            else:
                
                return 0
        elif self.operador == OPERACION_ARITMETICA.DIVIDO:
            if expder.val != 0:
                if expizq.tipo == TIPO_DE_DATO.ENTERO and expder.tipo == TIPO_DE_DATO.ENTERO:
                    return ExpresionNumero(expizq.val / expder.val, TIPO_DE_DATO.ENTERO,self.linea) 
                elif expizq.tipo == TIPO_DE_DATO.ENTERO and expder.tipo == TIPO_DE_DATO.DECIMAL:
                    return ExpresionNumero(expizq.val / expder.val, TIPO_DE_DATO.DECIMAL,self.linea) 
                elif expizq.tipo == TIPO_DE_DATO.DECIMAL and expder.tipo == TIPO_DE_DATO.ENTERO:
                    return ExpresionNumero(expizq.val / expder.val, TIPO_DE_DATO.DECIMAL,self.linea) 
                elif expizq.tipo == TIPO_DE_DATO.DECIMAL and expder.tipo == TIPO_DE_DATO.DECIMAL:
                    return ExpresionNumero(expizq.val / expder.val, TIPO_DE_DATO.DECIMAL,self.linea)
                else:
                   
                    return 0
            else:
                return ErrorReport('semantico', 'No se puede dividir entre 0' ,self.linea)
        elif self.operador == OPERACION_ARITMETICA.MODULO:
            if expizq.tipo == TIPO_DE_DATO.ENTERO and expder.tipo == TIPO_DE_DATO.ENTERO:
                return ExpresionNumero(expizq.val % expder.val, TIPO_DE_DATO.ENTERO,self.linea) 
            elif expizq.tipo == TIPO_DE_DATO.ENTERO and expder.tipo == TIPO_DE_DATO.DECIMAL:
                return ExpresionNumero(expizq.val % expder.val, TIPO_DE_DATO.DECIMAL,self.linea) 
            elif expizq.tipo == TIPO_DE_DATO.DECIMAL and expder.tipo == TIPO_DE_DATO.ENTERO:
                return ExpresionNumero(expizq.val % expder.val, TIPO_DE_DATO.DECIMAL,self.linea) 
            elif expizq.tipo == TIPO_DE_DATO.DECIMAL and expder.tipo == TIPO_DE_DATO.DECIMAL:
                return ExpresionNumero(expizq.val % expder.val, TIPO_DE_DATO.DECIMAL,self.linea)
            else:
                
                return 0
        elif self.operador == OPERACION_ARITMETICA.EXPONENTE:
            if expizq.tipo == TIPO_DE_DATO.ENTERO and expder.tipo == TIPO_DE_DATO.ENTERO:
                return ExpresionNumero(expizq.val ** expder.val, TIPO_DE_DATO.ENTERO,self.linea) 
            elif expizq.tipo == TIPO_DE_DATO.ENTERO and expder.tipo == TIPO_DE_DATO.DECIMAL:
                return ExpresionNumero(expizq.val ** expder.val, TIPO_DE_DATO.DECIMAL,self.linea) 
            elif expizq.tipo == TIPO_DE_DATO.DECIMAL and expder.tipo == TIPO_DE_DATO.ENTERO:
                return ExpresionNumero(int(expizq.val) ** expder.val, TIPO_DE_DATO.ENTERO,self.linea) 
            elif expizq.tipo == TIPO_DE_DATO.DECIMAL and expder.tipo == TIPO_DE_DATO.DECIMAL:
                return ExpresionNumero(expizq.val ** expder.val, TIPO_DE_DATO.DECIMAL,self.linea)
            else:
                
                return 0

# Clase de expresión negativa


class ExpresionNegativa(Expresion):
    def __init__(self, exp, linea):
        self.exp = exp
        self.linea = linea
    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"-\" ];"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp)) + ";\n"

        nodo += self.exp.dibujar()

        return nodo
    def ejecutar(self, ts):
        unario = self.exp.ejecutar(ts)
        return ExpresionNumero(-unario.val, unario.tipo, self.linea)


class ExpresionPositiva(Expresion):
    def __init__(self, exp, linea):
        self.exp = exp
        self.linea = linea

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"+\" ];"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp)) + ";\n"

        nodo += self.exp.dibujar()

        return nodo

    def ejecutar(self, ts):
        unario = self.exp.ejecutar(ts)
        return ExpresionNumero(unario.val, unario.tipo, self.linea)

# Clase de expresión numero


class ExpresionNumero(Expresion):
    def __init__(self, val, tipo, linea):
        self.val = val
        self.tipo = tipo
        self.linea = linea

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"" + str(self.val) + "\" ];\n"

        return nodo
    
    def ejecutar(self, ts):
        return self
        

class ExpresionID(Expresion):
    def __init__(self, val , linea , tabla = None):
        self.val = val
        self.linea = linea
        self.tabla = tabla

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"" + str(self.val) + "\" ];\n"

        return nodo
    def ejecutar(self ,ts):
        return self





# ------EXPRESIONES LOGICAS
# Expresión binaria de comparacion
class ExpresionComparacion(Expresion):
    def __init__(self, exp1, exp2, operador, linea):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
        self.linea = linea

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"" + self.operador + "\" ];"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp1)) + ";"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp2)) + ";\n"

        nodo += self.exp1.dibujar()
        nodo += self.exp2.dibujar()

        return nodo
    def ejecutar(self, ts):
        izq = self.exp1.ejecutar(ts)
        der = self.exp2.ejecutar(ts)
        
        if isinstance(izq , ErrorReport):
            return izq
        if isinstance(der , ErrorReport):
            return der
        # como expresionNumero abarca tanto decimales como enteros 
        if isinstance(izq,ExpresionNumero) and isinstance(izq,ExpresionNumero):
            if self.operador == OPERACION_RELACIONAL.DESIGUAL:
                return ExpresionBooleano(izq.val != der.val, self.linea)
            elif self.operador == OPERACION_RELACIONAL.IGUAL:
                return ExpresionBooleano(izq.val == der.val, self.linea)
            elif self.operador == OPERACION_RELACIONAL.MAYOR:
                return ExpresionBooleano(izq.val > der.val, self.linea)
            elif self.operador == OPERACION_RELACIONAL.MAYORIGUAL:
                return ExpresionBooleano(izq.val >= der.val, self.linea)
            elif self.operador == OPERACION_RELACIONAL.MENOR:
                return ExpresionBooleano(izq.val < der.val, self.linea)
            elif self.operador == OPERACION_RELACIONAL.MENORIGUAL:
                return ExpresionBooleano(izq.val <= der.val, self.linea)
        #elif isinstance() comparar cadenas  y ids 
        else:
            return ErrorReport('semantico', 'Error de tipos , en Operacion Relacional' ,self.linea)


class ExpresionLogica(Expresion):
    def __init__(self, exp1, exp2, operador, linea):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
        self.linea  = linea

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"" + self.operador + "\" ];"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp1)) + ";"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp2)) + ";\n"

        nodo += self.exp1.dibujar()
        nodo += self.exp2.dibujar()

        return nodo

    def ejecutar(self, ts):
        izq = self.exp1.ejecutar(ts)
        der = self.exp2.ejecutar(ts)
        # por si se quiere operar un error con una expresion buena ,  retorna de una el error
        if isinstance(izq , ErrorReport):
            return izq
        if isinstance(der , ErrorReport):
            return der
        
        if izq.tipo == TIPO_DE_DATO.BOOLEANO and der.tipo == TIPO_DE_DATO.BOOLEANO:
            if self.operador == OPERACION_LOGICA.AND:
                return ExpresionBooleano(izq.val and der.val,self.linea)
            elif self.operador == OPERACION_LOGICA.OR:
                return ExpresionBooleano(izq.val or der.val, self.linea)
        else:
            return ErrorReport('semantico', 'Error , se esta operando con valores No booleanos' ,self.linea)

# Expresion negada
class ExpresionNegada(Expresion):
    def __init__(self, exp):
        self.exp = exp
        self.tipo = TIPO_DE_DATO.BOOLEANO

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"NOT\" ];"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp)) + ";\n"

        nodo += self.exp.dibujar()

        return nodo
    def ejecutar(self, ts):
        expu = self.exp.ejecutar(ts)
        if expu.tipo == TIPO_DE_DATO.BOOLEANO:
            return ExpresionBooleano(not expu.val, expu.linea)
        else:
            print('Error semántico, operador no admitido para not', self.exp.tipo)

# Expresión booleana (Valor puro)
class ExpresionBooleano(Expresion):
    def __init__(self, val, linea):
        self.val = val
        self.tipo = TIPO_DE_DATO.BOOLEANO
        self.linea = linea

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"" + str(self.val) + "\" ];\n"

        return nodo
    
    def ejecutar(self, ts):
        return self

# Expresión Between: Contempla tanto al Between como al Between Symmetric, asi como las versiones negadas


class ExpresionBetween(Expresion):
    def __init__(self, evaluado, limiteInferior, limiteSuperior, invertido=False, simetria=False):
        self.evaluado = evaluado
        self.limiteInferior = limiteInferior
        self.limiteSuperior = limiteSuperior
        self.invertido = invertido
        self.simetria = simetria

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador

        if self.simetria:
            if self.invertido:
                nodo += "[ label = \"NOT BETWEEN SYMMETRIC\" ];"
            else:
                nodo += "[ label = \"BETWEEN SYMMETRIC\" ];"
        else:
            if self.invertido:
                nodo += "[ label = \"NOT BETWEEN\" ];"
            else:
                nodo += "[ label = \"BETWEEN\" ];"

        nodo += "\nAND" + identificador + "[ label = \"AND\" ];"
        nodo += "\n" + identificador + " -> AND" + identificador + ";"

        nodo += "\n" + identificador + " -> " + str(hash(self.evaluado)) + ";"
        nodo += self.evaluado.dibujar()

        nodo += "\nAND" + identificador + " -> " + \
            str(hash(self.limiteInferior)) + ";"
        nodo += self.limiteInferior.dibujar()

        nodo += "\nAND" + identificador + " -> " + \
            str(hash(self.limiteSuperior)) + ";"
        nodo += self.limiteSuperior.dibujar()

        return nodo

# Expresión is: Contempla todas su variaciones
class ExpresionIs(Expresion):
    def __init__(self, condicion, tipo, invertido=False, subcondicion=None):
        self.condicion = condicion
        self.invertido = invertido
        self.subcondicion = subcondicion

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador

        return nodo

# ------EXPRESIONES DE CADENAS
class ExpresionCadena(Expresion):
    def __init__(self, valor , tipo, linea):
        self.tipo = tipo 
        self.val = str(valor)
        self.linea = linea

    def dibujar(self):
        identificador = str(hash(self))
        temp = str(self.val)

        temp = temp.replace("\"", "")
        temp = temp.replace("\'", "")

        nodo = "\n" + identificador + "[ label =\"" + temp + "\" ];\n"

        return nodo
    def ejecutar(self,ts):
        return self

class ExpresionUnariaIs(Expresion):
    def __init__(self, exp, linea, tipo):
        self.exp = exp
        self.linea = linea
        self.tipo = tipo
    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"self.tipo.value\" ];"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp)) + ";\n"

        nodo += self.exp.dibujar()

        return nodo
    def ejecutar(self, ts):
        unario = self.exp.ejecutar(ts)
        if unario.tipo == TIPO_DE_DATO.BOOLEANO:
            if self.tipo == OPERACION_UNARIA_IS.IS_TRUE:
                return ExpresionBooleano(unario.val == True, self.linea) 
            elif self.tipo == OPERACION_UNARIA_IS.IS_FALSE:
                return ExpresionBooleano(unario.val == False, self.linea) 
            elif self.tipo == OPERACION_UNARIA_IS.IS_NOT_FALSE:
                return ExpresionBooleano(unario.val == True, self.linea) 
            elif self.tipo == OPERACION_UNARIA_IS.IS_NOT_TRUE:
                return ExpresionBooleano(unario.val == False, self.linea) 
        else:
            if self.tipo == OPERACION_UNARIA_IS.IS_NULL:
                return ExpresionBooleano(unario.val == None, self.linea)
            elif self.tipo == OPERACION_UNARIA_IS.IS_NOT_NULL:
                return ExpresionBooleano(unario.val != None, self.linea)

class ExpresionBinariaIs(Expresion):
    def __init__(self, exp1, exp2, operador, linea):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
        self.linea = linea

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"" + self.operador.value + "\" ];"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp1)) + ";"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp2)) + ";\n"

        nodo += self.exp1.dibujar()
        nodo += self.exp2.dibujar()

        return nodo
    def ejecutar(self, ts):
        izq = self.exp1.ejecutar(ts)
        der = self.exp2.ejecutar(ts)
    
        # como expresionNumero abarca tanto decimales como enteros 
        if isinstance(izq,ExpresionNumero) and isinstance(izq,ExpresionNumero):
            if self.operador == OPERACION_BINARIA_IS.IS_NOT_DISTINCT_FROM:
                return ExpresionBooleano(izq.val == der.val, self.linea)
            elif self.operador == OPERACION_BINARIA_IS.IS_DISTINCT_FROM:
                return ExpresionBooleano(izq.val != der.val, self.linea)
        #elif isinstance() comparar cadenas  y ids 
        else:
            return ErrorReport('semantico', 'Error de tipos , en Operacion Relacional' ,self.linea)
