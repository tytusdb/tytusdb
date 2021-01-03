class Atribb():
    def __init__(self):
        self.column = None
        self.order = None
        self.nulls = None

    
    def execute(self, parent):
        # Se recibe ATRIB_E
        for hijo in parent.hijos:
            if hijo.nombreNodo == "IDENTIFICADOR":
                self.column = hijo.valor.upper()
            elif hijo.nombreNodo == "OPC_ORDER":
                self.order = hijo.hijos[0].nombreNodo.upper()
            elif hijo.nombreNodo == "OPC_NULLS":
                self.nulls = hijo.hijos[0].nombreNodo.upper()
        if self.order == None:
            self.order = "DESC"

class Index():
    def __init__(self):
        self.name = None
        self.table = None
        self.method = None
        self.listaAtribb = []
        self.sentenciaWhere = None

    def setMethod(self, parent):
        self.method = parent.hijos[0].value



    def execute(self, parent):
        # Se recibe una sentencia CREATE INDEX
        self.name = parent.hijos[0].valor
        self.table = parent.hijos[1].valor
        for hijo in parent.hijos[2].hijos:
            if hijo.nombreNodo == "ATRIB_E":
                nuevaCol = Atribb()
                nuevaCol.execute(hijo)
                self.listaAtribb.append(nuevaCol)
            elif hijo.nombreNodo == "SENTENCIA_METHOD_INDEX":
                self.setMethod(hijo)
        if self.method == None:
            self.method = "BTREE"
        if len(parent.hijos) == 4:#Where
            self.sentenciaWhere = self.construirExpresionJSON(parent.hijos[3])
        
        #Se agrega a typeChecker
        






    def construirExpresionJSON(self, parent):
        if len(parent.hijos) == 3 :
            obj1 = self.construirExpresionJSON(parent.hijos[0])
            obj2 = self.construirExpresionJSON(parent.hijos[2])
            jsonExpresion = {
                'E0' : obj1,
                'operador' : parent.hijos[1].nombreNodo,
                'E1' : obj2
            }
            return jsonExpresion
        elif len(parent.hijos) == 2:
            jsonExpresion = {
                'nodo0' : self.construirExpresionJSON(parent.hijos[0]),
                'nodo1' : self.construirExpresionJSON(parent.hijos[1])
            }
            return jsonExpresion
        elif len(parent.hijos) == 1:
            jsonExpresion = {
                'nombre' : parent.hijos[0].nombreNodo,
                'valor' : parent.hijos[0].valor
            }
            return jsonExpresion