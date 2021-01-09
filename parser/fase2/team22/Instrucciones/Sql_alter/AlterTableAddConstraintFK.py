from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Sql_create.Tipo_Constraint import Tipo_Constraint, Tipo_Dato_Constraint
from Instrucciones.Excepcion import Excepcion
#from storageManager.jsonMode import *
from Optimizador.C3D import *
from Instrucciones.TablaSimbolos import Instruccion3D as c3d

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

    def generar3D(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append(c3d.asignacionH())
        code.append(c3d.aumentarP())
        t0 = c3d.getTemporal()
        code.append(c3d.asignacionString(t0, "ALTER TABLE " + self.tabla + "\\n"))
        t1 = c3d.getTemporal()
        code.append(c3d.operacion(t1, Identificador(t0), Valor("\"ADD CONSTRAINT " + self.id_constraint +  "\\n\"", "STRING"), OP_ARITMETICO.SUMA))
        t0 = t1
        t1 = c3d.getTemporal()
        code.append(c3d.operacion(t1, Identificador(t0), Valor("\"FOREIGN KEY (\"", "STRING"), OP_ARITMETICO.SUMA))
        t0 = t1
        t1 = c3d.getTemporal()

        sizeCol = len(self.lista_id1)
        contador = 1
        for id in self.lista_id1:
            code.append(c3d.operacion(t1, Identificador(t0), Valor("\"" + id + "\"", "STRING"), OP_ARITMETICO.SUMA))
            t0 = t1
            t1 = c3d.getTemporal()
            if contador != sizeCol:
                code.append(c3d.operacion(t1, Identificador(t0), Valor('", "', "STRING"), OP_ARITMETICO.SUMA))
                t0 = t1
                t1 = c3d.getTemporal()
            contador += 1
        
        code.append(c3d.operacion(t1, Identificador(t0), Valor("\")\\nREFERENCES " + self.tabla2 + "(\"", "STRING"), OP_ARITMETICO.SUMA))
        t0 = t1
        t1 = c3d.getTemporal()

        sizeCol = len(self.lista_id2)
        contador = 1
        for id in self.lista_id2:
            code.append(c3d.operacion(t1, Identificador(t0), Valor("\"" + id + "\"", "STRING"), OP_ARITMETICO.SUMA))
            t0 = t1
            t1 = c3d.getTemporal()
            if contador != sizeCol:
                code.append(c3d.operacion(t1, Identificador(t0), Valor('", "', "STRING"), OP_ARITMETICO.SUMA))
                t0 = t1
                t1 = c3d.getTemporal()
            contador += 1
        code.append(c3d.operacion(t1, Identificador(t0), Valor("\");\"", "STRING"), OP_ARITMETICO.SUMA))
        
        code.append(c3d.asignacionTemporalStack(t1))
        code.append(c3d.LlamFuncion('call_funcion_intermedia'))

        return code

    def generar3DV2(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append('h = p')
        code.append('h = h + 1')
        t0 = c3d.getTemporal()
        bd = arbol.getBaseDatos()
        if bd != None and bd != "":
            code.append(t0 + ' = "' + bd + '"')
        else:
            code.append(t0 + ' = ' + str(None))
        code.append('heap[h] = ' + t0)
        code.append('h = h + 1')
        t1 = c3d.getTemporal()
        code.append(t1 + ' = "' + str(self.tabla) + '"')
        code.append('heap[h] = ' + t1)
        code.append('h = h + 1')
        t2 = c3d.getTemporal()
        code.append(t2 + ' = "' + str(self.id_constraint) + '"')
        code.append('heap[h] = ' + t2)
        code.append('h = h + 1')
        if self.lista_id1 != None:
            code.append('heap[h] = []')
            for columna in self.lista_id1:
                t3 = c3d.getTemporal()
                code.append(t3 + ' = ["' + str(columna) + '"]')
                code.append('heap[h] = heap[h] + ' + t3)
        else:
            code.append('heap[h] = None')
        code.append('h = h + 1')
        t4 = c3d.getTemporal()
        code.append(t4 + ' = "' + str(self.tabla2) + '"')
        code.append('heap[h] = ' + t4)
        code.append('h = h + 1')
        if self.lista_id2 != None:
            code.append('heap[h] = []')
            for columna in self.lista_id2:
                t5 = c3d.getTemporal()
                code.append(t5 + ' = ["' + str(columna) + '"]')
                code.append('heap[h] = heap[h] + ' + t5)
        else:
            code.append('heap[h] = None')
        code.append('p = h')
        code.append('call_alterTable_addConstraintFK()')
        
        return code