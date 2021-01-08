from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.Sql_create.Tipo_Constraint import Tipo_Constraint, Tipo_Dato_Constraint
from sql.Instrucciones.Excepcion import Excepcion
#from sql.storageManager.jsonMode import *
# Asocia la integridad referencial entre llaves foráneas y llaves primarias, 
# para efectos de la fase 1 se ignora esta petición. 

class AlterTableAddFK(Instruccion):
    def __init__(self, tabla, lista_col, tabla_ref, lista_fk, strGram,linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.tabla = tabla
        self.lista_col = lista_col
        self.tabla_ref = tabla_ref
        self.lista_fk = lista_fk

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if arbol.bdUsar != None:
            objetoTabla = arbol.devolviendoTablaDeBase(self.tabla)
            if objetoTabla != 0:
                tablaForanea = arbol.devolviendoTablaDeBase(self.tabla_ref)
                if tablaForanea != 0:
                    listaTabla1 = []
                    tabla1Nombres = []
                    for c in self.lista_col:
                        for columnas in objetoTabla.lista_de_campos:
                            if columnas.nombre == c:
                                listaTabla1.append(columnas)
                                tabla1Nombres.append(columnas.nombre)
                    if(len(listaTabla1)==len(self.lista_col)):
                        listaForaneas = []
                        tabla2Nombres = []
                        for c in self.lista_fk:
                            for columnas in tablaForanea.lista_de_campos:
                                if columnas.nombre == c:
                                    listaForaneas.append(columnas)
                                    tabla2Nombres.append(columnas.nombre)
                        if(len(listaForaneas)==len(self.lista_fk)):
                            listaPrimarias = 0
                            for columna in listaForaneas:
                                if columna.constraint != None:
                                    for i in columna.constraint:
                                        if i.tipo == Tipo_Dato_Constraint.PRIMARY_KEY:
                                            listaPrimarias += 1
                                else:
                                    error = Excepcion('42P01',"Semántico","No hay restricción unique que coincida con las columnas dadas en la tabla referida «"+self.tabla_ref+"»",self.linea,self.columna)
                                    arbol.excepciones.append(error)
                                    arbol.consola.append(error.toString())
                                    return
                            if listaPrimarias == len(self.lista_fk):
                                for c in range(0,len(listaTabla1)):
                                    if listaTabla1[c].constraint != None:
                                        restriccion = Tipo_Constraint(self.tabla+"_"+listaTabla1[c].nombre+"_fkey", Tipo_Dato_Constraint.FOREIGN_KEY, listaForaneas[c])
                                        restriccion.referencia = self.tabla_ref
                                        listaTabla1[c].constraint.append(restriccion)
                                    else:
                                        listaTabla1[c].constraint = []
                                        restriccion = Tipo_Constraint(self.tabla+"_"+listaTabla1[c].nombre+"_fkey", Tipo_Dato_Constraint.FOREIGN_KEY, listaForaneas[c])
                                        restriccion.referencia = self.tabla_ref
                                        listaTabla1[c].constraint.append(restriccion)

                                arbol.consola.append("Consulta devuelta correctamente.") 
                            else:
                                error = Excepcion('42P01',"Semántico","No hay restricción unique que coincida con las columnas dadas en la tabla referida «"+self.tabla_ref+"»",self.linea,self.columna)
                                arbol.excepciones.append(error)
                                arbol.consola.append(error.toString())
                                return
                        else:
                            lista = set(self.lista_fk) - set(tabla2Nombres)
                            #print(tabla2Nombres,self.lista_fk)
                            #print(lista)
                            for i in lista:
                                error = Excepcion('42P01',"Semántico","No existe la columna «"+i+"» en la llave",self.linea,self.columna)
                                arbol.excepciones.append(error)
                                arbol.consola.append(error.toString())
                            return
                    else:
                        lista = set(self.lista_col) - set(tabla1Nombres)
                        #print(tabla1Nombres,self.lista_col)
                        #print(lista)
                        for i in lista:
                            error = Excepcion('42P01',"Semántico","No existe la columna «"+i+"» en la llave",self.linea,self.columna)
                            arbol.excepciones.append(error)
                            arbol.consola.append(error.toString())
                        return
                else:
                        error = Excepcion('42P01',"Semántico","No existe la relación "+self.tabla_ref,self.linea,self.columna)
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