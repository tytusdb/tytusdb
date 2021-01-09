from tkinter.constants import TRUE
from optimizer_folder.Element import Element
from optimizer_folder.Quadruple import Quadruple
import copy
from analizer_pl import grammar


class Optimizer:

    OL_MAYORQUE = 1
    OL_MENORQUE = 2
    OL_DISTINTODE = 3
    OL_IGUAL = 4
    OL_MAYORIGUALQUE = 5
    OL_MENORIGUALQUE = 6
    OP_MODULAR = 7
    OP_DIVISION = 8
    OP_PRODUCTO = 9
    OP_RESTA = 10
    OP_SUMA = 11
    OP_AND = 12
    OP_OR = 13
    OP_NOT = 14
    TOP_ARIT = 1
    TOP_JUMP = 2
    TOP_PROP = 4
    TOP_EXP = 8
    fuente = list()
    sumidero = list()
    registro = list()
    iteradorAuxiliar = 0

    def addIgnoreString(self, cadena, line, tab):
        new = Quadruple()
        elem1 = Element()
        elem1.constructor1(cadena, -1)
        new.constructor_1(elem1, None, None, -1, Quadruple.T_IGNORE, line, tab)
        self.fuente.append(new)

    def addLabel(self, cadena, line, tab=True):
        new = Quadruple()
        elem1 = Element()
        elem1.constructor1(cadena, Element.E_LABEL)
        new.constructor_1(None, None, elem1, -1, Quadruple.T_LABEL, line, tab)
        self.fuente.append(new)

    def addGoto(self, cadena, line, tab=True):
        new = Quadruple()
        elem1 = Element()
        elem1.constructor1(cadena, Element.E_GOTO)
        new.constructor_1(None, None, elem1, -1, Quadruple.T_GOTO, line, tab)
        self.fuente.append(new)
        return len(self.fuente)

    def addGoto_IF(self, cadena, line, index, tab=True):
        new = Quadruple()
        elem1 = Element()
        elem1.constructor1(cadena, Element.E_GOTO)
        new.constructor_1(None, None, elem1, -1, Quadruple.T_GOTO, line, tab)
        self.fuente[index] = new

    def addIF(self, op1, gt, line, tab=True):
        new = Quadruple()
        elem1 = Element()
        elem1.constructor1(op1, Element.E_SCALAR)
        elem2 = Element()
        elem2.constructor1(gt, Element.E_GOTO)
        new.constructor_1(elem1, None, elem2, None, Quadruple.T_IF, line, tab)
        self.fuente.append(new)

    def addIF_CASE(self, op1, gt, line, tab=True):
        new = Quadruple()
        elem1 = Element()
        elem1.constructor1(op1, Element.E_SCALAR)
        elem2 = Element()
        elem2.constructor1(gt, Element.E_GOTO)
        new.constructor_1(elem1, None, elem2, None, Quadruple.T_IF_CASE, line, tab)
        self.fuente.append(new)

    def addLabel_CASE(self, cadena, line, tab=True):
        new = Quadruple()
        elem1 = Element()
        elem1.constructor1(cadena, Element.E_LABEL)
        new.constructor_1(None, None, elem1, -1, Quadruple.T_LABEL_CASE, line, tab)
        self.fuente.append(new)

    def addGoto_CASE(self, cadena, line, tab=True):
        new = Quadruple()
        elem1 = Element()
        elem1.constructor1(cadena, Element.E_GOTO)
        new.constructor_1(None, None, elem1, -1, Quadruple.T_GOTO_CASE, line, tab)
        self.fuente.append(new)
        return len(self.fuente)

    def addScalarAsig(self, dest, src, line, tab):
        new = Quadruple()
        elem1 = Element()
        elem1.constructor1(src, Element.E_SCALAR)
        elem2 = Element()
        elem2.constructor1(dest, Element.E_SCALAR)
        new.constructor_1(elem1, None, elem2, -1, Quadruple.T_ASIG, line, tab)
        self.fuente.append(new)

    def addAritOp(self, dest, op1, op2, op, line, tab):
        new = Quadruple()
        elem1 = Element()
        elem1.constructor1(op1, Element.E_SCALAR)
        elem2 = Element()
        elem2.constructor1(op2, Element.E_GOTO)
        elem3 = Element()
        elem3.constructor1(dest, Element.E_SCALAR)
        new.constructor_1(elem1, elem2, elem3, op, Quadruple.T_ARITOP, line, tab)
        self.fuente.append(new)

    def init(self):
        self.fuente.clear()
        self.sumidero.clear()
        self.registro.clear()

    def optimization_of_common_expressions(self):
        actual = Quadruple()
        pivote = Quadruple()
        i = 0
        j = 0
        while i < len(self.fuente):
            pivote = self.fuente[i]
            if pivote.type == Quadruple.T_ARITOP:
                j = i + 1
                while j < len(self.fuente):
                    actual = self.fuente[j]
                    if actual.type == Quadruple.T_ARITOP:
                        if (
                            not (actual.resultado.id == pivote.resultado.id)
                            and not (actual.resultado.id == pivote.Elem1.id)
                            and not (actual.resultado.id == pivote.Elem2.id)
                        ):
                            if actual.operador == pivote.operador:
                                if (
                                    (actual.Elem1.id == pivote.Elem1.id)
                                    and (actual.Elem2.id == pivote.Elem2.id)
                                ) or (
                                    (actual.Elem1.id == pivote.Elem2.id)
                                    and (actual.Elem2.id == pivote.Elem1.id)
                                ):
                                    actual.Elem1 = pivote.resultado
                                    actual.Elem2 = None
                                    actual.operador = -1
                                    actual.type = Quadruple.T_ASIG
                                    actual.typeOpt = actual.typeOpt
                    else:
                        j = len(self.fuente)
                    j += 1
            i += 1

    def optimization_elimination_of_redundant(self):
        actual = Quadruple()
        i = 0
        while i < len(self.fuente):
            actual = self.fuente[i]
            # t = t -> eliminacion
            if actual.type == Quadruple.T_ASIG:
                if actual.resultado.id == actual.Elem1.id:
                    self.registro.append(
                        "---------------------------------------------"
                    )
                    self.registro.append("Regla 8 - 11")
                    self.registro.append(
                        actual.resultado.id + "=" + actual.Elem1.id + " -> Eliminacion"
                    )
                    del self.fuente[i]
                    i -= 1
            i += 1

    def arithmetic_optimization(self):
        iterator = iter(self.fuente)
        actual = Quadruple()
        nuevo = Quadruple()
        while True:
            try:
                actual = next(iterator)
                nuevo = copy.deepcopy(actual)
                if actual.type == Quadruple.T_ARITOP:
                    if actual.operador == self.OP_DIVISION:
                        # x = y/1 -> x=y
                        if actual.Elem2.id == "1":
                            nuevo.operador = -1
                            nuevo.type = Quadruple.T_ASIG
                            nuevo.typeOpt = self.TOP_ARIT
                            self.registro.append(
                                "---------------------------------------------"
                            )
                            self.registro.append("Regla 15")
                            self.registro.append(
                                actual.resultado.id
                                + "="
                                + actual.Elem1.id
                                + "/"
                                + actual.Elem2.id
                                + " -> "
                                + nuevo.resultado.id
                                + "="
                                + nuevo.Elem1.id
                            )
                            nuevo.Elem2 = None
                        if actual.Elem1.id == "0":
                            nuevo.Elem1.id = "0"
                            nuevo.operador = -1
                            nuevo.type = Quadruple.T_ASIG
                            nuevo.typeOpt = self.TOP_ARIT
                            self.registro.append(
                                "---------------------------------------------"
                            )
                            self.registro.append("Regla 18")
                            self.registro.append(
                                actual.resultado.id
                                + "="
                                + actual.Elem1.id
                                + "/"
                                + actual.Elem2.id
                                + " -> "
                                + nuevo.resultado.id
                                + "="
                                + nuevo.Elem1.id
                            )
                            nuevo.Elem2 = None
                    elif actual.operador == self.OP_PRODUCTO:
                        # x=y*1
                        if actual.Elem2.id == "1":
                            nuevo.operador = -1
                            nuevo.type = Quadruple.T_ASIG
                            nuevo.typeOpt = self.TOP_ARIT
                            self.registro.append(
                                "---------------------------------------------"
                            )
                            self.registro.append("Regla 14")
                            self.registro.append(
                                actual.resultado.id
                                + "="
                                + actual.Elem1.id
                                + "*"
                                + actual.Elem2.id
                                + " -> "
                                + nuevo.resultado.id
                                + "="
                                + nuevo.Elem1.id
                            )
                            nuevo.Elem2 = None
                            # x=1*y
                        elif actual.Elem1.id == "1":
                            nuevo.Elem1 = nuevo.Elem2
                            nuevo.operador = -1
                            nuevo.type = Quadruple.T_ASIG
                            nuevo.typeOpt = self.TOP_ARIT
                            self.registro.append(
                                "---------------------------------------------"
                            )
                            self.registro.append("Regla 14")
                            self.registro.append(
                                actual.resultado.id
                                + "="
                                + actual.Elem1.id
                                + "*"
                                + actual.Elem2.id
                                + " -> "
                                + nuevo.resultado.id
                                + "="
                                + nuevo.Elem1.id
                            )
                            nuevo.Elem2 = None
                        # x=y*0 or 0*y
                        elif actual.Elem1.id == "0" or actual.Elem2.id == "0":
                            nuevo.Elem1.constructor1("0", Element.E_SCALAR)
                            nuevo.operador = -1
                            nuevo.type = Quadruple.T_ASIG
                            nuevo.typeOpt = self.TOP_ARIT
                            self.registro.append(
                                "---------------------------------------------"
                            )
                            self.registro.append("Regla 17")
                            self.registro.append(
                                actual.resultado.id
                                + "="
                                + actual.Elem1.id
                                + "*"
                                + actual.Elem2.id
                                + " -> "
                                + nuevo.resultado.id
                                + "="
                                + nuevo.Elem1.id
                            )
                            nuevo.Elem2 = None
                        # x=y*2=y+y or 2*y=y+y
                        elif actual.Elem1.id != actual.Elem2.id:
                            if actual.Elem1.id == "2":
                                if actual.Elem2.id.isalnum():
                                    nuevo.Elem1.constructor1(
                                        actual.Elem2.id, Element.E_SCALAR
                                    )
                                    nuevo.Elem2.constructor1(
                                        actual.Elem2.id, Element.E_SCALAR
                                    )
                                    nuevo.operador = 11
                                    nuevo.typeOpt = self.TOP_ARIT
                                    self.registro.append(
                                        "---------------------------------------------"
                                    )
                                    self.registro.append("Regla 16")
                                    self.registro.append(
                                        actual.resultado.id
                                        + "="
                                        + actual.Elem1.id
                                        + "*"
                                        + actual.Elem2.id
                                        + " -> "
                                        + nuevo.resultado.id
                                        + "="
                                        + nuevo.Elem1.id
                                        + "+"
                                        + nuevo.Elem2.id
                                    )
                            elif actual.Elem2.id == "2":
                                if actual.Elem1.id.isalnum():
                                    nuevo.Elem1.constructor1(
                                        actual.Elem1.id, Element.E_SCALAR
                                    )
                                    nuevo.Elem2.constructor1(
                                        actual.Elem1.id, Element.E_SCALAR
                                    )
                                    nuevo.operador = 11
                                    nuevo.typeOpt = self.TOP_ARIT
                                    self.registro.append(
                                        "---------------------------------------------"
                                    )
                                    self.registro.append("Regla 16")
                                    self.registro.append(
                                        actual.resultado.id
                                        + "="
                                        + actual.Elem1.id
                                        + "*"
                                        + actual.Elem2.id
                                        + " -> "
                                        + nuevo.resultado.id
                                        + "="
                                        + nuevo.Elem1.id
                                        + "+"
                                        + nuevo.Elem2.id
                                    )
                    elif actual.operador == self.OP_RESTA:
                        # x=y-0 -> x=y
                        if actual.Elem2.id == "0":
                            nuevo.operador = -1
                            nuevo.type = Quadruple.T_ASIG
                            nuevo.typeOpt = self.TOP_ARIT
                            self.registro.append(
                                "---------------------------------------------"
                            )
                            self.registro.append("Regla 13")
                            self.registro.append(
                                actual.resultado.id
                                + "="
                                + actual.Elem1.id
                                + "-"
                                + actual.Elem2.id
                                + " -> "
                                + nuevo.resultado.id
                                + "="
                                + nuevo.Elem1.id
                            )
                            nuevo.Elem2 = None
                        # x=0-y -> x=-y
                        elif actual.Elem1.id == "0":
                            nuevo.Elem1 = nuevo.Elem2
                            nuevo.Elem1.id = " - " + nuevo.Elem1.id
                            nuevo.operador = -1
                            nuevo.type = Quadruple.T_ASIG
                            nuevo.typeOpt = self.TOP_ARIT
                            self.registro.append(
                                "---------------------------------------------"
                            )
                            self.registro.append("Regla 13")
                            self.registro.append(
                                actual.resultado.id
                                + "="
                                + actual.Elem1.id
                                + "-"
                                + actual.Elem2.id
                                + " -> "
                                + nuevo.resultado.id
                                + "="
                                + nuevo.Elem1.id
                            )
                            nuevo.Elem2 = None
                    elif actual.operador == self.OP_SUMA:
                        # x=y+0 -> x=y
                        if actual.Elem2.id == "0":
                            nuevo.operador = -1
                            nuevo.type = Quadruple.T_ASIG
                            nuevo.typeOpt = self.TOP_ARIT
                            self.registro.append(
                                "---------------------------------------------"
                            )
                            self.registro.append("Regla 12")
                            self.registro.append(
                                actual.resultado.id
                                + "="
                                + actual.Elem1.id
                                + "+"
                                + actual.Elem2.id
                                + " -> "
                                + nuevo.resultado.id
                                + "="
                                + nuevo.Elem1.id
                            )
                            nuevo.Elem2 = None
                        # x=0+y -> x=y
                        elif actual.Elem1.id == "0":
                            nuevo.Elem1 = nuevo.Elem2
                            nuevo.operador = -1
                            nuevo.type = Quadruple.T_ASIG
                            nuevo.typeOpt = self.TOP_ARIT
                            self.registro.append(
                                "---------------------------------------------"
                            )
                            self.registro.append("Regla 12")
                            self.registro.append(
                                actual.resultado.id
                                + "="
                                + actual.Elem1.id
                                + "+"
                                + actual.Elem2.id
                                + " -> "
                                + nuevo.resultado.id
                                + "="
                                + nuevo.Elem1.id
                            )
                            nuevo.Elem2 = None
                self.sumidero.append(nuevo)
            except StopIteration:
                break
        self.fuente = self.sumidero.copy()

    def copy_propagation_optimization(self):
        actual = Quadruple()
        pivote = Quadruple()
        updated = False
        i = 0
        j = 0
        while i < len(self.fuente):
            pivote = self.fuente[i]
            if pivote.type == Quadruple.T_ASIG:
                j = i + 1
                while j < len(self.fuente):
                    actual = self.fuente[j]
                    # x = t
                    # t = x -> x = t
                    if actual.type == Quadruple.T_ASIG:
                        if (
                            actual.resultado.id == pivote.Elem1.id
                            and actual.Elem1.id == pivote.resultado.id
                        ):
                            self.registro.append(
                                "---------------------------------------------"
                            )
                            self.registro.append("Regla 1")
                            self.registro.append(
                                pivote.resultado.id
                                + "="
                                + pivote.Elem1.id
                                + "\n#"
                                + actual.resultado.id
                                + "="
                                + actual.Elem1.id
                                + " \n # -> "
                                + pivote.resultado.id
                                + "="
                                + pivote.Elem1.id
                            )
                            del self.fuente[j]
                            j += 1
                        else:
                            j = len(self.fuente)
                    j += 1
            i += 1

    def optimization_by_jump_goto(self):
        actual = Quadruple()
        pivote = Quadruple()
        i = 0
        j = 0
        while i < len(self.fuente):
            pivote = self.fuente[i]
            if pivote.type == Quadruple.T_GOTO:
                j = i + 1
                while j < len(self.fuente):
                    actual = self.fuente[j]
                    # goto .label
                    # codigo inalcanzable
                    # label .label -> label .label
                    if actual.type == Quadruple.T_LABEL:
                        if pivote.resultado.id == actual.resultado.id:
                            self.registro.append(
                                "---------------------------------------------"
                            )
                            self.registro.append("Regla 2")
                            p = i
                            while p < j:
                                self.registro.append(str(self.fuente[i]))
                                del self.fuente[i]
                                p += 1
                            self.registro.append(str(actual) + "-> " + str(actual))
                            j = len(self.fuente)
                        else:
                            j = len(self.fuente)
                    elif actual.type == Quadruple.T_LABEL_CASE:
                        j = len(self.fuente)
                    elif actual.type == Quadruple.T_GOTO:
                        # goto .label
                        # goto .label -> goto.label
                        if pivote.resultado.id == actual.resultado.id:
                            self.registro.append(
                                "---------------------------------------------"
                            )
                            self.registro.append(str(pivote))
                            self.registro.append(str(actual))
                            self.registro.append("-> " + str(actual))
                            del self.fuente[i]
                            i += 1
                        # goto .label1
                        # goto .label -> goto.label1
                        else:
                            self.registro.append(
                                "---------------------------------------------"
                            )
                            self.registro.append(str(pivote))
                            self.registro.append(str(actual))
                            self.registro.append("-> " + str(pivote))
                            del self.fuente[j]
                    j += 1
            i += 1

    def optimization_by_jump_label(self):
        actual = Quadruple()
        pivote = Quadruple()
        i = 0
        while i < len(self.fuente):
            pivote = self.fuente[i]
            # label .label
            # goto .label -> goto.label
            if pivote.type == Quadruple.T_LABEL:
                if i + 1 < len(self.fuente):
                    actual = self.fuente[i + 1]
                    if actual.type == Quadruple.T_GOTO:
                        self.registro.append(
                            "---------------------------------------------"
                        )
                        self.registro.append("Regla 7")
                        self.registro.append(str(pivote))
                        self.registro.append(str(actual))
                        self.registro.append("-> " + str(actual))
                        del self.fuente[i]
                        i -= 1
            i += 1

    def optimization_if_jump(self):
        pivote = Quadruple()
        i = 0
        while i < len(self.fuente):
            pivote = self.fuente[i]
            # if expBoll goto .label1          if !expBoll goto .label2
            # goto .label2                       instrucciones
            # label .label1                      label .label2
            # instrucciones
            # label .label2
            if pivote.type == Quadruple.T_IF:
                self.registro.append("---------------------------------------------")
                self.registro.append("Regla 3")
                self.registro.append(str(pivote))
                self.registro.append(str(self.fuente[i + 1]))
                self.registro.append(str(self.fuente[i + 2]))
                pivote.Elem1.id = "not " + pivote.Elem1.id
                pivote.resultado = self.fuente[i + 1].resultado
                self.registro.append("->" + str(pivote))
                del self.fuente[i + 1]
                del self.fuente[i + 1]
            i += 2

    def optimize(self):
        try:
            self.arithmetic_optimization()
            self.optimization_of_common_expressions()
            self.copy_propagation_optimization()
            self.optimization_elimination_of_redundant()
            self.optimization_if_jump()
            # La regla 7 se contrandice con otras
            self.optimization_by_jump_label()
            self.optimization_by_jump_goto()
            temp = self.generatedOutput()
            self.fuente.clear()
            self.sumidero.clear()
            self.registro.clear()
            return temp
        except:
            grammar.PL_errors.append("Error en la optimizacion")
            return "Error en la optimizacion"

    def generatedOutput(self):
        iterator = iter(self.fuente)
        actual = Quadruple()
        cod = ""
        while True:
            try:
                actual = next(iterator)
                cod += (str(actual)) + "\n"
            except StopIteration:
                break
        iterator = iter(self.registro)
        while True:
            try:
                new = next(iterator)
                cod += "#" + (str(new)) + "\n"
            except StopIteration:
                break
        return cod
