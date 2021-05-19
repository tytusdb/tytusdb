from parserT28.controllers.error_controller import ErrorController
from parserT28.models.instructions.Expression.expression import Expression, Identifiers, PrimitiveData


data = '2001-02-16 20:38:40'
# print(data[17:19])


class ExtractFromIdentifiers(Expression):
    '''Para extraer fechas de columnas del select '''

    def __init__(self, name_date, type_date, name_opt, name_date2, line, column):
        self.name_date = name_date
        self.type_date = type_date
        self.name_opt = name_opt
        self.line = line
        self.column = column
        self.alias = f'{name_date2}({self.name_opt.alias})'
        self._tac = ''

    def __repr__(self):
        return str(vars(self))

    def process(self, expression):
        name_date = self.name_date
        type_date = ""
        name_opt = None
        result = None
        lista1 = []
        try:
            print(type(self.name_opt))
            if isinstance(self.type_date, PrimitiveData):
                type_date = self.type_date.process(expression)
            if isinstance(self.name_opt, Identifiers):
                name_opt = self.name_opt.process(expression)
            type_date = type_date.value.lower()
            if type_date == 'year':
                result = [columns[:4] for columns in name_opt[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            elif type_date == 'month':
                result = [columns[5:7] for columns in name_opt[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            elif type_date == 'day':
                result = [columns[8:10] for columns in name_opt[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            elif type_date == 'hour':
                result = [columns[11:13] for columns in name_opt[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            elif type_date == 'minute':
                result = [columns[14:16] for columns in name_opt[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            elif type_date == 'second':
                result = [columns[17:19] for columns in name_opt[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
        except:
            desc = "FATAL ERROR, ExtractFromIdentifiers, error en la extaccion de las fechas"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)
