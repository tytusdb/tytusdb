# Package:      C3D Gen
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Team 01

import os 
import json

path = 'c3d/'
#dataPath = path + 'databases'
   
##################
# Databases CRUD #
##################

# CREATE a database checking their existence
def createDatabaseC3D(database: str) -> int:
    try:
        if not database.isidentifier():
            raise Exception()
        ilabel = 0 
        f = open("./c3d/codigo3Dgenerado.py", "w")
        f.write("from sentencias import *\n")
        f.write("from goto import with_goto\n")
        f.write("@with_goto  # Decorador necesario.\n")
        f.write("\n")
        f.write("def main():\n")
        f.write("   t" + str(ilabel) + "='" + database + "'\n")
        ilabel += 1
        f.write("   t" + str(ilabel) + "= createDB(" + "t" + str(ilabel-1) + "" + ")\n")
        f.write("   \n")
        
        f.close()
        return 0
    except:
        return 1

 
###############
# Tables CRUD #
###############

# CREATE a table checking their existence
def createTableC3D(database: str, table: str, numberColumns: int) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() \
        or not isinstance(numberColumns, int):
            raise Exception()
        
        ilabel = 0 
        f = open("./c3d/codigo3Dgenerado.py", "a")
        f.write("\n")
        f.write("\n")
        f.write("\n")
        f.write("   t" + str(ilabel) + "='" + database + "'\n")
        ilabel += 1
        f.write("   t" + str(ilabel) + "='" + table + "'\n")
        ilabel += 1
        f.write("   t" + str(ilabel) + "=" + str(numberColumns) + "\n")
        ilabel += 1
        f.write("   t" + str(ilabel) + "= createTbl(" + "t" + str(ilabel-3) + ",t" + str(ilabel-2) + ",t" + str(ilabel-1)  + ")\n")
        f.write("   \n")
        f.write("   \n")
        f.write("main()\n")
        f.close()
        return 0
    except:
        return 1
