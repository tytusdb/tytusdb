import sys, os.path
storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\typeChecker')
sys.path.append(storage)

c3d_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\C3D\\')
sys.path.append(c3d_dir)
from Label import *
from Temporal import *
from typeChecker.typeChecker import *
tc = TypeChecker()

class ProcedureDB():
    def __init__(self, nombre, C3D, parametros):
        self.nombre = nombre
        self.C3D = C3D
        self.parametros = parametros

    
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
    
    def procesarArgumentos(self,parent):
        indice = 0
        for i in reversed(range(0,len(parent.hijos))):
            self.procesarParam(parent.hijos[i], indice)
            indice = indice + 1
        self.cuerpoResult.append("\tp = p + "+str(indice))

    def procesarParam(self,parent, indice):
        nombreArg = None
        for hijo in parent.hijos:
            if hijo.nombreNodo == "NOMBRE_ARGUMENTO":
                nombreArg = hijo.hijos[0].valor
        self.listaArgumentos.append(nombreArg)
        if nombreArg == None:
            nombreArg = instanceTemporal.getTemporal()
        tmp = instanceTemporal.getTemporal()
        self.cuerpoResult.append("\t"+tmp+"= p - 1")
        self.cuerpoResult.append("\t"+nombreArg + " = display["+tmp+"]")
        
    

    def execute(self,parent, enviroment=None):
        #Este método no mostrará nada, hará el C3D pero solo se guardará.
        
        dbActiva = self.verificarDBActiva()
        if dbActiva == None:
            print("No se ha seleccionado la base de datos")
            return

        for hijo in parent.hijos:
            if hijo.nombreNodo == "ORREPLACE":
                self.orreplace = True
            elif hijo.nombreNodo == "IDENTIFICADOR":
                self.nombre = hijo.valor.upper()
                self.cuerpoResult.append("@with_goto")
                self.cuerpoResult.append("def "+ hijo.valor+"():")
                self.cuerpoResult.append("\tglobal p")
            elif hijo.nombreNodo == "LISTA_ARG_FUNCION":
                self.procesarArgumentos(hijo)
                #print(instanceLabel.getLabel())
            elif hijo.nombreNodo == "DEFINICION_PROCEDURE":
                self.compileDefinicion(hijo, enviroment)

        if not self.orreplace:
            #No se tiene que reemplazar
            if tc.search_procedure(dbActiva.upper(),hijo.valor.upper()):
                print("Ya existe el procedimiento en la base de datos")
                return
        nuevoProcedureDB = ProcedureDB(self.nombre, self.cuerpoResult,self.listaArgumentos)
        tc.replace_procedure(dbActiva.upper(), nuevoProcedureDB)

        

        

