from sys import path
from os.path import dirname as dir
from shutil import rmtree

path.append(dir(path[0]))

from analizer import grammar
from analizer.reports import BnfGrammar

dropAll = 0
if dropAll:
    print("Eliminando registros")
    rmtree("data")


s = """ 

CREATE OR REPLACE DATABASE db1;
USE db1;
CREATE TABLE cities (
 id integer primary key,
 Fecha date 
);

CREATE TABLE country (
 id integer primary key,
 id2 integer check (id > 2),
 Foreign key (id2) references cities (id),
 Unique (id,id2)
);

Alter Table country DROP CONSTRAINT id2_UQ, DROP CONSTRAINT id2_ck, DROP CONSTRAINT id2_fk ;

Alter Table country ALTER COLUMN id SET DEFAULT 0;

ALTER TABLE country ADD COLUMN mood mood;

ALTER TABLE country RENAME COLUMN mood TO modosexo;
"""
result = grammar.parse(s)
print(result)

# BnfGrammar.grammarReport()
