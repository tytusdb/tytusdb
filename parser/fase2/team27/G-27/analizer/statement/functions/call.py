from analizer.abstract.expression import Expression, TYPE
from analizer.abstract import expression
from analizer.reports import Nodo
from analizer.statement.expressions.primitive import Primitive
import pandas as pd
from analizer.libs import TrigonometricFunctions as trf
from analizer.libs import MathFunctions as mf
from analizer.libs import StringFunctions as strf
from datetime import datetime


class FunctionCall(Expression):
    """
    Esta clase contiene las llamadas a funciones
    """

    def __init__(self, function, params, row, column):
        Expression.__init__(self, row, column)
        self.function = function.lower()
        self.params = params
        i = 0
        self.temp = str(function) + "("
        for t in params:
            if i > 0:
                self.temp += ", "
            self.temp += t.temp
            i += 1
        self.temp += ")"

    # TODO: Agregar un error de parametros incorrectos
    def execute(self, environment):
        type_ = TYPE.NUMBER
        try:
            valores = []
            types = []
            for p in self.params:
                obj = p.execute(environment)
                val = obj.value
                t = obj.type
                if isinstance(val, pd.core.series.Series):
                    val = val.tolist()
                valores.append(val)
                types.append(t)
            # Se toma en cuenta que las funcines matematicas
            # y trigonometricas producen un tipo NUMBER
            type_ = TYPE.NUMBER
            if self.function == "abs":
                value = mf.absolute(*valores)
            elif self.function == "cbrt":
                value = mf.cbrt(*valores)
            elif self.function == "ceil":
                value = mf.ceil(*valores)
            elif self.function == "ceiling":
                value = mf.ceiling(*valores)
            elif self.function == "degrees":
                value = mf.degrees(*valores)
            elif self.function == "div":
                value = mf.div(*valores)
            elif self.function == "exp":
                value = mf.exp(*valores)
            elif self.function == "factorial":
                value = mf.factorial(*valores)
            elif self.function == "floor":
                value = mf.floor(*valores)
            elif self.function == "gcd":
                value = mf.gcd(*valores)
            elif self.function == "lcm":
                value = mf.lcm(*valores)
            elif self.function == "ln":
                value = mf.ln(*valores)
            elif self.function == "log":
                value = mf.log(*valores)
            elif self.function == "log10":
                value = mf.log10(*valores)
            elif self.function == "mod":
                value = mf.mod(*valores)
            elif self.function == "pi":
                value = mf.pi()
            elif self.function == "power":
                value = mf.pow(*valores)
            elif self.function == "radians":
                value = mf.radians(*valores)
            elif self.function == "round":
                value = mf.round_(*valores)
            elif self.function == "sign":
                value = mf.sign(*valores)
            elif self.function == "sqrt":
                value = mf.sqrt(*valores)
            elif self.function == "trunc":
                value = mf.truncate_col(*valores)
            elif self.function == "width_bucket":
                value = mf.with_bucket(*valores)
            elif self.function == "random":
                value = mf.random_()
            elif self.function == "acos":
                value = trf.acos(*valores)
            elif self.function == "acosd":
                value = trf.acosd(*valores)
            elif self.function == "asin":
                value = trf.asin(*valores)
            elif self.function == "asind":
                value = trf.asind(*valores)
            elif self.function == "atan":
                value = trf.atan(*valores)
            elif self.function == "atand":
                value = trf.atand(*valores)
            elif self.function == "atan2":
                value = trf.atan2(*valores)
            elif self.function == "atan2d":
                value = trf.atan2d(*valores)
            elif self.function == "cos":
                value = trf.cos(*valores)
            elif self.function == "cosd":
                value = trf.cosd(*valores)
            elif self.function == "cot":
                value = trf.cot(*valores)
            elif self.function == "cotd":
                value = trf.cotd(*valores)
            elif self.function == "sin":
                value = trf.sin(*valores)
            elif self.function == "sind":
                value = trf.sind(*valores)
            elif self.function == "tan":
                value = trf.tan(*valores)
            elif self.function == "tand":
                value = trf.tand(*valores)
            elif self.function == "sinh":
                value = trf.sinh(*valores)
            elif self.function == "cosh":
                value = trf.cosh(*valores)
            elif self.function == "tanh":
                value = trf.tanh(*valores)
            elif self.function == "asinh":
                value = trf.asinh(*valores)
            elif self.function == "acosh":
                value = trf.acosh(*valores)
            elif self.function == "atanh":
                value = trf.atanh(*valores)
            elif self.function == "length":
                value = strf.lenght(*valores)
            elif self.function == "substring":
                type_ = TYPE.STRING
                value = strf.substring(*valores)
            elif self.function == "trim":
                type_ = TYPE.STRING
                value = strf.trim_(*valores)
            elif self.function == "get_byte":
                value = strf.get_byte(*valores)
            elif self.function == "md5":
                type_ = TYPE.STRING
                value = strf.md5(*valores)
            elif self.function == "set_byte":
                type_ = TYPE.STRING
                value = strf.set_byte(*valores)
            elif self.function == "sha256":
                type_ = TYPE.STRING
                value = strf.sha256(*valores)
            elif self.function == "substr":
                type_ = TYPE.STRING
                value = strf.substring(*valores)
            elif self.function == "convert_date":
                type_ = TYPE.DATETIME
                value = strf.convert_date(*valores)
            elif self.function == "convert_int":
                value = strf.convert_int(*valores)
            elif self.function == "encode":
                type_ = TYPE.STRING
                value = strf.encode(*valores)
            elif self.function == "decode":
                type_ = TYPE.STRING
                value = strf.decode(*valores)
            # Se toma en cuenta que la funcion now produce tipo DATE
            elif self.function == "now":
                type_ = TYPE.DATETIME
                value = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            else:
                # TODO: Agregar un error de funcion desconocida
                value = valores[0]
            if isinstance(value, list):
                if len(value) <= 1:
                    value = value[0]
                else:
                    value = pd.Series(value)
            return Primitive(type_, value, self.temp, self.row, self.column)
        except TypeError:
            expression.list_errors.append(
                "Error: 42883: La funcion "
                + str(self.function)
                + "("
                + str(type_)
                + ") no existe"
                + "\n En la linea: "
                + str(self.row)
            )
        except:
            expression.list_errors.append("Error: P0001: Error en funciones")

    def dot(self):
        f = Nodo.Nodo(self.function)
        p = Nodo.Nodo("PARAMS")
        new = Nodo.Nodo("CALL")
        new.addNode(f)
        new.addNode(p)
        for par in self.params:
            p.addNode(par.dot())
        return new
