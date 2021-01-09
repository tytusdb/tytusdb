from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Sql_create.Tipo_Constraint import Tipo_Constraint, Tipo_Dato_Constraint
from Instrucciones.Excepcion import Excepcion
#from storageManager.jsonMode import *

class AlterTableAddConstraintFK(Instruccion):
    def __init__(self, tabla, id_constraint, lista_id1,tabla2, lista_id2, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.tabla = tabla
        self.id_constraint = id_constraint
        self.lista_id1 = lista_id1
        self.tabla2 = tabla2
        self.lista_id2 = lista_id2
    
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if arbol.bdUsar != None:
            objetoTabla = arbol.devolviendoTablaDeBase(self.tabla)
            if objetoTabla != 0:
                tablaForanea = arbol.devolviendoTablaDeBase(self.tabla2)
                if tablaForanea != 0:
                    listaTabla1 = []
                    tabla1Nombres = []
                    for c in self.lista_id1:
                        for columnas in objetoTabla.lista_de_campos:
                            if columnas.nombre == c:
                                listaTabla1.append(columnas)
                                tabla1Nombres.append(columnas.nombre)
                    if(len(listaTabla1)==len(self.lista_id1)):
                        listaForaneas = []
                        tabla2Nombres = []
                        for c in self.lista_id2:
                            for columnas in tablaForanea.lista_de_campos:
                                if columnas.nombre == c:
                                    listaForaneas.append(columnas)
                                    tabla2Nombres.append(columnas.nombre)
                        if(len(listaForaneas)==len(self.lista_id2)):
                            listaPrimarias = 0
                            for columna in listaForaneas:
                                if columna.constraint != None:
                                    for i in columna.constraint:
                                        if i.tipo == Tipo_Dato_Constraint.PRIMARY_KEY:
                                            listaPrimarias += 1
                                else:
                                    error = Excepcion('42P01',"Semántico","No hay restricción unique que coincida con las columnas dadas en la tabla referida «"+self.tabla2+"»",self.linea,self.columna)
                                    arbol.excepciones.append(error)
                                    arbol.consola.append(error.toString())
                                    return
                            if listaPrimarias == len(self.lista_id2):
                                for c in range(0,len(listaTabla1)):
                                    if listaTabla1[c].constraint != None:
                                        restriccion = Tipo_Constraint(self.id_constraint, Tipo_Dato_Constraint.FOREIGN_KEY, listaForaneas[c])
                                        restriccion.referencia = self.tabla2
                                        listaTabla1[c].constraint.append(restriccion)
                                    else:
                                        listaTabla1[c].constraint = []
                                        restriccion = Tipo_Constraint(self.id_constraint, Tipo_Dato_Constraint.FOREIGN_KEY, listaForaneas[c])
                                        restriccion.referencia = self.tabla2
                                        listaTabla1[c].constraint.append(restriccion)
                                arbol.consola.append("Consulta devuelta correctamente.") 
                                print("Consulta ALTER TABLE ADD CONSTRAINT FK devuelta correctamente")
                            else:
                                error = Excepcion('42P01',"Semántico","No hay restricción unique que coincida con las columnas dadas en la tabla referida «"+self.tabla2+"»",self.linea,self.columna)
                                arbol.excepciones.append(error)
                                arbol.consola.append(error.toString())
                                return
                        else:
                            lista = set(self.lista_id2) - set(tabla2Nombres)
                            #print(tabla2Nombres,self.lista_id2)
                            #print(lista)
                            for i in lista:
                                error = Excepcion('42P01',"Semántico","No existe la columna «"+i+"» en la llave",self.linea,self.columna)
                                arbol.excepciones.append(error)
                                arbol.consola.append(error.toString())
                            return
                    else:
                        lista = set(self.lista_id1) - set(tabla1Nombres)
                        #print(tabla1Nombres,self.lista_id1)
                        #print(lista)
                        for i in lista:
                            error = Excepcion('42P01',"Semántico","No existe la columna «"+i+"» en la llave",self.linea,self.columna)
                            arbol.excepciones.append(error)
                            arbol.consola.append(error.toString())
                        return
                else:
                        error = Excepcion('42P01',"Semántico","No existe la relación "+self.tabla2,self.linea,self.columna)
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
        tabla2 = f"{self.tabla2}"
        campos1 = f""
        campos2 = f""
        
        for item in self.lista_id1:
            campos1 += f"{item}{', ' if self.lista_id1.index(item) < len(self.lista_id1) - 1 else ''}"    

        for item in self.lista_id2:
            campos2 += f"{item}{', ' if self.lista_id2.index(item) < len(self.lista_id2) - 1 else ''}"

        table = f"ALTER TABLE {tabla} ADD CONSTRAINT {self.id_constraint} FOREIGN KEY ({campos1}) REFERENCES {tabla2} ({campos2});"
 

        
        num_params = 1
        
        temp_param1 = arbol.getTemporal()
        temp_tam_func = arbol.getTemporal()
        temp_index_param1 = arbol.getTemporal()
        temp_return = arbol.getTemporal()
        temp_result = arbol.getTemporal()
        
        codigo = f"\t#ALTER TABLE ADD CONSTRAINT FK 3D\n"
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


