# File:         JSON Mode Test File for EDD
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Luis Espino

from storageManager import jsonMode as j

# assume no data exist or execute the next optional drop function
j.dropAll()

# test Databases CRUD
print(j.createDatabase('b1'))       # 0 
print(j.createDatabase('b1'))       # 2
print(j.createDatabase('b4'))       # 0
print(j.createDatabase('b5'))       # 0
print(j.createDatabase(0))          # 1
print(j.alterDatabase('b5','b1'))   # 3
print(j.alterDatabase('b5','b2'))   # 0
print(j.dropDatabase('b4'))         # 0
print(j.showDatabases())            # ['b1','b2']


