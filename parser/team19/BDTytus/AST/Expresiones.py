import AST.Nodo as Node
import math as m
from TablaSimbolos.Tipos import *
from TablaSimbolos.TS import *
from Errores.Nodo_Error import *


class Expression(Node.Nodo):
    def __init__(self, *args):
        if len(args) == 6:
            if args[5] == 'math2':
                self.val1 = args[1]
                self.val2 = args[2]
                self.line = args[3]
                self.column = args[4]
                self.function = args[0]
                self.op_type = args[5]
            else:
                self.exp1 = args[0]
                self.exp2 = args[1]
                self.op = args[2]
                self.line = args[3]
                self.column = args[4]
                self.op_type = args[5]
                self.val = None
                self.type = None
        elif len(args) == 5:
            if args[4] == 'unario':
                self.op_type = args[4]
                self.type = args[0]
                self.val = args[1]
                self.line = args[2]
                self.column = args[3]
            elif args[4] == 'as':
                self.type = None
                self.val = args[0]
                self.asid = args[1]
                self.line = args[2]
                self.column = args[3]
                self.op_type = 'as'
            elif args[4] == 'aggregate':
                self.val = args[0]
                self.asid = args[1]
                self.line = args[2]
                self.column = args[3]
                self.op_type = 'agg'
            elif args[4] == 'indice':
                self.val = args[0]
                self.asid = args[1]
                self.line = args[2]
                self.column = args[3]
                self.op_type = 'in'
            elif args[4] == 'math':
                self.val = args[1]
                self.function = args[0]
                self.line = args[2]
                self.column = args[3]
                self.op_type = 'math'
                self.type = None
            elif args[4] == 'trigo':
                self.val = args[1]
                self.function = args[0]
                self.line = args[2]
                self.column = args[3]
                self.op_type = 'trigo'
                self.type = None
        elif len(args) == 4:
            self.line = args[1]
            self.column = args[2]
            self.val = args[0]
            self.op_type = 'valor'
            if args[3] == "decimal":
                self.type = 'FLOAT'
            elif args[3] == "entero":
                self.type = 'INT'
            elif args[3] == "char":
                self.type = 'CHAR'
            elif args[3] == "string":
                self.type = 'STR'
            elif args[3] == "t_true":
                self.type = 'BOOLEAN'
                self.val = True
            elif args[3] == "t_false":
                self.type = 'BOOLEAN'
                self.val = False

        elif len(args) == 3:
            self.val = None
            self.type = None
            self.op_type = 'iden'
            self.id = args[0]
            self.line = args[1]
            self.column = args[2]

    def ejecutar(self, TS, Errores):
        if self.op_type == 'valor':
            return self
        elif self.op_type == 'unario':
            self.val.ejecutar(TS, Errores)
            if self.type == '-':
                self.val = -self.val.val
            return self
        elif self.op_type == 'as' or self.op_type == 'in' or self.op_type == 'agg':
            self.val.ejecutar(TS, Errores)
            self.asid.ejecutar(TS, Errores)
            self.asid = self.asid.id
            return self
        elif self.op_type == 'math':
            if self.function == 'ceil' or self.function == 'ceiling':
                self.val.ejecutar(TS, Errores)
                if isinstance(self.val.val, int):
                    self.val = m.__ceil__(self.val.val)
                else:
                    self.val = m.ceil(self.val.val)
            elif self.function == 'abs':
                self.val = m.fabs(self.val.val)
            elif self.function == 'cbrt':
                self.val = m.ceil(self.val.val**(1/3))
            elif self.function == 'degrees':
                self.val = m.degrees(self.val.val)
            elif self.function == 'div':
                self.val = m.exp(self.val.val)
            elif self.function == 'exp':
                self.val = m.exp(self.val.val)
            elif self.function == 'factorial':
                self.val = m.factorial(self.val.val)
            elif self.function == 'floor':
                self.val = m.floor(self.val.val)
            elif self.function == 'gcd':
                self.val = m.gcd(self.val.val)
            elif self.function == 'ln':
                self.val = m.log(self.val.val)
            elif self.function == 'log':
                self.val = m.log10(self.val.val)
            elif self.function == 'pi':
                self.val = m.pi
            return self
        elif self.op_type == 'trigo':
            if self.function == 'acos':
                self.val = m.acos(self.val.val)
            elif self.function == 'acosd':
                self.val = m.degrees(m.acos(self.val.val))
            elif self.function == 'asin':
                self.val = m.asin(self.val.val)
            elif self.function == 'asind':
                self.val = m.degrees(m.asin(self.val.val))
            elif self.function == 'atan':
                self.val = m.atan(self.val.val)
            elif self.function == 'atand':
                self.val = m.degrees(m.atan(self.val.val))
            elif self.function == 'cos':
                self.val = m.cos(self.val.val)
            elif self.function == 'cosd':
                self.val = m.cos(m.radians(self.val.val))
            elif self.function == 'sin':
                self.val = m.sin(self.val.val)
            elif self.function == 'sind':
                self.val = m.sin(m.radians(self.val.val))
            elif self.function == 'tan':
                self.val = m.tan(self.val.val)
            elif self.function == 'tand':
                self.val = m.tan(m.radians(self.val.val))
            return self
        elif self.op_type == 'iden':
            return self
        elif self.op_type == 'Aritmetica':
            val1 = self.exp1.ejecutar(TS, Errores)
            val2 = self.exp2.ejecutar(TS, Errores)
