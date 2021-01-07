import data.jsonMode as jm
import TypeCheck.Type_Checker as tp
from Errores.Nodo_Error import *

def evaluar(*args):
    res = list(jm.extractTable(args[0],args[1]))
# 0: db , 1: tb, 2:nameCol, 3:operador, 4: valor, 5: noCol, 6: noPK, 7: tipo select|delete
    if args[3] == '=':
        valores = []
        pks = []
        for n ,j in enumerate(res) :
            if args[4] == j[args[5]]:
                valores.append(j)
                pks.append(j[args[6]])
        if args[7] == 'delete':
            print(pks)
            return pks 
        elif args[7] == 'select':
            return valores
    elif args[3] == '>':
        valores = []
        pks = []
        for n ,j in enumerate(res) :
            if args[4] < j[args[5]]:
                valores.append(j)
                pks.append(j[args[6]])
        if args[7] == 'delete':
            return pks 
        elif args[7] == 'select':
            return valores
    elif args[3] == '<':
        valores = []
        pks = []
        for n ,j in enumerate(res) :
            if args[4] > j[args[5]]:
                valores.append(j)
                pks.append(j[args[6]])
        if args[7] == 'delete':
            return pks 
        elif args[7] == 'select':
            return valores
    elif args[3] == '<=':
        valores = []
        pks = []
        for n ,j in enumerate(res) :
            if args[4] >= j[args[5]]:
                valores.append(j)
                pks.append(j[args[6]])
        if args[7] == 'delete':
            return pks 
        elif args[7] == 'select':
            return valores
    elif args[3] == '<=':
        valores = []
        pks = []
        for n ,j in enumerate(res) :
            if args[4] <= j[args[5]]:
                valores.append(j)
                pks.append(j[args[6]])
        if args[7] == 'delete':
            return pks 
        elif args[7] == 'select':
            return valores
    elif args[3] == '!=':
        valores = []
        pks = []
        for n ,j in enumerate(res) :
            if args[4] != j[args[5]]:
                valores.append(j)
                pks.append(j[args[6]])
        if args[7] == 'delete':
            return pks 
        elif args[7] == 'select':
            return valores
    else: 
        return 'error'



