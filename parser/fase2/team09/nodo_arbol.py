class nodo_arbol():
    def __init__(self,valor,tipo):
        self.valor=valor
        self.id = 0
        self.tipo=tipo
        self.hijos=[]
        
    def agregarHijo(self,hijo):
        self.hijos.append(hijo)

    def modificarId(self, valor):
        self.id = valor
