from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from storageManager.jsonMode import *
from Instrucciones.Excepcion import Excepcion

class DeleteTable(Instruccion):
    def __init__(self, valor, tipo, insWhere, strGram ,linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor
        self.insWhere = insWhere


    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if(self.valor != None):
            if(self.insWhere != None):
                #delete(database: str, table: str, columns: list)
                arregloDeColumnasAEliminar = []
                #primero vamos a extraer la tabla
                if(arbol.getBaseDatos()!= None):
                    #resE = extractTable(arbol.getBaseDatos(),self.valor) 
                    #print("Entro al delete")
                    tablaSelect = extractTable(arbol.getBaseDatos(),self.valor)
                    if(self.insWhere != None):
                        #ejecutar el inswhere que me devuelva las columnas
                        arbol.setTablaActual(tablaSelect)
                        columnas = arbol.devolverColumnasTabla(self.valor)
                        arbol.setColumnasActual(columnas)
                        arregloDeColumnasAEliminar = self.insWhere.ejecutar(tabla,arbol)
                        arregloAEliminar = self.devolverIdentificadores(tablaSelect,arregloDeColumnasAEliminar)
                        for d in arregloAEliminar:
                            res = delete(arbol.getBaseDatos(),self.valor,[d])#SI IMPRIME 0, BORRO CON EXITO
                            if(res == 0):
                                arbol.consola.append(f"Se elimino el siguiente registro { d } correctamente.")
                                print("Se ejecutó correctamente el DELETE FROM\n")
                            else:
                                error = Excepcion("42P10","Semantico",f"No se elimino :'( ",self.linea,self.columna)
                                arbol.excepciones.append(error)
                                arbol.consola.append(error.toString())
                else:
                    #error no hay base de datos
                    error = Excepcion("42P10","Semantico",f"No hay base de datos",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())

    def devolverColumnas(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        val = ""
        columnas = ""
        res = []
        val = self.insWhere.ejecutar(tabla,arbol)
        columnas = arbol.devolverColumnasTabla(val)
        print(columnas)
        for x in range(0,len(columnas)):
            col = columnas[x].obtenerNombre()
            res.append(col)
        return res


    def devolverIdentificadores(self, tabla, fila):
        print(tabla)
        print(fila)
        res = []
        for x in range(0,len(tabla)):
            for y in range(0,len(fila)):
                if(tabla[x] == fila[y]):
                    res.append(x)
        
        nuevo = set(res)
        return nuevo

    def getCodigo(self, tabla, arbol):

        instruccionWhere = f""
        instruccionWhere += f"\tWHERE"
        print("----La cantidad de parámetros del WHERE es: " + self.insWhere.getCodigo(tabla, arbol) + "\n")
        #valor, tipo, insWhere,
        #for item in self.insWhere:
        print("WHERE_: "+ self.insWhere.getCodigo(tabla, arbol) + "\n")
        instruccionWhere += f" {self.insWhere.getCodigo(tabla, arbol)}"

        instruccionDelete = f"DELETE FROM {self.valor} "
        instruccionDelete += f"{instruccionWhere}"
        instruccionDelete += f";\t"

        num_params = 1
        
        temp_param1 = arbol.getTemporal()
        temp_tam_func = arbol.getTemporal()
        temp_index_param1 = arbol.getTemporal()
        temp_return = arbol.getTemporal()
        temp_result = arbol.getTemporal()

        codigo = f"\t#DELETE FROM 3D\n"
        codigo += f"\t{temp_param1} = f\"{instruccionDelete}\"\n"
        codigo += f"\t{temp_tam_func} = pointer + {num_params}\n"
        codigo += f"\t{temp_index_param1} = {temp_tam_func} + 1\n"
        codigo += f"\tstack[{temp_index_param1}] = {temp_param1}\n"
        codigo += f"\tpointer = pointer + {num_params}\n"
        codigo += f"\tinter()\n"
        #codigo += f"\t{temp_return} = pointer + 0\n"
        #codigo += f"\t{temp_result} = stack[{temp_return}]\n"
        codigo += f"\tpointer = pointer - {num_params}\n"
        #codigo += f"\tprint({temp_result})\n"
        
        #arbol.consola.append(codigo)
        return codigo





