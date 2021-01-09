from enum import Enum
from reporteErrores.errorReport import ErrorReport # EN EL AMBITO MAS EXTERIOR SE INGRESAN A LA LISTA , EN ESTAS SUB CLASES SOLO SE SUBE EL ERROR
# Enumeraciones para identificar expresiones que comparten clase
import sqlErrors
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

class BETWEEN(Enum):
    BETWEEN = "between"
    NOT_BETWEEN = "not between"
    BETWEEN_SYMMETRIC = "between symmetric"
    NOT_BETWEEN_SYMMETRIC = "not between symmetric"

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

        nodo = "\n" + identificador + "[ label =\"" + str(self.operador) + "\" ];"
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
            
    def evaluacionCheck(self ,ts) -> int: # 0 = booleano , 1 = entero , 2  = decimal , 3 = cadena , 4 = cadenaDate , 5 = id , 6 = Error  
        izq = self.exp1.evaluacionCheck(ts)
        der = self.exp2.evaluacionCheck(ts)
        if (izq != 1) or (der != 1):
            return 5
        return 1  # no importa que operacion realice va regresar un numero
    def getExpresionToString(self) -> str:
        izq  = self.exp1.getExpresionToString()
        der  = self.exp2.getExpresionToString()
        if isinstance(izq , ErrorReport):
            return izq
        if isinstance(der , ErrorReport):
            return der
        op = ''
        if self.operador == OPERACION_ARITMETICA.MAS:
            op = '+' # si fuera != le pone <>
        elif self.operador == OPERACION_ARITMETICA.MENOS:
            op = '-'
        elif self.operador == OPERACION_ARITMETICA.POR:
            op = '*'
        elif self.operador == OPERACION_ARITMETICA.DIVIDO:
            op = '/'
        elif self.operador == OPERACION_ARITMETICA.MODULO:
            op = '%'
        elif self.operador == OPERACION_ARITMETICA.EXPONENTE:
            op = '^'
        else:
            op = 'DESCONOCIDO'
        return str(izq + f' { op } '+der)
    
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
        if isinstance(unario , ErrorReport):
            return unario # si ya viene un error solo lo retorna
        if not (isinstance(unario , ExpresionNumero)):
            return ErrorReport('semantico', 'Error , Tipe Invalido UNARIO "-"' ,self.linea)
        try:
            return ExpresionNumero(-unario.val, unario.tipo, self.linea)          
        except:
            return ErrorReport('semantico', 'Error , Tipe Invalido UNARIO "-"' ,self.linea)  
        
    def evaluacionCheck(self ,ts) -> int: # 0 = booleano , 1 = entero , 2  = decimal , 3 = cadena , 4 = cadenaDate , 5 = id , 6 = Error  
        value = self.exp.evaluacionCheck(ts)
        if value != 1 and value != 2:
            return 5
        return value
    def getExpresionToString(self) -> str:
        sint = self.exp.getExpresionToString()
        if isinstance(sint , ErrorReport):
            return sint
        else:
            return str('-' + sint)

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
        if isinstance(unario , ErrorReport):
            return unario # si ya viene un error solo lo retorna
        if not (isinstance(unario , ExpresionNumero)):
            return ErrorReport('semantico', 'Error , Tipe Invalido UNARIO "+"' ,self.linea)
        try:
            return ExpresionNumero(unario.val, unario.tipo, self.linea)                       
        except:
            return ErrorReport('semantico', 'Error , Tipe Invalido UNARIO "+"' ,self.linea)
    
    def evaluacionCheck(self ,ts) -> int:
        value = self.exp.evaluacionCheck(ts)
        if value != 1 and value != 2: # o si ya fuera error lo sube
            return 5
        return value
    def getExpresionToString(self) -> str:
        sint = self.exp.getExpresionToString()
        if isinstance(sint , ErrorReport):
            return sint
        return str('+' + sint)
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
    
    def evaluacionCheck(self ,ts) -> int: # 0 = booleano , 1 = numero , 2 = cadena , 3 = cadenaDate , 4 = id , 5 = Error  , 6 = error Por formato de fecha
        return 1
    def getExpresionToString(self) -> str:
        return str(self.val)
        

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
        if isinstance(ts , TuplaCompleta):# PARA VALIDACIONES DE WHERE Y SELECT 
            valorYtipo = ts.getValue(self.val)
            if valorYtipo == None:
                return ErrorReport('Semantico','no se encontro esa columna', self.linea)
            else:
                if valorYtipo['tipo'] == 'SMALLINT' \
                or valorYtipo['tipo'] == 'BIGINT' \
                or valorYtipo['tipo'] == 'INTEGER':
                    return ExpresionNumero(valorYtipo['val'], TIPO_DE_DATO.ENTERO, self.linea)
                elif valorYtipo['tipo'] == 'DECIMAL' \
                or valorYtipo['tipo'] == 'NUMERIC' \
                or valorYtipo['tipo'] == 'REAL' \
                or valorYtipo['tipo']== 'DOUBLE_PRECISION' \
                or valorYtipo['tipo'] == 'MONEY':
                    return ExpresionNumero(valorYtipo['val'], TIPO_DE_DATO.DECIMAL, self.linea)
                elif valorYtipo['tipo'] == 'CHAR' \
                or valorYtipo['tipo'] == 'VARCHAR' \
                or valorYtipo['tipo'] == 'TEXT' \
                or valorYtipo['tipo'] == 'ENUM':
                    return ExpresionCadena(valorYtipo['val'], TIPO_DE_DATO.CADENA, self.linea)
                elif valorYtipo['tipo'] == 'BOOLEAN':
                    return ExpresionBooleano(valorYtipo['val'], self.linea)
                elif valorYtipo['tipo'] == 'DATE':
                    return ExpresionCadena(valorYtipo['val'], TIPO_DE_DATO.DECIMAL, self.linea, isFecha=True)
                return ErrorReport('Semantico','TIPO DESCONOCIDO', self.linea)
            
        else:# supongo que es para lo del check :v 
            try:
                symbol = ts.buscarSimbolo(self.val)
                if symbol.tipo == 'INTEGER':
                    return ExpresionNumero(symbol.valor, TIPO_DE_DATO.ENTERO, self.linea)
                elif symbol.tipo == 'DECIMAL':
                    return ExpresionNumero(symbol.valor, TIPO_DE_DATO.DECIMAL, self.linea)
                elif symbol.tipo == 'STRING' or \
                symbol.tipo == 'ENUM':
                    return ExpresionCadena(symbol.valor, TIPO_DE_DATO.CADENA, self.linea)
                elif symbol.tipo == 'BOOLEAN':
                    return ExpresionBooleano(symbol.valor, self.linea)
                elif symbol.tipo == 'DATE':
                    return ExpresionCadena(symbol.valor, TIPO_DE_DATO.CADENA, self.linea, isFecha=True)
                return ErrorReport('Semantico', 'Variable ' + self.val + ' not defined', self.linea)
            except:
                return ErrorReport('Semantico', 'Variable ' + self.val + ' not defined', self.linea)   
    def evaluacionCheck(self ,ts)-> int:
        try:
            symbol = ts.buscarSimbolo(self.val)
            return self.__comprobarTipo(symbol.tipo)
        except:
            return 5

    def getExpresionToString(self) -> str:
        return str(self.val)


    def __comprobarTipo(self,tipo: str) -> int:
        if tipo == 'SMALLINT' \
        or tipo == 'BIGINT' \
        or tipo == 'INTEGER'\
        or tipo == 'DECIMAL' \
        or tipo == 'NUMERIC' \
        or tipo == 'REAL' \
        or tipo == 'DOUBLE_PRECISION' \
        or tipo == 'MONEY':
            return 1
        elif tipo == 'CHAR' \
        or tipo == 'VARCHAR' \
        or tipo == 'TEXT' \
        or tipo == 'ENUM':
            return 2
        elif tipo == 'BOOLEAN':
            return 0
        elif tipo == 'DATE':
            return 3
        return 5




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

        nodo = "\n" + identificador + "[ label =\"" + str(self.operador) + "\" ];"
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
        elif isinstance(izq,ExpresionCadena) and isinstance(izq,ExpresionCadena):
            if self.operador == OPERACION_RELACIONAL.DESIGUAL:
                return ExpresionBooleano(izq.val != der.val, self.linea)
            elif self.operador == OPERACION_RELACIONAL.IGUAL:
                return ExpresionBooleano(izq.val == der.val, self.linea)      
        else:
            return ErrorReport('semantico', 'Error de tipos , en Operacion Relacional' ,self.linea)
    
    def evaluacionCheck(self ,ts)-> int: 
        izq  = self.exp1.evaluacionCheck(ts)
        der  = self.exp2.evaluacionCheck(ts)

        if izq == 3 and der == 3: # SI AMBOS SON CADENAS DE TIPO FECHA ES VALIDA SU COMPARACION Y RETORNA UN BOOL 
            return 0
        elif (self.operador == OPERACION_RELACIONAL.IGUAL or self.operador == OPERACION_RELACIONAL.DESIGUAL) and (izq == 2 or izq == 3) and (der == 2 or der ==3):
            return 0       
        elif izq == 1 and der == 1:
            return 0
        else:
            return 5
    def getExpresionToString(self) -> str:
        izq  = self.exp1.getExpresionToString()
        der  = self.exp2.getExpresionToString()
        if isinstance(izq , ErrorReport):
            return izq
        if isinstance(der , ErrorReport):
            return der
        op = ''
        if self.operador == OPERACION_RELACIONAL.DESIGUAL:
            op = '<>' # si fuera != le pone <>
        elif self.operador == OPERACION_RELACIONAL.IGUAL:
            op = '='
        elif self.operador == OPERACION_RELACIONAL.MAYOR:
            op = '>'
        elif self.operador == OPERACION_RELACIONAL.MENOR:
            op = '<'
        elif self.operador == OPERACION_RELACIONAL.MAYORIGUAL:
            op = '>='
        elif self.operador == OPERACION_RELACIONAL.MENORIGUAL:
            op = '<='
        else:
            op = 'DESCONOCIDO'
        return str(izq + f' { op } '+der)


