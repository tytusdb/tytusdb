class ListaErrores:
    def __init__(self):
        self.fin=None
        self.principio=None

    def insertar(self,r):
        if self.principio is None:
            self.principio=r
            self.fin=r
            return
        self.fin.siguiente=r
        r.anterior=self.fin
        self.fin=r
    
    def geterrores(self):
        texto = ""

        muestra = self.principio
        while (muestra != None):

            texto += "TIPO: " + muestra.tipo + " DESCRIPCION: " + muestra.descripcion + " LINEA: " + str(muestra.fila) + " COLUMNA: " + str(muestra.columna) + " \n"
            muestra = muestra.siguiente
        
        return texto