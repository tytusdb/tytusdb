from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion,IdId
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Time import Time
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.expresion import *
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Trigonometrica import Trigonometrica
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Math as  Math_
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion as  Expresion
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Binario as Binario

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
        elif (isinstance(IdAsId.id1, Math_.Math_)):
            valor = Math_.Math_.Resolver(IdAsId.id1,None,Consola,None)
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
        elif isinstance(IdAsId.id1,Expresion.Expresion):
            return Expresion.Expresion.Resolver(IdAsId.id1,None,Consola,None)
        return 'what -- ' + type(IdAsId.id1).__name__ + '\n'

    def ObtenerCadenaEntrada(IdAsId,condicion):
        id1=''
        id2=''
        if (isinstance(IdAsId.id1, Time)):
            #valor = Time.resolverTime(IdAsId.id1);
            return Time.ObtenerCadenaEntrada(IdAsId.id1);
        elif (isinstance(IdAsId.id1, Math_.Math_)):
            id1 = str(Math_.Math_.obtenerCadenaEntrada(IdAsId.id1,condicion))
        elif (isinstance(IdAsId.id1, Trigonometrica)):
            id1 = str(Trigonometrica.obtenerCadenaEntrada(IdAsId.id1,condicion))
        elif (isinstance(IdAsId.id1, Primitivo)):
            id1 = str(Primitivo.ObtenerCadenaEntrada(IdAsId.id1))
        elif (isinstance(IdAsId.id1,Id)):
            id1 = str(IdAsId.id1.id)
        elif (isinstance(IdAsId.id1,IdId)):
            id1 = IdId.ObtenerCadenaEntrada(IdAsId.id1)
        elif isinstance(IdAsId.id1,Expresion.Expresion):
            id1 = Expresion.Expresion.ObtenerCadenaEntrada(IdAsId.id1,condicion)
        elif isinstance(IdAsId.id1,Binario.Binario):
            id1 = Binario.Binario.ObtenerCadenaEntrada(IdAsId.id1,condicion)

        #ID2-----------------------------------------------------------
        if (isinstance(IdAsId.id2, Time)):
            # valor = Time.resolverTime(IdAsId.id1);
            return Time.ObtenerCadenaEntrada(IdAsId.id2);
        elif (isinstance(IdAsId.id2, Math_.Math_)):
            id2 = str(Math_.Math_.obtenerCadenaEntrada(IdAsId.id2,condicion))
        elif (isinstance(IdAsId.id2, Trigonometrica)):
            id2 = str(Trigonometrica.obtenerCadenaEntrada(IdAsId.id2,condicion))
        elif (isinstance(IdAsId.id2, Primitivo)):
            id2 = str(Primitivo.ObtenerCadenaEntrada(IdAsId.id2))
        elif (isinstance(IdAsId.id2, Id)):
            id2 = str(IdAsId.id2.id)
        elif (isinstance(IdAsId.id2, IdId)):
            id2= str(IdId.ObtenerCadenaEntrada(IdAsId.id2))
        elif isinstance(IdAsId.id2, Expresion.Expresion):
            id2 = str(Expresion.Expresion.ObtenerCadenaEntrada(IdAsId.id2,condicion))
        elif isinstance(IdAsId.id2,Binario.Binario):
            id2 = Binario.Binario.ObtenerCadenaEntrada(IdAsId.id2, condicion)

        return id1+' AS '+ id2 + ' '



    def Traducir(IdAsId):

        print("todo codigo de tradduccion")

