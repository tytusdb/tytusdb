from enum import Enum
from astDDL import Instruccion

class COMBINE_QUERYS(Enum):
    UNION = 1
    INTERSECT = 2
    EXCEPT = 3

class JOIN(Enum):
    INNER = 1
    LEFT = 2
    RIGHT = 3
    FULL = 4

# ------------------------ Select ----------------------------
# Select Table
class SelectTable(Instruccion):
    def __init__(self, campos, tablas = None, filtro = None, orden = None, limite = None, offset = None, join = None):
        self.campos = campos
        self.tablas = tablas
        self.filtro = filtro
        self.orden = orden
        self.limite = limite
        self.offset = offset
        self.join = join

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"SELECT TABLE\" ];" + "\nVALUES" + identificador + "[ label = \"FIELDS\" ];"
        nodo += "\n" + identificador + " -> VALUES" + identificador + ";"

        # Para los distintos campos que puedan ser objeto, una lista o un booleano
        if isinstance(self.campos, bool):
            nodo += "\nVALUES" + identificador + " -> " + str(hash(self.campos)) + ";"
            nodo += "\n" + str(hash(self.campos)) + "[ label = \"*\" ];"
        elif isinstance(self.campos, list):
            for campo in self.campos:
                nodo += "\nVALUES" + identificador + " -> " + str(hash(campo)) + ";"
                nodo += campo.dibujar()
        else:
            nodo += "\nVALUES" + identificador + " -> " + str(hash(self.campos)) + ";"
            nodo += self.campos.dibujar()

        # Para from
        if self.tablas:
            nodo += "\nFROM" + identificador + "[ label = \"FROM\" ];"
            nodo += "\n" + identificador + " -> FROM" + identificador + ";"
            for tabla in self.tablas:
                nodo += "\nFROM" + identificador + " -> " + str(hash(tabla)) + ";"
                nodo += tabla.dibujar()

        # Para filtro
        if self.filtro:
            nodo += "\n" + identificador + " -> " + str(hash(self.filtro)) + ";"
            nodo += self.filtro.dibujar()
        
        # Para orders
        if self.orden:
            nodo += "\n" + identificador + " -> " + str(hash(self.orden)) + ";"
            nodo += self.orden.dibujar()

        # Para limites
        if self.limite:
            nodo += "\n" + identificador + " -> " + str(hash(self.limite)) + ";"
            if isinstance(self.limite, int):
                nodo += "\n" + str(hash(self.limite)) + "[ label =  \"" + str(self.limite) + "\"];"
            else:            
                nodo += "\n" + str(hash(self.limite)) + "[ label =  \"ALL\"];"

        # Para offset
        if self.offset:
            nodo += "\n" + identificador + " -> " + str(hash(self.offset)) + ";"
            nodo += "\n" + str(hash(self.offset)) + "[ label =  \"" + str(self.offset) + "\"];"

        # Para join
        if self.join:
            nodo += "\n" + identificador + " -> " + str(hash(self.join)) + ";"
            nodo += self.join.dibujar()

        return nodo

# JOIN
class SelectJoin(Instruccion):
    def __init__(self, tabla, tipo, coincidencia = None, natural = False, outer = False):
        self.tabla = tabla
        self.tipo = tipo
        self.coincidencia = coincidencia
        self.natural = natural
        self.outer = outer

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador

        if self.natural:
            if self.outer:
                if self.tipo == JOIN.RIGHT:
                    nodo += "[ label = \"NATURAL RIGHT OUTER\" ];"
                elif self.tipo == JOIN.LEFT:
                    nodo += "[ label = \"NATURAL LEFT OUTER\" ];"
                else:
                    nodo += "[ label = \"NATURAL FULL OUTER\" ];"
            else:
                if self.tipo == JOIN.INNER:
                    nodo += "[ label = \"NATURAL INNER\" ];"
                elif self.tipo == JOIN.RIGHT:
                    nodo += "[ label = \"NATURAL RIGHT\" ];"
                elif self.tipo == JOIN.LEFT:
                    nodo += "[ label = \"NATURAL LEFT\" ];"
                else:
                    nodo += "[ label = \"NATURAL FULL\" ];"
        else:
            if self.outer:
                if self.tipo == JOIN.RIGHT:
                    nodo += "[ label = \"RIGHT OUTER\" ];"
                elif self.tipo == JOIN.LEFT:
                    nodo += "[ label = \"LEFT OUTER\" ];"
                else:
                    nodo += "[ label = \"FULL OUTER\" ];"
            else:
                if self.tipo == JOIN.INNER:
                    nodo += "[ label = \"INNER\" ];"
                elif self.tipo == JOIN.RIGHT:
                    nodo += "[ label = \"RIGHT\" ];"
                elif self.tipo == JOIN.LEFT:
                    nodo += "[ label = \"LEFT\" ];"
                else:
                    nodo += "[ label = \"FULL\" ];"
        
        nodo += "\n" + str(hash(self.tabla)) + "[ label = \"" + self.tabla + "\" ];"
        nodo += "\n" + identificador + " -> " + str(hash(self.tabla)) + ";"

        return nodo

