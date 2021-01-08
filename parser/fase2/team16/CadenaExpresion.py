from expresiones import *
from six import *
from Temporales import *

class CadenaExpresion():
    def __init__(self, expresion):
        expresion = expresion

    def cadena_expresion(self, expresiones):
        cadena = ""
        if isinstance(expresiones, ExpresionAritmetica):
            return self.cadena_aritmetica(expresiones)

        elif isinstance(expresiones, ExpresionRelacional):
            return self.cadena_relacional(expresiones)

        elif isinstance(expresiones, ExpresionLogica):
            return self.cadena_logica(expresiones)
        elif isinstance(expresiones, UnitariaNegAritmetica):
            return "- " + str(self.cadena_expresion(expresiones))
        elif isinstance(expresiones, UnitariaLogicaNOT):
            return "NOT " + str(self.cadena_expresion(expresiones))
        elif isinstance(expresiones, UnitariaNotBB):
            return "~ " + str(self.cadena_expresion(expresiones))
        elif isinstance(expresiones, ExpresionValor):
            if isinstance(expresiones.val, string_types):
                return '"' + str(expresiones.val) + '"'
            return str(expresiones.val)
        elif isinstance(expresiones, Variable):
            # Buscar variable en la tabla de simbolos
            r = None
            for item in self.t_global.tablaSimbolos:
                v: tipoSimbolo = self.t_global.obtenerSimbolo(item)

                if v.nombre == expresiones.id and v.ambito == self.ambitoFuncion:
                    # print(str(v.temporal))
                    r = str(v.temporal)

            if r is not None:
                return '""" + str(' + str(r) + ') + """'
            return expresiones.id
        elif isinstance(expresiones, UnitariaAritmetica):
            return self.getVar(expresiones.operador) + " " + str(self.cadena_expresion(expresiones.exp1))
        elif isinstance(expresiones, ExpresionFuncion):
            return self.cadena_expresion_funcion(expresiones)
        elif isinstance(expresiones, ExpresionTiempo):
            return expresiones.nombre
        elif isinstance(expresiones, ExpresionConstante):
            return expresiones.nombre



        elif isinstance(expresiones, CAMPO_TABLA_ID_PUNTO_ID):
            return expresiones.tablaid + "." + expresiones.campoid


        else:
            print(expresiones)
            print('Error:Expresion no reconocida')
        return None


