
class Tipo() :
    'Esta clase representa un tipo dentro de nuestra tabla de tipos'

    def __init__(self, tabla, id, tipo, restriccion, referencia, tablaRef) :
        self.tabla = tabla
        self.id = id
        self.tipo = tipo
        self.restriccion = restriccion
        self.referencia = referencia
        self.tablaRef = tablaRef

class TablaDeTipos() :
    'Esta clase representa la tabla de tipos'

    def __init__(self, tipos = []) :
        self.tipos = tipos

    def agregar(self, tipo) :
        self.tipos.append(tipo)
    
    def obtener(self, id) :
        if not id in self.tipos :
            print('Error: variable ', id, ' no definida.')

        return self.tipos[id]

    def actualizar(self,tipo, tabla, column) :
        i = 0
        while i < len(self.tipos):
            if self.tipos[i].tabla == tabla and self.tipos[i].id == column:
                self.tipos[i] = tipo
            i += 1

    def actualizarRestriccion(self,tipo, tabla, column, restriccion) :
        i = 0
        while i < len(self.tipos):
            if self.tipos[i].tabla == tabla and self.tipos[i].id == column:
                self.tipos[i].restriccion = restriccion
            i += 1

    def actualizarLlaveForanea(self,tipo, tabla, column, restriccion,tablaRef, referencia) :
        i = 0
        while i < len(self.tipos):
            if self.tipos[i].tabla == tabla and self.tipos[i].id == column:
                self.tipos[i].restriccion = restriccion
                self.tipos[i].referencia = referencia
                self.tipos[i].tablaRef = tablaRef
            i += 1

    def clear(self):
        self.tipos = []