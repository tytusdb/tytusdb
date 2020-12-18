import AST.Nodo as Node
from TablaSimbolos.Tipos import *
from TablaSimbolos.TS import *
from Errores.Nodo_Error import *


class Expression(Node.Nodo):
    def __init__(self, *args):
        if len(args) == 6:
            self.exp1 = args[0]
            self.exp2 = args[1]
            self.op = args[2]
            self.line = args[3]
            self.column = args[4]
            self.op_type = args[5]
            self.val = None
            self.type = None

        elif len(args) == 4:
            self.line = args[1]
            self.column = args[2]
            self.val = args[0]
            self.op_type = None
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
        if self.op_type is None:
            return self
        elif self.op_type == 'iden':
            if TS.exists(self.id):
                return self
            Errores.insertar(Nodo_Error("Semantico", "No existe el campo \'" + self.id + "\'", self.line, self.column))
            return TIPO_DATOS.ERROR
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
                else:
                    return TIPO_DATOS.ERROR
            return TIPO_DATOS.ERROR

    def getC3D(self, TS):
        codigo = ""
        codigo += self.Exp.getC3D(TS)
        temp = TS.getTemp()
        codigo += temp + '= (' + self.cast + ')' + self.Exp.temporal + ';\n'
        self.temporal = temp

        return codigo;

    def graficarasc(self, padre, grafica):
        pass


