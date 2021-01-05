# B+ Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team

import pickle
import os
import shutil
import sys

def Read(direction, name):
    max_rec = 0x1000000
    sys.setrecursionlimit(max_rec)
    sys.setrecursionlimit(max_rec)
    with open(direction+name+".bin","rb") as f:
        fil = pickle.load(f)
    return fil

def delete(direction):
    if os.path.isdir(direction):
        shutil.rmtree(direction)    

def write(direction, name, data):
    dire = direction+name
    os.mkdir(dire)
    max_rec = 0x10000
    sys.setrecursionlimit(max_rec)
    with open(dire+"/"+name+".bin","wb") as ff:
        pickle.dump(data, ff)

def update(direction, name, data):
    max_rec = 0x10000
    sys.setrecursionlimit(max_rec)
    with open(direction+"/"+name+".bin","wb") as ff:
        pickle.dump(data, ff)

def Rename(direction,oldDirection, NewDirection):
    os.rename(direction+oldDirection+"/"+oldDirection+".bin", direction+oldDirection+"/"+NewDirection+".bin")
    os.rename(direction+oldDirection, direction+NewDirection)
