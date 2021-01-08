from analizer_pl.abstract.expression import Expression
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment
from analizer_pl import grammar


class FunctionCall(Expression):
    def __init__(self, id, params, isBlock, temp, row, column) -> None:
        super().__init__(row, column)
        self.id = id
        self.params = params
        self.isBlock = isBlock
        self.temp = temp

    def execute(self, environment):
        c3d = ""
        tab = ""
        parVal = ""
        tab1 = False
        if isinstance(environment, Environment):
            tab += "\t"
            func = environment.globalEnv.getFunction(self.id)
            tab1 = True
        else:
            func = environment.getFunction(self.id)
        # Si es para PL/SQL
        if self.isBlock or environment.isBlock:
            # Si es una funcion definida
            if func:
                if self.params:
                    if len(self.params) == func.params:
                        # Se meten al reves los parametros en la pila
                        self.params.reverse()
                        for p in self.params:
                            pval = p.execute(environment)
                            c3d += pval.value
                            c3d += tab + "stack.append(" + pval.temp + ")\n"
                            grammar.optimizer_.addIgnoreString(
                                str("stack.append(" + pval.temp + ")"), self.row, tab1
                            )
                        c3d += tab + self.id + "()\n"
                        grammar.optimizer_.addIgnoreString(
                            str(self.id + "()"), self.row, tab1
                        )
                        c3d += tab + "t" + self.temp + " = stack.pop()\n"
                        grammar.optimizer_.addIgnoreString(
                            str("t" + self.temp + " = stack.pop()"), self.row, tab1
                        )
                        self.temp = "t" + self.temp
                        return code.C3D(c3d, self.temp, self.row, self.column)
                    else:
                        # TODO: ERROR: parametros no coinciden
                        pass
                else:
                    c3d += tab + self.id + "()\n"
                    grammar.optimizer_.addIgnoreString(
                        str(self.id + "()"), self.row, tab1
                    )
                    c3d += tab + "t" + self.temp + " = stack.pop()\n"
                    grammar.optimizer_.addIgnoreString(
                        str("t" + self.temp + " = stack.pop()"), self.row, tab1
                    )
                    self.temp = "t" + self.temp
                    return code.C3D(c3d, self.temp, self.row, self.column)
            # Si es una funcion sql
            else:
                if not self.id in sql_functions:
                    print("Error: Funcion " + self.id + " no definida")
                    grammar.PL_errors.append(
                        "Error P0000: No se encontro la funcion " + self.id
                    )
                    grammar.semantic_errors.append(
                        ["No se encontro la funcion " + self.id, self.row]
                    )
                    return code.C3D("", self.temp, self.row, self.column)
                parVal = ""
                self.temp = "t" + self.temp
                c3d += tab + self.temp + " = fase1.invokeFunction("
                c3d += '"' + self.id + '"'
                if self.params:
                    c3d += ", "
                    j = 0
                    for i in range(len(self.params) - 1):
                        j = i + 1
                        pval = self.params[i].execute(environment)
                        parVal += pval.value
                        c3d += pval.temp + ", "
                    pval = self.params[j].execute(environment)
                    parVal += pval.value
                    c3d += pval.temp
                c3d += ")\n"
                c3d = parVal + c3d
                grammar.optimizer_.addIgnoreString(str(c3d), self.row, False)
                return code.C3D(c3d, self.temp, self.row, self.column)
        # Si es para el parser
        else:
            # Si es una funcion definida
            if func:
                if self.params:
                    if len(self.params) == func.params:
                        # Se meten al reves los parametros en la pila
                        self.params.reverse()
                        environment.isBlock = True
                        for p in self.params:
                            pval = p.execute(environment)
                            c3d += pval.value
                            c3d += tab + "stack.append(" + pval.temp + ")\n"
                            grammar.optimizer_.addIgnoreString(
                                str("stack.append(" + pval.temp + ")"), self.row, tab1
                            )
                        environment.isBlock = False
                        c3d += tab + self.id + "()\n"
                        grammar.optimizer_.addIgnoreString(
                            str(self.id + "()"), self.row, tab1
                        )
                        c3d += tab + "t" + self.temp + " = stack.pop()\n"
                        grammar.optimizer_.addIgnoreString(
                            str("t" + self.temp + " = stack.pop()"), self.row, tab1
                        )
                        self.temp = '"+str(t' + self.temp + ')+"'
                        return code.C3D(c3d, self.temp, self.row, self.column)
                    else:
                        # TODO: ERROR: parametros no coinciden
                        pass
                else:
                    c3d += tab + self.id + "()\n"
                    grammar.optimizer_.addIgnoreString(
                        str(self.id + "()"), self.row, tab1
                    )
                    c3d += tab + "t" + self.temp + " = stack.pop()\n"
                    grammar.optimizer_.addIgnoreString(
                        str("t" + self.temp + " = stack.pop()"), self.row, tab1
                    )
                    self.temp = '"+str(t' + self.temp + ')+"'
                    return code.C3D(c3d, self.temp, self.row, self.column)
            # Si es una funcion sql
            else:
                if not self.id in sql_functions:
                    print("Error: Funcion " + self.id + " no definida")
                    grammar.PL_errors.append(
                        "Error P0000: No se encontro la funcion " + self.id
                    )
                    grammar.semantic_errors.append(
                        ["No se encontro la funcion " + self.id, self.row]
                    )
                    return code.C3D("", "", self.row, self.column)

                if self.id == "extract":
                    c3d += self.id.upper() + "("
                    pval = self.params[0].execute(environment)
                    c3d += pval.temp[1:-1].upper() + " FROM "
                    parVal += pval.value
                    pval = self.params[1].execute(environment)
                    c3d += pval.temp[1:-1].upper() + " "
                    parVal += pval.value
                    pval = self.params[2].execute(environment)
                    c3d += pval.temp + ")"
                    parVal += pval.value
                    return code.C3D(parVal, c3d, self.row, self.column)

                if self.id == "date_part":
                    c3d += self.id + "("
                    pval = self.params[0].execute(environment)
                    c3d += pval.temp + ", "
                    parVal += pval.value
                    pval = self.params[1].execute(environment)
                    c3d += pval.temp[1:-1].upper() + " "
                    parVal += pval.value
                    pval = self.params[2].execute(environment)
                    if pval.temp != "(":
                        c3d += pval.temp + ")"
                    else:
                        c3d += "())"
                    parVal += pval.value
                    return code.C3D(parVal, c3d, self.row, self.column)

                c3d += self.id + "("

                if self.params:
                    j = 0
                    for i in range(len(self.params) - 1):
                        j = i + 1
                        pval = self.params[i].execute(environment)
                        parVal += pval.value
                        c3d += pval.temp + ", "
                    pval = self.params[j].execute(environment)
                    parVal += pval.value
                    c3d += pval.temp
                c3d += ")"
                return code.C3D(parVal, c3d, self.row, self.column)

    def dot(self):
        new = Nodo("FUNCTION_CALL")
        if self.isBlock:
            new.addNode(Nodo(str(self.id)))
            if self.params:
                par = Nodo("PARAMS")
                new.addNode(par)
                for p in self.params:
                    par.addNode(p.dot())
        return new


sql_functions = [
    "abs",
    "cbrt",
    "ceil",
    "ceiling",
    "degrees",
    "div",
    "exp",
    "factorial",
    "floor",
    "gcd",
    "lcm",
    "ln",
    "log",
    "log10",
    "mod",
    "pi",
    "power",
    "radians",
    "round",
    "sign",
    "sqrt",
    "trunc",
    "width_bucket",
    "random",
    "acos",
    "acosd",
    "asin",
    "asind",
    "atan",
    "atand",
    "atan2",
    "atan2d",
    "cos",
    "cosd",
    "cot",
    "cotd",
    "sin",
    "sind",
    "tan",
    "tand",
    "sinh",
    "cosh",
    "tanh",
    "asinh",
    "acosh",
    "atanh",
    "length",
    "substring",
    "trim",
    "get_byte",
    "md5",
    "set_byte",
    "sha256",
    "substr",
    "convert_date",
    "convert_int",
    "encode",
    "decode",
    "now",
    "extract",
    "date_part",
    "count",
    "sum",
    "prom",
]
