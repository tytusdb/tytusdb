class Arbol:

    def __init__(self, instructions):
        self.instrucciones:list = instructions
        self.console:list = []
        self.ErroresSemanticos:list = []
        self.ErroresLexicos: list = []
        self.ErroresSintacticos: list = []
        self.ReporteTS: list = []
