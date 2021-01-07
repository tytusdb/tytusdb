import pickle

class binario():

	def commit(objeto,nombre): #guarda la estructura en memoria
		file = open("data/"+nombre+".bin","wb+") #abrir en forma binario o escribir forma binaria
		file.write(pickle.dumps(objeto))
		file.close()

	def rollback(nombre): #sai queremos obtener lo de antes, leer el archivo y tira el objeto deserealizado
		file = open("data/"+nombre+".bin","rb") #
		b = file.read()
		file.close()
		return pickle.loads(b)
