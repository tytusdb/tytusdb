from Parser.Reportes.Nodo1 import Nodo

#--------------- add Nodo ---------------
def add(t,destino:int,origen:int):
    t[destino].add(t[origen])


def UnionNode(t,inicio:int,fin:int) -> Nodo:
    value = ''
    for i in range(inicio,fin+1):
        value += t[i]+' '
    result = Nodo(value)
    return result

if __name__ == '__main__':

    t = [Nodo('holi'),Nodo('como'),Nodo('estas')]

    print(t)
    add(t,0,2)
    print(t)

    lol = ['holi','como','estas','heloo']

    node = UnionNode(lol,1,2)

    print(node.getValor())
