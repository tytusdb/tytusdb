from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion, IdId
from Compi2RepoAux.team21.Analisis_Ascendente.storageManager.jsonMode import *
import Compi2RepoAux.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.expresion import *
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Time import  Time

class Update(Instruccion):
    def __init__(self, id, asignaciones, where,fila,columna):
        self.id = id
        self.asignaciones = asignaciones
        self.where = where
        self.fila = fila
        self.columna = columna


    def ejecutar(updateinst, ts, consola, exceptions):

        #simular
        print('Update')

        print('add pk')
        alterAddPK('test', 'tabla1', [0])
        insert('test','tabla1',[1,'Daniel','Gonzalez', 24])
        insert('test','tabla1',[2,'Cindy','Lopez', 31])
        insert('test','tabla1',[3,'Isabel','Ochoa', 40])
        insert('test','tabla1',[4,'Andrea','Mendez', 15])



        lista = extractTable('test','tabla1')
        print(lista)

        if ts.validar_sim("usedatabase1234") == 1:
            bdactual = ts.buscar_sim("usedatabase1234") #devuelve el simbolo de usedatabase1234
            BD = ts.buscar_sim(bdactual.valor) #devuelve el nombre de la base de datos que esta en uso
            entornoBD = BD.Entorno #devuelve todo el entorno de la base de datos en uso, tabla de simbolos
            listaTablas = entornoBD.simbolos    #devuelve las tablas
            print(listaTablas)

            #indices de la posicion respecto a los campos de la tabla
            indices = []
            #id de la tabla
            tablaB = updateinst.id
            print('id: ' + tablaB)
            print(len(tablaB))
            #campos a actualizar
            lCampos =ListaCampos(updateinst.asignaciones)
            print(lCampos)
            #datos nuevos
            expr = []
            #campos y tipos de la tabla
            campos2 = []
            tipos = []
            indexPK = []
            if len(lCampos) != 0:
                expr = Asignaciones(updateinst.asignaciones, consola, ts, exceptions)
                for tabla in listaTablas:
                    if listaTablas.get(tabla).id == tablaB: #buscar la tabla
                        #listaTablas.get(tabla).categoria
                        print(listaTablas.get(tabla).id)
                        #listaTablas.get(tabla).tipo
                        #listaTablas.get(tabla).valor
                        entornoTabla = listaTablas.get(tabla).Entorno
                        campos = entornoTabla.simbolos
                        i = 0
                        for campo in campos:
                            #campos.get(campo).categoria
                            print(campos.get(campo).id)
                            tipos.append(campos.get(campo).tipo)
                            campos2.append(campos.get(campo).id)
                            for v in campos.get(campo).valor:
                                if v == 'PRIMARYKEY':
                                    indexPK.append(i)
                            i = i + 1
                print(indexPK)
                print(campos2)
                print(tipos)
                #indices
                indices = Indice(lCampos, campos2)
                print(indices)
                print(expr)
                if len(indices) == len(expr):
                    print('todo correcto')
                    #tienen que ser de la misma longitud
                    data = {}
                    i = 0
                    for ind in indices:
                        data[ind] = expr[i]
                        i = i + 1
                    print(data)
                    #data = {3: 30, 1: 'nom'}
                    #prueba
                    pk = []
                    pk.append(1)
                    print(extractTable(bdactual.valor, tablaB))

                    print(update(bdactual.valor, tablaB, data, pk))
                    # show all data
                    print(bdactual.valor)
                    print(extractTable(bdactual.valor, tablaB))

        else:
            consola.append("22005	error_in_assignment, No se ha seleccionado una BD\n")


def ListaCampos(asignaciones) -> list:
    campos = []
    for asign in asignaciones:
        if isinstance(asign, Expresion):
            if asign.operador == '=':
                if isinstance(asign.iz, Id):
                    if campos.count(asign.iz.id) == 0:
                        campos.append(asign.iz.id)
                    else:
                        print('error campos repetidos')
                        campos = []
                        return campos
                else:
                    print('error nombre campos')
                    campos = []
                    return campos
    return campos

def Indice(lCampos, campos2) -> list:
    indices = []
    for c1 in lCampos:
        idx = 0
        ban = False
        for c2 in campos2:
            if c1 == c2:
                indices.append(idx)
                ban = True

            if len(campos2) - 1 == idx:
                if ban == False:
                    print(c1)
                    print('el campo que desea modificar no existe en la tabla')
                    indices = []
                    return indices
            idx = idx + 1
    return indices

def Asignaciones(asignaciones, consola, ts, exceptios) -> list:
    print('asignaciones...')
    valores = []
    for asign in asignaciones:
        if isinstance(asign, Expresion):
            if asign.operador == '=':
                #iz debe ser Id o IdId
                #dr pasarlo a Expre
                valores.append(Expre(asign.dr, consola, ts, exceptios))

    return valores

def Expre(expre, consola, ts, exceptions):
    res = 0
    if isinstance(expre, Expresion):
        print('es expresion')
        res = Expresion.Resolver(expre, ts, consola, exceptions)
        print(str(res))
    elif isinstance(expre, Primitivo):
        res = expre.valor
        print('es primitivo ' + str(res))
    elif isinstance(expre, Id):
        print('es id error semantico')
        res = None
    elif isinstance(expre, Time):
        res = Time.resolverTime(expre)
    return res

def ValidacionTipos(valor, tipo):
    pass

def SinWhere(tabla, primaria) -> list:
    dev = []    #lista de listas con el valor que esta en la llave primaria
    for tupla in tabla:
        ll = []
        for c in tupla:
            pass
            ll.append(c)
        dev.append(ll)