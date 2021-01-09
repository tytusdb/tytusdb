from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Sql_create.Tipo_Constraint import Tipo_Constraint, Tipo_Dato_Constraint
from Instrucciones.Excepcion import Excepcion


class AlterTableAlterColumn(Instruccion):
    def __init__(self, tabla, col, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.tabla = tabla
        self.col = col

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if arbol.bdUsar != None:
            objetoTabla = arbol.devolviendoTablaDeBase(self.tabla)
            if objetoTabla != 0:
                existe = None
                for columnas in objetoTabla.lista_de_campos:
                    if columnas.nombre == self.col:
                        existe = columnas
                if existe != None:
                    #print(len(listaUnique),self.tabla, self.id)
                    #Insertar llaves Unique
                    if existe.constraint != None:
                        existe.constraint.append(Tipo_Constraint(None, Tipo_Dato_Constraint.NOT_NULL, None))
                        #print("MÁS DE UNA-----------------",existe.nombre, existe.tipo.toString(),len(existe.constraint))
                    else:
                        existe.constraint = []
                        existe.constraint.append(Tipo_Constraint(None, Tipo_Dato_Constraint.NOT_NULL, None))
                        #print("SOLO UNA-------------",existe.nombre, existe.tipo.toString(),len(existe.constraint)) 
                    arbol.consola.append("Consulta devuelta correctamente.")  
                    print ("Consulta ALTER TABLE ALTER COLUMN devuelta correctamente")
                else:
                    #print(listaNombres,self.lista_col)
                    #print(lista)
                    error = Excepcion('42P01',"Semántico","No existe la columna «"+self.col+"» en la llave",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
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
        
        # for item in self.col:
        #     campos += f"\t ALTER COLUMN {item}{', ' if self.col.index(item) < len(self.col) - 1 else ''}\n"
        campos += f"\t ALTER COLUMN {self.col}\n"
            
        table = f"ALTER TABLE {tabla} \n"
        table += f"{campos} SET NOT NULL"
        table += f"\t;"
        
        num_params = 1
        
        temp_param1 = arbol.getTemporal()
        temp_tam_func = arbol.getTemporal()
        temp_index_param1 = arbol.getTemporal()
        temp_return = arbol.getTemporal()
        temp_result = arbol.getTemporal()
        
        codigo = f"\t#ALTER TABLE ALTER COLUMN 3D\n"
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
