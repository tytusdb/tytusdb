from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from storageManager.jsonMode import *

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
    
    def getCodigo(self, tabla, arbol):
        _id = self.valor
        tipo = None
        strGram = self.strGram
        linea = self.linea
        columna = self.columna
        
        num_params = 5
        
        temp_param_id = arbol.getTemporal()
        temp_param_tipo = arbol.getTemporal()
        temp_param_strGram = arbol.getTemporal()
        temp_param_linea = arbol.getTemporal()
        temp_param_columna = arbol.getTemporal()
        temp_tam_func = arbol.getTemporal()
        temp_index_param_id = arbol.getTemporal()
        temp_index_param_tipo = arbol.getTemporal()
        temp_index_param_strGram = arbol.getTemporal()
        temp_index_param_linea = arbol.getTemporal()
        temp_index_param_columna = arbol.getTemporal()
        temp_return = arbol.getTemporal()
        temp_result = arbol.getTemporal()
        
        codigo = f"\t#DROP TABLE 3D\n"
        codigo += f"\t{temp_param_id} = \"{_id}\"\n"
        codigo += f"\t{temp_param_tipo} = {tipo}\n"
        codigo += f"\t{temp_param_strGram} = \"{strGram}\"\n"
        codigo += f"\t{temp_param_linea} = {linea}\n"
        codigo += f"\t{temp_param_columna} = {columna}\n"
        codigo += f"\t{temp_tam_func} = pointer + {num_params}\n"
        codigo += f"\t{temp_index_param_id} = {temp_tam_func} + 1\n"
        codigo += f"\tstack[{temp_index_param_id}] = {temp_param_id}\n"
        codigo += f"\t{temp_index_param_tipo} = {temp_tam_func} + 2\n"
        codigo += f"\tstack[{temp_index_param_tipo}] = {temp_param_tipo}\n"
        codigo += f"\t{temp_index_param_strGram} = {temp_tam_func} + 3\n"
        codigo += f"\tstack[{temp_index_param_strGram}] = {temp_param_strGram}\n"
        codigo += f"\t{temp_index_param_linea} = {temp_tam_func} + 4\n"
        codigo += f"\tstack[{temp_index_param_linea}] = {temp_param_linea}\n"
        codigo += f"\t{temp_index_param_columna} = {temp_tam_func} + 5\n"
        codigo += f"\tstack[{temp_index_param_columna}] = {temp_param_columna}\n"
        codigo += f"\tpointer = pointer + {num_params}\n"
        codigo += f"\tinter_dropTable()\n"
        codigo += f"\t{temp_return} = pointer + 0\n"
        codigo += f"\t{temp_result} = stack[{temp_return}]\n"
        codigo += f"\tpointer = pointer - {num_params}\n"
        codigo += f"\tprint({temp_result})\n"
        
        arbol.consola.append(codigo)
'''
instruccion = DropTable("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''