class ExpresionLogica(Expresion):
    def __init__(self, exp1, exp2, operador, linea):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
        self.linea  = linea

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"" + str(self.operador) + "\" ];"
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
    
    def evaluacionCheck(self ,ts)-> int: 
        izq  = self.exp1.evaluacionCheck(ts)
        der  = self.exp2.evaluacionCheck(ts)
        if izq != 0 or der != 0:
            return 5
        return 0
    def getExpresionToString(self) -> str:
        izq  = self.exp1.getExpresionToString()
        der  = self.exp2.getExpresionToString()
        if isinstance(izq , ErrorReport):
            return izq
        if isinstance(der , ErrorReport):
            return der
        return str(izq + f' {self.operador.name.lower()} ' + der)

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

    def evaluacionCheck(self ,ts)-> int: 
        sintetizado = self.exp.evaluacionCheck(ts)
        if sintetizado != 0:
            return 5
        return 0
    def getExpresionToString(self) -> str:
        sint = self.exp.getExpresionToString()
        if isinstance(sint , ErrorReport):
            return sint
        return str('not' + sint)
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
    
    def evaluacionCheck(self ,ts)-> int: 
        return 0
    def getExpresionToString(self) -> str:
        return str(self.val)

# Expresión Between: Contempla tanto al Between como al Between Symmetric, asi como las versiones negadas


