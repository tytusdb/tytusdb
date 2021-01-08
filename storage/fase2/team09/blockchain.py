import json
import hahslib
import os

def writeBlockChain(db, table, data):
    """escribe el blockchain"""
    initCheck()
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
    """muestra el grafo"""
    initCheck()
    name = db + "_" + table
    bchan = read("blockchain\\"+name+".json")
    f = list(map(_toHash, data))
    flag = True
    for x in range(0, len(bchan["list"])):
        if (f[x] == bchan["list"][x]) and flag:
            pass
        else:
            flag = False


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
    if type(data) is str:
        return md(data.encode())
    l = ""
    for x in data:
        l = l + str(x)
    return md(l.encode())