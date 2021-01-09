from Instrucciones.TablaSimbolos.Instruccion import Instruccion
# Para todas las definiciones que incluyan owner solamente aceptarlo en la sintaxis no hacer nada con ellos

class AlterDBOwner(Instruccion):
    def __init__(self, id, owner, strGram,linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.id = id
        self.owner = owner
        

    def ejecutar(self, tabla, arbol):
        #super().ejecutar(tabla,arbol)
        arbol.consola.append("Consulta devuelta correctamente.")
        print ("Consulta AlterDBOwner devuelta correctamente")

    def getCodigo(self, tabla, arbol):
               
        num_params = 5
        
        temp_param_1 = arbol.getTemporal()
        temp_param_2 = arbol.getTemporal()
        temp_param_3 = arbol.getTemporal()
        temp_param_4 = arbol.getTemporal()
        temp_param_5 = arbol.getTemporal()

        temp_tam_func = arbol.getTemporal()

        temp_index_param_1 = arbol.getTemporal()
        temp_index_param_2 = arbol.getTemporal()
        temp_index_param_3 = arbol.getTemporal()
        temp_index_param_4 = arbol.getTemporal()
        temp_index_param_5 = arbol.getTemporal()
        
        temp_return = arbol.getTemporal()
        temp_result = arbol.getTemporal()
        
        codigo = f"\t#ALTER DATABASE OWNER TO 3D\n"
        codigo += f"\t{temp_param_1} = \"{self.id}\"\n"
        codigo += f"\t{temp_param_2} = \"{self.owner}\"\n"
        codigo += f"\t{temp_param_3} = \"\"\n"
        codigo += f"\t{temp_param_4} = {-1}\n"
        codigo += f"\t{temp_param_5} = {-1}\n"
    

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

        
        codigo += f"\tpointer = pointer + {num_params}\n"
        codigo += f"\tinter_alterDataBaseOwner()\n"
        #codigo += f"\t{temp_return} = pointer + 0\n"
        #codigo += f"\t{temp_result} = stack[{temp_return}]\n"
        codigo += f"\tpointer = pointer - {num_params}\n"
        #codigo += f"\tprint({temp_result})\n"
        
        #arbol.consola.append(codigo)
        return codigo