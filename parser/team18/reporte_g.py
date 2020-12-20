
from expresiones import *
from instrucciones import *
import tablasimbolos as TS
#import markdown


class Reporte_Gramaticas:
    textoAsc = ''
    textoDsc = ''

    def __init__(self):
        print("Reportes gramaticales ASC y DSC")


    def grammarASC(self,instrucciones):

        lista_instrucciones = instrucciones
        global textoAsc

        textoAsc = '# Gramatica Ascendente \n'
        textoAsc += '```sh \n'
        textoAsc += '<init> ::= <l_sentencias> \n'
        textoAsc += '''<l_sentencias> ::= <l_sentencias sentencias>
        | <sentencias> \n'''
        textoAsc += '<sentencias> ::= <sentencia> ";" \n'
        textoAsc += '''<sentencia> ::= <sentencia_ddl>
        | <sentencia_dml> \n'''
        textoAsc += '<sentencia> ::= <sentencia_ddl> \n'
        textoAsc += '''<sentencia_ddl> ::= <crear> 
                | <liberar> \n'''
        textoAsc += '''<sentencia_dml> ::= <insertar>
                | <actualizar>
                | <eliminar>
                | <seleccionH>
                | <mostrar>
                | <altert> \n'''

        tam = 0
        while tam < len(lista_instrucciones):
            instruccion = lista_instrucciones[tam]

            if isinstance(instruccion, CrearBD):
                textoAsc += '<crear> ::= "CREATE" <reemplazar> "DATABASE" <verificacion> <ID> <propietario> <modo> \n'
            elif isinstance(instruccion, CrearTabla):
                textoAsc += '<crear> ::= "CREATE" "TABLE" <ID> "(" <columnas> ")" <herencia> \n'
            elif isinstance(instruccion,CrearType):
                textoAsc += '<crear> ::= "CREATE" "TYPE" <ID> "AS" "ENUM" ""(""<lista_exp> "")"" \n'
            elif isinstance(instruccion,EliminarDB):
                textoAsc += '<liberar> ::= "DROP" "DATABASE" <existencia> <ID> \n'
            elif isinstance(instruccion,EliminarTabla):
                textoAsc += '<liberar> ::= "DROP" "TABLE" <existencia> <ID> \n'
                
            '''elif isinstance(instruccion,Insertar):
                
            elif isinstance(instruccion,Actualizar):
                
            elif isinstance(instruccion,DBElegida):
                
            elif isinstance(instruccion,MostrarDB):'''
            tam = tam + 1

        textoAsc += '``` \n '
        
        #html = markdown.markdown(textoAsc)
        try:
            with open('gramatica_ASC.md','w') as rep:
                rep.write(textoAsc)
        except Exception as e:
            print("No fue posible generar el reporte gramatical ASC: "+ str(e))


    #Reporte gramatical descendente
    def grammarDSC(self,instrucciones):
        lista_instrucciones = instrucciones
        global textoDsc

        textoDsc = '# Gramatica Descendente \n'
        textoDsc += '```sh \n'
        textoDsc += '<init> ::= <l_sentencias> \n'
        textoDsc += '''<l_sentencias> ::= <l_sentencias sentencias>
        | <sentencias> \n'''
        textoDsc += '<sentencias> ::= <sentencia> ";" \n'
        textoDsc += '''<sentencia> ::= <sentencia_ddl>
        | <sentencia_dml> \n'''


        tam = 0
        while tam < len(lista_instrucciones):
            instruccion = lista_instrucciones[tam]

            if isinstance(instruccion, CrearBD):
                textoDsc += '<sentencia> ::= <sentencia_ddl> \n'
                textoDsc += '<sentencia_ddl> ::= <crear> \n'
                textoDsc += '<crear> ::= "CREATE" <reemplazar> "DATABASE" <verificacion> <ID> <propietario> <modo> \n'

            tam = tam +1
        textoDsc += '\n ``` \n'
        
        try:
            with open('gramatica_DSC.md','w') as rep:
                rep.write(textoDsc)
        except Exception as e:
            print("No fue posible generar el reporte gramatical DSC: "+ str(e))



    

