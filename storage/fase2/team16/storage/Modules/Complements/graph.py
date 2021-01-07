# Storage Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


import os


def generate(name: str, data: str):
    if not os.path.exists('./_tmp_'):
        os.makedirs('./_tmp_')
    old = name
    name = './_tmp_/' + name
    f = open(name + ".dot", "w")
    f.write(data)
    f.close()
    os.system("dot -Tsvg " + name + ".dot -o " + './_tmp_/' + old + ".svg")
    os.system('_tmp_\\' + old + ".svg")
