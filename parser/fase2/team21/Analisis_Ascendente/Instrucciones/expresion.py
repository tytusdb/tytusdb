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
    def __init__(self, valor,fila,columna, cadena):
        self.valor = valor
        self.fila = fila
        self.columna = columna
        self.cadena = cadena

    def ObtenerCadenaEntrada(prim):
        valor =''
        if isinstance(prim.valor,str):
            if str(prim.valor).upper() =='TRUE' or  str(prim.valor).upper() =='FALSE':
                return str(prim.valor)
            return '\''+str(prim.valor)+'\''
        else:
            return str(prim.valor)



class Id(Exp):
    def __init__(self, id,fila,columna):
        self.id = id
        self.fila = fila
        self.columna = columna
