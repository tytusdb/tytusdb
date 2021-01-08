from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Sql_create.ShowDatabases import ShowDatabases
from Instrucciones.Excepcion import Excepcion
from storageManager.jsonMode import *

class AlterDatabase(Instruccion):
    def __init__(self, id, tipo, opcion, id2, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.nombreAntiguo = id
        self.nombreNuevo = id2
        self.opcion = opcion

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #aqui vamos a renombrar el alter
        res = alterDatabase(self.nombreAntiguo, self.nombreNuevo)
        if( res == 1):
            Excepcion(3,"Semántico","No se pudo renombrar la base de datos",self.linea,self.columna)
        elif(res == 2):
            error = Excepcion("100","Semantico","La bd no existe.",self.linea,self.columna)
        elif(res == 3):
            error = Excepcion("100","Semantico","La bd nueva ya existe.",self.linea,self.columna)
        else:
            if(len(arbol.listaBd)==0):
                #aqui vamos a renombrar en memoria
                Instruccion = ShowDatabases(None, None, self.linea, self.columna)
                Instruccion.ejecutar(tabla,arbol)
                '''
                import os

                archivo = "/home/decodigo/Documentos/python/archivos/archivo.txt"
                nombre_nuevo = "/home/decodigo/Documentos/python/archivos/archivo_renombrado.txt"

                os.rename(archivo, nombre_nuevo)
                '''
                arbol.consola.append(f"La base de datos se cambio: {self.nombreNuevo} correctamente.")
                print(f"La base de datos se cambio: {self.nombreNuevo} correctamente.")
            else:
                #aqui vamos a renombrar en memoria
                arbol.renombrarBd(self.nombreAntiguo,self.nombreNuevo)
                arbol.consola.append(f"La base de datos se cambio: {self.nombreNuevo} correctamente.")
                print(f"La base de datos se cambio: {self.nombreNuevo} correctamente.")


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
        
        codigo = f"\t#ALTER DATABASE RENAME 3D\n"
        codigo += f"\t{temp_param_1} = \"{self.nombreAntiguo}\"\n"
        codigo += f"\t{temp_param_2} = {self.tipo}\n"
        codigo += f"\t{temp_param_3} = \"{self.opcion}\"\n"
        codigo += f"\t{temp_param_4} = \"{self.nombreNuevo}\"\n"
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
        codigo += f"\tinter_alterDataBaseRename()\n"
        #codigo += f"\t{temp_return} = pointer + 0\n"
        #codigo += f"\t{temp_result} = stack[{temp_return}]\n"
        codigo += f"\tpointer = pointer - {num_params}\n"
        #codigo += f"\tprint({temp_result})\n"
        
        #arbol.consola.append(codigo)
        return codigo

'''
instruccion = AlterDatabase("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''


