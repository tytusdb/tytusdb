import hashlib
from models.instructions.Expression.expression import Expression, PrimitiveData, DATA_TYPE

#TODO: REVISAR QUE NO MUERA CON .VALUE, DECODE, UNCODE, GETBYTE, SETBYTE, CONVERT
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
            l = len(self.value.process().alias)
            return PrimitiveData(DATA_TYPE.NUMBER, l, self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- StringFuncs")

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
            i = self.down.process().value
            j = self.up.process().value
            cadena = self.value.process().value
            substr = cadena[i:j]
            return PrimitiveData(DATA_TYPE.STRING, substr, self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- StringFuncs")

class Trim(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value, line, column) :
        self.value = value
        self.alias = f'SUBSTRING({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            cadena = self.value.process().value
            trim_str = cadena.strip()
            return PrimitiveData(DATA_TYPE.STRING, trim_str, self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- StringFuncs")

class MD5(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value, line, column) :
        self.value = value
        self.alias = f'SUBSTRING({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            cadena = self.value.process().value
            result = hashlib.md5(cadena.encode()) 
            return PrimitiveData(DATA_TYPE.STRING, result.hexdigest(), self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- StringFuncs")

class SHA256(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value, line, column) :
        self.value = value
        self.alias = f'SUBSTRING({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            cadena = self.value.process().value
            result = hashlib.sha256(cadena.encode()) 
            return PrimitiveData(DATA_TYPE.STRING, result.hexdigest(), self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- StringFuncs")

class GetByte(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value, line, column) :
        self.value = value
        self.alias = f'SUBSTRING({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            pass
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- StringFuncs")

class SetByte(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value, line, column) :
        self.value = value
        self.alias = f'SUBSTRING({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            pass
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- StringFuncs")

class Convert(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value, data_type, line, column) :
        self.value = value
        self.value = data_type
        self.alias = f'SUBSTRING({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            pass
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- StringFuncs")

class Encode(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value, format_text, line, column) :
        self.value = value
        self.value = format_text
        self.alias = f'SUBSTRING({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            pass
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- StringFuncs")

class Decode(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value, format_text, line, column) :
        self.value = value
        self.value = format_text
        self.alias = f'SUBSTRING({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            pass
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- StringFuncs")