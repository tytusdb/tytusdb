from Tytus import Tytus

tytus = Tytus()

tytus.createDatabase("db1")
tytus.createDatabase("db2")
tytus.createDatabase("db3")

tytus.createTable("db1", "profesores", 3)
tytus.createTable("db1", "estudiantes", 2)
tytus.createTable("db2", "cursos", 3)

tytus.alterAddPK("db1", "profesores", [0])

tytus.insert("db1", "profesores", [1, "Jose", "0174"])
tytus.insert("db1", "profesores", [2, "María", "0107"])
tytus.insert("db1", "profesores", [3, "Josefina", "0103"])
tytus.insert("db1", "profesores", [4, "Mario", "0107"])
tytus.insert("db1", "profesores", [5, "Daniel", "0105"])
tytus.insert("db1", "profesores", [6, "segio", "0159"])

#tytus.insert("db2", "cursos", [1, "MATE", "0107"])
#tytus.insert("db2", "cursos", [2, "DANU", "0105"])
#tytus.insert("db2", "cursos", [3, "FESU", "0159"])

print(tytus.showDatabases())
print(tytus.showTables("db1"))
print(tytus.showTables("db2"))
print(tytus.showTables("db4"))

tytus.extractTable("db1","profesores")
#tytus.extractTable("db1","cursos")


tytus.extractTable("db2","cursos")

tytus.extractRangeTable("db1","profesores",2,4)
