from Analisis_Ascendente.Instrucciones.instruccion import Instruccion

class Declaracion(Instruccion):
   def __init__(self, id, constant, tipo, collate, notnull, asignacion, fila, columna):
       self.id = id
       self.constant = constant
       self.tipo = tipo
       self.collate = collate
       self.notnull = notnull
       self.asignacion = asignacion
       self.fila = fila
       self.columna = columna

   def getC3D(self, lista_optimizaciones_C3D):
        constant = 'constant ' if self.constant else ''
        tipo = ''
        lista_tipo = self.tipo.tipo.split('-')
        if len(lista_tipo) == 1:
            tipo = self.tipo.tipo
        elif len(lista_tipo) == 2:
            if lista_tipo[0] == 'CHARACTERVARYING':
                tipo = 'CHARACTER VARYING ( %s )' % lista_tipo[1]
            else:
                tipo = '%s ( %s )' % (lista_tipo[0], lista_tipo[1])
        else:
            tipo = '%s ( %s, %s )' % (lista_tipo[0], lista_tipo[1], lista_tipo[2])
        collate_cadena = ("collate '%s' " % self.collate) if self.collate is not None else ''
        not_null = 'not null ' if self.notnull else ''
        plasig = '= %s' % str(self.asignacion) if self.asignacion is not None else ''
        return '%s %s%s %s%s%s; ' % (self.id, constant, tipo, collate_cadena, not_null, plasig)



