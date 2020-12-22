from sys import path
from os.path import dirname as dir
from shutil import rmtree

path.append(dir(path[0]))

from analizer import grammar

dropAll = 0
if dropAll:
    print("Eliminando registros")
    rmtree("data")


s = """ 
CREATE OR REPLACE DATABASE db1;
USE db1;
CREATE TABLE cities (
 name text,
 fecha date
);

insert into cities values ('Estela','2020-12-21');

"""
result = grammar.parse(s)
print(result)
