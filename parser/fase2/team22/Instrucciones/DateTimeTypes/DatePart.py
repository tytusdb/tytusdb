from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Simbolo import Simbolo 
from Instrucciones.TablaSimbolos import Instruccion3D as c3d
from Optimizador.C3D import Valor as ClassValor
from Optimizador.C3D import OP_ARITMETICO as ClassOP_ARITMETICO
from Optimizador.C3D import Identificador as ClassIdentificador

class DatePart(Instruccion):
    def __init__(self, id, id2, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
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
            return segundo
        elif(self.identificador == "minutes"):
            #print("minuto")
            #print(str(minuto))
            return minuto
        elif(self.identificador == "hour"):
            #print("hora")
            #print(str(hora))
            return hora

    def generar3D(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append(c3d.asignacionH())
        code.append(c3d.aumentarP())
        t0 = c3d.getLastTemporal()
        t1 = c3d.getTemporal()
        code.append(c3d.operacion(t1, ClassIdentificador(t0), ClassValor("\"DATE_PART('" + self.identificador + "', INTERVAL '" + self.valor + "')\"", "STRING"), ClassOP_ARITMETICO.SUMA))

        return code
        
'''
instruccion = Declare("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''