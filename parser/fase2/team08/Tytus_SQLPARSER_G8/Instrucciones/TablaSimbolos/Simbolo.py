class Simbolo():
    'Esta clase se utiliza para crear un símbolo de base para una declaración de variable.'

    def __init__(self, id, tipo, valor, linea, columna):
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.linea = linea
        self.columna = columna
        self.rol = ""
        self.posicion = -1
        self.tamanio = 0
        self.ambito = "-" 
        self.funcion = None
        self.constante = False