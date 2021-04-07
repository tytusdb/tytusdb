#-----------lista bloque
import os
from Block import Block
import hashlib

class Nodo:
    def __init__(self, idBloque, hash_anterior,data,hash_id):
        self.idBloque = idBloque
        self.data = data
        self.hash_anterior = hash_anterior
        self.hash_id = hash_id
        self.siguiente = None
        self.anterior = None
        self.hash_N = None

class BlockChain:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    #Método que verifica si la lista esta vacía
    def listaVacia(self):
        if self.primero is None:
            return True
        else:
            return False

    #Método agregar MÉTODO FUNCIONAL PARA ENVIAR
    def agregarLista(self,data,hash_id):
        if self.listaVacia() is True:
            self.id_block = 0
            hash_ant = 0
            nuevoNodo = Nodo(self.id_block, hash_ant,data,hash_id)
            self.primero = nuevoNodo
            self.ultimo = nuevoNodo
            self.primero.hash_N = self.primero.hash_id
        else:
            self.id_block += 1
            hash = self.ultimo.hash_id
            nuevoNodo = Nodo(self.id_block, hash, data,hash_id)
            self.ultimo.siguiente = nuevoNodo
            nuevoNodo.anterior = self.ultimo
            self.ultimo = nuevoNodo
            self.ultimo.hash_N = self.ultimo.hash_id

    #buscar para agregar y modificar
    def buscarModificar(self, dato):
        actual = self.primero
        encontrado = False
        if self.primero != None:
            while actual != None and encontrado != True:
                if actual.data == dato:
                    encontrado = True
                    return 2
                actual = actual.siguiente
            if not encontrado:
                return 0
        else:    
            return 1  

    #Método Modificar MÉTODO FUNCIONAL PARA ENVIAR
    def modificarNodo(self, bloque, new_data):
        try:
            actual = self.primero
            encontrado = False
            if self.primero != None:
                while actual != None and encontrado != True:
                    if actual.idBloque == bloque:
                        encontrado = True
                        actual.data = new_data
                        actual.hash_id = hashlib.sha256(str(actual.data).encode()).hexdigest()
                    actual = actual.siguiente
                if not encontrado:
                    return 2
            else:
                return 1
        except:
            return 1

    #Método imprimir MÉTODO FUNCIONAL PARA ENVIAR
    def imprimir(self):
        lista = []
        tmp = self.primero
        while tmp != None:
            lista.append([tmp.idBloque, tmp.hash_anterior,tmp.data,tmp.hash_id])
            tmp = tmp.siguiente
        return lista

    #MÉTODO GRAFICAR SIN LIBRERIAS DE GRAPHVIZ
    def GraficarConArchivo(self):
        f = open("blockchain.dot", "w")
        f.write("digraph g {\n")
        f.write("subgraph cluster1 {\n")
        #f.write("node [shape = record,style =\"rounded,filled\"fillcolor=\"orange:red\", width=1, height=0.4];\n")     
        f.write("node[shape = record, style=\"rounded,filled\",color=\"blue\", fillcolor=\"orange:red\"];\n") 
        f.write("rankdir=LR;\n")
        #validando el hash con el hash siguiente
        aux = self.primero
        while aux != None:
            #if aux.hash_id != aux.siguiente.hash_anterior:
            if aux.hash_id != aux.hash_N:
                print("cadena modificada")
                temp = aux
                f.write(str(temp.idBloque)+ "[label =\""+"{"+"Bloque: "+str(temp.idBloque)+"|"+"Hash Ant: "+str(temp.hash_anterior)+"|"+"Data: "+str(temp.data)+"|"+"Hash: "+str(temp.hash_id)+"}"+"\""+","+ "color =white"+","+" fillcolor=\"green:green\"];\n")
            else:
                temp = self.primero
                while temp != None:
                    f.write(str(temp.idBloque)+ "[label =\""+"{"+"Bloque: "+str(temp.idBloque)+"|"+"Hash Ant: "+str(temp.hash_anterior)+"|"+"Data: "+str(temp.data)+"|"+"Hash: "+str(temp.hash_id)+"}"+"\"];\n")
                    temp = temp.siguiente
            aux = aux.siguiente
        var = self.ultimo
        if var.siguiente is None and var.hash_id != var.hash_N:
            print("cadena modificada")
            temp = var
            f.write(str(temp.idBloque)+ "[label =\""+"{"+"Bloque: "+str(temp.idBloque)+"|"+"Hash Ant: "+str(temp.hash_anterior)+"|"+"Data: "+str(temp.data)+"|"+"Hash: "+str(temp.hash_id)+"}"+"\""+","+ "color =white"+","+" fillcolor=\"green:green\"];\n") 
            var = var.siguiente
        tmp = self.primero
        while tmp.siguiente != None:
            f.write(str(tmp.idBloque)+"->"+str(tmp.siguiente.idBloque)+";\n")
            tmp = tmp.siguiente
        f.write("label = Blockchain\n")
        f.write("color = blue")
        f.write("}\n")
        f.write("}")
        f.close()
        os.system("dot -Tjpg BlockChain.dot -o BlockChain.jpg")
        os.system("BlockChain.jpg")

    #Archivo Json
    def archivo_json(self):
        tmp = self.primero
        file = open("BlockChain.json", "w+")
        file.write("{\n")
        file.write("\t"+"\"""Blockchain""\""+":"+"[\n")
        
        while tmp != None:
            file.write("\t\t{\n")
            file.write("\t\t\t"+"\"""Bloque""\""+":"+str(tmp.idBloque)+",\n")
            file.write("\t\t\t"+"\"""Hash Anterior""\""+":"+"\""+str(tmp.hash_anterior)+"\""+",\n")
            file.write("\t\t\t"+"\"""Data""\""+":"+"\""+str(tmp.data)+"\""+",\n")
            file.write("\t\t\t"+"\"""Hash""\""+":"+"\""+str(tmp.hash_id)+"\""+"\n")
            if tmp == self.ultimo:
                file.write("\t\t}"+"\n")
            else:
                file.write("\t\t}"+",\n")
            tmp = tmp.siguiente
        file.write("\t"+"]\n")
        file.write("}")
        file.close()
    
    def abrirImagen(self):
        os.system("BlockChain.jpg")