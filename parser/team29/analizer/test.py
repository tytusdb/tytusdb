from sys import path
from os.path import dirname as dir
from shutil import rmtree

path.append(dir(path[0]))

from analizer import grammar

dropAll = 1
if dropAll:
    print("Eliminando registros")
    rmtree("data")


s = """ 
CREATE DATABASE IF NOT EXISTS test OWNER = 'root' MODE = 1;
USE test;
CREATE TABLE tbrolxusuario (
  idrol integer NOT NULL,
  idusuario integer NOT NULL
);
"""
result = grammar.parse(s)
print(result)
