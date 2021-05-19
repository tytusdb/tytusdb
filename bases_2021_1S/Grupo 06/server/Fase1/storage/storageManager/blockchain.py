import json 
from Fase1.storage.storageManager import sha256 as sha
import os

class bloque:
    def __init__(self, numero, data, anterior, hashid, estructura):
        self.id = numero
        self.data = data
        self.anterior = anterior
        self.hash = hashid
        self.estructura = estructura

    def get(self):
        return {"id":self.id, "content":self.data, "previous":self.anterior, "hash":self.hash, "Estructure": self.estructura}

class blockchain:
    def __init__(self):
        self.anterior = '0000000000000000000000000000000000000000000000000000000000000000'

    def crear(self, database, table):
        file = open("./Data/security/"+database+"_"+table+".json", "w+", encoding='utf-8')
        file.write(json.dumps('', indent=4))
        file.close()

    def insertar(self, tablas, database, table):
        file = open("./Data/security/"+database+"_"+table+".json", "r")
        lista = json.loads(file.read())
        file.close()
        if type(lista)!=list:
            lista = []
        else:
            self.anterior = lista[-1]['hash']
        key = len(lista)
        key+=1
        val = []
        
        for x in list(tablas.values()):
            if type(x) == type(b''):
                x = x.decode()
            val.append(x)
        values = ",".join(str(x) for x in val)
        id_hash = sha.generate(values)
        nuevo = bloque(key, tablas, self.anterior, id_hash, 'correcta')
        lista.append(nuevo.get())
        file = open("./Data/security/"+database+"_"+table+".json", "w+", encoding='utf-8')
        file.write(json.dumps([j for j in lista], indent=4))
        self.anterior = id_hash

    def insert(self, data: list, database: str, table: str):
        dic = {}
        y=1
        for x in data:
            if type(x) == type(b''):
                x = x.decode()
            dic.update({y:x})
            y+=1
        self.insertar(dic, database, table)

    def update(self, tabla, registro, database, table, h2):
        file = open("./Data/security/"+database+"_"+table+".json", "r")
        lista = json.loads(file.read())
        file.close()
        for bloque in lista:
            if registro == bloque["hash"]:
                bloque["content"] = tabla
                bloque["hash"] = h2
                if registro != h2:
                    bloque["Estructure"] = 'incorrecta'
                    break
        file = open("./Data/security/"+database+"_"+table+".json", "w+", encoding='utf-8')
        file.write(json.dumps([j for j in lista], indent=4))
        file.close()
        # self.graficar(database, table)
    
    def dropAddColumn(self, row1, row2, database, table):
        ldata = ",".join(str(x) for x in row1)
        lnewData = ",".join(str(x) for x in row2)
        h1 = sha.generate(ldata)
        h2 = sha.generate(lnewData)
        dic = {}
        y=1
        for x in row2:
            dic.update({y:x})
            y+=1
        self.update(dic, h1, database, table, h2)

    def delete(self, registro, database, table):
        file = open("./Data/security/"+database+"_"+table+".json", "r")
        lista = json.loads(file.read())
        file.close()
        anterior = None
        i=0
        for bloque in lista:
            if registro == bloque["hash"]:
                if anterior:
                    if i!=len(lista)-1:
                        siguiente = lista[i+1]
                        if anterior["hash"]!= siguiente["previous"]:
                            siguiente["Estructure"]='incorrecta'
                else:
                    if len(lista):
                        di = lista[i+1]
                        di["Estructure"]='incorrecta'
                lista.remove(bloque)
            anterior = bloque
            i+=1

        file = open("./Data/security/"+database+"_"+table+".json", "w+", encoding='utf-8')
        file.write(json.dumps([j for j in lista], indent=4))
        file.close()
        # self.graficar(database, table)

    def CompararHash(self, data:list, newData: list, database, table):
        ldata = ",".join(str(x) for x in data)
        lnewData = ",".join(str(x) for x in newData)
        h1 = sha.generate(ldata)
        h2 = sha.generate(lnewData)
        dic = {}
        y=1
        for x in newData:
            dic.update({y:x})
            y+=1
        self.update(dic, h1, database, table, h2)
        if h1 == h2:
            return 0
        return 6
    
    def EliminarHash(self, registro, database, table):
        row = ",".join(str(x) for x in registro)
        h1 = sha.generate(row)
        self.delete(h1, database, table)
    
    def graficar(self, database, table):
        file = open("./Data/security/"+database+"_"+table+".json", "r")
        lista = json.loads(file.read())
        file.close()
        if type(lista)!=list:
            lista = []
        if type(lista)==list:
            f= open('./Data/security/'+database+'_'+table+'.dot', 'w',encoding='utf-8')
            f.write("digraph dibujo{\n")
            f.write('graph [ordering="out"];')
            f.write('rankdir=TB;\n')
            f.write('node [shape = box];\n')
            data =""
            t=0
            color = 'white'
            for x in lista:
                if x['Estructure']=='incorrecta':
                    color = 'orangered'
                nombre = 'Nodo'+str(t)
                data = ''
                for y in list(x.values()):
                    if type(y) == dict:
                        d = ",".join(str(x) for x in list(y.values()))
                        data+="""<tr><td>"""+d+"""</td></tr>"""
                    else:
                        if str(y)!='correcta' and str(y)!='incorrecta':
                            data+="""<tr><td>"""+str(y)+"""</td></tr>"""
                tabla ="""<<table BGCOLOR='"""+color+"""' cellspacing='0' cellpadding='20' border='0' cellborder='1'>
                    """+data+"""        
                </table> >"""
                f.write(nombre+' [label = '+tabla+',  fontsize="30", shape = plaintext ];\n')
                t+=1
            f.write('}')
            f.close()
            os.system('dot -Tpng ./Data/security/'+database+'_'+table+'.dot -o tupla.png')
        
    def fail(self, database, table):
        file = open("./Data/security/"+database+"_"+table+".json", "r")
        lista = json.loads(file.read())
        file.close()
        if type(lista)!=list:
            lista = []
        for x in lista:
            if x['Estructure']=='incorrecta':
                return True
        return False

    
    def activo(self, database, table):
        if os.path.isfile("./Data/security/"+database+"_"+table+".json"):
            return True
        return False