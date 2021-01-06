class Cartesiano():
    def __init__(self):
        pass

    #region Producto Cartesiano
    def cartesiano(self, listaMatrices):
        # Función que realiza el producto cartesiano entre matrices
        # Aunque en realidad el producto cartesiano se va a realizar
        # únicamente en los selects, todas las peticiones pasan por
        # este proceso.
        array = []
        for i in range(0,listaMatrices[0].noFilas):
            array.append([True,i])
        return self.funcionNXN(listaMatrices,1,array)
    
    def funcionNXN(self, listaMatrices, indice, matrizInicial):
        if indice<len(listaMatrices) :
            matrizPivote = listaMatrices[indice]
            result = []
            for i in range(0,len(matrizInicial)):
                for j in range(0,matrizPivote.noFilas):
                    a = matrizInicial[i][:]
                    a.append(j)
                    result.append(a)
            return self.funcionNXN(listaMatrices,indice+1,result)
        else:
            return matrizInicial
    #endregion
