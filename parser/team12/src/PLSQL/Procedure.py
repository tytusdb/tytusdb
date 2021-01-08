from goto import with_goto
class Procedure():
    def __init__(self):
        self.orreplace = False #No se reemplaza por default.
        self.nombre = None #Nombre del procedimiento
        self.listaArgumentos = []

    @with_goto
    def compile(self,parent):
        
        if True:
            goto .holaMundo
        else:
            goto .end

        label .holaMundo
        print("Hola Mundo")
        label .end