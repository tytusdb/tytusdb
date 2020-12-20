from Tipo import Tipo
from Instrucciones.Instruccion import Instruccion
from storageManager import jsonMode as DBMS
from Entorno.Entorno import Entorno
from Entorno.Simbolo import Simbolo
from Entorno.TipoSimbolo import TipoSimbolo


class Insert(Instruccion):
    def __init__(self, nombre,valores=[]):
        self.nombre=nombre
        self.valores=valores

    def ejecutar(self, ent:Entorno):
        completo=self.nombre+'_'+ent.getDataBase()
        tabla:Simbolo = ent.buscarSimbolo(completo)
        if tabla != None:
            columnas=tabla.valor
            if len(self.valores)== len(columnas):
                i=0
                correcto=True
                for columna in columnas:
                    nombre=columna.nombre
                    tipo=columna.tipo
                    util=Tipo(None,None,-1,-1)
                    if util.comparetipo(tipo,self.valores[i].tipo):
                        'todo correcto'
                    else:
                        correcto=False
                        return 'Error los tipos de los valores no coinciden con la definicion de la tabla'
                    i=i+1
                terminales = []
                for val in self.valores:
                    terminales.append(val.getval(ent))

                DBMS.insert(ent.getDataBase(),self.nombre,terminales)









