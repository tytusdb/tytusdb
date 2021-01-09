# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Andree Avalos
import pickle
import threading
import os 

path = './Data/dict/'
if not os.path.isdir("./Data/dict"):
    os.mkdir("./Data/dict")

def commit(objeto, nombre):
    try:
        file = open(path+nombre+".bin","wb+")
        file.write(pickle.dumps(objeto))
        file.close()
    except:
        ''
    

def rollback(nombre):
    try:
        file = open(path+nombre+".bin", "rb")
        b = file.read()
        file.close()
        return pickle.loads(b)
    except:
        return {}

def hacerCommit(objeto, nombre):
    h1 = threading.Thread(target=commit, args=(objeto, nombre), daemon= True)
    h1.start()