class ExpresionBetween(Expresion):
    def __init__(self, evaluado, limiteInferior, limiteSuperior, tipo, linea, invertido=False, simetria=False):
        self.evaluado = evaluado
        self.limiteInferior = limiteInferior
        self.limiteSuperior = limiteSuperior
        self.invertido = invertido
        self.simetria = simetria
        self.tipo = tipo
        self.linea = linea

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
    def ejecutar(self, ts):
        ev = self.evaluado.ejecutar(ts)
        inf = self.limiteInferior.ejecutar(ts)
        sup = self.limiteSuperior.ejecutar(ts)
        if isinstance(ev,ExpresionNumero) and isinstance(inf,ExpresionNumero) and isinstance(sup,ExpresionNumero):
            if self.tipo == BETWEEN.BETWEEN:
                return ExpresionBooleano(inf.val <= ev.val <= sup.val, self.linea)
            elif self.tipo == BETWEEN.NOT_BETWEEN:
                return ExpresionBooleano(not inf.val <= ev.val <= sup.val, self.linea)
            elif self.tipo == BETWEEN.BETWEEN_SYMMETRIC:
                return ExpresionBooleano((inf.val <= ev.val <= sup.val) ^ (ev.val <= inf.val or sup.val <= ev.val), self.linea)
            elif self.tipo == BETWEEN.NOT_BETWEEN_SYMMETRIC:
                return ExpresionBooleano(not ((inf.val <= ev.val <= sup.val) ^ (ev.val <= inf.val or sup.val <= ev.val)), self.linea)
        else:
             return ErrorReport('semantico', 'Error de tipos , en Operacion Relacional' ,self.linea)


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
    def __init__(self, valor , tipo, linea , isFecha = False):
        self.tipo = tipo 
        self.val = str(valor)
        self.linea = linea
        self.isFecha = isFecha

    def dibujar(self):
        identificador = str(hash(self))
        temp = str(self.val)

        temp = temp.replace("\"", "")
        temp = temp.replace("\'", "")

        nodo = "\n" + identificador + "[ label =\"" + temp + "\" ];\n"

        return nodo
    def ejecutar(self,ts):
        return self
    
    def evaluacionCheck(self ,ts)-> int: 
        if self.isFecha == True:
            return 3
        return 2
    def getExpresionToString(self) -> str:
        return str('\''+self.val+'\'')

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
        if (isinstance(izq,ExpresionNumero) and isinstance(izq,ExpresionNumero)) or (isinstance(izq,ExpresionCadena) and isinstance(izq,ExpresionCadena)):
            if self.operador == OPERACION_BINARIA_IS.IS_NOT_DISTINCT_FROM:
                return ExpresionBooleano(izq.val == der.val, self.linea)
            elif self.operador == OPERACION_BINARIA_IS.IS_DISTINCT_FROM:
                return ExpresionBooleano(izq.val != der.val, self.linea)
        else:
            return ErrorReport('semantico', 'Error de tipos , en Operacion Relacional' ,self.linea)
        

    
