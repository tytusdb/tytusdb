# GRUPO 5
# 201213062 - Mónica Raquel Calderon Muñoz
# 201213223 - Astrid Edith Hernandez Gonzalez
# 201213255 - Leonel Eduardo Avila Calvillo
# 201220159 - Diego Ahtohil Noj Armira
# 201220165 - Oscar Rolando Bernard Peralta

# INSTRUCCIONES [select]
class Instruccion:
    """ This is an abstract class """


# INSTRUCCION SELECT MINIMO
class Select(Instruccion):
    """ Instrucción SELECT """

    def __init__(self, valores, pfrom, complementos):
        self.valores = valores
        self.pfrom = pfrom
        self.complementos = complementos

# INSTRUCCION SELECT WITH WHERE 
class Select1(Instruccion):
    """ Instrucción SELECT """

    def __init__(self, valores, pfrom, where, complementos):
        self.valores = valores
        self.pfrom = pfrom
        self.where = where
        self.complementos = complementos

# INSTRUCCION SELECT DISTINCT
class Select2(Instruccion):
    """ Instrucción SELECT """

    def __init__(self, valores, pfrom, complementos):
        self.valores = valores
        self.pfrom = pfrom
        self.complementos = complementos

# INSTRUCCION SELECT DISTINCT WITH WHERE
class Select3(Instruccion):
    """ Instrucción SELECT """

    def __init__(self, valores, pfrom, where, complementos):
        self.valores = valores
        self.pfrom = pfrom
        self.where = where
        self.complementos = complementos

# INSTRUCCION SELECT SOLO VALORES
class Select4(Instruccion):
    """ Instrucción SELECT """

    def __init__(self, valores):
        self.valores = valores

# INSTRUCCION COMPLEMENTOSELECTUNION
class ComplementoSelectUnion(Instruccion):
    """ Instrucción COMPLEMENTO SELECT """

    def __init__(self, select):
        self.select = select

# INSTRUCCION COMPLEMENTOSELECTALL
class ComplementoSelectUnionAll(Instruccion):
    """ Instrucción COMPLEMENTO SELECT """

    def __init__(self, select):
        self.select = select

# INSTRUCCION COMPLEMENTOSELECTINTERSECT
class ComplementoSelectIntersect(Instruccion):
    """ Instrucción COMPLEMENTO SELECT """

    def __init__(self, select):
        self.select = select

# INSTRUCCION COMPLEMENTOSELECTINTERSECTALL
class ComplementoSelectIntersectALL(Instruccion):
    """ Instrucción COMPLEMENTO SELECT """

    def __init__(self, select):
        self.select = select

# INSTRUCCION COMPLEMENTOSELECTEXCEPT
class ComplementoSelectExcept(Instruccion):
    """ Instrucción COMPLEMENTO SELECT """

    def __init__(self, select):
        self.select = select

# INSTRUCCION COMPLEMENTOSELECTEXCEPTALL
class ComplementoSelectExceptAll(Instruccion):
    """ Instrucción COMPLEMENTO SELECT """

    def __init__(self, select):
        self.select = select

# INSTRUCCION COMPLEMENTOSELECTEXCEPTPCOMA
class ComplementoSelectExceptPcoma(Instruccion):
    """ Instrucción COMPLEMENTO SELECT """

    def __init__(self, param=None):
        self.param = param
        # NO RECIBE PARAMETROS

# ----------FIN DE CLASES SELECT--------------

# ----------INICIO DE CREATE------------------

# INSTRUCCION CREATE
class Create(Instruccion):
    """ Instrucción CREATE """

    def __init__(self, replace):
        self.replace = replace

# INSTRUCCION CREATE1
class Create(Instruccion):
    """ Instrucción CREATE """

    def __init__(self, table):
        self.table = table

# INSTRUCCION CREATE2
class Create(Instruccion):
    """ Instrucción CREATE """

    def __init__(self, tipe):
        self.tipe = tipe

# ----------FIN DE CLASES CREATE--------------

# ----------INICIO DE DROP--------------------
# INSTRUCCION DROP
class Drop(Instruccion):
    """ Instrucción DROP """

    def __init__(self, tdrop):
        self.tdrop = tdrop

# INSTRUCCION DROPDB
class DropDB(Instruccion):
    """ Instrucción DROPDB """

    def __init__(self, ifexist):
        self.ifexist = ifexist

# INSTRUCCION IFEXIST
class IfExist(Instruccion):
    """ Instrucción EXIST """

    def __init__(self, i_id):
        self.i_id = i_id

# ----------INICIO DE DROP--------------------
