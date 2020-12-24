
import os

class nodoGramatical():

    def __init__(self, instruccion):
        self. instruccion= instruccion
        self. listDetalle=[]

    def agregarDetalle(self, detalle):
        self.listDetalle.append(detalle)



class nodoArbol():
    def __init__(self, id , etiquetav):
        self.id = id
        self.etiquetav= etiquetav


class nodoDireccion():
    def __init__(self, id):
        self.id = id
        self.listDirecciones=[]

    def agregar(self,direccion):
        self.listDirecciones.append(direccion)
        

class contenidoG():
    def __init__(self, parse, grafica , listNodes, listDirec):
        self.parse= parse
        self.grafica= grafica
        self.listNodes = listNodes
        self.listDirec = listDirec