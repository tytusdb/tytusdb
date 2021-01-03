class Arbol:

    def __init__(self, instructions):
        self.instrucciones:list = instructions
        self.console:list = []
        self.ErroresSemanticos:list = []
        self.ErroresLexicos: list = []
        self.ErroresSintacticos: list = []
        self.ReporteTS: list = []

        # Soporte de temporales
        self.noTemp:int = 0
        self.ultimoTemp = ""

        # Soporte de labels
        self.noLabel:int = 0
        self.ultimoLabel = ""

        self.C3D = ""

    def getTemp(self) -> str:
        temporal = "t" + str(self.noTemp)
        self.ultimoTemp = temporal
        self.noTemp = self.noTemp + 1
        return str(temporal)

    def getLabel(self) -> str:
        label = "L" + str(self.noLabel)
        self.ultimoLabel = label
        self.noLabel = self.noLabel + 1
        return str(label)

    def addC3D(self, data):
        if data != None:
            self.C3D = self.C3D + str(data) + "\n"
        else:
            pass

    def getC3D(self):
        return self.C3D
