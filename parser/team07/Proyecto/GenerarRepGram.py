import os
Lineas = []

class GenerarRepGram():
    


    def AgregarTexto(Texto):
        Lineas.append(Texto)

    def GenerarReporte():

        Archivo = 'ReporteGramatical.md'

        f = open(Archivo, "w")
        f.write("")
        f.close()

        f = open(Archivo, "a+")

        for linea in reversed(Lineas):
            f.write(linea)

        f.close()

 