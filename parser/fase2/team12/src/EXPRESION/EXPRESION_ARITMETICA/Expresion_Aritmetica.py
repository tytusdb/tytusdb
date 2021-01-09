import sys, os.path

nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\ENTORNO\\')
sys.path.append(nodo_dir)

from Tipo import Data_Type

# **************************************************************************************************************
def suma(exp1, exp2, expRes, enviroment):
    val1 = exp1.execute(enviroment)
    val2 = exp2.execute(enviroment)

    if exp1.tipo.data_type == Data_Type.numeric and exp2.tipo.data_type == Data_Type.numeric :
        expRes.tipo = exp1.tipo
        expRes.valorExpresion = val1 + val2
    else:
        expRes.tipo.data_type = Data_Type.error
        expRes.valorExpresion = None

    return expRes
# **************************************************************************************************************
# **************************************************************************************************************
def resta(exp1, exp2, expRes, enviroment):
    val1 = exp1.execute(enviroment)
    val2 = exp2.execute(enviroment)
    
    if exp1.tipo.data_type == Data_Type.numeric and exp2.tipo.data_type == Data_Type.numeric :
        expRes.tipo = exp1.tipo
        expRes.valorExpresion = val1 - val2
    else:
        expRes.tipo.data_type = Data_Type.error
        expRes.valorExpresion = None

    return expRes
# **************************************************************************************************************
# **************************************************************************************************************
def mult(exp1, exp2, expRes, enviroment):
    val1 = exp1.execute(enviroment)
    val2 = exp2.execute(enviroment)
    
    if exp1.tipo.data_type == Data_Type.numeric and exp2.tipo.data_type == Data_Type.numeric :
        expRes.tipo = exp1.tipo
        expRes.valorExpresion = val1 * val2
    else:
        expRes.tipo.data_type = Data_Type.error
        expRes.valorExpresion = None

    return expRes
# **************************************************************************************************************
# **************************************************************************************************************
def div(exp1, exp2, expRes, enviroment):
    val1 = exp1.execute(enviroment)
    val2 = exp2.execute(enviroment)

    if exp1.tipo.data_type == Data_Type.numeric and exp2.tipo.data_type == Data_Type.numeric :
        
        if val2 == 0:
            expRes.tipo.data_type = Data_Type.error
            expRes.valorExpresion = None
        else:
            expRes.tipo = exp1.tipo
            expRes.valorExpresion = val1 / val2

    else:
        expRes.tipo.data_type = Data_Type.error
        expRes.valorExpresion = None

    return expRes
# **************************************************************************************************************
# **************************************************************************************************************
def mod(exp1, exp2, expRes, enviroment):
    val1 = exp1.execute(enviroment)
    val2 = exp2.execute(enviroment)

    if exp1.tipo.data_type == Data_Type.numeric and exp2.tipo.data_type == Data_Type.numeric :
        
        if val2 == 0:
            expRes.tipo.data_type = Data_Type.error
            expRes.valorExpresion = None
        else:
            expRes.tipo = exp1.tipo
            expRes.valorExpresion = val1 % val2

    else:
        expRes.tipo.data_type = Data_Type.error
        expRes.valorExpresion = None

    return expRes
# **************************************************************************************************************
# **************************************************************************************************************
def pot(exp1, exp2, expRes, enviroment):
    val1 = exp1.execute(enviroment)
    val2 = exp2.execute(enviroment)
    
    if exp1.tipo.data_type == Data_Type.numeric and exp2.tipo.data_type == Data_Type.numeric :
        expRes.tipo = exp1.tipo
        expRes.valorExpresion = val1 ** val2
    else:
        expRes.tipo.data_type = Data_Type.error
        expRes.valorExpresion = None

    return expRes
# **************************************************************************************************************
# **************************************************************************************************************
def numNeg(exp1, expRes, enviroment):
    val1 = exp1.execute(enviroment)
    
    if exp1.tipo.data_type == Data_Type.numeric  :
        expRes.tipo = exp1.tipo
        expRes.valorExpresion = val1 * -1
    else:
        expRes.tipo.data_type = Data_Type.error
        expRes.valorExpresion = None

    return expRes
# **************************************************************************************************************