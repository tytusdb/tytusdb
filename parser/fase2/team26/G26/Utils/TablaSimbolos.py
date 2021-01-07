class TablaSimbolos:
    'Clase abstracta'

class TableData(TablaSimbolos):
    def __init__(self, name, type, size, pk, fk, default, null, unique, check):
        self.name = name
        self.type = type
        self.size = size
        self.pk = pk
        self.fk = fk
        self.default = default
        self.null = null
        self.check = check
        self.unique = unique

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)

class DatabaseData(TablaSimbolos):
        def __init__(self, name, owner, mode, use):
            self.name = name
            self.owner = owner
            self.use = use

        def execute(self):
            return self

        def __repr__(self):
            return str(self.__dict__)

class EnumData(TablaSimbolos):
        def __init__(self, name, val, database):
            self.name = name
            self.owner = owner
            self.use = use

        def execute(self):
            return self

        def __repr__(self):
            return str(self.__dict__)

class ConstraintData(TablaSimbolos):
        def __init__(self, name, val, tipo):
            self.name = name
            self.val = val
            self.tipo = tipo

        def execute(self):
            return self

        def __repr__(self):
            return str(self.__dict__)

class DataFile(TablaSimbolos):
    
    def __init__(self):
        ''
    
    def __repr__(self):
            return str(self.__dict__)

    def readData(self, datos):
        try:
            f = open("./Utils/tabla.txt", "r")
            text = f.read()
            f.close()
            text = text.replace('\'','"')
            text = text.replace('False','"False"')
            text = text.replace('None','""')
            text = text.replace('True','"True"')

            #print(text)
            datos.reInsertarValores(json.loads(text))
            #print(str(datos))
        except:
            print('')
    
    def writeData(self, datos):
        f = open("./Utils/tabla.txt", "w")
        f.write(str(datos))
        f.close()