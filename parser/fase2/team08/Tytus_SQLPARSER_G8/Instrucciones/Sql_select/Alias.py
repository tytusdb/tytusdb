
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Identificador import Identificador
class Alias(Instruccion):
    def __init__(self, id, expresion, pas):
        Instruccion.__init__(self,None,None,None,None)
        self.id = id
        self.expresion = expresion
        self.tipo = None
        self.pas = pas

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        pass
    def analizar(self, tabla, arbol):
        super().analizar(tabla,arbol)
        pass

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        cadena=""
        #print("ALIAS")
        #print(type(self.id))
        if isinstance(self.expresion,str):
            if self.id != None:
                cadena += f"{self.id}.{self.expresion} "
            else:
                cadena += self.expresion + " "
        elif isinstance(self.expresion, Identificador):
            if self.pas=="AS":
                cadena += f"{self.expresion.concatenar(tabla,arbol)} {self.pas} " + str(self.id).replace(" ", "")
            else:
                cadena += f"{self.expresion.concatenar(tabla,arbol)} " + str(self.id).replace(" ", "")
        else:
            if self.pas=="AS":
                cadena += f"{self.expresion.traducir(tabla,arbol)} {self.pas} " + str(self.id).replace(" ", "")
            else:
                cadena += f"{self.expresion.traducir(tabla,arbol)} " + str(self.id).replace(" ", "")
        return cadena