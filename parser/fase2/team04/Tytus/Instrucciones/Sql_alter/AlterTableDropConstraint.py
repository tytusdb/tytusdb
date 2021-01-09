from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion
from storageManager.jsonMode import *

class AlterTableDropConstraint(Instruccion):
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
                constraintBorrar = None
                for columnas in objetoTabla.lista_de_campos:
                    if columnas.constraint != None:
                        for const in columnas.constraint:
                            if const.id == self.col:
                                existe = columnas
                                constraintBorrar = const
                if existe != None:
                    existe.constraint.remove(constraintBorrar)
                    arbol.consola.append("Consulta devuelta correctamente.")  
                    print ("Consulta ALTER TABLE DROP CONSTRAINT devuelta correctamente")
                else:
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

        '''
        resultado = 0
        #resultado = alterDropColumn(arbol.getBaseDatos(),self.tabla,c.id)
        if resultado == 1:
            error = Excepcion('XX000',"Semántico","Error interno",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        elif resultado == 2:
            error = Excepcion('42P00',"Semántico","La base de datos "+str(arbol.getBaseDatos())+" no existe",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        elif resultado == 3:
            error = Excepcion('42P01',"Semántico","No existe la relación "+self.tabla,self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        elif resultado == 4:
            error = Excepcion('2BP01',"Semántico","No se puede eliminar columna "+self.col+" de "+self.tabla+" prueba porque otros objetos dependen de él",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        elif resultado == 5:
            error = Excepcion('XX002',"Semántico","Columna fuera de limites."+self.tabla,self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        arbol.consola.append("Consulta devuelta correctamente.")
        '''
    
    def getCodigo(self, tabla, arbol):
        tabla = f"{self.tabla}"
        columna = f"{self.col}"
        #tipo = f"{self.tipo}"
        campos = f""
        idCol = f""
        tipoCol = f""
        
        #for item in self.col:
        campos += f"\tDROP CONSTRAINT {columna}\n"
        
            
        table = f"ALTER TABLE {tabla} \n"
        table += f"{campos}"
        table += f"\t;"
        
        num_params = 1
        
        temp_param1 = arbol.getTemporal()
        temp_tam_func = arbol.getTemporal()
        temp_index_param1 = arbol.getTemporal()
        temp_return = arbol.getTemporal()
        temp_result = arbol.getTemporal()
        
        codigo = f"\t#ALTER TABLE DROP CONSTRAINT 3D\n"
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