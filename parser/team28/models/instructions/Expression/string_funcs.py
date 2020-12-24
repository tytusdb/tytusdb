import hashlib
from models.instructions.Expression.expression import Expression, PrimitiveData, DATA_TYPE
from controllers.error_controller import ErrorController
#TODO: REVISAR QUE NO MUERA CON DECODE, UNCODE, GETBYTE, SETBYTE, CONVERT
class Length(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value, line, column) :
        self.value = value
        self.alias = f'LENGTH({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
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

class Substring(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value, down, up, line, column) :
        self.value = value
        self.alias = f'SUBSTRING({self.value.alias})'
        self.up = up
        self.down = down
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            i = self.down.process(environment).value
            j = self.up.process(environment).value
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

class Substr(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value, down, up, line, column) :
        self.value = value
        self.alias = f'SUBSTR({self.value.alias})'
        self.up = up
        self.down = down
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            i = self.down.process(environment).value
            j = self.up.process(environment).value
            cadena = self.value.process(environment).value
            substr = cadena[i:j]
            return PrimitiveData(DATA_TYPE.STRING, substr, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Substr"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

class Trim(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value, line, column) :
        self.value = value
        self.alias = f'TRIM({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
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

class MD5(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value, line, column) :
        self.value = value
        self.alias = f'MD5({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
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

class SHA256(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value, line, column) :
        self.value = value
        self.alias = f'SHA256({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
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

class GetByte(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value, line, column) :
        self.value = value
        self.alias = f'GETBYTE({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            pass
        except TypeError:
            desc = "Tipo de dato invalido para GetByte"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

class SetByte(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value, line, column) :
        self.value = value
        self.alias = f'SETBYTE({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            pass
        except TypeError:
            desc = "Tipo de dato invalido para SetByte"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

class Convert(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value, data_type, line, column) :
        self.value = value
        self.value = data_type
        self.alias = f'CONVERT({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            pass
        except TypeError:
            desc = "Tipo de dato invalido para Convert"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

class Encode(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value, format_text, line, column) :
        self.value = value
        self.value = format_text
        self.alias = f'ENCODE({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            pass
        except TypeError:
            desc = "Tipo de dato invalido para Encode"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

class Decode(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value, format_text, line, column) :
        self.value = value
        self.value = format_text
        self.alias = f'DECODE({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            pass
        except TypeError:
            desc = "Tipo de dato invalido para Decode"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- StringFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)