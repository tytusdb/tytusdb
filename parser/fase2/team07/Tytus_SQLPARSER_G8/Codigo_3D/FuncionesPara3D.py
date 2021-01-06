import sintactico

import reportes.RealizarReportes
import reportes.reportesimbolos as rs
import reportes.RealizarGramatica

from Instrucciones.TablaSimbolos.Tabla import Tabla
from Instrucciones.TablaSimbolos.Arbol import Arbol
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Sql_create.CreateDatabase import CreateDatabase

from Instrucciones.Tablas.BaseDeDatos import BaseDeDatos

global arbol
arbol = Arbol(None)
global tablaGlobal
tablaGlobal = Tabla(None)

class FuncionesPara3D():

    def GenerarArchivo(codigo):
        nombre_archivo = "Codigo_3D/Codigo3D.py"


        #Se borra el contenido del archivo
        f = open(nombre_archivo, "w")
        f.write("")
        f.close()
        f = open(nombre_archivo, "a+")

        #Se escriben codigo quemado como los imports
        cont = "from Codigo_3D.FuncionesPara3D import FuncionesPara3D\n\n"
        
        cont += "class Codigo3D():\n\n"

        cont += "\tdef __init__(self):\n"
        cont += "\t\tself.mensaje = \"\" \n\n"

        cont += "\tdef ejecutar(self):\n\n"
        #Se esribe el codigo traducido
        cont += codigo
        
        f.write(cont)
        f.close()
        
    def ejecutarsentecia(sentecia):
        global arbol
        global tablaGlobal
        #Elimina el Contenido de txtsalida
        #Inserta "Archivo Analizado" en txtsalida
        #self.txtsalida[self.tab.index("current")].insert(INSERT,"Archivo Analizado")
        #Selecciona el contenido de txt entrada
        #print(self.txtentrada[self.tab.index("current")].get(1.0,END))
        input=sentecia
        
        inst = sintactico.ejecutar_analisis(input)
        arbol.setInstrucciones(inst)

        if len(sintactico.lista_lexicos)>0:
            messagebox.showerror('Tabla de Errores','La Entrada Contiene Errores!')
            reportes.RealizarReportes.RealizarReportes.generar_reporte_lexicos(sintactico.lista_lexicos)
        # Ciclo que recorrerá todas las instrucciones almacenadas por la gramática.
        arbol.lRepDin.append("<init> ::= <instrucciones>")
        arbol.lRepDin.append("<instrucciones>   ::=  <instrucciones> <instruccion>")
        arbol.lRepDin.append("<instrucciones> ::= <instruccion>")
        
        for i in arbol.instrucciones:
            # La variable resultado nos permitirá saber si viene un return, break o continue fuera de sus entornos.
            resultado = i.ejecutar(tablaGlobal,arbol)
        # Después de haber ejecutado todas las instrucciones se verifica que no hayan errores semánticos.
        if len(arbol.excepciones) != 0:
            reportes.RealizarReportes.RealizarReportes.generar_reporte_lexicos(arbol.excepciones)
        # Ciclo que imprimirá todos los mensajes guardados en la variable consola.
        mensaje = ''
        for m in arbol.consola:
            mensaje += m + '\n'
        print(mensaje)
        return mensaje