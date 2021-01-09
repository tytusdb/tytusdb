from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from storageManager.jsonMode import *
class DropDatabase(Instruccion):
    def __init__(self, id, tipo, existe, opcion, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.id = id
        self.tipo =  tipo
        self.opcion = opcion
        self.existe = existe

        
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        bandera = False
        listaBD = showDatabases()
        for bd in listaBD:
            if bd == self.id:
                bandera = True
                break

        #LA BD se encontro
        if self.existe and bandera:
            print(f"La Base de Datos: {self.id} ha sido eliminada")
            arbol.consola.append(f"Se encontro la base de datos: {self.id} ha sido eliminada")
            dropDatabase(self.id)
            arbol.eliminarBD(self.id)
        elif self.existe and not bandera:
            arbol.consola.append(f"La Base de datos: {self.id} no existe")
            print(f"La Base de Datos: {self.id} no existe")
        elif not self.existe and bandera:
            arbol.consola.append(f"La Base de Datos: {self.id} ha sido eliminada")
            print(f"La Base de Datos: {self.id} ha sido eliminada")
            dropDatabase(self.id)
            arbol.eliminarBD(self.id)
        elif not self.existe and not bandera:
            error = Exception("XX000", "Semantico", "Error Base de Datos no existe", self.linea, self.columna)
            print(error)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())



    def getCodigo(self, tabla, arbol):
               
        num_params = 7
        
        temp_param_1 = arbol.getTemporal()
        temp_param_2 = arbol.getTemporal()
        temp_param_3 = arbol.getTemporal()
        temp_param_4 = arbol.getTemporal()
        temp_param_5 = arbol.getTemporal()
        temp_param_6 = arbol.getTemporal()
        temp_param_7 = arbol.getTemporal()

        temp_tam_func = arbol.getTemporal()

        temp_index_param_1 = arbol.getTemporal()
        temp_index_param_2 = arbol.getTemporal()
        temp_index_param_3 = arbol.getTemporal()
        temp_index_param_4 = arbol.getTemporal()
        temp_index_param_5 = arbol.getTemporal()
        temp_index_param_6 = arbol.getTemporal()
        temp_index_param_7 = arbol.getTemporal()
        
        temp_return = arbol.getTemporal()
        temp_result = arbol.getTemporal()
        
        codigo = f"\t#DROP DATABASE 3D\n"
        codigo += f"\t{temp_param_1} = \"{self.id}\"\n"
        codigo += f"\t{temp_param_2} = {self.tipo}\n"
        codigo += f"\t{temp_param_3} = {self.existe}\n"
        codigo += f"\t{temp_param_4} = {self.opcion}\n"
        codigo += f"\t{temp_param_5} = \"\"\n"
        codigo += f"\t{temp_param_6} = {-1}\n"
        codigo += f"\t{temp_param_7} = {-1}\n"
    

        codigo += f"\t{temp_tam_func} = pointer + {num_params}\n"

        codigo += f"\t{temp_index_param_1} = {temp_tam_func} + 1\n"
        codigo += f"\tstack[{temp_index_param_1}] = {temp_param_1}\n"

        codigo += f"\t{temp_index_param_2} = {temp_tam_func} + 2\n"
        codigo += f"\tstack[{temp_index_param_2}] = {temp_param_2}\n"

        codigo += f"\t{temp_index_param_3} = {temp_tam_func} + 3\n"
        codigo += f"\tstack[{temp_index_param_3}] = {temp_param_3}\n"

        codigo += f"\t{temp_index_param_4} = {temp_tam_func} + 4\n"
        codigo += f"\tstack[{temp_index_param_4}] = {temp_param_4}\n"

        codigo += f"\t{temp_index_param_5} = {temp_tam_func} + 5\n"
        codigo += f"\tstack[{temp_index_param_5}] = {temp_param_5}\n"

        codigo += f"\t{temp_index_param_6} = {temp_tam_func} + 6\n"
        codigo += f"\tstack[{temp_index_param_6}] = {temp_param_6}\n"

        codigo += f"\t{temp_index_param_7} = {temp_tam_func} + 7\n"
        codigo += f"\tstack[{temp_index_param_7}] = {temp_param_7}\n"

        
        codigo += f"\tpointer = pointer + {num_params}\n"
        codigo += f"\tinter_DropDataBase()\n"
        #codigo += f"\t{temp_return} = pointer + 0\n"
        #codigo += f"\t{temp_result} = stack[{temp_return}]\n"
        codigo += f"\tpointer = pointer - {num_params}\n"
        #codigo += f"\tprint({temp_result})\n"
        
        #arbol.consola.append(codigo)
        return codigo
            
        
'''
instruccion = Use("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''