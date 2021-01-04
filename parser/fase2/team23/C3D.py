import pickle
from analizer.abstract import instruction as inst

with open("obj.pickle", "rb") as f:
    result = pickle.load(f)

pila = 0
eje_if = "Verdadero"

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

    elif isinstance(result[cont], inst.IfCls):
        r = result[cont]


        if eje_if == "Verdadero":
            for l in r.lista_stm:
                l.execute(None)


        elif eje_if == "Else":
            for l in r.else_:
                l.execute(None)


        elif eje_if == "Elsif":
            for l in r.elsif_:
                l.execute(None)

    else:
        r = result[cont].execute(None)