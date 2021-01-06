
class controlador():
    def __init__(self):
        self.c3d = ''
        self.cont_temp = 0
        self.etiquetas = 0
        self.heap = 0
        self.stack = 0
        self.errores = []

    def append_3d(self, codigo):
        self.c3d += codigo +'\n'

    def get_etiqueta(self):
        self.etiquetas = self.etiquetas+1
        return 'L' +  str(self.etiquetas)

    