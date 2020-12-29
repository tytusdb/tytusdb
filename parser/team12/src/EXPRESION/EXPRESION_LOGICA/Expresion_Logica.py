import sys, os.path

nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\ENTORNO\\')
sys.path.append(nodo_dir)

from Tipo import Data_Type

# **************************************************************************************************************
def NOT(exp, expRes, enviroment):
    val = exp.execute(enviroment)

    if exp.tipo.data_type == Data_Type.boolean :
        expRes.tipo = exp.tipo
        expRes.valorExpresion = not val
    else:
        expRes.tipo.data_type == Data_Type.error
        expRes.valorExpresion = None

    return expRes
# **************************************************************************************************************
# **************************************************************************************************************
def AND(exp1, exp2, expRes, enviroment):
    val1 = exp1.execute(enviroment)
    val2 = exp2.execute(enviroment)

    if exp1.tipo.data_type == Data_Type.boolean and exp2.tipo.data_type == Data_Type.boolean:

        expRes.tipo.data_type = Data_Type.boolean
        expRes.valorExpresion = val1 and val2

    else:
        expRes.tipo.data_type == Data_Type.error
        expRes.valorExpresion = None

    return expRes
# **************************************************************************************************************
# **************************************************************************************************************
def OR(exp1, exp2, expRes, enviroment):
    val1 = exp1.execute(enviroment)
    val2 = exp2.execute(enviroment)

    if exp1.tipo.data_type == Data_Type.boolean and exp2.tipo.data_type == Data_Type.boolean:

        expRes.tipo.data_type = Data_Type.boolean
        expRes.valorExpresion = val1 or val2

    else:
        expRes.tipo.data_type == Data_Type.error
        expRes.valorExpresion = None

    return expRes
# **************************************************************************************************************