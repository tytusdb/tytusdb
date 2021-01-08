from optimizer_folder.Element import Element


class Quadruple:

    T_ARITOP = 1
    T_LABEL = 2
    T_GOTO = 3
    T_IF = 4
    T_IGNORE = 5
    T_ASIG = 6
    T_COMMENT = 8
    T_IF_CASE = 9
    T_LABEL_CASE = 10
    T_GOTO_CASE = 11

    def constructor_1(self, Elem1, Elem2, Elem3, op, type, l, tab):
        self.Elem1 = Elem1
        self.Elem2 = Elem2
        self.resultado = Elem3
        self.comment = 0
        switcher = {
            ">": 1,
            "<": 2,
            "!=": 3,
            "=": 4,
            ">=": 5,
            "<=": 6,
            "%": 7,
            "/": 8,
            "*": 9,
            "-": 10,
            "+": 11,
            "and": 12,
            "AND": 12,
            "OR":13,
            "or": 13,
            "= not": 14,
            "": -1,
        }
        self.tab = tab
        self.operador = switcher.get(op, 12)
        self.type = type
        self.line = l

    def __init__(self):
        self.Elem1 = Element()
        self.Elem2 = Element()
        self.resultado = Element()
        self.operador = -1
        self.type = 0
        self.line = -1
        self.typeOpt = 0
        self.comment = 0
        self.tab = False

    def constructor_3(self, Quadruple):
        elem1 = Element()
        elem1.copy(Quadruple.Elem1)
        elem2 = Element()
        elem1.copy(Quadruple.Elem2)
        elem3 = Element()
        elem1.copy(Quadruple.resultado)
        self.constructor_1(
            elem1,
            elem2,
            elem3,
            Quadruple.operador,
            Quadruple.type,
            Quadruple.line,
            Quadruple.tab,
        )
        self.typeOpt = Quadruple.typeOpt

    def __str__(self):
        ret = ""
        signo = ""
        switcher = {
            1: ">",
            2: "<",
            3: "!=",
            4: "=",
            5: ">=",
            6: "<=",
            7: "%",
            8: "/",
            9: "*",
            10: "-",
            11: "+",
            12: "and",
            13: "or",
            14: "= not",
            -1: "",
        }

        signo = switcher.get(self.operador, "?")
        switcher_type = {
            1: str(self.resultado)
            + " = "
            + str(self.Elem1)
            + " "
            + signo
            + " "
            + str(self.Elem2),
            2: "label ." + str(self.resultado),
            3: "goto ." + str(self.resultado),
            4: "if " + str(self.Elem1) + ": goto ." + str(self.resultado),
            5: str(self.Elem1),
            6: str(self.resultado) + " = " + str(self.Elem1),
            9: "if " + str(self.Elem1) + ": goto ." + str(self.resultado),
            10: "label ." + str(self.resultado),
            11: "goto ." + str(self.resultado),
        }

        ret = switcher_type.get(self.type, "//--")
        if self.tab:
            ret = "\t" + ret
        return ret