import pickle
import os
import shutil

def Read(direction, name):
    with open(direction+name+".bin","rb") as f:
        fil = pickle.load(f)
        f.close()
    return fil

def delete(direction):
    if os.path.isdir(direction):
        shutil.rmtree(direction)    

def write(direction, name, data):
    dire = direction+name
    os.mkdir(dire)
    with open(dire+"/"+name+".bin","wb") as ff:
        pickle.dump(data, ff)
        ff.close()

def update(direction, name, data):
    with open(direction+name+".bin","wb") as ff:
        pickle.dump(data, ff)
        ff.close()

def Rename(direction,oldDirection, NewDirection):
    os.rename(direction+oldDirection+"/"+oldDirection+".bin", direction+oldDirection+"/"+NewDirection+".bin")
    os.rename(direction+oldDirection, direction+NewDirection)
