from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.expresion import *
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion as Expresion

class Llamada(Instruccion):
    def __init__(self, caso, id, listaE, linea, columna):
        self.caso = caso
        self.id = id
        self.listaE = listaE
        self.linea = linea
        self.columna = columna

    def obtenerCadena(llamada,condicion):
        if llamada.caso == 2:
            return str(llamada.id)+"()"
        elif llamada.caso == 1:
            concatenar = str(llamada.id)+"("
            con = 0
            for expr in llamada.listaE:
                if isinstance(expr,Primitivo):
                    concatenar +=  Primitivo.ObtenerCadenaEntrada(expr)

                elif isinstance(expr,Unario):
                    exp1 = Expresion.Expresion.ObtenerCadenaEntrada(expr.op,condicion)
                    concatenar += str(expr.operador)+exp1
                elif isinstance(expr,Id):
                    concatenar +=expr.id
                con += 1
                if con < len(llamada.listaE):
                    concatenar += ","
            concatenar += ")"
            return  concatenar

