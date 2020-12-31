import pickle
from analizer.abstract import instruction as inst

with open("obj.pickle", "rb") as f:
    result = pickle.load(f)

pila = 0

def ejecutar():
    cont = pila
    if isinstance(result[cont], inst.Select) or isinstance(result[cont], inst.SelectOnlyParams):
        r = result[cont].execute(None)
        if r:
            list_ = r[0].values.tolist()
            labels = r[0].columns.tolist()
            querys.append([labels, list_])
        else:
            querys.append(None)
    else:
        r = result[cont].execute(None)