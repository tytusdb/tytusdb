# JSON Mode Test File
# Released under MIT License
# Copyright (c) 2020 TytusDb Team

from storageManager import jsonMode as j

# create db1 and db2, return two 0's and show return list
print(j.createDatabase("db1"))
print(j.createDatabase("db2"))
print(j.showDatabases())

# try create db1 and db2, return error value 2 and show return list
print(j.createDatabase("db1"))
print(j.createDatabase("db2"))
print(j.showDatabases())

# rename db1 to db3, return 0 and show return list
print(j.alterDatabase("db1","db3"))
print(j.showDatabases())

# rename db2 to db1, return 0 and show return list
print(j.alterDatabase("db2","db1"))
print(j.showDatabases())

# drop db3 and db1, return two 0's
print(j.dropDatabase("db3"))
print(j.dropDatabase("db1"))

# show empty-list of databases
print(j.showDatabases())

# again create db1 and db2, return two 0's and show return list of databases
print(j.createDatabase("db1"))
print(j.createDatabase("db2"))
print(j.showDatabases())

# create two table in db1 and show return tables list of db1 database
print(j.createTable("db1", "table1", 5))
print(j.createTable("db1", "table2", 8))
print(j.showTables("db1"))

# rename table1 to table 3 and show return tables list of db1 database
print(j.alterTable("db1", "table1","table3"))
print(j.showTables("db1"))

# drop table3 of db1 and show return tables list of db1 database
print(j.dropTable("db1", "table3"))
print(j.showTables("db1"))

# drop db1 with tables, first return 0 and second return None
print(j.dropDatabase("db1"))
print(j.showTables("db1"))
