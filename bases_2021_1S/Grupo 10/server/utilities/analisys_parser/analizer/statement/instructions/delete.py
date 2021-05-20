from utilities.storage import avlMode
from utilities.analisys_parser.analizer.typechecker.Metadata import Struct
from utilities.analisys_parser.analizer.symbol.environment import Environment
from utilities.analisys_parser.analizer.reports import Nodo
from utilities.analisys_parser.analizer.abstract import instruction

# carga de datos
Struct.load()


class Delete(instruction.Instruction):
    def __init__(self, fromcl, wherecl, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.wherecl = wherecl
        self.fromcl = fromcl

    def execute(self, environment):
        try:
            Struct.load()
            # Verificamos que no pueden venir mas de 1 tabla en el clausula FROM
            if len(self.fromcl.tables) > 1:
                instruction.semanticErrors.append(
                    ["Error sintactico cerca de ,", self.row]
                )
                instruction.syntaxPostgreSQL.append(
                    "Error: 42601: Error sintactico cerca de , en la linea "
                    + str(self.row)
                )
                return "Error: syntax error at or near ','"
            newEnv = Environment(environment, instruction.dbtemp)
            instruction.envVariables.append(newEnv)
            self.fromcl.execute(newEnv)
            value = [newEnv.dataFrame[p] for p in newEnv.dataFrame]
            labels = [p for p in newEnv.dataFrame]
            for i in range(len(labels)):
                newEnv.dataFrame[labels[i]] = value[i]
            if self.wherecl == None:
                return newEnv.dataFrame.filter(labels)
            wh = self.wherecl.execute(newEnv)
            w2 = wh.filter(labels)
            # Si la clausula WHERE devuelve un dataframe vacio
            if w2.empty:
                return "Operacion DELETE completada"
            # Logica para eliminar
            table = self.fromcl.tables[0].name
            pk = Struct.extractPKIndexColumns(instruction.dbtemp, table)
            # Se obtienen las parametros de las llaves primarias para proceder a eliminar
            rows = []
            if pk:
                for row in w2.values:
                    rows.append([row[p] for p in pk])
            else:
                rows.append([i for i in w2.index])
            print(rows)
            # TODO: La funcion del STORAGE esta bugueada
            bug = False
            for row in rows:
                result = avlMode.delete(instruction.dbtemp, table, row)
                if result != 0:
                    bug = True
                    break
            if bug:
                return ["Error: Funcion DELETE del Storage", rows]
            return "Operacion DELETE completada"
        except:
            instruction.syntaxPostgreSQL.append(
                "Error: P0001: Error en la instruccion DELETE"
            )

    def dot(self):
        new = Nodo.Nodo("DELETE")
        new.addNode(self.fromcl.dot())
        if self.wherecl:
            new.addNode(self.wherecl.dot())
        return new