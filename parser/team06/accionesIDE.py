import sys

class accionesIde():

    def cerrarVentana(self,valor):
        sys.exit(valor.exec_())
    
    def abrirArchivo(self,ruta):
        with open(ruta) as f:
            read_data=f.read()
            f.closed
            return read_data
    
    def guardarArchivo(self,ruta,texto):
        print("ruta:",ruta)
        print("el texto: ",texto)
        with open(ruta, "w") as f:
            f.write(texto)
            f.closed
            return True
    
    def AlternarValor(self,val):
        global valor
        valor=val+1
        return valor



