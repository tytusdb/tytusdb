from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Simbolo import Simbolo 
from Instrucciones.TablaSimbolos.Simbolo3D import Simbolo3d
from Instrucciones.TablaSimbolos.Tipo import Tipo, Tipo_Dato

class DatePart(Instruccion):
    def __init__(self, id, id2, strGram, linea, columna, strSent):
        Instruccion.__init__(self,None,linea,columna,strGram, strSent)
        self.identificador = id
        self.valor = id2
        
    def ejecutar(self, ts, arbol):
        #super().ejecutar(ts,arbol)
        #el id es para guardarlo en la tabla
        #tamaño de cadena
       
        tam = len(self.valor)
        parser = self.valor.split()
        
        segundo = 0
        minuto = 0
        hora = 0
        for x in range(0,len(parser)):
            print(parser[x])
            if(parser[x]=="seconds"):
                segundo = parser[x-1]
            elif(parser[x]=="minutes"):
                minuto = parser[x-1]
            elif(parser[x]=="hours"):
                hora = parser[x-1]
                

        if(self.identificador == "seconds"):
            #print("segundo")
            #print(str(segundo))
            self.tipo = Tipo("",Tipo_Dato.INTEGER)
            return segundo
        elif(self.identificador == "minutes"):
            #print("minuto")
            #print(str(minuto))
            self.tipo = Tipo("",Tipo_Dato.INTEGER)
            return minuto
        elif(self.identificador == "hour"):
            #print("hora")
            #print(str(hora))
            self.tipo = Tipo("",Tipo_Dato.INTEGER)
            return hora


    def traducir(self, tabla, arbol, cadenaTraducida):
        resultado = self.ejecutar(tabla, arbol)
        if isinstance(resultado,Excepcion):
            return resultado        
        codigo = ""
        temporal = arbol.generaTemporal()
        codigo += "\t" + temporal + " = " + str(resultado) + "\n"
        nuevo = Simbolo3d(self.tipo, temporal, codigo, None, None)
        return nuevo
        
'''
instruccion = Declare("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''