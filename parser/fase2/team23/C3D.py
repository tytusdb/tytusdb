import pickle
from analizer.abstract import instruction as inst
from analizer.symbol.environment import Environment
from prettytable import PrettyTable

with open("obj.pickle", "rb") as f:
    result = pickle.load(f)

pila = 0
eje_if = "Verdadero"
tabla = Environment()

def ejecutar():
    cont = pila
    
    if isinstance(result[cont], inst.Select) or isinstance(result[cont], inst.SelectOnlyParams):
        r = result[cont].execute(tabla)
        if r:
            list_ = r[0].values.tolist()
            labels = r[0].columns.tolist()
            salidaTabla = PrettyTable()
            encabezados = labels
            salidaTabla.field_names = encabezados
            cuerpo = list_
            salidaTabla.add_rows(cuerpo)
            print(salidaTabla)
            print("\n")
            print("\n")
        else:
           print("")

    elif isinstance(result[cont], inst.IfCls):
        r = result[cont]
        r.execute(tabla)

    else:
        r = result[cont].execute(tabla)