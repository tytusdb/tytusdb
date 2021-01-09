from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.TablaSimbolos.Simbolo import Simbolo
from Instrucciones.TablaSimbolos.Tabla import Tabla
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Retorno import Retorno
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.TablaSimbolos.Simbolo import Simbolo
from Instrucciones.Tablas.Tablas import Tablas
from Optimizador.C3D import *
from Instrucciones.TablaSimbolos import Instruccion3D as c3d
import os.path
from os import path
import webbrowser

class CreateProcedure(Instruccion):
    def __init__(self, id, replace, parametros, declaraciones, instrucciones, tipo, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna,strGram)
        self.id = id
        self.replace = replace
        self.parametros = parametros
        self.declaraciones = declaraciones
        self.instrucciones = instrucciones

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        
        # tablaNueva = Tablas(self.id,None)
        # arbol.agregarTablaABd(tablaNueva)   

        # var = self.lcol[x]
        # objetoTabla = arbol.devolviendoTablaDeBase(val)
        # self.crear_tabla()


        arbol.lista_funciones.append(self.id)

        parametros_rep = ''
        for param in self.parametros:
            i = 0
            for parametro in param:
                if i == 1:
                    parametros_rep += str(parametro) + ' ['
                elif i == 2:
                    dato = str(parametro.tipo).replace("Tipo_Dato.", "").lower()
                    if 'varchar' == dato:
                        parametros_rep += dato +'(' + str(parametro.dimension)  + ')], '
                    else:
                        parametros_rep += dato + '], '
                    i = 0
                i += 1

        arbol.lista_funciones.append(parametros_rep)
        arbol.lista_funciones.append(self.id)
        arbol.lista_funciones.append('Procedimiento')
        
        self.crear_tabla(arbol)
        arbol.consola.append(f"Se Creo la Funcion: {self.id} correctamente.")



        '''tablaLocal = Tabla(None)
        print("==>>>", self.parametros)
        for i in self.parametros:
            i.ejecutar(tablaLocal, arbol)

        for i in self.declaraciones:
            i.analizar(tablaLocal, arbol)

        tablaLocal.anterior = tabla
        
        esFuncion = False
        if self.tipo.tipo != Tipo_Dato.VOID:
            esFuncion = True
        
        hayReturn = False
        for i in self.instrucciones:
            resultado = i.analizar(tablaLocal, arbol)
            if isinstance(i, Retorno):
                if isinstance(resultado, Excepcion):
                    return resultado
                hayReturn = True

        if esFuncion and not hayReturn:
            error = Excepcion("42723", "Semantico", f"La función {self.id} requiere un valor de retorno", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        
        if not esFuncion and hayReturn:
            error = Excepcion("42723", "Semantico", f"El método {self.id} no requiere un valor de retorno", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error  
        pass
'''
    def llenarTS(self, tabla, arbol):
        existe = tabla.getSimboloFuncion(self.id)
        if existe != None:
            if self.replace != None:
                # Espacio para el return
                arbol.contador += 1

                # Espacio para los parámetros
                arbol.contador += len(self.parametros)

                # Espacio para los parámetros
                arbol.contador += len(self.declaraciones)

                print("tamaño de la función ------------>",arbol.contador)

                existe.rol = "Metodo"
                existe.funcion = self
                existe.tamanio = arbol.contador 
                arbol.contador = 0
                print("se limpió? ------------>",arbol.contador, existe.tamanio)
                return 
            else:
                error = Excepcion("42723", "Semantico", f"La función {self.id} ya existe.", self.linea, self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        
        if self.tipo.tipo != Tipo_Dato.VOID:
            # Espacio para el return
            arbol.contador += 1

        # Espacio para los parámetros
        arbol.contador += len(self.parametros)

        # Espacio para los parámetros
        arbol.contador += len(self.declaraciones)

        #print("tamaño de la función ------------>",arbol.contador)

        f = Simbolo(self.id, self.tipo, "", self.linea, self.columna)
        f.rol = "Metodo"
        f.funcion = self
        f.tamanio = arbol.contador
        tabla.agregarSimbolo(f) 
        arbol.contador = 0
        #print("se limpió? ------------>",arbol.contador, f.tamanio)       



    
    def crear_tabla(self, arbol):
        filename = "TablaFunciones.html"
        file = open(filename,"w",encoding='utf-8')
        file.write(self.reporte_tabla(arbol.lista_funciones))
        file.close()
        # webbrowser.open_new_tab(filename)


    def reporte_tabla(self, lista_funciones):
        cadena = ''
        cadena += "<html><head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/><title>Reporte</title><style> \n"
        cadena += "table{ \n"
        cadena += "width:100%;"
        cadena += "} \n"
        cadena += "table, th, td {\n"
        cadena += "border: 1px solid black;\n"
        cadena += "border-collapse: collapse;\n"
        cadena += "}\n"
        cadena += "th, td {\n"
        cadena += "padding: 5px;\n"
        cadena += "text-align: left;\n"
        cadena += "}\n"
        cadena += "table#t01 tr:nth-child(even) {\n"
        cadena += "background-color: #eee;\n"
        cadena += "}\n"
        cadena += "table#t01 tr:nth-child(odd) {\n"
        cadena += "background-color:#fff;\n"
        cadena += "}\n"
        cadena += "table#t01 th {\n"
        cadena += "background-color: black;\n"
        cadena += "color: white;\n"
        cadena += "}\n"
        cadena += "</style></head><body><h1><center>Tabla de Funciones y Procedimientos</center></h1>\n"
        cadena += "<table id=\"t01\">\n"

        cadena += "<tr>\n"
        cadena += "<th><center>#</center></th>\n"
        cadena += "<th><center>ID</center></th>\n"
        cadena += "<th><center>Parametros</center></th>\n"
        cadena += "<th><center>Tipo Retorno</center></th>\n"
        cadena += "<th><center>Tipo Instruccion</center></th>\n"
        cadena += "</tr>\n"

        contador = 0
        while(contador < len(lista_funciones) ):
            cadena += "<tr>\n"
            val = (contador+4)/4
            cadena += "<td><center>" + str(val) + "</center></td>\n"

            cadena += "<td><center>" + lista_funciones[contador] + "</center></td>\n"
            cadena += "<td><center>" + lista_funciones[contador + 1] + "</center></td>\n"
            cadena += "<td><center>" + lista_funciones[contador + 2] + "</center></td>\n"
            cadena += "<td><center>" + lista_funciones[contador + 3] + "</center></td>\n"
            cadena += "</tr>\n"
            contador += 4


        cadena += "</table>\n"
        cadena += "</body>\n"
        cadena += "</html>"
        return cadena


    def generar3D(self, tabla, arbol):  
        super().generar3D(tabla,arbol)
        code = []
        code.append(c3d.asignacionH())
        code.append(c3d.aumentarP())
        t0 = c3d.getTemporal()
        # code.append(c3d.asignacionString(t0, "CREATE INDEX " + self.ID))
        code.append(c3d.asignacionString(t0, "CREATE INDEX test2_mm_idx ON tabla(id);"))
        #CREATE INDEX test2_mm_idx ON tabla(id);

        # code.append(c3d.operacion(t1, Identificador(t0), Valor("\";\"", "STRING"), OP_ARITMETICO.SUMA))
        code.append(c3d.asignacionTemporalStack(t0))
        code.append(c3d.LlamFuncion('call_funcion_intermedia'))

        return code