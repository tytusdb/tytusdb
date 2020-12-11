import time
from Hash import TablaHash

t = TablaHash(100000)

# t0 = time.time()
for item in range(0, 100000):
    t.insertarDato(item)
# t1 = time.time()

# t.insertarDato(33)
# t.insertarDato(21)
# t.insertarDato(10)
# t.insertarDato(12)
# t.insertarDato(14)
# t.insertarDato(56)
# t.insertarDato(100)

# t.printTbl()

t0 = time.time()
t.buscar(99999)
t1 = time.time()
print(t1 - t0)

"""print(20%7)
print(33%7)
print(21%7)
print(10%7)
print(12%7)
print(14%7)
print(56%7)
print(100%7)
"""