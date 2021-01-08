from Instrucciones.PL.Llamada import Llamada
from Instrucciones.Expresiones import Aritmetica
from Instrucciones.Identificador import Identificador
import Instrucciones
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Sql_select.Select import Select
from Instrucciones.Tablas.Tablas import Tablas
from Instrucciones.Expresiones.Primitivo import *


class SelectLista(Instruccion):
    def __init__(self, lista, strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.QUERY),linea,columna,strGram)
        self.lista = lista

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        columnas = []
        valores = []
        selectEncontrado = 0
        for ins in self.lista:
            if isinstance(ins, Alias):
                resultado = ins.expresion.ejecutar(tabla, arbol)
                if isinstance(resultado, Excepcion):
                    return resultado
                valores.append(str(resultado))
                columnas.append(ins.id)
            elif isinstance(ins, Select):
                resultado = ins.ejecutar(tabla, arbol)
                if isinstance(resultado, Excepcion):
                    return resultado
                valores = resultado
                columnas = ins.devolverColumnas(tabla,arbol)
                if isinstance(columnas, Excepcion):
                    return columnas
                selectEncontrado = 1
            else:
                resultado = ins.ejecutar(tabla, arbol)
                if isinstance(resultado, Excepcion):
                    return resultado
                valores.append(str(resultado))
                columnas.append('col')
        #print("COLUMNAS-------------------------->",columnas)
        #print("VALORES-------------------------->",valores)
        if(selectEncontrado == 0):
            valores = [valores]
            
            if(arbol.getRelaciones() == False):
                arbol.getMensajeTabla(columnas,valores)
            else:
                n = Tablas("tabla",None)
                n.data = valores
                n.lista_de_campos = columnas
                return n
        else:
            if(arbol.getRelaciones() == False):
                arbol.getMensajeTabla(columnas,valores)
            else:
                n = Tablas("tabla",None)
                n.lista_de_campos = columnas
                n.data = valores
                return n

    def analizar(self, tabla, arbol):
        pass
        
    def traducir(self, tabla, arbol):
        #print("SELECT LISTA")
        cadena = ""
        cadena += "\"SELECT "

        print(type(self.lista))
        for query in self.lista:
            if isinstance(query, Llamada):
                cadena += query.concatenar(tabla,arbol)
            elif isinstance(query, Primitivo):
                #print("SELECT",query.traducir(tabla, arbol).temporalAnterior)
                cadena += query.traducir(tabla,arbol).temporalAnterior
            elif isinstance(query, Select):
                cadena +=f"{query.traducir(tabla,arbol)}"
            elif isinstance(query, Aritmetica.Aritmetica):
                cadena += f"{query.concatenar(tabla,arbol)}"
            else:
                cadena += f"{query.traducir(tabla,arbol)}"
            if self.lista.index(query) == len(self.lista)-1:
                cadena += " "
            else:
                cadena += ", "

        cadena += ";\""

        if(arbol.getRelacionales()==False):
            arbol.addComen("Asignar cadena")
            temporal1 = tabla.getTemporal()
            arbol.addc3d(f"{temporal1} = { cadena }")

            arbol.addComen("Entrar al ambito")
            temporal2 = tabla.getTemporal()
            arbol.addc3d(f"{temporal2} = P+2")
            temporal3 = tabla.getTemporal()
            arbol.addComen("parametro 1")
            arbol.addc3d(f"{temporal3} = { temporal2}+1")
            arbol.addComen("Asignacion de parametros")
            arbol.addc3d(f"Pila[{temporal3}] = {temporal1}")

            arbol.addComen("Llamada de funcion")
            arbol.addc3d(f"P = P+2")
            arbol.addc3d(f"funcionintermedia()")
            
            arbol.addComen("obtener resultado")
            temporalX = tabla.getTemporal()
            arbol.addc3d(f"{temporalX} = P+2")
            temporalR = tabla.getTemporal()
            arbol.addc3d(f"{temporalR} = Pila[{ temporalX }]")

            arbol.addComen("Salida de funcion")
            arbol.addc3d(f"P = P-2")
        else:
            return cadena

    def traducir2(self, tabla, arbol):
        cadena = ""
        cadena += "(SELECT "
        for query in self.lista:
            if isinstance(query, Primitivo):
                #print("SELECT",query.traducir(tabla, arbol).temporalAnterior)
                cadena += query.traducir(tabla,arbol).temporalAnterior
            elif isinstance(query, Select):
                cadena +=f"{query.traducir(tabla,arbol)}"
            elif isinstance(query, Aritmetica.Aritmetica):
                cadena += f"{query.concatenar(tabla,arbol)}"
            else:
                cadena += f"{query.traducir(tabla,arbol)}"
                
            if self.lista.index(query) == len(self.lista)-1:
                cadena += " "
            else:
                cadena += ", "
        
        cadena = cadena.rstrip() + ")"
        return cadena

class Alias(Instruccion):
    def __init__(self, id, expresion, pas):
        Instruccion.__init__(self,None,None,None,None)
        self.id = id
        self.expresion = expresion
        self.tipo = None
        self.pas = pas

    def ejecutar(self, tabla, arbol):
        pass
    def analizar(self, tabla, arbol):
        pass

    def traducir(self, tabla, arbol):
        cadena=""
        print("PASO ALIAS")
        print(self.expresion, self.id)

        
            
        if isinstance(self.expresion,str):
            if self.id != None:
                cadena += f"{self.id}.{self.expresion} "
            else:
                cadena += self.expresion + " "
        elif isinstance(self.expresion, Identificador):
            if self.pas=="AS":
                cadena += f"{self.expresion.concatenar(tabla,arbol)} {self.pas} '{self.id}'"
            else:
                cadena += f"{self.expresion.concatenar(tabla,arbol)} '{self.id}'"
        else:
            if self.pas=="AS":
                cadena += f"{self.expresion.traducir(tabla,arbol)} {self.pas} '{self.id}'"
            else:
                cadena += f"{self.expresion.traducir(tabla,arbol)} '{self.id}'"
        return cadena