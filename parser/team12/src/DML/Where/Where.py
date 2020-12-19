import random
class Where():
    def __init__(self):
        self.listaMatricesColumnas = []


    def executeAND(self, nodoPadre, listaMatrices, listaPivotes):
        for i in range(0,len(listaPivotes)):
            if listaPivotes[i][0] :
                listaPivotes[i][0] = self.validateCondition(None,None,None,None)  

    def executeOR(self, nodoPadre, listaMatrices, listaPivotes):
        for i in range(0,len(listaPivotes)):
            if not listaPivotes[i][0] :
                listaPivotes[i][0] = self.validateCondition(None,None,None, None)  

    def validateCondition(self,nodoPadre, listaValores, listaColumnas, listaTablas):
        # Llamar al método de Daniel para validar las expresiones
        # La llamada sería nodoPadre.execute(Enviroment)
        # Enviroment lleva la columna y el valor de cada columna
        # Se deben de tener la misma cantidad de numeros y valores
        
        return bool(random.getrandbits(1))


