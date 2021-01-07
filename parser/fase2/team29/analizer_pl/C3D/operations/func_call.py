from analizer_pl.abstract.expression import Expression
from analizer_pl.abstract.expression import TYPE
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
        if isinstance(environment, Environment):
            tab += "\t"
            func = environment.globalEnv.getFunction(self.id)
        else:
            func = environment.getFunction(self.id)
        # Si es para PL/SQL
        if self.isBlock:
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
                                str("stack.append(None)"), self.row
                            )
                        c3d += tab + self.id + "()\n"
                        grammar.optimizer_.addIgnoreString(
                            str(self.id + "()"), self.row
                        )
                        c3d += tab + "t" + self.temp + " = stack.pop()\n"
                        grammar.optimizer_.addIgnoreString(
                            str("t" + self.temp + " = stack.pop()"), self.row
                        )
                        self.temp = "t" + self.temp
                    else:
                        # TODO: ERROR: parametros no coinciden
                        pass
                else:
                    c3d += tab + self.id + "()\n"
                    c3d += tab + "t" + self.temp + " = stack.pop()\n"
                    self.temp = "t" + self.temp
            # Si es una funcion sql
            else:
                if not self.id in sql_functions:
                    print("Error: Funcion no definida")
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
        # Si es para el parser
        else:
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
                                str("stack.append(" + pval.temp + ")"), self.row
                            )
                        c3d += tab + self.id + "()\n"
                        grammar.optimizer_.addIgnoreString(
                            str(self.id + "()"), self.row
                        )
                        c3d += tab + "t" + self.temp + " = stack.pop()\n"
                        grammar.optimizer_.addIgnoreString(
                            str("t" + self.temp + " = stack.pop()"), self.row
                        )
                        self.temp = '"+t' + self.temp + '+"'
                    else:
                        # TODO: ERROR: parametros no coinciden
                        pass
                else:
                    c3d += tab + self.id + "()\n"
                    c3d += tab + "t" + self.temp + " = stack.pop()\n"
                    self.temp = '"+t' + self.temp + '+"'
            # Si es una funcion matematica
            else:
                if not self.id in sql_functions:
                    print("Error: Funcion no definida")
                    return code.C3D("", self.temp, self.row, self.column)
        return code.C3D(c3d, self.temp, self.row, self.column)

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
]
