from classesQuerys import exp_query
def cond_OR(lst1, lst2): 
    final_list = list(set(lst1) | set(lst2)) 
    return final_list 

def cond_AND(lst1, lst2): 
    final_list = list(set(lst1) & set(lst2)) 
    return final_list 

class condition(exp_query):
    def _init_(self,exp ,tipo):
        self.exp = exp
        self.tipo = tipo

class select_condition():
    

    def ejecutar(tables,lcond):
        condition = lcond
        if len(condition) == 0:
            return None
        elif len(condition) == 1:
            return condition[0].exp.ejecutar(tables)
        else:
            #Obtengo las primeras posiciones y dependiendo 
            valor = condition[0].exp.ejecutar(tables)
            res =  valor['posiciones']
            
            for i in range(1, len(condition)):
                if condition[i].tipo == 'AND':
                    res = cond_AND(res, condition[i].exp.ejecutar(tables))

                else:
                    res = cond_OR(res, condition[i].exp.ejecutar(tables))
            return res