#----------------------------------------------------------------------> Se validan operaciones con int
            if isinstance(val1.val, int):
                if isinstance(val2.val, int):
                    if self.op == '+':
                        self.val = val1.val + val2.val
                    elif self.op == '-':
                        self.val = val1.val - val2.val
                    elif self.op == '*':
                        self.val = val1.val * val2.val
                    elif self.op == '/':
                        if val2.val != 0:
                            self.val = val1.val / val2.val
                        else:
                            Errores.insertar(
                                Nodo_Error("Semantico", "No es posible division entre 0", self.line,
                                           self.column))
                            return TIPO_DATOS.ERROR
                    elif self.op == '%':
                        self.val = val1.val % val2.val
                    elif self.op == '^':
                        self.val = pow(val1.val, val2.val)
                    return self
                elif isinstance(val2.val, float):
                    if self.op == '+':
                        self.val = val1.val + val2.val
                    elif self.op == '-':
                        self.val = val1.val - val2.val
                    elif self.op == '*':
                        self.val = val1.val * val2.val
                    elif self.op == '/':
                        if val2.val != 0.0:
                            self.val = val1.val / val2.val
                        else:
                            Errores.insertar(
                                Nodo_Error("Semantico", "No es posible division entre 0", self.line,
                                           self.column))
                            return TIPO_DATOS.ERROR
                    elif self.op == '%':
                        self.val = val1.val % val2.val
                    elif self.op == '^':
                        self.val = pow(val1.val, val2.val)
                    return self
                elif isinstance(val2.val, bool):
                    if self.op == '+':
                        self.val = val1.val + val2.val
                    elif self.op == '-':
                        self.val = val1.val - val2.val
                    elif self.op == '*':
                        self.val = val1.val * val2.val
                    elif self.op == '/':
                        if val2 != 0 or val2 is not False:
                            self.val = val1.val / val2.val
                        else:
                            Errores.insertar(
                                Nodo_Error("Semantico", "No es posible division entre 0", self.line,
                                           self.column))
                            return TIPO_DATOS.ERROR
                    elif self.op == '%':
                        self.val = val1.val % val2.val
                    elif self.op == '^':
                        self.val = pow(val1.val, val2.val)
                    return self
                else:
                    Errores.insertar(Nodo_Error("Semantico", "No es posible ejecutar la operacion \'"+ str(self.op) +"\' con los tipos de datos \'"+str(val1.type)+"\' y " + "\'" + str(val2.type) + "\' en", self.line, self.column))
                    return TIPO_DATOS.ERROR

#----------------------------------------------------------------------> Se validan operaciones con FLOAT
            elif isinstance(val1.val, float):
                if isinstance(val2.val, int):
                    if self.op == '+':
                        self.val = val1.val + val2.val
                    elif self.op == '-':
                        self.val = val1.val - val2.val
                    elif self.op == '*':
                        self.val = val1.val * val2.val
                    elif self.op == '/':
                        if val2.val != 0:
                            self.val = val1.val / val2.val
                        else:
                            Errores.insertar(
                                Nodo_Error("Semantico", "No es posible division entre 0", self.line,
                                           self.column))
                            return TIPO_DATOS.ERROR
                    elif self.op == '%':
                        self.val = val1.val % val2.val
                    elif self.op == '^':
                        self.val = pow(val1.val, val2.val)
                    return self
                elif isinstance(val2.val, float):
                    if self.op == '+':
                        self.val = val1.val + val2.val
                    elif self.op == '-':
                        self.val = val1.val - val2.val
                    elif self.op == '*':
                        self.val = val1.val * val2.val
                    elif self.op == '/':
                        if val2.val != 0.0:
                            self.val = val1.val / val2.val
                        else:
                            Errores.insertar(
                                Nodo_Error("Semantico", "No es posible division entre 0", self.line,
                                           self.column))
                            return TIPO_DATOS.ERROR
                    elif self.op == '%':
                        self.val = val1.val % val2.val
                    elif self.op == '^':
                        self.val = pow(val1.val, val2.val)
                    return self
                elif isinstance(val2.val, bool):
                    if self.op == '+':
                        self.val = val1.val + val2.val
                    elif self.op == '-':
                        self.val = val1.val - val2.val
                    elif self.op == '*':
                        self.val = val1.val * val2.val
                    elif self.op == '/':
                        if val2 != 0 or val2 is not False:
                            self.val = val1.val / val2.val
                        else:
                            Errores.insertar(
                                Nodo_Error("Semantico", "No es posible division entre 0", self.line,
                                           self.column))
                            return TIPO_DATOS.ERROR
                    elif self.op == '%':
                        self.val = val1.val % val2.val
                    elif self.op == '^':
                        self.val = pow(val1.val, val2.val)
                    return self
                else:
                    Errores.insertar(Nodo_Error("Semantico", "No es posible ejecutar la operacion \'"+ str(self.op) +"\' con los tipos de datos \'"+str(val1.type)+"\' y " + "\'" + str(val2.type) + "\' en", self.line, self.column))
                    return TIPO_DATOS.ERROR

