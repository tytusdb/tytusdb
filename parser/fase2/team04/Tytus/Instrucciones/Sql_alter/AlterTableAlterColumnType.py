from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion
import collections
#from storageManager.jsonMode import *
# Solo reconocerlo en la gramatica y modificarlo en tu table de tipos

class AlterTableAlterColumnType(Instruccion):
    def __init__(self, tabla, lista_col, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.tabla = tabla
        self.lista_col = lista_col

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if arbol.bdUsar != None:
            objetoTabla = arbol.devolviendoTablaDeBase(self.tabla)
            if objetoTabla != 0:
                listaMatch = []
                listaAlterar = []
                for c in self.lista_col:
                    for columnas in objetoTabla.lista_de_campos:
                        if columnas.nombre == c.id:
                            listaMatch.append(c)
                            listaAlterar.append(columnas)
                if len(listaMatch) == 0:
                    for c in self.lista_col:
                        error = Excepcion('42703',"Semántico","No existe la columna «"+c.id+"» en la relación «"+self.tabla+"»",c.linea,c.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                    return
                elif len(listaMatch) == len(self.lista_col):
                    # Existen columnas con el mismo nombre a alterar
                    nombres = []
                    for columnas in self.lista_col:
                        nombres.append(columnas.id)
                    duplicados = [item for item, count in collections.Counter(nombres).items() if count > 1]
                    for columnas in duplicados:
                        error = Excepcion('42701',"Semántico","No se puede alterar el tipo de la columna «"+columnas+"» dos veces",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                    if len(duplicados) != 0:
                        return
                    # Las columnas se alterarán en memoria.
                    for c in self.lista_col:
                        for columnas in listaAlterar:
                            if columnas.nombre == c.id:
                                columnas.tipo = c.tipo
                    arbol.consola.append("Consulta devuelta correctamente.")
                    print("Consulta ALTER TABLE ALTER COLUMN TYPE devuleta correctamente")
                else:
                    for c in list(set(self.lista_col) - set(listaMatch)):
                        error = Excepcion('42703',"Semántico","No existe la columna «"+c.id+"» en la relación «"+self.tabla+"»",c.linea,c.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                    return
            else:
                error = Excepcion('42P01',"Semántico","No existe la relación "+self.tabla,self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        else:
            error = Excepcion("100","Semantico","No ha seleccionado ninguna Base de Datos.",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
    
    def getCodigo(self, tabla, arbol):
        tabla = f"{self.tabla}"
        columna = f"{self.columna}"
        #tipo = f"{self.tipo}"
        campos = f""
        idCol = f""
        tipoCol = f""
        
        for item in self.lista_col:
            col = item.getCodigo(columna, arbol)
            campos += f"\tALTER COLUMN {item.id} TYPE {item.getCodigoTipo(tabla, arbol)}{', ' if self.lista_col.index(item) < len(self.lista_col) - 1 else ''}\n"
        
            
        table = f"ALTER TABLE {tabla} \n"
        table += f"{campos}"
        table += f"\t;"
        
        num_params = 1
        
        temp_param1 = arbol.getTemporal()
        temp_tam_func = arbol.getTemporal()
        temp_index_param1 = arbol.getTemporal()
        temp_return = arbol.getTemporal()
        temp_result = arbol.getTemporal()
        
        codigo = f"\t#ALTER TABLE ALTER COLUMN TYPE 3D\n"
        codigo += f"\t{temp_param1} = f\"{table}\"\n"
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