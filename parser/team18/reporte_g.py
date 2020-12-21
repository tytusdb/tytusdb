
from expresiones import *
from instrucciones import *
import tablasimbolos as TS
#import markdown


class Reporte_Gramaticas:
    textoAsc = ''

    def __init__(self):
        print("Reportes gramaticales ASC y DSC")


    def grammarASC(self,instrucciones):

        lista_instrucciones = instrucciones
        global textoAsc

        textoAsc = '# Reporte Gramatical Ascendente \n'
        textoAsc += '```sh \n'
        textoAsc += '<init> ::= <l_sentencias> { init.val = l_sentencias.val } \n'
        textoAsc += '''<l_sentencias> ::= <l_sentencias sentencias> { l_sentencias.val = l_sentencias.append(sentencias.val) }
        | <sentencias>   \n'''
        textoAsc += '<sentencias> ::= <sentencia> ";"  { sentencias.val = sentencia.val }  \n'
        textoAsc += '''<sentencia> ::= <sentencia_ddl> { sentencia.val = sentencia_ddl.val}
        | <sentencia_dml>  { sentencia = sentencia_dml.val} \n'''
        textoAsc += '''<sentencia_ddl> ::= <crear> { sentencia_ddl.val = crear.val  }
                | <liberar>  { sentencia_ddl.val =  liberar.val } \n'''
        textoAsc += '''<sentencia_dml> ::= <insertar> { sentencia_dml.val = insertar.val }
                | <actualizar> { sentencia_dml.val = actualizar.val }
                | <eliminar> { sentencia_dml.val = eliminar.val }
                | <seleccionH> { sentencia_dml.val = seleccionH.val }
                | <mostrar> { sentencia_dml.val = mostrar.val}
                | <altert>  { sentencia_dml.val = altert.val} 
                | <usar>  { sentencia_dml.val = usar.val } \n'''

        tam = 0
        while tam < len(lista_instrucciones):
            instruccion = lista_instrucciones[tam]

            if isinstance(instruccion, CrearBD):
                textoAsc += '<crear> ::= "CREATE" <reemplazar> "DATABASE" <verificacion> <ID> <propietario> <modo> { crear.val = CrearBD(t[2], t[4], Operando_ID( %s ), t[6], t[7]) } \n ' %(str(instruccion.nombre.id))

            elif isinstance(instruccion, CrearTabla):
                textoAsc += '<crear> ::= "CREATE" "TABLE" <ID> "(" <columnas> ")" <herencia> { crear.val = CrearTabla(Operando_ID( %s ),t[7],t[5])  }  \n' %(str(instruccion.nombre.id))
            elif isinstance(instruccion,CrearType):
                textoAsc += '<crear> ::= "CREATE" "TYPE" <ID> "AS" "ENUM" ""(""<lista_exp> "")""  { crear.val =CrearType(Operando_ID( %s ),t[7])  }  \n' %(str(instruccion.nombre.id))
            elif isinstance(instruccion,EliminarDB):
                textoAsc += '<liberar> ::= "DROP" "DATABASE" <existencia> <ID> { liberar.val =EliminarDB(t[3],Operando_ID( %s )) }  \n' %(str(instruccion.nombre.id))
            elif isinstance(instruccion,EliminarTabla):
                textoAsc += '<liberar> ::= "DROP" "TABLE" <existencia> <ID> { liberar.val = EliminarTabla(t[3],Operando_ID( %s )) } \n' %(str(instruccion.nombre.id))
                
            elif isinstance(instruccion,Insertar):
                textoAsc += '<insertar> ::= "INSERT" "INTO" <ID> <para_op> "VALUES" "(" <lista_exp> ")" \n'
                textoAsc += '<para_op> ::= PAR_A <lnombres> PAR_C { para_op.val = lnombres.val } \n'
                
            elif isinstance(instruccion,Actualizar):
                textoAsc += '<actualizar> ::= "UPDATE" <ID> "SET" <lista_update> "WHERE" <exp> { actualizar = Actualizar(Operando_ID(t[2]),t[6],t[4])  } \n'
                textoAsc += '<lista_update> ::= <lista_update> "," campoupdate \n'
                textoAsc += '               | campoupdate     { listaupdate.append(campoupdate) listaupdate.val = campoupdate.val} \n'
                
                
            elif isinstance(instruccion,DBElegida):
                textoAsc += '<usar> ::= "USE" <ID> { usar.val = DBElegida(Operando_ID( %s ))} \n' %(str(instruccion.nombre.id))
            elif isinstance(instruccion,MostrarDB):
                textoAsc += '<mostrar> ::= "SHOW" "DATABASES" { mostrar.val = MostrarDB() } \n'
            elif isinstance(instruccion,MostrarTB):
                textoAsc += '<mostrar> ::= "SHOW" "TABLE" { mostrar.val = MostrarTB() } \n'

            tam = tam + 1

        textoAsc += '``` \n '
        
        #html = markdown.markdown(textoAsc)
        try:
            with open('gramatica_ASC.md','w') as rep:
                rep.write(textoAsc)
        except Exception as e:
            print("No fue posible generar el reporte gramatical ASC: "+ str(e))


    

