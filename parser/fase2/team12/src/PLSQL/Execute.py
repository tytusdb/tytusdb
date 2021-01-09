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
        self.codigo3Direcciones = []


    #region Metodos Genericos
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
    #endregion
    

    #region Lista Parámetros
    def getNoParametros(self,proc):
        return len(proc['parametros'])

    def verificarParametros(self, parent):
        for hijo in parent.hijos:
            val = hijo.compile(None)
            for cad in val.splitlines():
                self.codigo3Direcciones.append(cad)
            
            self.codigo3Direcciones.append("display[p] = "+hijo.dir)
            self.codigo3Direcciones.append("p = p + 1 ")


    #endregion

    def compile(self, parent):
        self.dbUsada = self.verificarDBActiva()
        if self.dbUsada == None:
            return ""
        res  = self.getProcedure(parent.hijos[0])
        if res == None:
            print("No se encuentra el procedimiento")
            return ""
        #Verificación de parametros
        print("Aca")
        if len(parent.hijos) <=1 and self.getNoParametros(res)!=0:
            print ("La funcion tiene parametros")
            return ""
        elif len(parent.hijos) > 1:
            if self.getNoParametros(res)!= len(parent.hijos[1].hijos):
                return ""
            else:
                self.verificarParametros(parent.hijos[1])


        
        self.codigo3Direcciones.append(self.nombre + "()")
        return self.codigo3Direcciones