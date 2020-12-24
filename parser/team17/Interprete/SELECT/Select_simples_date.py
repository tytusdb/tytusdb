from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from Interprete.Primitivos.TIPO import TIPO
from datetime import datetime, date


class Select_simples_date(NodoArbol):

    def __init__(self, line, column, type_, firsparam_=None, secondparam_=None):
        super().__init__(line, column)
        self.type = type_
        self.firstparam = firsparam_
        self.secondparam = secondparam_

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        if self.type == 'extract':
            entry: Valor = self.secondparam.execute(entorno, arbol)
            try:
                result = self.extract(entry)
                print(result)
                retorno: Valor = Valor(TIPO.DATE, result)
                return retorno
            except:
                print('ERROR EN EL FORMATO DE FECHA INGRESADO')
        elif self.type == 'date_part':
            entry: Valor = self.secondparam.execute(entorno, arbol)
            array = entry.data.split(' ')
            if self.firstparam == 'hour':
                print(array[0])
                retorno: Valor = Valor(TIPO.DATE, array[0])
                return retorno
            elif self.firstparam == 'minutes':
                print(array[2])
                retorno: Valor = Valor(TIPO.DATE, array[2])
                return retorno
            elif self.firstparam == 'seconds':
                print(array[4])
                retorno: Valor = Valor(TIPO.DATE, array[4])
                return retorno
        elif self.type == 'now':
            today = str(datetime.now())
            print(today)
            retorno: Valor = Valor(TIPO.DATE, today)
            return retorno
        elif self.type == 'current_date':
            today = str(date.today())
            print(today)
            retorno: Valor = Valor(TIPO.DATE, today)
            return retorno
        elif self.type == 'current_time':
            today = datetime.now()
            now = today.strftime("%H:%M:%S")
            print(now)
            retorno: Valor = Valor(TIPO.DATE, now)
            return retorno
        elif self.type == 'timestamp':
            today = str(datetime.now())
            print(today)
            retorno: Valor = Valor(TIPO.DATE, today)
            return retorno

    def extract(self, entry):
        date_obj = datetime.strptime(entry.data, '%Y-%m-%d %H:%M:%S')
        out = ''
        if self.firstparam == 'year':
            out = date_obj.year
        elif self.firstparam == 'month':
            out = date_obj.month
        elif self.firstparam == 'day':
            out = date_obj.day
        elif self.firstparam == 'hour':
            out = date_obj.hour
        elif self.firstparam == 'minute':
            out = date_obj.minute
        elif self.firstparam == 'second':
            out = date_obj.second
        return out
