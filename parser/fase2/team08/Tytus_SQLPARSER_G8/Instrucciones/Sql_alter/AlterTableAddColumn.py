from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion
import collections
from storageManager.jsonMode import *

class AlterTableAddColumn(Instruccion):
    def __init__(self, tabla, lista_col, strGram,linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.tabla = tabla
        self.lista_col = lista_col
    

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if arbol.bdUsar != None:
            objetoTabla = arbol.devolviendoTablaDeBase(self.tabla)
            if objetoTabla != 0:
                existeColumna = False
                for c in self.lista_col:
                    for columnas in objetoTabla.lista_de_campos:
                        # Si la columna ya existe retorna error semántico
                        if columnas.nombre == c.id:
                            existeColumna = True
                            error = Excepcion('42701',"Semántico","Ya existe la columna «"+c.id+"» en la relación «"+self.tabla+"»",c.linea,c.columna)
                            arbol.excepciones.append(error)
                            arbol.consola.append(error.toString())
                if existeColumna:
                    return
                # Existen columnas con el mismo nombre a insertar
                nombres = []
                for columnas in self.lista_col:
                    nombres.append(columnas.id)
                duplicados = [item for item, count in collections.Counter(nombres).items() if count > 1]
                for columnas in duplicados:
                    existeColumna = True
                    error = Excepcion('42701',"Semántico","Ya existe la columna «"+columnas+"» en la relación «"+self.tabla+"»",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                if existeColumna:
                    return
                # Las columnas se almacenan en memoria.
                for c in self.lista_col:     
                    objetoTabla.agregarColumna(c.id, c.tipo,None, None)
                # Las columnas se almacenan en disco.
                for columnas in self.lista_col:
                    resultado = alterAddColumn(arbol.getBaseDatos(),self.tabla,columnas.id)
                    if resultado == 1:
                        error = Excepcion('XX000',"Semántico","Error interno",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    elif resultado == 2:
                        error = Excepcion('42P00',"Semántico","La base de datos "+str(arbol.getBaseDatos())+" no existe",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    elif resultado == 3:
                        error = Excepcion('42P01',"Semántico","No existe la relación "+self.tabla,self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                arbol.consola.append("Consulta devuelta correctamente.")
            else:
                error = Excepcion('42P01',"Semántico","No existe la relación "+self.tabla,self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        else:
            error = Excepcion("100","Semantico","No ha seleccionado ninguna Base de Datos.",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
    
    def analizar(self, tabla, arbol):
        pass
    
    def traducir(self, tabla, arbol):
        cadena = "\"alter table "
        if(self.tabla):
            cadena += self.tabla
        cadena += " add column "
        if(self.lista_col):
            for x in range(0,len(self.lista_col)):
                cadena += self.lista_col[x].traducir(tabla,arbol)
                valor = self.lista_col[x].getTipo()
                x = valor.name
                y = x.lower()
                cadena += " " + y
        cadena += ";\""

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
