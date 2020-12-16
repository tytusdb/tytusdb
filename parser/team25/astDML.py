from astDDL import Instruccion

# ------------------------ DML ----------------------------
# Insert into table
class InsertTable(Instruccion):
    def __init__(self, tabla, valores):
        self.tabla = tabla
        self.valores = valores
    
    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"INSERT TABLE\" ];"

        nodo += "\nINTO" + identificador + "[ label = \"INTO\" ];"
        nodo += "\n" + identificador + " -> INTO" + identificador + ";"
        nodo += "\nNAME" + identificador + "[ label = \"" + self.tabla + "\" ];"
        nodo += "\nINTO" + identificador + " -> NAME" + identificador + ";"
        nodo += "\nVALUES" + identificador + "[ label = \"VALUES\" ];"
        nodo += "\n" + identificador + " -> VALUES" + identificador + ";"
        
        for valor in self.valores:
            nodo += "\nVALUES" + identificador + " -> " + str(hash(valor)) + ";"
            nodo += valor.dibujar()

        return nodo

# Delete from a table
class DeleteTabla(Instruccion):
    def __init__(self, tabla, condiciones = None):
        self.tabla = tabla
        self.condiciones = condiciones

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"DELETE TABLE\" ];"

        nodo += "\nFROM" + identificador + "[ label = \"FROM\" ];"
        nodo += "\n" + identificador + " -> FROM" + identificador + ";"
        nodo += "\nNAME" + identificador + "[ label = \"" + self.tabla + "\" ];"
        nodo += "\nFROM" + identificador + " -> NAME" + identificador + ";"

        if self.condiciones:
            nodo += "\nWHERE" + identificador + "[ label = \"WHERE\" ];"
            nodo += "\n" + identificador + " -> WHERE" + identificador + ";"

            for condicion in self.condiciones:
                nodo += "\nWHERE" + identificador + " -> " + str(hash(condicion)) + ";"
                nodo += condicion.dibujar()

        return nodo

class UpdateTable(Instruccion):
    def __init__(self, tabla, asignaciones, condiciones = None):
        self.tabla = tabla
        self.asignaciones = asignaciones
        self.condiciones = condiciones

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"DELETE TABLE\" ];"

        nodo += "\nNAME" + identificador + "[ label = \"" + self.tabla + "\" ];"
        nodo += "\n" + identificador + " -> NAME" + identificador + ";"

        nodo += "\nSET" + identificador + "[ label = \"SET\" ];"
        nodo += "\n" + identificador + " -> SET" + identificador + ";"

        for asignacion in self.asignaciones:
            nodo += "\nSET" + identificador + " -> " + str(hash(asignacion)) + ";"
            nodo += asignacion.dibujar()

        if self.condiciones:
            nodo += "\nWHERE" + identificador + "[ label = \"WHERE\" ];"
            nodo += "\n" + identificador + " -> WHERE" + identificador + ";"

            for condicion in self.condiciones:
                nodo += "\nWHERE" + identificador + " -> " + str(hash(condicion)) + ";"
                nodo += condicion.dibujar()

        return nodo