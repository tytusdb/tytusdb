import sys, os.path
storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\typeChecker')
sys.path.append(storage)
from typeChecker.typeChecker import *
tc = TypeChecker()

class ProcedureDB():
    def __init__(self, nombre, C3D):
        self.nombre = nombre
        self.C3D = C3D
        self.parametros = []

    
class Procedure():
    def __init__(self):
        self.orreplace = False #No se reemplaza por default.
        self.nombre = None #Nombre del procedimiento
        self.listaArgumentos = []
        self.cuerpoResult = []

    def compileDefinicion(self,parent, enviroment):
        for hijo in parent.hijos:
            if hijo.nombreNodo == "CUERPO_PROCEDURE":
                result = hijo.compile(enviroment)
                for cadena in result:
                    self.cuerpoResult.append("\t"+cadena)

    def verificarDBActiva(self):
        # Verifica si hay una base de datos activa, se utiliza para cualquier instrucción
        with open('src/Config/Config.json') as file:
            config = json.load(file)
        dbUse = config['databaseIndex']
        if dbUse == None:
            print("Se debe seleccionar una base de datos")
            return None
        return dbUse.upper()
    
    def compile(self,parent, enviroment):
        
        dbActiva = self.verificarDBActiva()
        if dbActiva == None:

            return

        for hijo in parent.hijos:
            if hijo.nombreNodo == "ORREPLACE":
                self.orreplace = True
            elif hijo.nombreNodo == "IDENTIFICADOR":
                self.nombre = hijo.valor.upper()
                self.cuerpoResult.append("@with_goto")
                self.cuerpoResult.append("def "+ hijo.valor+"():")
            elif hijo.nombreNodo == "LISTA_ARG_FUNCION":
                print("Lista_arg_funcion")
            elif hijo.nombreNodo == "DEFINICION_PROCEDURE":
                self.compileDefinicion(hijo, enviroment)

        if not self.orreplace:
            #No se tiene que reemplazar
            if tc.search_procedure(dbActiva.upper(),hijo.valor.upper()):
                print("Ya existe el procedimiento en la base de datos")
                return
        
        nuevoProcedureDB = ProcedureDB(self.nombre, self.cuerpoResult)
        tc.create_procedure(dbActiva.upper(), nuevoProcedureDB)

        

        

