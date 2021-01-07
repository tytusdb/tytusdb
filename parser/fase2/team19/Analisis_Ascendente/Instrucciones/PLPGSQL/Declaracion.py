from Analisis_Ascendente.Instrucciones.instruccion import Instruccion

class Declaracion(Instruccion):
   def __init__(self, id, constant, tipo, collate, notnull, asignacion, fila, columna):
       self.id = id
       self.constant = constant
       self.tipo = tipo
       self.collate = collate,
       self.notnull = notnull,
       self.asignacion = asignacion
       self.fila = fila
       self.columna = columna




