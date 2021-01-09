import sys, os.path
nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\AST\\')
sys.path.append(nodo_dir)

c3d_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\C3D\\')
sys.path.append(c3d_dir)

from Nodo import Nodo

class Sentencia_Asignacion(Nodo):

    def __init__(self, nombreNodo, fila = -1, columna = -1, valor = None):
        Nodo.__init__(self,nombreNodo, fila, columna, valor)
    
    def execute(self, enviroment):

        identificador = self.hijos[0]
        expresion = self.hijos[1]
        value = expresion.execute(enviroment)

        nombreVariableAsignar = identificador.valor.lower()
        variableBuscar = enviroment.obtenerSimbolo(nombreVariableAsignar)

        if variableBuscar == None :
            print('Error al buscar variable')
        else :
            
            if variableBuscar.data_type.data_type == expresion.tipo.data_type :
                variableBuscar.valor = value
            else:
                print('Error: No coincide el tipo de dato')


        pass
    
    def compile(self, enviroment):
        pass

    def getText(self):
        pass