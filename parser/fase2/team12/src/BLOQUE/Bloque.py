import sys, os.path
nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\AST\\')
sys.path.append(nodo_dir)

c3d_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\C3D\\')
sys.path.append(c3d_dir)

group_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\DML\\Groups')
sys.path.append(group_path)

from Nodo import Nodo
from Union import Union
from UnionAll import UnionAll
from Intersect import Intersect
from Except import Except

class Bloque(Nodo):

    def __init__(self, nombreNodo, fila = -1, columna = -1, valor = None):
        Nodo.__init__(self,nombreNodo, fila, columna, valor)
    
    def execute(self, enviroment):
        
        for hijo in self.hijos:

            if hijo.nombreNodo == 'SENTENCIA_INSERT':
                hijo.execute(enviroment)

            elif hijo.nombreNodo == 'SENTENCIA_UPDATE':
                hijo.execute(enviroment)
            
            elif hijo.nombreNodo == 'SENTENCIA_DELETE':
                hijo.execute(enviroment)
            
            elif hijo.nombreNodo == 'SENTENCIA_SELECT':
                hijo.execute(enviroment)
            
            elif hijo.nombreNodo == 'SENTENCIA_UNION':
                nuevoUnion = Union()
                resp = nuevoUnion.execute(hijo)
            
            elif hijo.nombreNodo == 'SENTENCIA_UNION_ALL':
                nuevoUnionAll = UnionAll()
                resp = nuevoUnionAll.execute(hijo)
            
            elif hijo.nombreNodo == 'SENTENCIA_INTERSECT':
                nuevoIntersect = Intersect()
                resp = nuevoIntersect.execute(hijo)
            
            elif hijo.nombreNodo == 'SENTENCIA_EXCEPT':
                nuevoExcept = Except()                
                resp = nuevoExcept.execute(hijo)                    

            elif hijo.nombreNodo == 'SENTENCIA_ASIGNACION':
                hijo.execute(enviroment)
            
            elif hijo.nombreNodo == 'SENTENCIA_IF':
                valor = hijo.execute(enviroment)

                if valor != None :
                    return valor
            
            elif hijo.nombreNodo == 'SENTENCIA_RETURN':
                #print('Vino Return')
                return hijo.execute(enviroment)
                        
        pass

    def compile(self, enviroment):

        textoCompile = []

        for hijo in self.hijos:

            if hijo.nombreNodo == 'SENTENCIA_INSERT':
                textoCompile += hijo.compile().splitlines()
                textoCompile.append("execute()")

            elif hijo.nombreNodo == 'SENTENCIA_UPDATE':
                textoCompile += hijo.compile().splitlines()
                textoCompile.append("execute()")
            
            elif hijo.nombreNodo == 'SENTENCIA_DELETE':
                textoCompile += hijo.compile().splitlines()
                textoCompile.append("execute()")

            
            elif hijo.nombreNodo == 'SENTENCIA_SELECT':
                textoCompile += hijo.compile(enviroment)
                textoCompile.append("execute()")
            
            elif hijo.nombreNodo == 'SENTENCIA_UNION':
                nuevoUnion = Union()
                #resp = nuevoUnion.execute(hijo)
            
            elif hijo.nombreNodo == 'SENTENCIA_UNION_ALL':
                nuevoUnionAll = UnionAll()
                #resp = nuevoUnionAll.execute(hijo)
            
            elif hijo.nombreNodo == 'SENTENCIA_INTERSECT':
                nuevoIntersect = Intersect()
                #resp = nuevoIntersect.execute(hijo)
            
            elif hijo.nombreNodo == 'SENTENCIA_EXCEPT':
                nuevoExcept = Except()                
                #resp = nuevoExcept.execute(hijo)                    

            elif hijo.nombreNodo == 'SENTENCIA_ASIGNACION':
                textoCompile += hijo.compile(enviroment)
            
            elif hijo.nombreNodo == 'SENTENCIA_IF':
                textoCompile += hijo.compile(enviroment)
        return textoCompile

    def getText(self):
        pass