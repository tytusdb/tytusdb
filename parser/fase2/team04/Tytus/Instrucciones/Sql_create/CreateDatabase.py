from Instrucciones.Excepcion import Excepcion
from tkinter.constants import FALSE
from Instrucciones.Sql_create.ShowDatabases import ShowDatabases
from Instrucciones.TablaSimbolos.Instruccion import *
from Instrucciones.Tablas.BaseDeDatos import BaseDeDatos
from storageManager.jsonMode import *
class CreateDatabase(Instruccion):
    def __init__(self, base, tipo, existe, owner, mode, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.base=base
        self.tipo=tipo
        self.existe = existe
        self.owner=owner
        self.mode=mode

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        bandera = False
        #SE OBTIENE LA LISTA DE BD
        lb=showDatabases()
        #SE RECORRE LA BD PARA VERIFICAR QUE NO EXISTA
        for bd in lb:
            if bd== self.base:
                #SI SE ENCUENTRA LA BD SE TERMINA EL RECORRIDO
                bandera = True
                break
        if self.existe=="IF NOT EXISTS" and bandera==True:
            arbol.consola.append(f"La Base de Datos ya existe: {self.base}.")
            print(f"LA BASE DE DATOS: {self.base} YA EXISTE.")
        elif self.existe=="IF NOT EXISTS" and bandera==False:
            arbol.consola.append(f"Se Creo la base de datos: {self.base} correctamente.")
            print(f"SE CREO LA BASE DE DATOS: {self.base} CORRECTAMENTE.")
            createDatabase(str(self.base))
            nueva = BaseDeDatos(str(self.base))
            arbol.setListaBd(nueva)
        elif self.existe=="NULL" and bandera==True:
            error = Excepcion("42P04","Semantico",f"La Base de Datos {self.base} ya Existe.",self.linea,self.columna)
            print(f"LA BASE DE DATOS: {self.base} YA EXISTE.")
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
        elif self.existe=="NULL" and bandera==False:
            #AVISOS
            arbol.consola.append(f"Se Creo la base de datos: {self.base} correctamente.")
            print(f"SE CREO LA BASE DE DATOS: {self.base} CORRECTAMENTE.")
            createDatabase(str(self.base))
            nueva = BaseDeDatos(str(self.base))
            arbol.setListaBd(nueva)
            
    def getCodigo(self, tabla, arbol):
        base = self.base
        tipo = self.tipo
        existe = self.existe
        owner = f"\"{self.owner}\"" if self.owner else None 
        mode = self.mode
        strGram = self.strGram
        linea = self.linea
        columna = self.columna
        
        num_params = 8
        
        temp_param_base = arbol.getTemporal()
        temp_param_tipo = arbol.getTemporal()
        temp_param_existe = arbol.getTemporal()
        temp_param_owner = arbol.getTemporal()
        temp_param_mode = arbol.getTemporal()
        temp_param_strGram = arbol.getTemporal()
        temp_param_linea = arbol.getTemporal()
        temp_param_columna = arbol.getTemporal()

        temp_tam_func = arbol.getTemporal()
        temp_index_param_base = arbol.getTemporal()
        temp_index_param_tipo = arbol.getTemporal()
        temp_index_param_existe = arbol.getTemporal()
        temp_index_param_owner = arbol.getTemporal()
        temp_index_param_mode = arbol.getTemporal()
        temp_index_param_strGram = arbol.getTemporal()
        temp_index_param_linea = arbol.getTemporal()
        temp_index_param_columna = arbol.getTemporal()
        temp_return = arbol.getTemporal()
        temp_result = arbol.getTemporal()
        
        codigo = f"\t#CREATE DATABASE 3D\n"
        codigo += f"\t{temp_param_base} = \"{base}\"\n"
        codigo += f"\t{temp_param_tipo} = {tipo}\n"
        codigo += f"\t{temp_param_existe} = \"{existe}\"\n"
        codigo += f"\t{temp_param_owner} =  {owner}\n"
        codigo += f"\t{temp_param_mode} = {mode}\n"
        codigo += f"\t{temp_param_strGram} = \"{strGram}\"\n"
        codigo += f"\t{temp_param_linea} = {linea}\n"
        codigo += f"\t{temp_param_columna} = {columna}\n"

        codigo += f"\t{temp_tam_func} = pointer + {num_params}\n"

        codigo += f"\t{temp_index_param_base} = {temp_tam_func} + 1\n"
        codigo += f"\tstack[{temp_index_param_base}] = {temp_param_base}\n"
        codigo += f"\t{temp_index_param_tipo} = {temp_tam_func} + 2\n"
        codigo += f"\tstack[{temp_index_param_tipo}] = {temp_param_tipo}\n"
        codigo += f"\t{temp_index_param_existe} = {temp_tam_func} + 3\n"
        codigo += f"\tstack[{temp_index_param_existe}] = {temp_param_existe}\n"
        codigo += f"\t{temp_index_param_owner} = {temp_tam_func} + 4\n"
        codigo += f"\tstack[{temp_index_param_owner}] = {temp_param_owner}\n"
        codigo += f"\t{temp_index_param_mode} = {temp_tam_func} + 5\n"
        codigo += f"\tstack[{temp_index_param_mode}] = {temp_param_mode}\n"
        codigo += f"\t{temp_index_param_strGram} = {temp_tam_func} + 6\n"
        codigo += f"\tstack[{temp_index_param_strGram}] = {temp_param_strGram}\n"
        codigo += f"\t{temp_index_param_linea} = {temp_tam_func} + 7\n"
        codigo += f"\tstack[{temp_index_param_linea}] = {temp_param_linea}\n"
        codigo += f"\t{temp_index_param_columna} = {temp_tam_func} + 8\n"
        codigo += f"\tstack[{temp_index_param_columna}] = {temp_param_columna}\n"
        
        codigo += f"\tpointer = pointer + {num_params}\n"
        codigo += f"\tinter_createDataBase()\n"
        #codigo += f"\t{temp_return} = pointer + 0\n"
        #codigo += f"\t{temp_result} = stack[{temp_return}]\n"
        codigo += f"\tpointer = pointer - {num_params}\n"
        #codigo += f"\tprint({temp_result})\n"
        
        #arbol.consola.append(codigo)
        return codigo

'''
instruccion = CreateDatabase("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''