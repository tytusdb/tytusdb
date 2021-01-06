# Storage Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16
import os

def draw(name:str, data:str):
    File = open(name + ".dot", "w")
    File.write(data)
    File.close()
    os.system("dot -Tpng " + name + ".dot -o " + name + ".png")
    os.system(name + ".png")