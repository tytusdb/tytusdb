import sys, os.path
storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\typeChecker')
sys.path.append(storage)
from typeChecker.typeChecker import *
tc = TypeChecker()

class Execute():
    def __init__(self):
        self.procedimiento = None
        self.nombre = None
        self.dbUsada = None
        self.codigo3Dimensiones = None

    def verificarDBActiva(self):
        # Verifica si hay una base de datos activa, se utiliza para cualquier instrucción
        with open('src/Config/Config.json') as file:
            config = json.load(file)
        dbUse = config['databaseIndex']
        if dbUse == None:
            print("Se debe seleccionar una base de datos")
            return None
        return dbUse.upper()

    def getProcedure(self, parent):
        self.nombre = parent.valor
        return tc.search_procedure(self.dbUsada, parent.valor.upper())


    def compile(self, parent):
        self.dbUsada = self.verificarDBActiva()
        if self.dbUsada == None:
            return
        res  = self.getProcedure(parent.hijos[0])
        if res == None:
            print("No se encuentra el procedimiento")
            return
        #Verificación de parametros
        self.codigo3Dimensiones = res['C3D']
        self.procedimiento = self.nombre + "()"
        