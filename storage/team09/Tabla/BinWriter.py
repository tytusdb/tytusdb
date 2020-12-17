import os


def read(self):
    archivo = open(self.ruta,"br")
    content = archivo.readlines()
    archivo.close()
    return content

def write(self, salida):
    archivo = open(rutaSalida,"bw")
    archivo.writelines(salida)
    archivo.close()
