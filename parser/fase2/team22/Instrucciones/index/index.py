from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from storageManager.jsonMode import *
from Instrucciones.Sql_select.OrderBy import OrderBy
from Instrucciones.Sql_select.GroupBy import GroupBy
from Instrucciones.Sql_select.Having import Having
from Instrucciones.Sql_select.Limit import Limit
from Instrucciones.Identificador import Identificador
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Sql_select import SelectLista 
from Instrucciones.TablaSimbolos.Simbolo import Simbolo
from Instrucciones.Tablas.indice import Indice
import numpy as np
import pandas as pd
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Optimizador.C3D import *
from Instrucciones.TablaSimbolos import Instruccion3D as c3d
class index(Instruccion):
    def __init__(self, idIndex, idTabla , lcol, where, tipoIndex ,strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.QUERY),linea,columna,strGram)
        self.idIndex = idIndex
        self.idTabla = idTabla
        self.lcol = lcol
        self.where = where
        self.tipoIndex = tipoIndex

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        val = self.idTabla.devolverTabla(tabla, arbol)

        if(val == 0):
            error = Excepcion("42P01", "Semantico", "La tabla " + str(self.identificador.devolverId(tabla, arbol)) + " no existe", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            print('ERROR: tabla no existe')
            return error

        tablaIndex = extractTable(arbol.getBaseDatos(), val)
        arbol.setTablaActual(tablaIndex)
        columnas = arbol.devolverColumnasTabla(val)
        data = np.array((tablaIndex))
        res = []
        for x in range(0, len(columnas)):
            col = columnas[x].obtenerNombre()
            res.append(col)

        arbol.setColumnasActual(res)
        listaMods = []
        if self.where:
            listaMods = self.where.ejecutar(tabla, arbol)

        for x in range(0, len(self.lcol)):
            var = self.lcol[x]
            objetoTabla = arbol.devolviendoTablaDeBase(val)
            try:
                for variable in var:

                    if 'Identificador' in str(variable):
                        idcol = variable.id

                        if self.validar_columna(variable.id, res):
                            if objetoTabla:
                                for indices in objetoTabla.lista_de_indices:
                                    if indices.obtenerNombre == variable.id :
                                        error = Excepcion('42P01',"Semántico","el indice «"+variable.id+"» ya fue creado.",self.linea,self.columna)
                                        arbol.excepciones.append(error)
                                        arbol.consola.append(error.toString())
                                        return error
                                
                            ind = Indice(self.idIndex, "Indice")
                            tipo = ''
                            # try:
                            #     if 'Identificador' in self.lcol[x+1]:
                            #         tipo = ''
                            #         print("===>", self.lcol[x+1])
                            #     else:
                            #         print(">==>", self.lcol[x+1])
                            #         tipo = self.lcol[x+1]
                            # except :
                            #     pass
                            
                            ind.lRestricciones.append(variable.id + '#' + str(self.lcol[x]))
                            if self.tipoIndex:
                                ind.lRestricciones.append(self.tipoIndex)
                            
                            objetoTabla.lista_de_indices.append(ind)
                            arbol.consola.append("Indice agregado con la columna: " + variable.id) 
                        else:
                            print("La columna indicada no pertenece a la tabla: " + self.idTabla)
            except:
                if 'Identificador' in str(var):
                    variable = var
                    idcol = variable.id

                    if self.validar_columna(variable.id, res):
                        if objetoTabla:
                            for indices in objetoTabla.lista_de_indices:
                                if indices.obtenerNombre == variable.id :
                                    error = Excepcion('42P01',"Semántico","el indice «"+variable.id+"» ya fue creado.",self.linea,self.columna)
                                    arbol.excepciones.append(error)
                                    arbol.consola.append(error.toString())
                                    return error
                            
                        ind = Indice(self.idIndex, "Indice")
                        tipo = ''
                        try:
                            if 'Identificador' in self.lcol[x+1]:
                                tipo = ''
                            else:
                                tipo = self.lcol[x+1]
                        except :
                            pass
                        ind.lRestricciones.append(variable.id + '#' + str(tipo))
                        if self.tipoIndex:
                            ind.lRestricciones.append(self.tipoIndex)
                        
                        objetoTabla.lista_de_indices.append(ind)
                        arbol.consola.append("Indice agregado con la columna: " + variable.id)    
                    else:
                        print("La columna indicada no pertenece a la tabla: " + self.idTabla)


    def validar_columna(self, nombre, listacolumnas):
        for i in range(0, len(listacolumnas)):
            if listacolumnas[i] == nombre:
                return True
            # else:
            #     return False
        return False


    def generar3D(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        t0 = c3d.getTemporal()
        # code.append(c3d.asignacionString(t0, "CREATE INDEX " + self.ID))
        params = ''
        for x in range(0, len(self.lcol)):
            var = self.lcol[x]
            if params != '':
                params += ', '
            if 'Identificador' in str(var):
                params += var.id

        code.append(c3d.asignacionString(t0, "CREATE INDEX" + str(self.idIndex.id) + " ON " + str(self.idTabla.id) + " ( " + params + " ) ;"))
        code.append(c3d.asignacionString(t0, "CREATE INDEX test2_mm_idx ON tabla(id);"))
        #CREATE INDEX test2_mm_idx ON tabla(id);

        # code.append(c3d.operacion(t1, Identificador(t0), Valor("\";\"", "STRING"), OP_ARITMETICO.SUMA))
        code.append(c3d.asignacionTemporalStack(t0))
        code.append(c3d.aumentarP())

        return code