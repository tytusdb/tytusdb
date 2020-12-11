from Hash import TablaHash

t = TablaHash(10, "db1", "table1", 3)

t.insertarDato(["1", "Carlos", "25"])
t.insertarDato(["23", "Mario", "33"])
t.insertarDato(["34", "Daniel", "49"])
t.insertarDato(["45", "David", "20"])
t.insertarDato(["58", "Luis", "48"])
t.insertarDato(["67", "Rodrigo", "25"])
t.insertarDato(["70", "Alberto", "35"])

t.printTbl()

print(f"Valor encontrado: {t.buscar('45')}")