class ExpresionAgrupacion(Expresion):
    def __init__(self, exp):
        self.exp = exp

    def dibujar(self):
        return self.exp.dibujar()
    def ejecutar(self, ts):
        return self.exp.ejecutar(ts)
    
    def evaluacionCheck(self ,ts)-> int: 
        return self.exp.evaluacionCheck(ts)
    
    def getExpresionToString(self) -> str:
        sint = self.exp.getExpresionToString()
        return str('(' + sint +')')
    
    



class TuplaCompleta:
    def __init__(self, tupla):
        self.tupla = tupla
        
    def getValue(self, id , referciaTabla = None): # a veces no viene
        # VALIDAR QUE NO HAYA AMBIGUEDAD PRIMERO , aun no lo tengo :v 
        for columna in self.tupla:
            # 3 POSIBLES CASOS  , TABLA.COLUMNA , ALIAS.COLUMNA , COLUMNA 
            if columna['id'] == id:
                return columna
            # elif self.coincideConAlias(columna['id']):
            #     pass
            elif self.quitarRef(columna['id']) == id:
                return columna
        return None
    
    def quitarRef(self,cadena):# le quito la referencia de su tabla 
        cadena = cadena.split('.')
        return cadena[1]
    def coincideConAlias(self,columna):# le quito la referencia de su tabla 
        aux = columna['id'].split('.')
        return columna['alias']+'.'+aux[1]