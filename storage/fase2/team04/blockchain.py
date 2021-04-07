import os
import json

class blockchain:
    def __init__(self,name):
        self.name = name	
    #{"key":35,"checksum":ask2k3jasa,"valid":True}
    #{'blocks': [{'key': 35, 'checksum': 'ask2k3jasa', 'valid': True}, {'key': 23, 'checksum': 'ask2k3jasa', 'valid': True}]}

    #Crea un nuevo bloque en la blockchain. Los nuevos bloques siempre se generan con True como valor por defecto para la propiedad valid.
    # Parámetros:
    #     key La clave que se usará como identificador para el bloque.
    #     checksum El checksum calculado para el bloque.
    # Valores de retorno:
    #     0 El bloque fue creado exitosamente.
    #     1 Ocurrió un problema durante la creación del bloque.
    def new_block(self,key,checksum):
        try:
            if os.path.isdir(os.getcwd() + "\\DataJsonBC"):#existe el directorio

                #verificar si existe el archivo
                if os.path.isfile(os.getcwd() + "\\DataJsonBC\\" + self.name + ".json"):
                    with open(os.getcwd() + "\\DataJsonBC\\" + self.name + ".json","r") as f:
                        data = f.read()
                    dic = json.loads(data) #convierto a diccionario
                    g = {"key":key,"checksum":checksum,"valid":True} #genero dic
                    dic["blocks"].append(g) #inserto en diccionario 
                    dicJson = json.dumps(dic) #archivo json

                    with open(os.getcwd() + "\\DataJsonBC\\" + self.name + ".json","w+") as f2:
                        f2.write(dicJson)
                    return 0 #creado exito

                else:
                    dic =  {'blocks':[{"key":key,"checksum":checksum,"valid":True}]}# genero diccionario
                    dicJson = json.dumps(dic)# archivo json
                    with open(os.getcwd() + "\\DataJsonBC\\" + self.name + ".json","w") as f2:
                        f2.write(dicJson)
                    return 0 #creado primer registro

            else:#no existe Directorio
                os.mkdir(os.getcwd() + "\\DataJsonBC")
                dic =  {'blocks':[{"key":key,"checksum":checksum,"valid":True}]}# genero diccionario
                dicJson = json.dumps(dic)# archivo json
                with open(os.getcwd() + "\\DataJsonBC\\" + nombre + ".json","w") as f:
                    f.write(dicJson)
                return 0 #creo primer registro
        except:
            return 1#error

    # Devuelve el bloque cuya key coincida con la indicada.
    # Parámetros:
    # 	key El identificador del bloque que se desea obtener.
    # Valores de retorno:`
    # 	None En caso de que no se encuentre ningún bloque con el identificador indicado.
    #	dict Un diccionario con la información del bloque, la estructura del diccionario debe ser la siguiente:
    def get_block(self,key):
        try:
            if os.path.isdir(".\\DataJsonBC"):
                if os.path.isfile(".\\DataJsonBC\\" + self.name + ".json"):
                    with open(".\\DataJsonBC\\" + self.name + ".json") as bc:
                        data = bc.read()
                    blocks = json.loads(data)["blocks"]
                    for block in blocks:
                        if block["key"] == key:
                            return block
            return None
        except:
            return None

    #Actualiza la información de un bloque determinado.
    # Parámetros:
    # 	key El identificador del bloque que se desea actualizar.
    #   checksum El nuevo checksum del bloque.
    #   valid El nuevo estado de validez del bloque.
    # Valores de retorno:
    # 	0 El bloque se actualizó exitosamente.
    #   1 Ocurrió un problema durante la actualización del bloque.
    def update_block(self, key, checksum, valid):
        try:
            if os.path.isdir(".\\DataJsonBC"):
                if os.path.isfile(".\\DataJsonBC\\" + self.name + ".json"):
                    with open(".\\DataJsonBC\\" + self.name + ".json") as bc:
                        data = bc.read()
                    blockchain_data = json.loads(data)
                    for block in blockchain_data["blocks"]:
                        if block["key"] == key:
                            block["checksum"] = checksum
                            block["valid"] = valid
                            with open(".\\DataJsonBC\\" + self.name + ".json", "w") as bc:
                                bc.write(json.dumps(blockchain_data))
                            return 0
            return 1
        except:
            return 1

    #Rompe la blockchain a partir del bloque indicado. Define la propiedad valid como False para el bloque indicado y todos los bloques posteriores.
    # Parámetros:
    # 	key El identificador del bloque.
    # Valores de retorno:
    # 	0 La blockchain se rompió exitosamente.
    # 	1 Ocurrió un problema durante la ruptura de la blockchain.
    def break_blockchain(self,key):
        try:
            if os.path.isdir(os.getcwd() + "\\DataJsonBC"):#existe el directorio

                #verificar si existe el archivo
                if os.path.isfile(os.getcwd() + "\\DataJsonBC\\" + self.name + ".json"):
                    with open(os.getcwd() + "\\DataJsonBC\\" + self.name + ".json","r") as f:
                        data = f.read()
                    dic = json.loads(data)["blocks"] #obtengo lista
                    desvorde = False
                    for reg in dic:
                        if reg["key"] == key:
                            desvorde = True

                        if desvorde:
                            reg["valid"] = False

                    dicJson = json.dumps(dic)
                    with open(os.getcwd() + "\\DataJsonBC\\" + self.name + ".json","w+") as f2:
                        f2.write(dicJson)
                    return 0 #

                else:
                    return 1
        except:
            return 1
    def graficar(self):
        pass
