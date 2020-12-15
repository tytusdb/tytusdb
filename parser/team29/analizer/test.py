from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

# from storage.storageManager import jsonMode as j
from analizer import grammar

s = """ 
    --SELECT padres.parent as p, padres.child from parents as padres;
    --SELECT name, phone, location from company, users;
    SELECT pi();
"""

result = grammar.parse(s)

# j.hola()

print(result)
