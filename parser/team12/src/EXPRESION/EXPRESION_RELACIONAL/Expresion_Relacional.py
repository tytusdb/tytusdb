import sys, os.path
import datetime

nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\ENTORNO\\')
sys.path.append(nodo_dir)

from Tipo import Data_Type

# **************************************************************************************************************
def diferente(exp1, exp2, expRes, enviroment):
    val1 = exp1.execute(enviroment)
    val2 = exp2.execute(enviroment)

    if exp1.tipo.data_type == Data_Type.numeric and exp2.tipo.data_type == Data_Type.numeric :

        expRes.tipo.data_type = Data_Type.boolean
        expRes.valorExpresion = val1 != val2    

    elif exp1.tipo.data_type == Data_Type.character and exp2.tipo.data_type == Data_Type.character :

        expRes.tipo.data_type = Data_Type.boolean
        expRes.valorExpresion = val1 != val2    

    elif exp1.tipo.data_type == Data_Type.boolean and exp2.tipo.data_type == Data_Type.boolean :

        expRes.tipo.data_type = Data_Type.boolean
        expRes.valorExpresion = val1 != val2 
        
    else:

        expRes.tipo.data_type = Data_Type.error
        expRes.valorExpresion = None
    
    return expRes
# **************************************************************************************************************
# **************************************************************************************************************
def igualdad(exp1, exp2, expRes, enviroment):
    val1 = exp1.execute(enviroment)
    val2 = exp2.execute(enviroment)

    if exp1.tipo.data_type == Data_Type.numeric and exp2.tipo.data_type == Data_Type.numeric :

        expRes.tipo.data_type = Data_Type.boolean
        expRes.valorExpresion = val1 == val2    

    elif exp1.tipo.data_type == Data_Type.character and exp2.tipo.data_type == Data_Type.character :

        expRes.tipo.data_type = Data_Type.boolean
        expRes.valorExpresion = val1 == val2    

    elif exp1.tipo.data_type == Data_Type.boolean and exp2.tipo.data_type == Data_Type.boolean :

        expRes.tipo.data_type = Data_Type.boolean
        expRes.valorExpresion = val1 == val2    

    else:

        expRes.tipo.data_type = Data_Type.error
        expRes.valorExpresion = None
    
    return expRes
# **************************************************************************************************************
# **************************************************************************************************************
def mayor(exp1, exp2, expRes, enviroment):
    val1 = exp1.execute(enviroment)
    val2 = exp2.execute(enviroment)

    if exp1.tipo.data_type == Data_Type.numeric and exp2.tipo.data_type == Data_Type.numeric :

        expRes.tipo.data_type = Data_Type.boolean
        expRes.valorExpresion = val1 > val2    

    elif exp1.tipo.data_type == Data_Type.character and exp2.tipo.data_type == Data_Type.character :

        expRes.tipo.data_type = Data_Type.boolean
        expRes.valorExpresion = val1 > val2    

    elif exp1.tipo.data_type == Data_Type.boolean and exp2.tipo.data_type == Data_Type.boolean :

        expRes.tipo.data_type = Data_Type.boolean
        expRes.valorExpresion = val1 > val2    

    else:

        expRes.tipo.data_type = Data_Type.error
        expRes.valorExpresion = None
    
    return expRes
# **************************************************************************************************************
# **************************************************************************************************************
def mayorigual(exp1, exp2, expRes, enviroment):
    val1 = exp1.execute(enviroment)
    val2 = exp2.execute(enviroment)

    if exp1.tipo.data_type == Data_Type.numeric and exp2.tipo.data_type == Data_Type.numeric :

        expRes.tipo.data_type = Data_Type.boolean
        expRes.valorExpresion = val1 >= val2    

    elif exp1.tipo.data_type == Data_Type.character and exp2.tipo.data_type == Data_Type.character :

        expRes.tipo.data_type = Data_Type.boolean
        expRes.valorExpresion = val1 >= val2    

    elif exp1.tipo.data_type == Data_Type.boolean and exp2.tipo.data_type == Data_Type.boolean :

        expRes.tipo.data_type = Data_Type.boolean
        expRes.valorExpresion = val1 >= val2    

    else:

        expRes.tipo.data_type = Data_Type.error
        expRes.valorExpresion = None
    
    return expRes
# **************************************************************************************************************
# **************************************************************************************************************
def menor(exp1, exp2, expRes, enviroment):
    val1 = exp1.execute(enviroment)
    val2 = exp2.execute(enviroment)

    if exp1.tipo.data_type == Data_Type.numeric and exp2.tipo.data_type == Data_Type.numeric :

        expRes.tipo.data_type = Data_Type.boolean
        expRes.valorExpresion = val1 < val2    

    elif exp1.tipo.data_type == Data_Type.character and exp2.tipo.data_type == Data_Type.character :

        expRes.tipo.data_type = Data_Type.boolean
        expRes.valorExpresion = val1 < val2    

    elif exp1.tipo.data_type == Data_Type.boolean and exp2.tipo.data_type == Data_Type.boolean :

        expRes.tipo.data_type = Data_Type.boolean
        expRes.valorExpresion = val1 < val2    

    else:

        expRes.tipo.data_type = Data_Type.error
        expRes.valorExpresion = None
    
    return expRes
# **************************************************************************************************************
# **************************************************************************************************************
def menorigual(exp1, exp2, expRes, enviroment):
    val1 = exp1.execute(enviroment)
    val2 = exp2.execute(enviroment)

    if exp1.tipo.data_type == Data_Type.numeric and exp2.tipo.data_type == Data_Type.numeric :

        expRes.tipo.data_type = Data_Type.boolean
        expRes.valorExpresion = val1 <= val2    

    elif exp1.tipo.data_type == Data_Type.character and exp2.tipo.data_type == Data_Type.character :

        expRes.tipo.data_type = Data_Type.boolean
        expRes.valorExpresion = val1 <= val2    

    elif exp1.tipo.data_type == Data_Type.boolean and exp2.tipo.data_type == Data_Type.boolean :

        expRes.tipo.data_type = Data_Type.boolean
        expRes.valorExpresion = val1 <= val2    

    else:

        expRes.tipo.data_type = Data_Type.error
        expRes.valorExpresion = None
    
    return expRes
# **************************************************************************************************************