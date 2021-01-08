from analizer.abstract.expression import Expression, TYPE
from analizer.abstract import expression
from analizer.reports import Nodo
from datetime import datetime
from analizer.statement.expressions.primitive import Primitive
import pandas as pd


class ExtractDate(Expression):
    def __init__(self, opt, type, str, row, column):
        super().__init__(row, column)
        self.opt = opt
        self.type = type
        self.str = str.split()
        self.temp = "EXTRACT( " + opt + " FROM " + type + " " + str + " )"

    def execute(self, environment):
        try:
            if self.type == "TIMESTAMP":
                if self.str[0] == "now":
                    self.str = datetime.now().strftime("%Y/%m/%d %H:%M:%S").split()
                if self.opt == "YEAR":
                    val = self.str[0][:4]
                elif self.opt == "MONTH":
                    val = self.str[0][5:7]
                elif self.opt == "DAY":
                    val = self.str[0][8:10]
                elif self.opt == "HOUR":
                    val = self.str[1][:2]
                elif self.opt == "MINUTE":
                    val = self.str[1][3:5]
                elif self.opt == "SECOND":
                    val = self.str[1][6:8]
                else:
                    val = self.str
                    raise Exception
            elif self.type == "DATE":
                if self.opt == "YEAR":
                    val = self.str[0][:4]
                elif self.opt == "MONTH":
                    val = self.str[0][5:7]
                elif self.opt == "DAY":
                    val = self.str[0][8:10]
                else:
                    val = self.str
                    raise Exception
            elif self.type == "TIME":
                if self.opt == "HOUR":
                    val = self.str[0][:2]
                elif self.opt == "MINUTE":
                    val = self.str[0][3:5]
                elif self.opt == "SECOND":
                    val = self.str[0][6:8]
                else:
                    val = self.str
                    raise Exception
            elif self.type == "INTERVAL":
                if self.opt == "YEAR":
                    idx = self.str.index("years")
                    val = self.str[idx - 1]
                elif self.opt == "MONTH":
                    idx = self.str.index("months")
                    val = self.str[idx - 1]
                elif self.opt == "DAY":
                    idx = self.str.index("days")
                    val = self.str[idx - 1]
                elif self.opt == "HOUR":
                    idx = self.str.index("hours")
                    val = self.str[idx - 1]
                elif self.opt == "MINUTE":
                    idx = self.str.index("minutes")
                    val = self.str[idx - 1]
                elif self.opt == "SECOND":
                    idx = self.str.index("seconds")
                    val = self.str[idx - 1]
                else:
                    val = self.str
                    raise Exception
            else:
                val = self.str
                raise Exception
            return Primitive(TYPE.NUMBER, int(val), self.temp, self.row, self.column)
        except TypeError:
            expression.list_errors.append(
                "Error: 42804: discrepancia de tipo de datos "
            )
        except ValueError:  # cuando no tiene el valor INTERVAL
            expression.list_errors.append(
                "Error: 22007:sintaxis de entrada no válida para el tipo 'interval' "
            )
        except:
            expression.list_errors.append(
                "Error: 22007: Formato de fecha invalido " + str(self.str)
            )

    def dot(self):
        f = Nodo.Nodo("EXTRACT")
        p = Nodo.Nodo("PARAMS")
        new = Nodo.Nodo("CALL")
        new.addNode(f)
        new.addNode(p)
        ntype = Nodo.Nodo(str(self.type))
        nstr = Nodo.Nodo(str(self.str))
        nopt = Nodo.Nodo(str(self.opt))
        p.addNode(nopt)
        p.addNode(ntype)
        p.addNode(nstr)
        return new


class ExtractColumnDate(Expression):
    def __init__(self, opt, colData, row, column):
        super().__init__(row, column)
        self.opt = opt
        self.colData = colData
        self.temp = "EXTRACT( " + opt + " FROM " + colData.temp + " )"

    def execute(self, environment):
        try:
            valores = self.colData.execute(environment)

            if isinstance(valores.value, pd.core.series.Series):
                lst = valores.value.tolist()
                lst = [v.split() for v in lst]
            else:
                lst = [valores.split()]
            if valores.type == TYPE.TIMESTAMP or valores.type == TYPE.DATETIME:
                if self.opt == "YEAR":
                    val = [date[0][:4] for date in lst]
                elif self.opt == "MONTH":
                    val = [date[0][5:7] for date in lst]
                elif self.opt == "DAY":
                    val = [date[0][8:10] for date in lst]
                elif self.opt == "HOUR":
                    val = [date[1][:2] for date in lst]
                elif self.opt == "MINUTE":
                    val = [date[1][3:5] for date in lst]
                elif self.opt == "SECOND":
                    val = [date[1][6:8] for date in lst]
                else:
                    # ERROR
                    expression.list_errors.append(
                        "Error: 22007: Formato de fecha invalido " + str(self.str)
                    )
                    val = self.str
            elif valores.type == TYPE.DATE:
                if self.opt == "YEAR":
                    val = [date[0][:4] for date in lst]
                elif self.opt == "MONTH":
                    val = [date[0][5:7] for date in lst]
                elif self.opt == "DAY":
                    val = [date[0][8:10] for date in lst]
                else:
                    val = self.str
                    raise Exception
            elif valores.type == TYPE.TIME:
                if self.opt == "HOUR":
                    val = [date[0][:2] for date in lst]
                elif self.opt == "MINUTE":
                    val = [date[0][3:5] for date in lst]
                elif self.opt == "SECOND":
                    val = [date[0][6:8] for date in lst]
                else:
                    val = self.str
                    raise Exception
            else:
                val = self.str
                raise Exception
            if isinstance(val, list):
                if len(val) <= 1:
                    val = val[0]
                else:
                    val = pd.Series(val)

            return Primitive(TYPE.NUMBER, val, self.temp, self.row, self.column)
        except TypeError:
            expression.list_errors.append(
                "Error: 42804: discrepancia de tipo de datos "
            )
        except ValueError:  # cuando no tiene el valor INTERVAL
            expression.list_errors.append(
                "Error: 22007:sintaxis de entrada no válida para el tipo 'interval' "
            )
        except:
            raise expression.list_errors.append(
                "Error: 22007: Formato de fecha invalido " + str(self.str)
            )

    def dot(self):
        f = Nodo.Nodo("EXTRACT")
        p = Nodo.Nodo("PARAMS")
        new = Nodo.Nodo("CALL")
        new.addNode(f)
        new.addNode(p)
        nstr = Nodo.Nodo(str(self.colData.temp))
        nopt = Nodo.Nodo(str(self.opt))
        p.addNode(nopt)
        p.addNode(nstr)
        return new