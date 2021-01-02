# File:         JSON Mode Test File for EDD
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Luis Espino

from storageManager import jsonMode as j

# assume no data exist or execute the next drop function
j.dropAll()

# test Databases CRUD
print(j.createDatabase('db1'))      # 0 
print(j.createDatabase('db1'))      # 2
print(j.createDatabase('db4'))      # 0
print(j.createDatabase('db5'))      # 0
print(j.createDatabase(0))          # 1
print(j.alterDatabase('db5','db1')) # 3
print(j.alterDatabase('db5','db2')) # 0
print(j.dropDatabase('db4'))        # 0
print(j.showDatabases())            # ['db1','db2']

# test Tables CRUD
print(j.createTable('db1','tb4',3))     # 0
print(j.createTable('db1','tb4',3))     # 3
print(j.createTable('db1','tb1',3))     # 0
print(j.createTable('db1','tb2',3))     # 0
print(j.alterTable('db1','tb4','tb3'))  # 0
print(j.dropTable('db1','tb3'))         # 0
print(j.alterAddPK('db1','tb1',0))      # 1
print(j.alterAddPK('db1','tb1',[0]))    # 0
print(j.showTables('db1'))              # ['tb1', 'tb2']

# test Registers CRUD
print(j.insert('db1','tb1',[1,1]))              # 5
print(j.insert('db1','tb1',['1','line','one']))   # 0
print(j.loadCSV('tb1.csv','db1','tb1'))         # [0, 0, 0, 0, 0]
print(j.extractTable('db1','tb1'))          
# [['1', 'line', 'one'], ['2', 'line', 'two'],
#  ['3', 'line', 'three'], ['4', 'line', 'four'],
#  ['5', 'line', 'five'], ['6', 'line', 'six']]
