# -------------------------------
# Released under MIT License
# Copyright (c) 2020 TytusDb Team

import os
from storage import TytusStorage as h


def graphDSD(database: str):
    pat = "data/graph"
    try:
        os.mkdir(pat)
    except:
        pass

    try:

        list_node = []
        file = open("data/graph/_DSD.dot","w")
        file.write("digraph dibujo{\n")
        file.write("rankdir=LR;\nnode[shape=record];\n")
        tmp = h._database(database)
        if tmp:
            for j in h.showTables(database):
                node = j+'[shape=record label="' + j + '"];\n'
                list_node.append([j, node])

            for j in h.showTables(database):
                tmp = h._table(database, j)["foreign_keys"].extractTable()
                for k in tmp:
                    for l in list_node:
                        if k[1] == l[0]:
                            file.write(l[1])
                        elif k[2] == l[0]:
                            file.write(l[1])

            for j1 in h.showTables(database):
                tmp = h._table(database, j1)["foreign_keys"].extractTable()
                for k in tmp:
                    file.write(k[2] + "->"+ k[1] + '[color="blue"];\n')

            file.write("}")
            file.close()
            os.system('dot -Tpng data/graph/_DSD.dot -o data/graph/_DSD.png')
            os.remove("data/graph/_DSD.dot")
            path = os.getcwd()+"data\\graph\\_DSD.png"
            return path
    except:
        return None


def graphDF(database: str, table: str):
    pat = "data/graph"
    try:
        os.mkdir(pat)
    except:
        pass
    try:
        list_node = []
        list_node_PK = []
        file = open("data/graph/_DF.dot", "w")
        file.write("digraph dibujo{\n")
        file.write("rankdir=LR;\nnode[shape=record];\n")


        tmp = h._database(database)
        if tmp:
            tmp = h._table(database, table)
            if tmp:
                tmp = h._table(database,table)["unique_index"].extractTable()
                if tmp:
                    for k in tmp:
                        for l in k[2]:
                            list_node.append([str(l), 'UK_'+str(l)+'[shape=record label=" Unique |'+str(l)+'"];\n'])
                            file.write('UK_'+str(l)+'[shape=record label=" Unique |'+str(l)+'"];\n')

                tmp = h._table(database,table)["pk"]
                if tmp:
                    for k in tmp:
                        list_node_PK.append([str(k), 'PK_'+str(k)+'[shape=record label=" PK |'+str(k)+'"];\n'])
                        file.write('PK_'+str(k)+'[shape=record label=" PK |'+str(k)+'"];\n')


        '''
            LISTA AUXILIAR DE COLUMNAS QUE TIENE LA TABLA
        '''
        list_aux=[]
        for i in range(int(h._table(database, table)["columnas"])):
            list_aux.append(str(i))


        '''
            ELIMINAR LAS LLAVES UNICAS 
            DE LA LISTA DE COLUMNAS
        '''
        for i in list_node:
            for j in range(int(h._table(database, table)["columnas"])):
                if i[0] == str(j):
                    list_aux.remove(str(i[0]))

        '''
            ELIMINAR LAS LLAVES PRIMARIAS 
            DE LA LISTA DE COLUMNAS
        '''
        for i in list_node_PK:
            for j in list_aux:
                if i[0] == str(j):
                    list_aux.remove(str(i[0]))


        '''
            CREAR LAS RELACIONES DE LAS LLAVES UNICAS 
             CON LAS EL RESTO DE COLUMNAS
        '''
        for i in list_node:
            for k in list_aux:
                if i[0] != str(k):
                    file.write('UK_'+i[0] +"->"+ str(k)+';\n')

        '''
            CREAR LAS RELACIONES DE  LAS LLAVES 
            PRIMARIAS CON LAS EL RESTO DE COLUMNAS
        '''
        for i in list_node_PK:
            for k in list_aux:
                if i[0] != str(k):
                    file.write('PK_' + i[0] + "->" + str(k) + ';\n')

        file.write("}")
        file.close()
        os.system('dot -Tpng data/graph/_DF.dot -o data/graph/_DF.png')
        os.remove("data/graph/_DF.dot")
        path = os.getcwd() + "data\\graph\\_DF.png"
        return path
    except:
        return None



