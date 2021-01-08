from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Sql_select.Select import Select
from Instrucciones.Tablas.Tablas import Tablas
from Instrucciones.Identificador import Identificador
import pandas as pd


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
    def get_methods(object6, spacing=20):
        methodList = []
        for method_name in dir(object6):
            try:
                if callable(getattr(object6, method_name)):
                    methodList.append(str(method_name))
            except:
                methodList.append(str(method_name))
        processFunc = (lambda s: ' '.join(s.split())) or (lambda s: s)
        for method in methodList:
            try:
                print(str(method.ljust(spacing)) + ' ' +
                    processFunc(str(getattr(object6, method).__doc__)[0:90]))
            except:
                print(method.ljust(spacing) + ' ' + ' getattr() failed')

    def extraer(self,tabla,arbol):
        
        cadena = " "
        print("select99999") 
        mitabla =" "

        try: 
              cadena = "\"select "
              wherecond = " "
              for x in self.lista:
                print("entro") 
                print(x)
                print("ttttt") 

                print(x.lcol2)
                print("entrrrrrrrro") 
                if isinstance(x, Select):
                    print("isinstance Select") 
                    lcol2=x.getparam2(tabla,arbol)

                    for xu in lcol2:
                        print("xu lcol2 es ",xu) 
                        if isinstance(xu, Identificador):
                            print("isinstance Identificador") 
                            mitabla =  xu.devolverId(tabla,arbol)
                            print("mitabla es",mitabla) 


                    lcol20=x.getparam1(tabla,arbol)

                    for xu in lcol20:
                        print("xu lcoli20 es ",xu) 
                        print(xu) 

                        try:
                            if isinstance(xu, Identificador):
                                print("isinstance Identificador") 
                                cadena +=  xu.devolverId(tabla,arbol)
                                print("cadena es") 
                                print(xu.devolverId(tabla,arbol))
                            else :
                                print("no es") 

                                cadena +=  xu
                                print("no es",cadena) 

                        except Exception as e:
                             print(e)
                    print("cadu.deena es",cadena) 


                     

              cadena += " from "+mitabla 

              if x.where !=None:
                    wherecond=x.where.extraer(tabla,arbol)
              cadena += wherecond

              cadena += ";\""
              print("cadenao es",cadena) 

        except Exception as e:
              print(e)
 
        return cadena          
    def traducir(self, tabla, arbol):

        cadena = " "

        print("seguira ") 
        try: 
            cadena = self. extraer(tabla,arbol)

        except Exception as e:
              print(e)
        print("cadenaiuo es",cadena) 

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

        print("hello")

        print(arbol.get3d())
        print("dsliio hello")


class Alias():
    def __init__(self, id, expresion):
        self.id = id
        self.expresion = expresion
        self.tipo = None