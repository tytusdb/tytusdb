import sys, os.path
nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\AST\\')
sys.path.append(nodo_dir)

storage_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\storageManager\\')
sys.path.append(storage_dir)

exp_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\EXPRESION\\\\EXPRESION\\')
sys.path.append(exp_dir)

from Expresion import *
from Nodo import Nodo
from jsonMode import showDatabases

class Insert(Nodo):
    def __init__(self, nombreNodo,fila = -1 ,columna = -1 ,valor = None):
        Nodo.__init__(self,nombreNodo, fila, columna, valor)
        
    def compile(self):
        tmp = instanceTemporal.getTemporal()
        dir = f"{tmp} = \"{self.getText()}\"\n"
        dir += f'display[p] = {tmp}\n'
        dir += 'p = p + 1\n'
        return dir
    
    def execute(self,enviroment = None):
        print('Llamar al insert')

    def getText(self):
        nombre_tabla = self.hijos[0].getText()
        if len(self.hijos) > 2:
            #CON NOMBRES DE COLUMNAS
            lista_ids = self.sacar_ids(self.hijos[1].hijos)
            parametros = self.hijos[2].hijos
            str_params = self.getTextParams(parametros)
            return f'INSERT INTO {nombre_tabla} ({lista_ids}) VALUES ({str_params});'
        else:
            #SOLO VALUES
            parametros = self.hijos[1].hijos
            str_params = self.getTextParams(parametros)
            return f' INSERT INTO {nombre_tabla} VALUES ({str_params});'

    def sacar_ids(self,lista):
        lista_ids = ''
        count = 0
        for item in lista:
            coma = ','
            if count == len(lista) - 1:
                coma = ''
            count += 1    
            lista_ids += f'{item.valor}{coma}'
        return lista_ids

    def getTextParams(self,lista):
        string_ = ''
        i = 0
        while i < len(lista):
            actual = lista[i]
            try:
                siguiente = lista[i+1]
            except:
                siguiente = None
            if(actual.nombreNodo == "E"):
                if(i+3 > len(lista)-1):
                    coma = ''
                else:
                    coma = ','
                try:
                    string_ += actual.getText() + siguiente.nombreNodo + lista[i+2].getText() + coma
                except:
                    string_ += ''
                i = i + 3
            elif 'FUNCION' in actual.nombreNodo:
                padre = Expresion("E",-1,-1,None)
                padre.hijos.append(actual)
                if(i >= len(lista)-1):
                    coma = ''
                else:
                    coma = ','                
                string_ += padre.getText() + coma
                i = i + 1
            else:
                if actual.nombreNodo == 'Cadena':
                    separador = "'"
                else:
                    separador = ''

                if(i >= len(lista)-1):
                    coma = ''
                else:
                    coma = ','                      
                string_ += f'{separador}{str(actual.valor)}{separador}{coma}'
                i = i + 1
        return string_