# Select From
class SelectFrom(Instruccion):
    def __init__(self, fuente, alias = None):
        self.fuente = fuente
        self.alias = alias
    
    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador
        if self.alias:
            nodo += "[ label = \"AS: " + self.alias + "\" ];"
            nodo += "\n" + identificador + " -> " + str(hash(self.fuente)) + ";"
            if isinstance(self.fuente, str):
                nodo += "\n" + str(hash(self.fuente)) + "[ label = \"" + self.fuente + "\" ];\n"
            else:
                nodo += self.fuente.dibujar()
        else:
            if isinstance(self.fuente, str):
                nodo += "[ label = \"" + self.fuente + "\" ];\n"
            else:
                nodo += "[ label = \"SUBQUERY\" ];"
                nodo += "\n" + identificador + " -> " + str(hash(self.fuente)) + ";"
                nodo += self.fuente.dibujar()
        return nodo

# Select filter
class SelectFilter(Instruccion):
    def __init__(self, where, groupby = None, having = None):
        self.where = where
        self.groupby = groupby
        self.having = having

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"FILTER\" ];"

        # Para el where
        nodo += "\nWHERE" + identificador + "[ label = \"WHERE\" ];"
        nodo += "\n" + identificador + " -> WHERE" + identificador + ";"
        nodo += "\nWHERE" + identificador + " -> " + str(hash(self.where)) + ";"

        # Para el group by
        if self.groupby:
            nodo += "\nGROUPBY" + identificador + "[ label = \"GROUP BY\" ];"
            nodo += "\n" + identificador + " -> GROUPBY" + identificador + ";"
            nodo += "\nGROUPBY" + identificador + " -> " + str(hash(self.groupby)) + ";"

        if self.having:
            nodo += "\nHAVING" + identificador + "[ label = \"HAVING\" ];"
            nodo += "\n" + identificador + " -> HAVING" + identificador + ";"
            nodo += "\nHAVING" + identificador + " -> " + str(hash(self.having)) + ";"        

        return nodo

# Select orderby
class SelectOrderBy(Instruccion):
    def __init__(self, exp, orden = None, nulo = None):
        self.exp = exp
        self.orden = orden
        self.nulo = nulo
    
    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"ORDER BY\" ];"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp)) + ";"
        nodo += self.exp.dibujar()

        if self.orden:
            nodo += "\n" + str(hash(self.orden)) + "[ label = \"" + self.orden + "\" ];"
            nodo += "\n" + identificador + " -> " + str(hash(self.orden)) + ";\n"

        if self.nulo:
            nodo += "\n" + str(hash(self.nulo)) + "[ label = \"" + self.nulo + "\" ];"
            nodo += "\n" + identificador + " -> " + str(hash(self.nulo)) + ";\n"

        return nodo

# Select Aggregate
class SelectAggregate(Instruccion):
    def __init__(self, funcion, parametro):
        self.funcion = funcion
        self.parametro = parametro

# Combine Select
class CombineSelect(Instruccion):
    def __init__(self, select1, select2, funcion, all = False):
        self.select1 = select1
        self.select2 = select2
        self.funcion = funcion
        self.all = all

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador 

        if self.all:
            if self.funcion == COMBINE_QUERYS.UNION:
                nodo += "[ label = \"UNION ALL\" ];"
            elif self.funcion == COMBINE_QUERYS.INTERSECT:
                nodo += "[ label = \"INTERSECT ALL\" ];"
            else:
                nodo += "[ label = \"EXCEPT ALL\" ];"
        else:
            if self.funcion == COMBINE_QUERYS.UNION:
                nodo += "[ label = \"UNION\" ];"
            elif self.funcion == COMBINE_QUERYS.INTERSECT:
                nodo += "[ label = \"INTERSECT\" ];"
            else:
                nodo += "[ label = \"EXCEPT\" ];"

        nodo += "\n" + identificador + " -> " + str(hash(self.select1)) + ";"
        nodo += self.select1.dibujar() + "\n"

        nodo += "\n" + identificador + " -> " + str(hash(self.select2)) + ";"
        nodo += self.select2.dibujar() + "\n"

        return nodo