class temporalesp():
    
    def __init__(self, numero=0, posiciones = [], actual ='', anterior = '', siguiente = '' ):
        self.numero = 0
        self.posiciones = posiciones
        self.actual = actual
        self.anterior = anterior
        self.siguiente = siguiente


    def incTemporal(self):
        self.numero += 1
        return self.numero

    def addPosicion(self, nombre : str, posicion : int):
        itempos = []
        itempos.append(nombre)
        itempos.append(posicion)
        self.posiciones.append(itempos)
        return 0

    