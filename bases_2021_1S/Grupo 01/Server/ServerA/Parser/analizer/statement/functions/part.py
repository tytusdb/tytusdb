from Parser.analizer.abstract.expression import Expression, TYPE
from Parser.analizer.abstract import expression
from Parser.analizer.reports import Nodo
from datetime import datetime
from Parser.analizer.statement.expressions.primitive import Primitive


class DatePart(Expression):
    def __init__(self, opt, type, str, row, column) -> None:
        super().__init__(row, column)
        self.opt = opt.lower()
        self.type = type
        self.str = str.split()
        self.temp = "date_part( " + opt + " , " + type + " " + str + " )"

    def execute(self, environment):
        try:
            if self.type == "TIMESTAMP":
                if self.str[0] == "now":
                    self.str = datetime.now().strftime("%Y/%m/%d %H:%M:%S").split()
                if self.opt == "years":
                    val = self.str[0][:4]
                elif self.opt == "months":
                    val = self.str[0][5:7]
                elif self.opt == "days":
                    val = self.str[0][8:10]
                elif self.opt == "hours":
                    val = self.str[1][:2]
                elif self.opt == "minutes":
                    val = self.str[1][3:5]
                elif self.opt == "seconds":
                    val = self.str[1][6:8]
                else:
                    expression.list_errors.append(
                        "Error: 22007: Formato de fecha invalido " + str(self.str)
                    )
                    # ERROR
                    val = self.str
            elif self.type == "DATE":
                if self.opt == "years":
                    val = self.str[0][:4]
                elif self.opt == "months":
                    val = self.str[0][5:7]
                elif self.opt == "days":
                    val = self.str[0][8:10]
                else:
                    expression.list_errors.append(
                        "Error: 22007: Formato de fecha invalido " + str(self.str)
                    )
                    # ERROR
                    val = self.str
            elif self.type == "TIME":
                if self.opt == "hours":
                    val = self.str[0][:2]
                elif self.opt == "minutes":
                    val = self.str[0][3:5]
                elif self.opt == "seconds":
                    val = self.str[0][6:8]
                else:
                    expression.list_errors.append(
                        "Error: 22007: Formato de fecha invalido " + str(self.str)
                    )
                    # ERROR
                    val = self.str
            elif self.type == "INTERVAL":
                if self.opt == "years":
                    idx = self.str.index("years")
                    val = self.str[idx - 1]
                elif self.opt == "months":
                    idx = self.str.index("months")
                    val = self.str[idx - 1]
                elif self.opt == "days":
                    idx = self.str.index("days")
                    val = self.str[idx - 1]
                elif self.opt == "hours":
                    idx = self.str.index("hours")
                    val = self.str[idx - 1]
                elif self.opt == "minutes":
                    idx = self.str.index("minutes")
                    val = self.str[idx - 1]
                elif self.opt == "seconds":
                    idx = self.str.index("seconds")
                    val = self.str[idx - 1]
                else:
                    expression.list_errors.append(
                        "Error: 22007: Formato de fecha invalido " + str(self.str)
                    )
                    # ERROR
                    val = self.str
            elif self.type == "NOW":
                self.str = datetime.now().strftime("%Y/%m/%d %H:%M:%S").split()
                if self.opt == "years":
                    val = self.str[0][:4]
                elif self.opt == "months":
                    val = self.str[0][5:7]
                elif self.opt == "days":
                    val = self.str[0][8:10]
                elif self.opt == "hours":
                    val = self.str[1][:2]
                elif self.opt == "minutes":
                    val = self.str[1][3:5]
                elif self.opt == "seconds":
                    val = self.str[1][6:8]
                else:
                    expression.list_errors.append(
                        "Error: 22007: Formato de fecha invalido " + str(self.str)
                    )
                    # ERROR
                    val = self.str
            else:
                val = self.str
                expression.list_errors.append(
                    "Error: 22007: Formato de fecha invalido " + str(self.str)
                )
                # ERROR
            return Primitive(TYPE.NUMBER, int(val), self.temp, self.row, self.column)
        except TypeError:
            expression.list_errors.append(
                "Error: 42804: discrepancia de tipo de datos "
            )
            pass
        except ValueError:  # cuando no tiene el valor INTERVAL
            expression.list_errors.append(
                "Error: 22007:sintaxis de entrada no válida para el tipo 'interval' "
            )
            pass

    def dot(self):
        f = Nodo.Nodo("date_part")
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
