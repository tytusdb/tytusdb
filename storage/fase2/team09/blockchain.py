import json
import hashlib
import os
import pathlib
from graphviz import Digraph
import threading

def writeBlockChain(db, table, data, falg = True):
    """escribe el blockchain"""
    initCheck()
    if not pathlib.Path("blockchain/" + db + "_" + table + ".json").is_file() and falg:
        return
    bchain ={}
    f = list(map(_toHash, data))
    for x in range(0, len(f)):
        temp ={}
        if x == 0:
            temp["prev"] = "--"
        else:
            temp["prev"] = f[x-1]
        try:
            temp["next"] = f[x+1]
        except:
            temp["next"] = "--"
        bchain[f[x]] = temp
    target = {"list" : f, "bchain" : bchain}
    name = db + "_" + table
    write("blockchain\\"+name+".json",target)



def showBlockChain(db, table, data):
    hilo = threading.Thread(target=_showBlockChain, args = (db, table, data))
    hilo.start()


def _showBlockChain(db, table, data):
    """muestra el grafo"""
    initCheck()
    name = db + "_" + table
    bchan = read("blockchain\\"+name+".json")
    f = list(map(_toHash, data))
    flag = True
    imagen = Digraph(name=name, filename="blockchain\\"+name, format="png")
    for x in range(0, len(bchan["list"])):
        actual = bchan["list"][x]
        content = "prev: " + bchan["bchain"][actual]["prev"] + "\n actual: " + bchan["list"][x] + "\nnext: " + \
                  bchan["bchain"][actual]["next"]
        if (f[x] == bchan["list"][x]) and flag:
            imagen.node(name=bchan["list"][x], label=content, shape="box", color ="blue")
            imagen.edge(actual, bchan["bchain"][actual]["next"],arrowhead="vee")
            imagen.edge(actual ,bchan["bchain"][actual]["prev"],arrowhead = "vee")

        else:
            flag = False
            imagen.node(name=bchan["list"][x], label=content, shape="box", color="crimson")
            imagen.edge(actual, bchan["bchain"][actual]["next"], arrowhead="vee")
            imagen.edge(actual, bchan["bchain"][actual]["prev"], arrowhead="vee")
    imagen.render(view=True)


def initCheck():
    if not os.path.exists('blockchain'):
        os.makedirs('blockchain')

def read(path: str) -> dict:
    with open(path) as file:
        return json.load(file)

# Write a JSON file
def write(path: str, data: dict):
    with open(path, 'w') as file:
        json.dump(data, file)


def md(pieza):
    """crea los id de las tuplas con un hash"""
    try:
        r = hashlib.md5(pieza)
        return str(r.hexdigest())
    except:
        return None

def _toHash(data):
    """convierte las tuplas a hash"""
    if type(data) is str:
        return md(data.encode())
    l = ""
    for x in data:
        l = l + str(x)
    return md(l.encode())