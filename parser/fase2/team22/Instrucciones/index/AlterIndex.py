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

class AlterIndex(Instruccion):
    def __init__(self, id_tabla, idIndex, columnaOld, columnaNew, existe, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna, strGram)
        self.idIndex = idIndex
        self.columnaOld = columnaOld
        self.columnaNew = columnaNew
        self.existe = existe
        self.id_tabla = id_tabla

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)

        if self.existe == 1:
            error = Excepcion("42P01", "Semantico", "El indice " + str(self.id_indice) + " no existe", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            print('ERROR: tabla no existe')
            return error

        # objetoTabla.lista_de_indices.remove(self.id_indice)

        print(type(self.columnaNew))

        if type(self.columnaNew) == str:
            # print("*********************************")
            val = self.id_tabla.devolverTabla(tabla, arbol)
            objetoTabla = arbol.devolviendoTablaDeBase(val)

            for i in objetoTabla.lista_de_indices:
                ind = Indice(i.nombre.id, "Indice")
                # print("---", i.lRestricciones)
                # ind.lRestricciones.remove('id#[\'ASC\', \'NULLS LAST\']')
                
                consideraciones = str(i.lRestricciones).replace("[", "").replace("'", "").replace("\"", "").replace("]", "").replace(",", "")
                column_index = consideraciones.split("#")

                # print(column_index[0], "<>", self.columnaOld)
                if column_index[0] == self.columnaOld and i.nombre.id == self.idIndex.id:
                    i.lRestricciones = self.columnaNew + '#' + column_index[1]

        elif type(self.columnaNew) == int:
            # print("============================================")
            val = self.id_tabla.devolverTabla(tabla, arbol)
            objetoTabla = arbol.devolviendoTablaDeBase(val)
            iterador = self.columnaNew
            columna_a_cambiar = ''
            
            for i in objetoTabla.lista_de_campos:
                # print("*.", i.nombre)
                iterador = iterador - 1
                if iterador == 0:
                    columna_a_cambiar = i.nombre
            # print("+++++++++++++++++++++", columna_a_cambiar)


            for i in objetoTabla.lista_de_indices:
                ind = Indice(i.nombre.id, "Indice")
                # print("---", i.lRestricciones)
                # ind.lRestricciones.remove('id#[\'ASC\', \'NULLS LAST\']')
                
                consideraciones = str(i.lRestricciones).replace("[", "").replace("'", "").replace("\"", "").replace("]", "").replace(",", "")
                column_index = consideraciones.split("#")

                # print(column_index[0], "<==>", self.columnaOld)
                if column_index[0] == self.columnaOld and i.nombre.id == self.idIndex.id:
                    i.lRestricciones = columna_a_cambiar + '#' + column_index[1]
                # print("!!!!",i.nombre.id,'-',self.idIndex.id )


    def generar3D(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        t0 = c3d.getTemporal()
        column = ''
        if type(self.columnaNew) == 'int':
            column = self.columnaNew
        else:
            column = self.columnaNew

        code.append(c3d.asignacionString(t0, "ALTER INDEX " + self.idIndex.id + " " + self.columnaOld + " " + str(column) + ";"))
        code.append(c3d.asignacionTemporalStack(t0))
        code.append(c3d.aumentarP())
        
        return code

'''
instruccion = DropTable("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''