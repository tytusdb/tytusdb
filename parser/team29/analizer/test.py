from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

# from storage.storageManager import jsonMode as j
from analizer import grammar

s = """ 
    --SELECT padres.parent as p, padres.child from parents as padres;
    --SELECT name, phone, location from company, users;
    --SELECT 9+8!=8+9 or 8*8 != 64;
    SELECT 9+8!=8+9 and 8*8 = 64;
    --SHOW DATABASES;
    --USE DATABASE db1;
    --INSERT INTO company VALUES (2, "Pillofon", 3200);
    --USE DATABASE db5;
    --INSERT INTO company VALUES (2, "Microsoft", 8080);
    CREATE DATABASE estela;
"""

result = grammar.parse(s)

# j.hola()

print(result)
