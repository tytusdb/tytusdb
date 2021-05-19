import hashlib
from parserT28.models.instructions.Expression.expression import Expression, PrimitiveData, DATA_TYPE, Identifiers
from parserT28.controllers.error_controller import ErrorController
from parserT28.controllers.three_address_code import ThreeAddressCode
# TODO: REVISAR QUE NO MUERA CON DECODE, UNCODE, GETBYTE, SETBYTE, CONVERT


class Length(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''

    def __init__(self, value, line, column):
        self.value = value
        self.alias = f'LENGTH({self.value.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            val = None
            result = 0
            lista1 = []
            if isinstance(self.value, Identifiers):
                val = self.value.process(environment)
                result = [len(columns) for columns in val[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                val = self.value.process(environment).value
                l = len(val)
                return PrimitiveData(DATA_TYPE.NUMBER, l, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Length"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temp = ThreeAddressCode().newTemp()
            val = self.value.compile(environment).value
            dataTemp = f"{temp} = '{val}'"

            cambio = False
            if val[0] == 't':
                sub = val[1:]
                if sub.isnumeric():  # ES UN TEMPORAL
                    dataTemp = f"{temp} = {val}"
                    cambio = True
            if cambio is False:
                dataTemp = f"{temp} = '{val}'"

            ThreeAddressCode().addCode(dataTemp)
            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(f"{temporal} = len({temp})")
            return PrimitiveData(DATA_TYPE.STRING, temporal, self.line, self.column)
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Substring(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''

    def __init__(self, value, down, up, line, column):
        self.value = value
        self.alias = f'SUBSTRING({self.value.alias})'
        self.up = up
        self.down = down
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            val = None
            result = 0
            lista1 = []
            i = self.down.process(environment).value
            j = self.up.process(environment).value
            if isinstance(self.value, Identifiers):
                val = self.value.process(environment)
                result = [columns[i:j] for columns in val[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                cadena = self.value.process(environment).value
                substr = cadena[i:j]
                return PrimitiveData(DATA_TYPE.STRING, substr, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Substring"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            i = self.down.compile(environment).value
            j = self.up.compile(environment).value
            temp = ThreeAddressCode().newTemp()
            val = self.value.compile(environment).value
            dataTemp = f"{temp} = '{val}'"

            cambio = False
            if val[0] == 't':
                sub = val[1:]
                if sub.isnumeric():  # ES UN TEMPORAL
                    dataTemp = f"{temp} = {val}"
                    cambio = True
            if cambio is False:
                dataTemp = f"{temp} = '{val}'"

            tempi = ThreeAddressCode().newTemp()
            tempj = ThreeAddressCode().newTemp()
            dataTempi = f"{tempi} = {i}"
            dataTempj = f"{tempj} = {j}"
            ThreeAddressCode().addCode(dataTemp)
            ThreeAddressCode().addCode(dataTempi)
            ThreeAddressCode().addCode(dataTempj)
            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(f"{temporal} = {temp}[{tempi}:{tempj}]")
            return PrimitiveData(DATA_TYPE.STRING, temporal, self.line, self.column)
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Substr(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''

    def __init__(self, value, down, up, line, column):
        self.value = value
        self.alias = f'SUBSTR({self.value.alias})'
        self.up = up
        self.down = down
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            val = None
            result = 0
            lista1 = []
            i = self.down.process(environment).value
            j = self.up.process(environment).value
            if isinstance(self.value, Identifiers):
                val = self.value.process(environment)
                result = [columns[i:j] for columns in val[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                cadena = self.value.process(environment).value
                substr = cadena[i:j]
                return PrimitiveData(DATA_TYPE.STRING, substr, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Substring"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            i = self.down.compile(environment).value
            j = self.up.compile(environment).value
            temp = ThreeAddressCode().newTemp()
            val = self.value.compile(environment).value
            dataTemp = f"{temp} = '{val}'"

            cambio = False
            if val[0] == 't':
                sub = val[1:]
                if sub.isnumeric():  # ES UN TEMPORAL
                    dataTemp = f"{temp} = {val}"
                    cambio = True
            if cambio is False:
                dataTemp = f"{temp} = '{val}'"

            tempi = ThreeAddressCode().newTemp()
            tempj = ThreeAddressCode().newTemp()
            dataTempi = f"{tempi} = {i}"
            dataTempj = f"{tempj} = {j}"
            ThreeAddressCode().addCode(dataTemp)
            ThreeAddressCode().addCode(dataTempi)
            ThreeAddressCode().addCode(dataTempj)
            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(f"{temporal} = {temp}[{tempi}:{tempj}]")
            return PrimitiveData(DATA_TYPE.STRING, temporal, self.line, self.column)
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Trim(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''

    def __init__(self, value, line, column):
        self.value = value
        self.alias = f'TRIM({self.value.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            if isinstance(self.value, Identifiers):
                lista1 = []
                val = self.value.process(environment)
                result = [columns.strip() for columns in val[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                cadena = self.value.process(environment).value
                trim_str = cadena.strip()
                return PrimitiveData(DATA_TYPE.STRING, trim_str, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Trim"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temp = ThreeAddressCode().newTemp()
            val = self.value.compile(environment).value
            dataTemp = f"{temp} = '{val}'"

            cambio = False
            if val[0] == 't':
                sub = val[1:]
                if sub.isnumeric():  # ES UN TEMPORAL
                    dataTemp = f"{temp} = {val}"
                    cambio = True
            if cambio is False:
                dataTemp = f"{temp} = '{val}'"

            ThreeAddressCode().addCode(dataTemp)
            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(f"{temporal} = {temp}.strip()")
            return PrimitiveData(DATA_TYPE.STRING, temporal, self.line, self.column)
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class MD5(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''

    def __init__(self, value, line, column):
        self.value = value
        self.alias = f'MD5({self.value.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            if isinstance(self.value, Identifiers):
                lista1 = []
                val = self.value.process(environment)
                result = [hashlib.md5(columns.encode()).hexdigest()
                          for columns in val[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                cadena = self.value.process(environment).value
                result = hashlib.md5(cadena.encode())
                return PrimitiveData(DATA_TYPE.STRING, result.hexdigest(), self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para md5"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temp = ThreeAddressCode().newTemp()
            val = self.value.compile(environment).value
            dataTemp = f"{temp} = '{val}'"

            cambio = False
            if val[0] == 't':
                sub = val[1:]
                if sub.isnumeric():  # ES UN TEMPORAL
                    dataTemp = f"{temp} = {val}"
                    cambio = True
            if cambio is False:
                dataTemp = f"{temp} = '{val}'"

            ThreeAddressCode().addCode(dataTemp)
            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(
                f"{temporal} = md5({temp}.encode()).hexdigest()")
            return PrimitiveData(DATA_TYPE.STRING, temporal, self.line, self.column)
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class SHA256(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''

    def __init__(self, value, line, column):
        self.value = value
        self.alias = f'SHA256({self.value.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            if isinstance(self.value, Identifiers):
                lista1 = []
                val = self.value.process(environment)
                result = [hashlib.sha256(columns.encode()).hexdigest()
                          for columns in val[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                cadena = self.value.process(environment).value
                result = hashlib.sha256(cadena.encode())
                return PrimitiveData(DATA_TYPE.STRING, result.hexdigest(), self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para sha256"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temp = ThreeAddressCode().newTemp()
            val = self.value.compile(environment).value
            dataTemp = f"{temp} = '{val}'"

            cambio = False
            if val[0] == 't':
                sub = val[1:]
                if sub.isnumeric():  # ES UN TEMPORAL
                    dataTemp = f"{temp} = {val}"
                    cambio = True
            if cambio is False:
                dataTemp = f"{temp} = '{val}'"

            ThreeAddressCode().addCode(dataTemp)
            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(
                f"{temporal} = sha256({temp}.encode()).hexdigest()")
            return PrimitiveData(DATA_TYPE.STRING, temporal, self.line, self.column)
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class GetByte(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''

    def __init__(self, value, pos, line, column):
        self.value = value
        self.pos = pos
        self.alias = f'GETBYTE({self.value.alias})'
        self.line = line
        self.column = column

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            index = self.pos.process(environment).value
            if isinstance(self.value, Identifiers):
                lista1 = []
                val = self.value.process(environment)
                result = [ord(columns[index]) for columns in val[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                cadena = self.value.process(environment).value
                result = ord(cadena[index])
                return PrimitiveData(DATA_TYPE.STRING, result, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para GetByte"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temp = ThreeAddressCode().newTemp()
            val = self.value.compile(environment).value
            tempPos = ThreeAddressCode().newTemp()
            index = self.pos.compile(environment).value
            dataTemp = f"{temp} = '{val}'"

            cambio = False
            if val[0] == 't':
                sub = val[1:]
                if sub.isnumeric():  # ES UN TEMPORAL
                    dataTemp = f"{temp} = {val}"
                    cambio = True
            if cambio is False:
                dataTemp = f"{temp} = '{val}'"

            dataPos = f'{tempPos} = {index}'
            ThreeAddressCode().addCode(dataTemp)
            ThreeAddressCode().addCode(dataPos)
            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(f"{temporal} = ord({temp}[{tempPos}])")
            return PrimitiveData(DATA_TYPE.STRING, temporal, self.line, self.column)
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class SetByte(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''

    def __init__(self, value, pos, no_char, line, column):
        self.value = value
        self.pos = pos
        self.no_char = no_char
        self.alias = f'SETBYTE({self.value.alias})'
        self.line = line
        self.column = column

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            index = self.pos.process(environment).value
            char = self.no_char.process(environment).value
            if isinstance(self.value, Identifiers):
                lista1 = []
                val = self.value.process(environment)
                result = [(columns[:index] + chr(char) + columns[index + 1:])
                          for columns in val[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                cadena = self.value.process(environment).value
                result = cadena[:index] + chr(char) + cadena[index + 1:]
                return PrimitiveData(DATA_TYPE.STRING, result, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para SetByte"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self):
        return super().compile()


class Convert(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''

    def __init__(self, value, data_type, line, column):
        self.value = value
        self.data_type = data_type
        self.alias = f'CONVERT({self.value.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            if self.data_type.lower() == "integer":
                if isinstance(self.value, Identifiers):
                    lista1 = []
                    val = self.value.process(environment)
                    result = [int(columns) for columns in val[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                else:
                    cadena = self.value.process(environment).value
                    return PrimitiveData(DATA_TYPE.NUMBER, int(cadena), self.line, self.column)
            else:
                if isinstance(self.value, Identifiers):
                    lista1 = []
                    val = self.value.process(environment)
                    result = [str(columns) for columns in val[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                else:
                    cadena = self.value.process(environment).value
                    return PrimitiveData(DATA_TYPE.STRING, cadena, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Convert"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            if self.data_type.lower() == 'integer':
                temp = ThreeAddressCode().newTemp()
                val = self.value.compile(environment).value
                dataTemp = f"{temp} = '{val}'"

                cambio = False
                if val[0] == 't':
                    sub = val[1:]
                    if sub.isnumeric():  # ES UN TEMPORAL
                        dataTemp = f"{temp} = {val}"
                        cambio = True
                if cambio is False:
                    dataTemp = f"{temp} = '{val}'"

                ThreeAddressCode().addCode(dataTemp)
                temporal = ThreeAddressCode().newTemp()
                ThreeAddressCode().addCode(
                    f"{temporal} = int({temp})")
                return PrimitiveData(DATA_TYPE.STRING, temporal, self.line, self.column)
            else:
                temp = ThreeAddressCode().newTemp()
                val = self.value.compile(environment).value
                dataTemp = f"{temp} = '{val}'"
                ThreeAddressCode().addCode(dataTemp)
                temporal = ThreeAddressCode().newTemp()
                ThreeAddressCode().addCode(
                    f"{temporal} = {temp}")
                return PrimitiveData(DATA_TYPE.STRING, temporal, self.line, self.column)
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Encode(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''

    def __init__(self, value, format_text, line, column):
        self.value = value
        self.value = format_text
        self.alias = f'ENCODE({self.value.alias})'
        self.line = line
        self.column = column

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            if isinstance(self.value, Identifiers):
                lista1 = []
                val = self.value.process(environment)
                result = [str(columns) for columns in val[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                cadena = self.value.process(environment).value
                return PrimitiveData(DATA_TYPE.STRING, cadena, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Encode"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self):
        pass


class Decode(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''

    def __init__(self, value, format_text, line, column):
        self.value = value
        self.value = format_text
        self.alias = f'DECODE({self.value.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            if isinstance(self.value, Identifiers):
                lista1 = []
                val = self.value.process(environment)
                result = [str(columns) for columns in val[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                cadena = self.value.process(environment).value
                return PrimitiveData(DATA_TYPE.STRING, cadena, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Decode"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self):
        pass
