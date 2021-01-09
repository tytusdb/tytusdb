class Arbol():

    def __init__(self):
        self.i = 0
    
    def generar_dot(self, raiz):
        dotReporte = 'digraph Arbol_AST{ node[shape=\"box\"]'
        dotReporte += self.dot_Arbol(raiz)
        dotReporte += '}'
        return dotReporte
    
    def dot_Arbol(self, raiz):

        cuerpoRecorridoArbol = ''''''
        self.i = self.i + 1
        padre = '''n'''+str(self.i)
        
        if raiz.valor != None :
            cuerpoRecorridoArbol += padre + '''[label = \"''' + str(raiz.nombreNodo) + '''\\n''' + str(raiz.valor) + '''\"];'''
        else :
            cuerpoRecorridoArbol += padre + '''[label = \"''' + str(raiz.nombreNodo) + '''\"];'''

        for nodo in raiz.hijos:
            cuerpoRecorridoArbol += padre + ''' -> n''' + (str(self.i + 1)) + ''';\n'''
            cuerpoRecorridoArbol += self.dot_Arbol(nodo)

        return cuerpoRecorridoArbol