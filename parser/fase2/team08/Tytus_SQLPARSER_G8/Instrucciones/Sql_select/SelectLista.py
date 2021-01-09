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
from Instrucciones.TablaSimbolos.Nodo3D import Nodo3D
from Instrucciones.Sql_select.Alias import Alias
import numpy as np

class SelectLista(Instruccion):
    def __init__(self, lista, strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.QUERY),linea,columna,strGram)
        self.lista = lista

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        columnas = []
        valores = []
        selectEncontrado = 0
        tipoResultado = None
        for ins in self.lista:
            if isinstance(ins, Alias):
                resultado = ins.expresion.ejecutar(tabla, arbol)
                if isinstance(resultado, Excepcion):
                    return resultado
                valores.append(str(resultado))
                columnas.append(ins.id)
                tipoResultado = ins.tipo
            elif isinstance(ins, Select):
                resultado = ins.ejecutar(tabla, arbol)
                if isinstance(resultado, Excepcion):
                    return resultado
                tipoResultado = ins.tipo
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
                tipoResultado = ins.tipo
        #print("COLUMNAS-------------------------->",columnas)
        #print("VALORES-------------------------->",valores)
        if arbol.expre_query:
            if tipoResultado.tipo == Tipo_Dato.SMALLINT or tipoResultado.tipo == Tipo_Dato.INTEGER or tipoResultado.tipo == Tipo_Dato.BIGINT:
                return int(valores[0])
            elif tipoResultado.tipo == Tipo_Dato.NUMERIC or tipoResultado.tipo == Tipo_Dato.DECIMAL or tipoResultado.tipo == Tipo_Dato.REAL or tipoResultado.tipo == Tipo_Dato.DOUBLE_PRECISION:
                return float(valores[0])
            else:
                if isinstance(valores[0], (np.ndarray, np.generic)):
                    #print(valores[0][0])
                    return valores[0][0]
                else:
                    return valores[0]

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
        return self.tipo
        
    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        cadena = ""
        cadena += "f\"SELECT "

        for query in self.lista:
            if isinstance(query, Llamada):
                cadena += query.concatenar(tabla,arbol)
            elif isinstance(query, Primitivo):
                #print("SELECT",query.traducir(tabla, arbol).temporalAnterior)
                cadena += query.traducir(tabla,arbol).temporalAnterior
            #elif isinstance(query, Select):
                #cadena +=f"{query.traducir(tabla,arbol)}"
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

    def c3d(self, tabla, arbol):
        retorno = Nodo3D()
        #print("SELECT LISTA")
        cadena = ""
        cadena += "f\"SELECT "

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
            retorno.temporalAnterior = temporalR
            return retorno
        else:
            return cadena


class SelectLista2(Instruccion):
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
        return valores[0]
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
        return self.tipo
        
    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        cadena = ""
        cadena += "f\"SELECT "

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

    def c3d(self, tabla, arbol):
        retorno = Nodo3D()
        #print("SELECT LISTA")
        cadena = ""
        cadena += "f\"SELECT "

        for query in self.lista:
            if isinstance(query, Llamada):
                cadena += query.concatenar(tabla,arbol)
            elif isinstance(query, Primitivo):
                #print("SELECT",query.traducir(tabla, arbol).temporalAnterior)
                cadena += query.traducir(tabla,arbol).temporalAnterior
            #elif isinstance(query, Select):
            #    cadena +=f"{query.traducir(tabla,arbol)}"
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

            if arbol.tamanio_actual == None:
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
                retorno.temporalAnterior = temporalR
            else:
                arbol.addComen("Asignar cadena")
                tempcadena = tabla.getTemporal()
                arbol.addc3d(f"{tempcadena} = { cadena }")

                arbol.addComen("Simulando el paso de parámetros")
                temp1 = tabla.getTemporal()
                arbol.addc3d(f"{temp1} = P + 2")
                temporal1 = tabla.getTemporal()
                arbol.addc3d(f"{temporal1} = {temp1} + {arbol.tamanio_actual}")
                arbol.addComen("Asignación de parámetros")
                
                temporal2 = tabla.getTemporal()
                arbol.addComen("parametro 1")
                arbol.addc3d(f"{temporal2} = { temporal1} + 1")
                arbol.addComen("Asignacion de parametros")
                arbol.addc3d(f"Pila[{temporal2}] = {tempcadena}")

                temporal3 = tabla.getTemporal()
                temporal4 = tabla.getTemporal()
                arbol.addComen("Cambio de ámbito")
                arbol.addc3d(f"P = P + 2")
                arbol.addc3d(f"P = P + {arbol.tamanio_actual}")
                arbol.addComen("Llamada a la función")
                arbol.addc3d(f"funcionintermedia()")
                arbol.addComen("Posición del return en el ámbito de la función")
                arbol.addc3d(f"{temporal3} = {temporal1} + 2")
                arbol.addc3d(f"{temporal4} = Pila[{temporal3}]")        
                arbol.addc3d(f"P = P - 2")
                arbol.addc3d(f"P = P - {arbol.tamanio_actual}")
                retorno.temporalAnterior = temporal4
                return retorno

            return retorno
        else:
            return cadena

'''
class Alias(Instruccion):
    def __init__(self, id, expresion, pas):
        Instruccion.__init__(self,None,None,None,None)
        self.id = id
        self.expresion = expresion
        self.tipo = None
        self.pas = pas

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        pass
    def analizar(self, tabla, arbol):
        super().analizar(tabla,arbol)
        pass

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        cadena=""
    
        if isinstance(self.expresion,str):
            if self.id != None:
                cadena += f"{self.id}.{self.expresion} "
            else:
                cadena += self.expresion + " "

        elif isinstance(self.expresion, Identificador):
            if self.pas=="AS":
                cadena += f"{self.expresion.concatenar(tabla,arbol)} {self.pas} {self.id}"
            else:
                cadena += f"{self.expresion.concatenar(tabla,arbol)} {self.id}"
        else:
            if self.pas=="AS":
                cadena += f"{self.expresion.traducir(tabla,arbol)} {self.pas} {self.id}"
            else:
                cadena += f"{self.expresion.traducir(tabla,arbol)} {self.id}"
        return cadena


'''