
class Nodo:
    def __init__(self,etiqueta,hijos=None,esHoja=None, lexema=None):
         self.etiqueta = etiqueta
         self.lexema = lexema

         if hijos :
              self.hijos = hijos
         else:
              self.hijos = []
            

         self.esHoja = esHoja