# ----------------------------------------------------------------------> Se validan operaciones con BOOLEAN
            elif isinstance(val1.val, bool):
                    if isinstance(val2.val, int):
                        if self.op == '+':
                            self.val = val1.val + val2.val
                        elif self.op == '-':
                            self.val = val1.val - val2.val
                        elif self.op == '*':
                            self.val = val1.val * val2.val
                        elif self.op == '/':
                            if val2.val != 0:
                                self.val = val1.val / val2.val
                            else:
                                Errores.insertar(
                                    Nodo_Error("Semantico", "No es posible division entre 0", self.line,
                                               self.column))
                                return TIPO_DATOS.ERROR
                        elif self.op == '%':
                            self.val = val1.val % val2.val
                        elif self.op == '^':
                            self.val = pow(val1.val, val2.val)
                        return self
                    elif isinstance(val2.val, float):
                        if self.op == '+':
                            self.val = val1.val + val2.val
                        elif self.op == '-':
                            self.val = val1.val - val2.val
                        elif self.op == '*':
                            self.val = val1.val * val2.val
                        elif self.op == '/':
                            if val2.val != 0.0:
                                self.val = val1.val / val2.val
                            else:
                                Errores.insertar(
                                    Nodo_Error("Semantico", "No es posible division entre 0", self.line,
                                               self.column))
                                return TIPO_DATOS.ERROR
                        elif self.op == '%':
                            self.val = val1.val % val2.val
                        elif self.op == '^':
                            self.val = pow(val1.val, val2.val)
                        return self
                    elif isinstance(val2.val, bool):
                        if self.op == '+':
                            self.val = val1.val + val2.val
                        elif self.op == '-':
                            self.val = val1.val - val2.val
                        elif self.op == '*':
                            self.val = val1.val * val2.val
                        elif self.op == '/':
                            if val2 != 0 or val2 is not False:
                                self.val = val1.val / val2.val
                            else:
                                Errores.insertar(
                                    Nodo_Error("Semantico", "No es posible division entre 0", self.line,
                                               self.column))
                                return TIPO_DATOS.ERROR
                        elif self.op == '%':
                            self.val = val1.val % val2.val
                        elif self.op == '^':
                            self.val = pow(val1.val, val2.val)
                        return self
                    else:
                        Errores.insertar(Nodo_Error("Semantico", "No es posible ejecutar la operacion \'"+ str(self.op) +"\' con los tipos de datos \'"+str(val1.type)+"\' y " + "\'" + str(val2.type) + "\' en", self.line, self.column))
                        return TIPO_DATOS.ERROR

        elif self.op_type == 'Relacional':
            val1 = self.exp1.ejecutar(TS, Errores)
            val2 = self.exp2.ejecutar(TS, Errores)
            # ----------------------------------------------------------------------> Se validan operaciones con int
            while val1 != TIPO_DATOS.ERROR:
                if isinstance(val1.val, int):
                    if isinstance(val2.val, int):
                        if self.op == '<':
                            self.val = val1.val < val2.val
                        elif self.op == '>':
                            self.val = val1.val > val2.val
                        elif self.op == '<>':
                            self.val = val1.val != val2.val
                        elif self.op == '!=':
                            self.val = val1.val != val2.val
                        elif self.op == '>=':
                            self.val = val1.val >= val2.val
                        elif self.op == '<=':
                            self.val = val1.val <= val2.val
                        elif self.op == '=':
                            self.val = val1.val == val2.val
                        return self
                    elif isinstance(val2.val, float):
                        if self.op == '<':
                            self.val = val1.val < val2.val
                        elif self.op == '>':
                            self.val = val1.val > val2.val
                        elif self.op == '<>':
                            self.val = val1.val != val2.val
                        elif self.op == '!=':
                            self.val = val1.val != val2.val
                        elif self.op == '>=':
                            self.val = val1.val >= val2.val
                        elif self.op == '<=':
                            self.val = val1.val <= val2.val
                        elif self.op == '=':
                            self.val = val1.val == val2.val
                        return self
                    elif isinstance(val2.val, str):
                        if self.op == '<':
                            self.val = val1.val < int(val2.val)
                        elif self.op == '>':
                            self.val = val1.val > int(val2.val)
                        elif self.op == '<>':
                            self.val = val1.val != int(val2.val)
                        elif self.op == '!=':
                            self.val = val1.val != int(val2.val)
                        elif self.op == '>=':
                            self.val = val1.val >= int(val2.val)
                        elif self.op == '<=':
                            self.val = val1.val <= int(val2.val)
                        elif self.op == '=':
                            self.val = val1.val == int(val2.val)
                        return self
                    else:
                        Errores.insertar(Nodo_Error("Semantico", "No es posible ejecutar la operacion '" + str(
                            self.op) + "' con los tipos de datos \'" + str(val2.type) + "\' y " + "'" + str(
                            val2.type) + "' en", self.line, self.column))
                        return TIPO_DATOS.ERROR
                # ----------------------------------------------------------------------> Se validan operaciones con int
                elif isinstance(val1.val, float):
                    if isinstance(val2.val, int):
                        if self.op == '<':
                            self.val = val1.val < val2.val
                        elif self.op == '>':
                            self.val = val1.val > val2.val
                        elif self.op == '<>':
                            self.val = val1.val != val2.val
                        elif self.op == '!=':
                            self.val = val1.val != val2.val
                        elif self.op == '>=':
                            self.val = val1.val >= val2.val
                        elif self.op == '<=':
                            self.val = val1.val <= val2.val
                        elif self.op == '=':
                            self.val = val1.val == val2.val
                        return self
                    elif isinstance(val2.val, float):
                        if self.op == '<':
                            self.val = val1.val < val2.val
                        elif self.op == '>':
                            self.val = val1.val > val2.val
                        elif self.op == '<>':
                            self.val = val1.val != val2.val
                        elif self.op == '!=':
                            self.val = val1.val != val2.val
                        elif self.op == '>=':
                            self.val = val1.val >= val2.val
                        elif self.op == '<=':
                            self.val = val1.val <= val2.val
                        elif self.op == '=':
                            self.val = val1.val == val2.val
                        return self
                    elif isinstance(val2.val, str):
                        if self.op == '<':
                            self.val = val1.val < float(val2.val)
                        elif self.op == '>':
                            self.val = val1.val > float(val2.val)
                        elif self.op == '<>':
                            self.val = val1.val != float(val2.val)
                        elif self.op == '!=':
                            self.val = val1.val != float(val2.val)
                        elif self.op == '>=':
                            self.val = val1.val >= float(val2.val)
                        elif self.op == '<=':
                            self.val = val1.val <= float(val2.val)
                        elif self.op == '=':
                            self.val = val1.val == float(val2.val)
                        return self
                    else:
                        Errores.insertar(Nodo_Error("Semantico", "No es posible ejecutar la operacion \'" + str(
                            self.op) + "\' con los tipos de datos \'" + str(val1.type) + "\' y " + "\'" + str(
                            val2.type) + "\' en", self.line, self.column))
                        return TIPO_DATOS.ERROR
                elif val1.op_type == 'iden':
                    val1.val = val2.val
                    return val1
                else:
                    return TIPO_DATOS.ERROR
            return TIPO_DATOS.ERROR
        elif self.op_type == 'Logica':
            val1 = self.exp1.ejecutar(TS, Errores)
            val2 = self.exp2.ejecutar(TS, Errores)
            if isinstance(val1.val, bool):
                if isinstance(val2.val, bool):
                    if self.op == 'and':
                        self.val = val1.val and val2.val
                    elif self.op == 'or':
                        self.val = val1.val or val2.val
                    return self


    def getC3D(self, TS):
        codigo = ""
        codigo += self.Exp.getC3D(TS)
        temp = TS.getTemp()
        codigo += temp + '= (' + self.cast + ')' + self.Exp.temporal + ';\n'
        self.temporal = temp

        return codigo;

    def graficarasc(self, padre, grafica):
        pass


