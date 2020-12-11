import abc
class Nodo(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def analizar(self,TS,Errores):
        pass
    @abc.abstractmethod
    def getC3D(self,TS):
        pass
    @abc.abstractmethod
    def graficarasc(self,padre,grafica):
        pass