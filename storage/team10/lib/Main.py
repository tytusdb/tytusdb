from Tytus import Tytus

tytus = Tytus()

tytus.createDatabase("db1")
tytus.createDatabase("db2")
tytus.createDatabase("db3")

tytus.createTable("db1", "profesores", 3)
tytus.createTable("db1", "estudiantes", 2)
tytus.createTable("db2", "cursos", 3)

tytus.alterAddPK("db1", "profesores", [0])

print(tytus.showDatabases())
print(tytus.showTables("db1"))
print(tytus.showTables("db2"))
print(tytus.showTables("db4"))

print("============Datos de Extract Table==============================")
try:
    for i in tytus.extractTable("db1","profesores"):
        print(i)
except:
    print("None")

print("============Datos de Extract Range Table==============================")
try:
    c=0
    for i in tytus.extractRangeTable("db1","profesores",1,"Ta","o"):
        print(i)
        c+=1
    if c == 0:
        print("[ ]")    
except:
    print("None")
