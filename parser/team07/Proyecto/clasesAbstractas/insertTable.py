from .instruccionAbstracta import InstruccionAbstracta

class InsertTable(InstruccionAbstracta):

    def __init__(self, nombreTabla, listaColumnas = [], listaExpresiones=[], defaultValues = False):
        self.nombreTabla = nombreTabla
        self.listaColumnas = listaColumnas
        self.listaExpresiones = listaExpresiones
        self.defaultValues = defaultValues


    

    def ejecutar(self, tabalSimbolos, listaErrores):

        print("Ejecutando InsertTable")             
        
        for tupla in self.listaExpresiones:
            listaExp = tupla.hijos[0]

            for expresion in listaExp.hijos:
                simb = expresion.ejecutar(tabalSimbolos,listaErrores)
                if simb != None:
                    print(simb.valorRetorno)
                else:
                    # guardar el valor como 
                    print("Nada")




        pass   

