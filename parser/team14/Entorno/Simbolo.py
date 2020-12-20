from Entorno.TipoSimbolo import TipoSimbolo

class Simbolo:
    def __init__(self, tipo = "", nombre = "", valor = None, linea = 0):
        self.tipo = tipo
        self.nombre = nombre
        self.valor = valor
        self.linea = linea
        self.atributos = {}
        self.baseDatos = ""
        self.tabla = ""
    
    def toString(self):
        cadena:str = ""
        if self.nombre != None:
            cadena += "<TR>"
            if self.tipo == TipoSimbolo.TABLA:
                cadena += "<TD>" + self.nombre + "</TD><TD>TABLA</TD><TD>" + self.baseDatos + "</TD><TD>" + self.tabla + "</TD>"
                #for col in self.valor:
                    #cadena += "<TD>" +  + "</TD>"

            cadena += "</TR>"
        return cadena
        