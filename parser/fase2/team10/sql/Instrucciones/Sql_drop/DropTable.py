from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.storageManager.jsonMode import *

class DropTable(Instruccion):
    def __init__(self, id, tipo, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = id

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        bd = arbol.getBaseDatos()
        if bd :
            operacion = dropTable(str(bd), self.valor)
            if operacion == 0 :
                arbol.consola.append(f"Se ha eliminado la Tabla {self.valor} de la Base de Datos {str(bd)}")
                arbol.eliminarTabla(self.valor)
                
            elif operacion == 1:
                error = Exception('XX000',"Semantico","Error Interno",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
            elif operacion == 2:
                error = Exception('XX000',"Semantico","La Base de datos no existe",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
            else :
                error = Exception('XX000',"Semantico","La tabla no existe",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())

            print(showTables(str(bd)))

            return
        
        print(f"Error en linea {str(self.linea)} y columna {str(self.columna)} No hay base de datos")

        #error = Exception('XX000',"Semantico","Error Interno",self.linea,self.columna)
        #arbol.excepciones.append(error)
        #arbol.consola.append(error.toString())        
       # createTable(bd, "Mitabla")
       # showTables(bd)
'''
instruccion = DropTable("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''