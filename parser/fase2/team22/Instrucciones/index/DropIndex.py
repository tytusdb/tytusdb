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

class DropIndex(Instruccion):
    def __init__(self, id_tabla, id_indice, existe, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna, strGram)
        self.id_indice = id_indice
        self.id_tabla = id_tabla
        self.existe = existe

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)

        if self.existe == 1:
            error = Excepcion("42P01", "Semantico", "El indice " + str(self.id_indice) + " no existe", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            print('ERROR: tabla no existe')
            return error

        val = self.id_tabla.devolverTabla(tabla, arbol)
        objetoTabla = arbol.devolviendoTablaDeBase(val)
        # objetoTabla.lista_de_indices.remove(self.id_indice)

        for i in objetoTabla.lista_de_indices:
            # print("***", i.nombre.id)
            ind = Indice(i.nombre.id, "Indice")
            # print("---", ind.lRestricciones)
            # ind.lRestricciones.remove('id#[\'ASC\', \'NULLS LAST\']')

            for a in objetoTabla.lista_de_indices:
                if a.nombre.id == self.id_indice:
                    a.nombre.id = ''
                # print("~~:", a.nombre.id)

        


    def generar3D(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append(c3d.asignacionH())
        code.append(c3d.aumentarP())
        t0 = c3d.getTemporal()
        code.append(c3d.asignacionString(t0, "DROP INDEX " + self.id_indice + ";"))
        code.append(c3d.asignacionTemporalStack(t0))
        code.append(c3d.LlamFuncion('call_funcion_intermedia'))
        
        return code

'''
instruccion = DropTable("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''