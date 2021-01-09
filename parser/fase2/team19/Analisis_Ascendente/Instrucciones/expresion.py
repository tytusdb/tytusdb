class Exp:
    'clase abstracta'


#EXPRESION


class Unario(Exp):
    def __init__(self, operador, op,fila,columna):
        self.operador = operador
        self.op = op
        self.fila = fila
        self.columna = columna


class Primitivo(Exp):
    def __init__(self, valor,fila,columna):
        self.valor = valor
        self.fila = fila
        self.columna = columna

    def getC3D(self, lista_optimizaciones_C3D):
        if isinstance(self.valor, str):
            return "'%s'" % self.valor
        else:
            return self.valor

    def get_quemado(self):
        if isinstance(self.valor, str):
            return "'%s'" % self.valor
        else:
            return self.valor


class Id(Exp):
    def __init__(self, id,fila,columna):
        self.id = id
        self.fila = fila
        self.columna = columna

    def get_quemado(self):
        return self.id

    def getC3D(self, lista_optimizaciones_C3D):
        return self.id

class Funcion(Exp):
    def __init__(self,id,expresiones,fila,columna):
        self.id = id
        self.listaexpresiones = expresiones
        self.fila = fila
        self.columna = columna

    def getC3D(self):
        code = self.id + '('
        exps = ''
        if self.listaexpresiones is not None:
            for exp in self.listaexpresiones:
                if isinstance(exp, Primitivo):
                    if isinstance(exp.valor, str):
                        exps += '\'' + exp.valor + '\'' + ','
                    else:
                        exps += str(exp.valor) + ','
            expresiones = list(exps)
            siz = len(expresiones) - 1
            del (expresiones[siz])
            t = "".join(expresiones)
            code += t
        code += ')'
        return code