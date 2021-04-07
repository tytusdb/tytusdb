import sql.reportes.RealizarReportes
import sql.reportes.reportesimbolos as rs
import sql.reportes.RealizarGramatica

from sql.Instrucciones.TablaSimbolos.Tabla import Tabla
from sql.Instrucciones.TablaSimbolos.Arbol import Arbol
from sql.Instrucciones.Excepcion import Excepcion
from sql.Instrucciones.Sql_create.CreateDatabase import CreateDatabase

import sql.reportes.RealizarReportes
import sql.reportes.reportesimbolos as rs
import sql.reportes.RealizarGramatica
import PLSQLParser as analisar
from sql.storageManager.jsonMode import  *
import sql.sintactico as sintactico

global arbol
arbol = None

def main():
    print('ejecutando main')
    tablaGlobal = Tabla(None)
    inst = sintactico.ejecutar_analisis("create database  mainbase31; use mainbase31; create table empleado4(id int not null , nombre varchar(30)); insert into empleado4 values(1, 'Pedro');insert into empleado4 values(2, 'Juan'); select * from empleado4 where id = 2;")
    arbol = Arbol(inst)
    for i in arbol.instrucciones:
            # La variable resultado nos permitirá saber si viene un return, break o continue fuera de sus entornos.
        resultado = i.ejecutar(tablaGlobal,arbol)
        # Después de haber ejecutado todas las instrucciones se verifica que no hayan errores semánticos.
        # if len(arbol.excepciones) != 0:
        #     reportes.RealizarReportes.RealizarReportes.generar_reporte_lexicos(arbol.excepciones)
        # # Ciclo que imprimirá todos los mensajes guardados en la variable consola.
        # mensaje = ''

    f = open("entrada.txt", "r")
    input = f.read()
    print(input)
    Instrus = analisar.getParser(input) 
    
main()
