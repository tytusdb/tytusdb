import sys
class Tipo():
    '''
        Esta clase representa una expresión
    '''

    'Todas las Instrrucciones tienen un valor y un tipo'
    def __init__(self,valor,tipo):
        'Obtener el valor de la Instrruccion'
        self.valor=valor
        self.tipo = tipo

    def tipoInt(self):
        'devueleve el tipo indicado de tipo int'
        if self.valor<=32767 and self.valor>= -32768:
            return 'smallint'
        elif self.valor<=2147483647 and self.valor>= -2147483648:
            return 'integer'
        elif self.valor<=9223372036854775807 and self.valor>= -9223372036854775808:
            return 'bigint'

    def tipoDecimal(self):
        'devueleve el tipo indicado de tipo decimal'
        size=sys.getsizeof(self.valor)
        if size<= 4:
            return 'real'
        elif size<=8:
            if self.val>=-92233720368547758.08  and self.val <=92233720368547758.07:
                return 'money'
            return 'double'
        else:
            return 'decimal' #numeric es lo mismo que decimal



    def getTipo(self):
        'Metodo Abstracto para obtener el valor de la Instrruccion'
        if self.tipo == 'int':
            return self.tipoInt(self)
        elif self.tipo == 'decimal':
            return self.tipoDecimal(self)
        else:
            return self.tipo

