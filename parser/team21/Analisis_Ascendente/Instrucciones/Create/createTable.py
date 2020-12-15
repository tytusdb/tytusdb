from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion

#CREATE TABLE
class CreateTable(Instruccion):
    def __init__(self, id, campos, idInherits):
        self.id = id
        self.campos = campos
        self.idInherits = idInherits