#llamada alas subconsultas


    def cadena_logica(self, expresion: ExpresionLogica):
        cadena = ""
        exp1 = self.cadena_expresion(expresion.exp1)
        exp2 = self.cadena_expresion(expresion.exp2)

        if exp1 is not None and exp2 is not None:
            cadena = str(exp1) + " " + self.getVar(expresion.operador) + " " + str(exp2)
            return cadena

        if exp1 is not None and exp2 is None:
            cadena = self.getVar(expresion.operador) + " " + str(exp1)
            return cadena

        return None


    def cadena_relacional(self, expresion: ExpresionRelacional):
        cadena = ""

        exp1 = self.cadena_expresion(expresion.exp1)
        exp2 = self.cadena_expresion(expresion.exp2)

        cadena += str(exp1) + " " + self.getVar(expresion.operador) + " " + str(exp2)

        return cadena



    def cadena_aritmetica(self, expresion:ExpresionAritmetica):
        cadena = ""

        exp1 = self.cadena_expresion(expresion.exp1)
        exp2 = self.cadena_expresion(expresion.exp2)

        cadena += str(exp1) + " " + self.getVar(expresion.operador) + " " + str(exp2)

        return cadena



    def cadena_expresion_funcion(self, expresion: ExpresionFuncion, tipo_exp=""):
        cadena = ""

        cadena = self.getVar(expresion.id_funcion) + "("

        parametro1 = ""
        parametro2 = ""
        parametro3 = ""
        parametro4 = ""

        if expresion.exp1 is not None:
            parametro1 = ""
        if expresion.exp2 is not None:
            parametro2 = ""
        if expresion.exp3 is not None:
            parametro3 = ""
        if expresion.exp4 is not None:
            parametro4 = ""

        if expresion.id_funcion == FUNCION_NATIVA.EXTRACT:
            cadena += parametro1 + " FROM TIMESTAMP " + parametro2
        elif expresion.id_funcion == FUNCION_NATIVA.DATE_PART:
            cadena += parametro1 + ", INTERVAL " + parametro2
        else:
            cadena += parametro1

            if parametro2 != "":
                cadena += ", " + parametro2
            if parametro3 != "":
                cadena += ", " + parametro3
            if parametro4 != "":
                cadena += ", " + parametro4

        cadena += ")"
        return cadena


    def getVar(self, padreID):
        if padreID == OPERACION_ARITMETICA.MAS:
            return '+'
        elif padreID == OPERACION_ARITMETICA.MENOS:
            return '-'
        elif padreID == OPERACION_ARITMETICA.MULTI:
            return '*'
        elif padreID == OPERACION_ARITMETICA.DIVIDIDO:
            return '/'
        elif padreID == OPERACION_ARITMETICA.RESIDUO:
            return '%'
        elif padreID == OPERACION_LOGICA.AND:
            return 'AND'
        elif padreID == OPERACION_LOGICA.OR:
            return 'OR'
        elif padreID == OPERACION_RELACIONAL.IGUALQUE:
            return '='
        elif padreID == OPERACION_RELACIONAL.DISTINTO:
            return '!='
        elif padreID == OPERACION_RELACIONAL.MAYORIGUAL:
            return '>='
        elif padreID == OPERACION_RELACIONAL.MENORIGUAL:
            return '!='
        elif padreID == OPERACION_RELACIONAL.MAYORQUE:
            return '>'
        elif padreID == OPERACION_RELACIONAL.MENORQUE:
            return '<'
        # NUEVAS COSAS
        elif padreID == OPERACION_LOGICA.IS_NOT_NULL:
            return 'IS_NOT_NULL'
        elif padreID == OPERACION_LOGICA.IS_NOT_TRUE:
            return 'IS_NOT_TRUE'
        elif padreID == OPERACION_LOGICA.IS_NOT_FALSE:
            return 'IS_NOT_FALSE'
        elif padreID == OPERACION_LOGICA.IS_NOT_UNKNOWN:
            return 'IS_NOT_UNKNOWN'
        elif padreID == OPERACION_LOGICA.IS_NULL:
            return 'IS_NULL'
        elif padreID == OPERACION_LOGICA.IS_TRUE:
            return 'IS_TRUE'
        elif padreID == OPERACION_LOGICA.IS_FALSE:
            return 'IS_FALSE'
        elif padreID == OPERACION_LOGICA.IS_UNKNOWN:
            return 'IS_NOT_UNKNOWN'
        elif padreID == OPERACION_LOGICA.IS_NOT_DISTINCT:
            return 'IS_NOT_DISTINCT'
        elif padreID == OPERACION_LOGICA.IS_DISTINCT:
            return 'IS_DISTINCT'
        elif padreID == OPERACION_LOGICA.EXISTS:
            return 'EXISTS'
        elif padreID == OPERACION_LOGICA.NOT_EXISTS:
            return 'NOTEXISTS'
        elif padreID == OPERACION_LOGICA.IN:
            return 'IN'
        elif padreID == OPERACION_LOGICA.NOT_IN:
            return 'NOTIN'
        elif padreID == FUNCION_NATIVA.ABS:
            return 'ABS'
        elif padreID == FUNCION_NATIVA.CBRT:
            return 'CBRT'
        elif padreID == FUNCION_NATIVA.CEIL:
            return 'CEIL'
        elif padreID == FUNCION_NATIVA.CEILING:
            return 'CEILING'
        elif padreID == FUNCION_NATIVA.DEGREES:
            return 'DEGREES'
        elif padreID == FUNCION_NATIVA.EXP:
            return 'EXP'
        elif padreID == FUNCION_NATIVA.FACTORIAL:
            return 'FACTORIAL'
        elif padreID == FUNCION_NATIVA.FLOOR:
            return 'FLOOR'
        elif padreID == FUNCION_NATIVA.LN:
            return 'LN'
        elif padreID == FUNCION_NATIVA.LOG:
            return 'LOG'
        elif padreID == FUNCION_NATIVA.MOD:
            return 'MOD'
        elif padreID == FUNCION_NATIVA.RADIANS:
            return 'RADIANS'
        elif padreID == FUNCION_NATIVA.ROUND:
            return 'ROUND'
        elif padreID == FUNCION_NATIVA.SIGN:
            return 'SIGN'
        elif padreID == FUNCION_NATIVA.SQRT:
            return 'SQRT'
        elif padreID == FUNCION_NATIVA.TRUNC:
            return 'TRUNC'
        elif padreID == FUNCION_NATIVA.ACOS:
            return 'ACOS'
        elif padreID == FUNCION_NATIVA.ACOSD:
            return 'ACOSD'
        elif padreID == FUNCION_NATIVA.ASIN:
            return 'ASIN'
        elif padreID == FUNCION_NATIVA.ASIND:
            return 'ASIND'
        elif padreID == FUNCION_NATIVA.ATAN:
            return 'ATAN'
        elif padreID == FUNCION_NATIVA.ATAND:
            return 'ATAND'
        elif padreID == FUNCION_NATIVA.COS:
            return 'COS'
        elif padreID == FUNCION_NATIVA.COSD:
            return 'COSD'
        elif padreID == FUNCION_NATIVA.COT:
            return 'COT'
        elif padreID == FUNCION_NATIVA.COTD:
            return 'COTD'
        elif padreID == FUNCION_NATIVA.COSD:
            return 'COSD'
        elif padreID == FUNCION_NATIVA.SIN:
            return 'SIN'
        elif padreID == FUNCION_NATIVA.SIND:
            return 'SIND'
        elif padreID == FUNCION_NATIVA.TAN:
            return 'TAN'
        elif padreID == FUNCION_NATIVA.TAND:
            return 'TAND'
        elif padreID == FUNCION_NATIVA.SINH:
            return 'SINH'
        elif padreID == FUNCION_NATIVA.COSH:
            return 'COSH'
        elif padreID == FUNCION_NATIVA.TANH:
            return 'TANH'
        elif padreID == FUNCION_NATIVA.ASINH:
            return 'ASINH'
        elif padreID == FUNCION_NATIVA.ACOSH:
            return 'ACOSH'
        elif padreID == FUNCION_NATIVA.ATANH:
            return 'ATANH'
        elif padreID == FUNCION_NATIVA.LENGTH:
            return 'LENGTH'
        elif padreID == FUNCION_NATIVA.TRIM:
            return 'TRIM'
        elif padreID == FUNCION_NATIVA.MD5:
            return 'MD5'
        elif padreID == FUNCION_NATIVA.SHA256:
            return 'SHA256'
        elif padreID == FUNCION_NATIVA.DIV:
            return 'DIV'
        elif padreID == FUNCION_NATIVA.GCD:
            return 'GCD'
        elif padreID == FUNCION_NATIVA.MOD:
            return 'MOD'
        elif padreID == FUNCION_NATIVA.POWER:
            return 'POWER'
        elif padreID == FUNCION_NATIVA.ATAN2:
            return 'ATAN2'
        elif padreID == FUNCION_NATIVA.ATAN2D:
            return 'ATAN2D'
        elif padreID == FUNCION_NATIVA.GET_BYTE:
            return 'GET_BYTE'
        elif padreID == FUNCION_NATIVA.ENCODE:
            return 'ENCODE'
        elif padreID == FUNCION_NATIVA.DECODE:
            return 'DECODE'
        elif padreID == CONDICIONAL_SUBQUERY.ANY:
            return 'ANY'
        elif padreID == CONDICIONAL_SUBQUERY.ALL:
            return 'ALL'
        elif padreID == CONDICIONAL_SUBQUERY.SOME:
            return 'SOME'
        elif padreID == FUNCION_NATIVA.SUBSTRING:
            return 'SUBSTRING'
        elif padreID == FUNCION_NATIVA.SUBSTR:
            return 'SUBSTR'
        elif padreID == FUNCION_NATIVA.SET_BYTE:
            return 'SET_BYTE'
        elif padreID == FUNCION_NATIVA.WIDTH_BUCKET:
            return 'WIDTH_BUCKET'
        elif padreID == OPERACION_ARITMETICA.CUBICA:
            return '||'
        elif padreID == OPERACION_ARITMETICA.CUADRATICA:
            return '|'
        elif padreID == OPERACION_ARITMETICA.POTENCIA:
            return '^'
        elif padreID == FUNCION_NATIVA.EXTRACT:
            return 'EXTRACT'
        elif padreID == FUNCION_NATIVA.DATE_PART:
            return 'DATE_PART'
        elif padreID == FUNCION_NATIVA.NOW:
            return 'NOW'
        elif padreID == FUNCION_NATIVA.PI:
            return 'PI'
        elif padreID == FUNCION_NATIVA.RANDOM:
            return 'RANDOM'
        else:
            return 'op'
