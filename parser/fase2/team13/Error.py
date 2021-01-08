class ErrorS:
    def __init__(self, tipo, descripcion):
        self.tipo  = tipo
        self.descripcion = descripcion

    def __str__(self):
        return "ERROR => tipo: %s, descripcion: %s " % (
        self.tipo, self.descripcion,)


class Error:
    def __init__(self, lexema, tipo, descripcion, columna, fila):
        self.lexema      = lexema
        self.tipo  = tipo
        self.descripcion = descripcion
        self.columna     = columna
        self.fila        = fila
    
    def __str__(self):
        return "ERROR => lexema: %s, tipo: %s, descripcion: %s, columna: %d, fila: %d " % (self.lexema, self.tipo, self.descripcion, self.columna, self.fila)

class item3D:
    def __init__(self, cod3d, opt, regla):
        self.cod3d = cod3d
        self.opt  = opt
        self.regla = regla
    
    def __str__(self):
        return "C3D => cod3d: %s, opt: %s, regla: %s " % (self.cod3d, self.opt, self.regla)