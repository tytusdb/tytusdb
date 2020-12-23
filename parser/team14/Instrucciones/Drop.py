from Instrucciones.Instruccion import Instruccion
from storageManager import jsonMode as DBMS
from Entorno.Entorno import Entorno
from Entorno.Simbolo import Simbolo
from Entorno.TipoSimbolo import TipoSimbolo

class DropTable(Instruccion):
    def __init__(self, id:str):
        self.id =id

    def ejecutar(self, ent:Entorno):
        if (ent.getDataBase()==None):
            return "ERROR >> En la instrucción Drop Table "+self.id+", actualmente no hay ninguna base de datos en uso"
        else:
            resultado = DBMS.dropTable(ent.getDataBase(),self.id)
            if (resultado==0):
                ent.eliminarSimbolo(self.id+"_"+ent.getDataBase())
                ent.eliminarSymTabla(self.id)
                return "La tabla: ("+self.id+") ha sido eliminada con exito"
            else:
                return "ERROR >> En la instrucción Drop Table "+self.id+", La tabla a eliminar NO EXISTE"
    
class DropAll(Instruccion):
    def __init__(self):
        print("---------------")

    def ejecutar(self, ent):
        DBMS.dropAll()
        ent.eliminarTodo()
        return "Instrucción Drop All ejecutado con exito"
