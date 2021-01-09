

from numpy.core.defchararray import isdigit
from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from sql.Instrucciones.Excepcion import Excepcion


class WidthBucket(Instruccion):
    def __init__(self, valor, min, max, count, tipo, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor
        self.min = min
        self.max = max
        self.count = count

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        resultado = self.valor.ejecutar(tabla,arbol)
        try:
            if self.count.tipo.tipo == Tipo_Dato.INTEGER:
                print(self.count.tipo.toString(),Tipo_Dato.INTEGER)
                temp = (self.max.valor - self.min.valor)/self.count.valor
                contador= float(self.min.valor)
                cubo=0
                if float(resultado)==contador:
                        self.tipo = Tipo(Tipo_Dato.INTEGER)
                        return 1
                while contador < float(self.max.valor):
                    if float(resultado)<contador:
                        self.tipo = Tipo(Tipo_Dato.INTEGER)
                        return cubo
                        
                    contador += temp
                    cubo+=1
                self.tipo = Tipo(Tipo_Dato.INTEGER)
                return cubo +1
            else:
                error = Excepcion('42883',"Semántico",f"No existe la función width_bucket({self.valor.tipo.toString()},{self.min.tipo.toString()},{self.max.tipo.toString()},{self.count.tipo.toString()})",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                arbol.consola.append("El Cuarto Párametro debe ser Integer.")
                return error 
        except:
            error = Excepcion('XX000',"Semántico",f"Error Interno width_bucket",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error 
