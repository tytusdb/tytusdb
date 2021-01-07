import math
from analizadorFase2.Operaciones.TiposOperacionesA import TiposOperaciones
from analizadorFase2.Abstractas.Expresion import Expresion


class funcion_avg(Expresion):
    def __init__(self, lnumf):
        self.lnumf = lnumf

class funcion_funIntermedia1(Expresion): 
    '''clase que va a obtener una lista de valores y apoyarse con 
    una pila para saber que accion tomar '''
    def __init__(self, ftipo, lnumf):
        self.ftipo = ftipo
        self.lnumf = lnumf

    def traduccionFunNativas(self): 
        #traduccion del codigo 3D 
        cadenaC3D=""
        #meter el tipo de funcion a la pila
        cadenaC3D='pilaFun.encolar(' + self.ftipo + ')' + '\n' 
        #recorro el arreglo en su primer nodo 
        #si es temporal lo meto en la pila 
        
        #si es una variable buscar el valor en la TS y meterlo en la pila 
        #si es una expresion meter el valor a la pila 
        if isinstance(self.lnumf[0], int):
            #si es un valor meterlo a la pila 
            cadenaC3D='pilaFun.encolar('
            

        
        #meter el temporal a la pila 
        return cadenaC3D

    def ejecutarFunNativas(self): 
        
        #buscar en la pila que tipo de funcion es 
        #recorrer la lista 
        month=""
        switch (month) {
            case 1:  monthString = "January";
                     break;
            case 2:  monthString = "February";
                     break;
            case 3:  monthString = "March";
                     break;
            case 4:  monthString = "April";
                     break;
            case 5:  monthString = "May";
                     break;
            case 6:  monthString = "June";
                     break;
            case 7:  monthString = "July";
                     break;
            case 8:  monthString = "August";
                     break;
            case 9:  monthString = "September";
                     break;
            case 10: monthString = "October";
                     break;
            case 11: monthString = "November";
                     break;
            case 12: monthString = "December";
                     break;
            default: monthString = "Invalid month";
                     break;
        }
            #si es un temporal meterlo a la pila 
            #si es un valor meterlo a la pila 
            #si es una variable buscarla en la TS y luego meterlo a la pila 
            #si es una expresion, ejecutarlo y meter el temporal a la pila


def sum(column):
    """
    Funcion encargada de sumar todas las cantidades de una columna
    """

    return math.fsum(column)


def count(column):
    """
    Funcion encargada de contar cuantas filas tiene una columna
    """
    return len(column)


def avg(column):
    """
    Funcion encargada de promediar todas las cantidades de una columna
    """
    return sum(column) / count(column)


def max(column):
    """
    Funcion encargada de devolver el valor maximo de una columna
    """
    return max(column)


def min(column):
    """
    Funcion encargada de devolver el valor minimo de una columna
    """
    return min(column)
