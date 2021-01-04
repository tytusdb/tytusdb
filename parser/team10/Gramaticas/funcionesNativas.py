class nativas:
    '''Clase abstracta para almacenamiento de datos de diferentes funciones'''

class campo(nativas):
    def __init__(self, id, tipo, isLlave, hasCheck, isIdentity , setNull, setConstraint):
        self.id = id
        self.tipo = tipo
        self.isLlave = isLlave
        self.hasCheck = hasCheck
        self.isIdentity = isIdentity
        self.setNull  = setNull
        self.setConstraint = setConstraint
        self.dimension =''

    def setDimension(self, dimen):
        self.dimension = dimen

    def setCheck(self, hasCheck):
        self.hasCheck = hasCheck

class constraintRule(nativas):
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor


class TablaB(nativas):
    def __init__(self, nombre, listCampos , listLlavesForeign , listLlavesPrimary):
        self.nombre = nombre
        self.listCampos = listCampos
        self.listLlavesForeign = listLlavesForeign
        self.listLlavesPrimary = listLlavesPrimary

    def agregar(self, campo) :
        self.listCampos[campo.id] = campo
    
    def obtener(self, id) :
        if not id in self.listCampos :
            print('Error: variable ', id, ' no definida.')

        return self.listCampos[id]


    def delete(self, id):
       del self.listCampos[id]


    def actualizar(self, campo) :
        if not campo.id in self.listCampos :
            print('Error: variable ', campo.id, ' no definida.')
        else :
            self.listCampos[campo.id] = campo


    def existe(self, id):
        return id in self.listCampos

