import pickle

##serializacion
def serialize(filename, data):
    objetos=data
    nombre_archivo=filename
    
    #creacion del archivo
    archivo_dat=open(nombre_archivo,'wb')
    pickle.dump(objetos,archivo_dat)
    archivo_dat.close()
    del archivo_dat

def deserialize(filename):
    archivo_dat=open(filename,'rb')
    recover_data={}
    recover_data=pickle.load(archivo_dat)
    archivo_dat.close()
    
    #print("recover data:",recover_data)
    return recover_data
##fin serializacion
