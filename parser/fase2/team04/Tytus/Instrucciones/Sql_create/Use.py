from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion
from storageManager.jsonMode import *
from Instrucciones.Tablas.BaseDeDatos import BaseDeDatos

class Use(Instruccion):
    def __init__(self, id, strGram ,linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.valor = id

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #SE OBTIENE LA LISTA DE BD
        arbol.lRepDin.append(self.strGram)
        lb=showDatabases()
        #SE RECORRE LA BD PARA VERIFICAR QUE NO EXISTA
        for bd in lb:
            if bd== self.valor:
                #SI SE ENCUENTRA LA BD SE TERMINA EL RECORRIDO
                arbol.setBaseDatos(self.valor)
                #llenar la base de datos
                if(arbol.existeBd(self.valor) == 0):
                    nueva = BaseDeDatos(self.valor)
                    arbol.setListaBd(nueva)
                    arbol.llenarTablas(nueva)
                arbol.consola.append(f"Se selecciono la BD: {self.valor} correctamente.")
                print(f"BASE DE DATOS: {self.valor} SELECCIONADA.")
                return
        error = Excepcion("100","Semantico",f"No existe la BD: {self.valor}",self.linea,self.columna)
        arbol.excepciones.append(error)
        arbol.consola.append(error.toString())
        #print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))
        
    def getCodigo(self, tabla, arbol):
        _id = self.valor
        strGram = self.strGram
        linea = self.linea
        columna = self.columna
        
        num_params = 4
        
        temp_param_id = arbol.getTemporal()
        temp_param_strGram = arbol.getTemporal()
        temp_param_linea = arbol.getTemporal()
        temp_param_columna = arbol.getTemporal()
        temp_tam_func = arbol.getTemporal()
        temp_index_param_id = arbol.getTemporal()
        temp_index_param_strGram = arbol.getTemporal()
        temp_index_param_linea = arbol.getTemporal()
        temp_index_param_columna = arbol.getTemporal()
        temp_return = arbol.getTemporal()
        temp_result = arbol.getTemporal()
        
        codigo = f"\t#USE DATABASE 3D\n"
        codigo += f"\t{temp_param_id} = \"{_id}\"\n"
        codigo += f"\t{temp_param_strGram} = \"{strGram}\"\n"
        codigo += f"\t{temp_param_linea} = {linea}\n"
        codigo += f"\t{temp_param_columna} = {columna}\n"
        codigo += f"\t{temp_tam_func} = pointer + {num_params}\n"
        codigo += f"\t{temp_index_param_id} = {temp_tam_func} + 1\n"
        codigo += f"\tstack[{temp_index_param_id}] = {temp_param_id}\n"
        codigo += f"\t{temp_index_param_strGram} = {temp_tam_func} + 2\n"
        codigo += f"\tstack[{temp_index_param_strGram}] = {temp_param_strGram}\n"
        codigo += f"\t{temp_index_param_linea} = {temp_tam_func} + 3\n"
        codigo += f"\tstack[{temp_index_param_linea}] = {temp_param_linea}\n"
        codigo += f"\t{temp_index_param_columna} = {temp_tam_func} + 4\n"
        codigo += f"\tstack[{temp_index_param_columna}] = {temp_param_columna}\n"
        codigo += f"\tpointer = pointer + {num_params}\n"
        codigo += f"\tinter_useDataBase()\n"
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