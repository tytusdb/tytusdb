from Instrucciones.TablaSimbolos.Instruccion import Instruccion
# Para todas las definiciones que incluyan owner solamente aceptarlo en la sintaxis no hacer nada con ellos

class AlterDBOwner(Instruccion):
    def __init__(self, id, owner, strGram,linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.id = id
        self.owner = owner
        

    def ejecutar(self, tabla, arbol):
        #super().ejecutar(tabla,arbol)
        arbol.consola.append("Consulta devuelta correctamente.")

    def analizar(self, tabla, arbol):
        print("analizar")

    def traducir(self, tabla, arbol):
        
        cadena = "\"alter database " + self.id
        cadena += " owner to "
        cadena += self.owner
        cadena += ";\""

        arbol.addComen("Asignar cadena")
        temporal1 = tabla.getTemporal()
        arbol.addc3d(f"{temporal1} = { cadena }")

        arbol.addComen("Entrar al ambito")
        temporal2 = tabla.getTemporal()
        arbol.addc3d(f"{temporal2} = P+2")
        temporal3 = tabla.getTemporal()
        arbol.addComen("parametro 1")
        arbol.addc3d(f"{temporal3} = { temporal2}+1")
        arbol.addComen("Asignacion de parametros")
        arbol.addc3d(f"Pila[{temporal3}] = {temporal1}")

        arbol.addComen("Llamada de funcion")
        arbol.addc3d(f"P = P+2")
        arbol.addc3d(f"funcionintermedia()")
        
        arbol.addComen("obtener resultado")
        temporalX = tabla.getTemporal()
        arbol.addc3d(f"{temporalX} = P+2")
        temporalR = tabla.getTemporal()
        arbol.addc3d(f"{temporalR} = Pila[{ temporalX }]")

        arbol.addComen("Salida de funcion")
        arbol.addc3d(f"P = P-2")