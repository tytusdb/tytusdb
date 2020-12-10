import gramaticaASC as g
from sentencias import *


def interpretar_sentencias(arbol):
    for nodo in arbol:
        if isinstance(nodo, SCrearBase):
            print("Creando Base-----")
            print(nodo.id)
            print("Es con replace?")
            print(nodo.replace)
            print("Es con if not exists?")
            print(nodo.exists)
            # aqui va el metodo para ejecutar crear base
        elif isinstance(nodo, SShowBase):
            print("Mostrando Base-----")
            print(nodo.like)
            # aqui va el metodo para ejecutar show base
        elif isinstance(nodo, SAlterBase):
            print("Alterando Base-----")
            print(nodo.id)
            # aqui va el metodo para ejecutar alter base
        elif isinstance(nodo, SDropBase):
            print("Drop Base-----")
            print(nodo.exists)
            print(nodo.id)
            # aqui va el metodo para ejecutar drop base
        elif isinstance(nodo, STypeEnum):
            print("Enum Type------")
            print(nodo.id)
            for val in nodo.lista:
                print(val.valor)
        elif isinstance(nodo,SUpdateBase):
            print("Update Table-----------")
            print(nodo.id)
            for val in nodo.listaSet:
                print("columna------")
                print(val.columna)
                print("------------")
                if isinstance(val.valor, SOperacion):
                    val2=val.valor
                    print(val2.opIzq.valor)
                    print(val2.operador)
                    print(val2.opDer.valor)
                else:
                    val2=val.valor
                    print(val2.valor)
            print(nodo.listaWhere)

f = open("./entrada.sql", "r")
input = f.read()

arbol = g.parse(input)

interpretar_sentencias(arbol)
