import sys, os.path

where_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\Where')
sys.path.append(where_path)


from Where import Where



class Select():

    def __init__(self):
        print("Inicio")

    def execute(self):
        MatA = [['A','Juan','Perez'],['B','Daniel','Gonzales'],['C','Esbin','Gonzales'],['D','Walter','Parede'],['E','Josue','Sol'],['F','Edilson','Jimenez'],['G','Gonzalo','Garcia']]
        MatB = [['A','123456'],['A','000000'],['B','111111'],['E','222222'],['F','333333'],['E','444444'],['F','555555']]
        MatC = [['F','333333'],['E','444444'],['F','555555']]
        listaMatrices = []
        listaMatrices.append(MatA)
        listaMatrices.append(MatB)
        listaMatrices.append(MatC)
        sentenciaWhere = Where()
        listaPivotes = self.cartesiano(listaMatrices)
        
        sentenciaWhere.executeAND(None,listaMatrices,listaPivotes)
    

    def cartesiano(self, listaMatrices):
        array = []
        for i in range(0,len(listaMatrices[0])):
            array.append([True,i])
        return self.funcionNXN(listaMatrices,1,array)
    

    def funcionNXN(self, listaMatrices, indice, matrizInicial):
        if indice<len(listaMatrices) :
            matrizPivote = listaMatrices[indice]
            result = []
            for i in range(0,len(matrizInicial)):
                for j in range(0,len(matrizPivote)):
                    a = matrizInicial[i][:]
                    a.append(j)
                    result.append(a)
            return self.funcionNXN(listaMatrices,indice+1,result)
        else:
            return matrizInicial
        


        

