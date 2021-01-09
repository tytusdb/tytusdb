from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Simbolo import Simbolo 

class DatePart(Instruccion):
    def __init__(self, id, id2, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.identificador = id
        self.valor = id2
        
    def ejecutar(self, ts, arbol):
        super().ejecutar(ts,arbol)
       
        tam = len(self.valor)
        parser = self.valor.split()
        
        segundo = 0
        minuto = 0
        hora = 0
        for x in range(0,len(parser)):
            if(parser[x]=="seconds"):
                segundo = parser[x-1]
            elif(parser[x]=="minutes"):
                minuto = parser[x-1]
            elif(parser[x]=="hours"):
                hora = parser[x-1]
                

        if(self.identificador == "seconds"):
            #print("segundo")
            #print(str(segundo))
            return segundo
        elif(self.identificador == "minutes"):
            #print("minuto")
            #print(str(minuto))
            return minuto
        elif(self.identificador == "hour"):
            #print("hora")
            #print(str(hora))
            return hora
        
    def analizar(self, tabla, arbol):
        return super().analizar(tabla, arbol)

    def traducir(self, ts, arbol):
        super().traducir(ts, arbol)
        cadena = f"date_part( '{self.identificador}', INTERVAL '{self.valor}' )"
        return cadena
        
'''
instruccion = Declare("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''