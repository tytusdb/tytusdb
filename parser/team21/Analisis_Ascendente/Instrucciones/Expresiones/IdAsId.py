from tytus.parser.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion,IdId
from tytus.parser.team21.Analisis_Ascendente.Instrucciones.Time import Time
from tytus.parser.team21.Analisis_Ascendente.Instrucciones.expresion import *
from tytus.parser.team21.Analisis_Ascendente.Instrucciones.Expresiones.Trigonometrica import Trigonometrica
from tytus.parser.team21.Analisis_Ascendente.Instrucciones.Expresiones.Math import  Math_
from tytus.parser.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion import  Expresion

class IdAsId(Instruccion):
    '''ID ID
        o
        ID AS ID'''
    def __init__(self, id1, id2,fila,columna):
        self.id1 = id1  # puede venir time, math, trig, binario
        self.id2 = id2  # puede venir una cadena
        self.fila = fila
        self.columna = columna


    def Resolver(IdAsId,Consola):

        if (isinstance(IdAsId.id1, Time)):
            valor = Time.resolverTime(IdAsId.id1);
            return valor;
        elif (isinstance(IdAsId.id1, Math_)):
            valor = Math_.Resolver(IdAsId.id1,None,Consola,None)
            return str(valor)
        elif (isinstance(IdAsId.id1, Trigonometrica)):
            valor = Trigonometrica.Resolver(IdAsId.id1,None,Consola,None)
            return valor
        elif (isinstance(IdAsId.id1, Primitivo)):
            valor = IdAsId.id1.valor;
            return  valor
        elif (isinstance(IdAsId.id1,Id)):
            valor = IdAsId.id1.id
            return  valor
        elif (isinstance(IdAsId.id1,IdId)):
            valor1 = IdAsId.id1.id1
            valor2 = IdAsId.id1.id2
            return [valor1,valor2]
        elif isinstance(IdAsId.id1,Expresion):
            return Expresion.Resolver(IdAsId.id1,Consola)
        return 'what -- ' + type(IdAsId.id1).__name__ + '\n'
