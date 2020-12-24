import pickle

# Almacena el archivo que se tiene en memoria
def commit(obj_file, name):
    file = open(name+".bin","wb+")
    file.write(pickle.dumps(obj_file))
    file.close()

# Lee el archivo binario y lo obtenemos de-serializado
def rollback(name):
    file = open(name+".bin", "rb")
    b = file.read()
    file.close()
    return pickle.loads(b)