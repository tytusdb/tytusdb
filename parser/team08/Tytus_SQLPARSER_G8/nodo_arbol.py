class Nodo_Arbol():
    def __init__(self,valor,tipo):
        self.valor=valor
        self.tipo=tipo
        self.hijos=[]
        
    def agregarHijo(self,hijo):
        self.hijos.insert(hijo)