# JSON Mode Test File
# Released under MIT License
# Copyright (c) 2020 TytusDb Team

from storageManager import jsonMode as j
import pandas as pd
from datetime import *

# drop all databases if exists

# create database
j.createDatabase('BD1')

# create tables
j.createTable('BD1', 'personas', 5)
j.createTable('BD1', 'pais',    4)
j.createTable('BD1', 'idiomas', 4)

# create simple primary keys
j.alterAddPK('BD1', 'personas', [0])
j.alterAddPK('BD1', 'pais',    [0])
j.alterAddPK('BD1', 'idiomas', [0])

# insert data in countries
j.insert('BD1', 'pais', ['GTM', 'Guatemala',  'Central America', 108889])
j.insert('BD1', 'pais', ['MX', 'Mexico', 'Norte America',  21041])  
j.insert('BD1', 'pais', ['EEUU', 'Estados Unidos', 'Norte America',  21041]) 

# insert data in cities
j.insert('BD1', 'personas', [1, 'Jossie',    'Castrillo','27',    'GTM'])
j.insert('BD1', 'personas', [2, 'Juanpi',    'Garcia','27',    'GTM'])
j.insert('BD1', 'personas', [3, 'Byron',    'Cermeno','27',    'GTM'])
j.insert('BD1', 'personas', [4, 'Hayrton',    'Ixpata','27',    'GTM'])
j.insert('BD1', 'personas', [5, 'Dulce',    'DeLeon','25',    'MX'])
j.insert('BD1', 'personas', [6, 'Miguel',    'Basir','26',    'GTM'])
j.insert('BD1', 'personas', [7, 'Nose',    'Algo','30',    'EEUU'])
         
# inser data in languages
j.insert('BD1', 'idiomas', ['GTM', 'Espanol', 'official',  64.7])
j.insert('BD1', 'idiomas', ['EEUU', 'Espanol', 'official', 100.0])
j.insert('BD1', 'idiomas', ['MX', 'Espanol', 'official', 100.0])

# show all data
#j.showCollection()
a=j.extractTable("BD1", "personas")

horaActual= datetime.now().strftime("%H:%M:%S")
print(horaActual)

