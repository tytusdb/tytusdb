from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion, IdId
from tytus.parser.fase2.team21.Analisis_Ascendente.storageManager.jsonMode import *
import tytus.parser.fase2.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.expresion import *
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Time import  Time
import re

class Update(Instruccion):
    def __init__(self, id, asignaciones, where,concatena,fila,columna):
        self.id = id
        self.asignaciones = asignaciones
        self.where = where
        self.concatena = concatena
        self.fila = fila
        self.columna = columna


    def ejecutar(updateinst, ts, consola, exceptions):

        #simular
        print('Update')

        #print('add pk')
        ##alterAddPK('test', 'tabla1', [1])       ##
        #insert('test','tabla1',['Daniel',1,'Gonzalez', 24])
        #insert('test','tabla1',['Cindy', 2,'Lopez', 15])
        #insert('test','tabla1',['Isabel',3,'Ochoa', 40])
        #insert('test','tabla1',['Andrea',4,'Mendez', 15])
        #insert('test','tabla1',['Maria',5,'Mendez', 15])



        #lista = extractTable('test','tabla1')
        #print(lista)

        if ts.validar_sim("usedatabase1234") == 1:
            bdactual = ts.buscar_sim("usedatabase1234") #devuelve el simbolo de usedatabase1234
            BD = ts.buscar_sim(bdactual.valor) #devuelve el nombre de la base de datos que esta en uso
            entornoBD = BD.Entorno #devuelve todo el entorno de la base de datos en uso, tabla de simbolos
            listaTablas = entornoBD.simbolos    #devuelve las tablas
            #print(listaTablas)

            #indices de la posicion respecto a los campos de la tabla
            indices = []
            #id de la tabla
            tablaB = updateinst.id
            #print('id: ' + tablaB)
            #print(len(tablaB))
            #campos a actualizar
            lCampos =ListaCampos(updateinst.asignaciones, consola, exceptions, updateinst)
            #print(lCampos)
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
                        #print(listaTablas.get(tabla).id)
                        #listaTablas.get(tabla).tipo
                        #listaTablas.get(tabla).valor
                        entornoTabla = listaTablas.get(tabla).Entorno
                        campos = entornoTabla.simbolos
                        i = 0
                        for campo in campos:
                            #campos.get(campo).categoria
                            #print(campos.get(campo).id)
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
                indices = Indice(lCampos, campos2, consola, exceptions, updateinst)
                print(indices)
                print(expr)
                si = VTipo(expr, tipos, indices)
                if len(indices) == len(expr) and si:#si coinciden los tipos
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
                    #pk = []
                    #pk.append(1)
                    ##fin prueba
                    #si no tiene where
                    ta = extractTable(bdactual.valor, tablaB)
                    print(ta)

                    #prueba del where
                    if updateinst.where != None:
                        print('SI HAY WHERE')
                        ta = WhereUp(updateinst.where, ta, campos2, ts, consola, exceptions, updateinst)
                    else:
                        print('no hay WHERE')
                    primarias = ValorLLaves(ta, indexPK)
                    print('primarias')
                    print(primarias)
                    print(indexPK)
                    if primarias != None and len(indexPK) != 0:
                        bandera = 1
                        for p in primarias:
                            #pk = p
                            print(p)
                            bandera = update(bdactual.valor, tablaB, data, p)
                        if bandera == 0:
                            consola.append(f"Se actualizó la tabla {tablaB} exitosamente\n")
                        else:
                            #consola.append(f"La tabla {tablaB} no puede actualizarse")
                            exceptions.append(f"Error semantico-42601- 42601  	syntax_error-{updateinst.fila}-{updateinst.columna}")
                    else:
                        print('no se puede actualizar')
                    print(bdactual.valor)
                    print(extractTable(bdactual.valor, tablaB))


                elif not si:
                    consola.append(f"La tabla {tablaB} no puede actualizarse, tipos incorrectos\n")
                    exceptions.append(f"Error semantico-42P18- 42P18			indeterminate_datatype, tipos incorrectos -{updateinst.fila}-{updateinst.columna}")
                else:
                    consola.append(f"La tabla {tablaB} no puede actualizarse, campos incorrectos\n")
                    exceptions.append(f"Error semantico-42703- 42703		undefined_column, campos incorrectos -{updateinst.fila}-{updateinst.columna}")

        else:
                consola.append("22005	error_in_assignment, No se ha seleccionado una BD\n")

    def traducir(instr, ts, consola, exceptions,tv):
        info = ""
        #print("concatena \n")
        #print(instr.concatena)
        for data in instr.concatena:
            info += " " + data

        contador = tv.Temp()
        consola.append(f"\n\t{contador} = \"{info}\"")
        contador2 = tv.Temp()
        consola.append(f"\n\t{contador2} = T({contador})")
        consola.append(f"\n\tT1 = T3({contador2})")
        consola.append(f"\n\tstack.append(T1)\n")

def ListaCampos(asignaciones, consola, exceptions, updateinst) -> list:
    campos = []
    for asign in asignaciones:
        if isinstance(asign, Expresion):
            if asign.operador == '=':
                if isinstance(asign.iz, Id):
                    if campos.count(asign.iz.id) == 0:
                        campos.append(asign.iz.id)
                    else:
                        print('error campos repetidos')
                        consola.append(f"La tabla {updateinst.id} no puede actualizarse, campos repetidos\n")
                        exceptions.append(f"Error semantico-42701- 42701		duplicate_column, campos repetidos -{updateinst.fila}-{updateinst.columna}")
                        campos = []
                        return campos
                else:
                    print('error nombre campos')
                    consola.append(f"La tabla {updateinst.id} no puede actualizarse, campos incorrectos\n")
                    exceptions.append(f"Error semantico-42703- 42703	undefined_column, campos incorrectos -{updateinst.fila}-{updateinst.columna}")
                    campos = []
                    return campos
    return campos

def Indice(lCampos, campos2, consola, exceptions, updateinst) -> list:
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
                    consola.append(f"La tabla {updateinst.id} no puede actualizarse, campos incorrectos\n")
                    exceptions.append(f"Error semantico-42P01- 42P01	undefined_table, campos incorrectos -{updateinst.fila}-{updateinst.columna}")

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
    if isinstance(expre, Primitivo):
        res = expre.valor
        #print('es primitivo ' + str(res))
    elif isinstance(expre, Id):
        #print('es id error semantico')
        res = None
    elif isinstance(expre, Time):
        res = Time.resolverTime(expre)
    else:
        #print('es expresion')
        res = Expresion.Resolver(expre, ts, consola, exceptions)
        #print(str(res))
    return res

def VTipo(valores, tipos, indices) -> bool:
    if len(indices) != 0 and len(valores) != 0 and len(tipos) != 0:
        i = 0
        for valor in valores:
            bandera = ValidacionTipos(valor, tipos[indices[i]])
            if not bandera:
                return False
            i = i + 1
        return True
    return False

def ValidacionTipos(valor, tipo) -> bool:
    #print(valor, '   ', tipo)
    var = tipo.split('-')
    if var[0] == 'CHARACTER' or var[0] == 'VARCHAR' or var[0] == 'CHAR' or var[0] == 'CHARACTERVARYING':
        return Varchar(valor, var[1])
    #elif tipo == 'DATE':
    #    return TDate(valor)
    elif tipo == 'INTEGER' or tipo == 'BIGINT' or tipo == 'SMALLINT' or tipo == 'NUMERIC' or tipo == 'SERIAL':
        return Entero(valor)
    elif tipo == 'REAL' or tipo == 'DOUBLE':
        return Decimal(valor)
    elif var[0] == 'DECIMAL':
        return Decimal(valor)
    elif tipo == 'BOOLEAN':
        if valor == True or valor == False:
            return True
        else:
            return False
    elif tipo == 'MONEY':
        if Entero(valor) or Decimal(valor):
            return True
        else:
            return False
    elif tipo == 'TEXT' or tipo == 'TIMESTAMP' or tipo == 'DATE' or tipo == 'DATE' or tipo == 'INTERVAL' or tipo == 'DATE':
        if isinstance(valor, str):
            return True
        else:
            return False

def ValorLLaves(tabla, primaria) -> list:
    #print(primaria)
    dev = []    #lista de listas con el valor que esta en la llave primaria
    if tabla != None:
        for tupla in tabla:
            ll = []
            for p in primaria:
                ll.append(tupla[p])
            dev.append(ll)
    #print(dev)
    return dev

def TDate(valor) -> bool:
    if len(str(valor)) == 10:
        if (valor[4] == '.' and valor[7] == '.') or (valor[4] == '/' and valor[7] == '/'):
            return True
        else:
            return True
    else:
        return False

def Entero(valor) -> bool:
    try:
        int(valor)
        return True
    except:
        return False

def Decimal(valor) -> bool:
    try:
        float(valor)
        return True
    except:
        return False

def Varchar(valor, longitud) -> bool:
    #print(valor, ' - ', longitud)
    try:
        if isinstance(valor, str):
            if len(valor) <= int(longitud):
                #print('longitud correcta')
                return True
            else:
                return False
        else:
            return False
    except:
        return False


#where
def WhereUp(where, tabla, campos, ts, consola, exceptions, updateinst) -> list:
    if isinstance(where, Expresion):
        if isinstance(where.iz, Id):
            ix = 0 #el indice del campo a filtar
            bandera = False
            for c in campos:
                if c == where.iz.id:
                    print(str(ix), 'aqui esta el campo id')
                    bandera = True
                    break
                ix = ix + 1
            expre = Expresion.Resolver(where.dr, ts, consola, exceptions)
            if bandera:
                tf = Filtrar(tabla, ix, where.operador, expre)
                print('filtrado')
                print(tf)
                return tf
            else:
                print('el campo no existe')
                consola.append(f"La tabla {updateinst.id} no puede actualizarse, el campo no existe\n")
                exceptions.append(f"Error semantico-42703- 42703	undefined_column, el campo no existe -{updateinst.fila}-{updateinst.columna}")

                return []
        ##------------
        elif where.operador == 'or' or where.operador == 'and':
            tf1 = []
            tf2 = []
            if isinstance(where.iz, Expresion):
                tf1 = WhereUp(where.iz, tabla, campos, ts, consola, exceptions, updateinst)
                print('tf1')
                print(tf1)
            if isinstance(where.dr, Expresion):
                tf2 = WhereUp(where.dr, tabla, campos, ts, consola, exceptions, updateinst)
                print('tf2')
                print(tf2)
            if where.operador == 'and':
                tabla = AndManual(tf1, tf2)
                print('filtrado and')
                print(tabla)
                return tabla
            elif where.operador == 'or':
                if len(tf1) != 0 and len(tf2) != 0:
                    tabla = tf1 + tf2
                    print('filtrado or')
                    print(tabla)
                    return tabla
                else:
                    return []
        else:
            print('error el campo no existe')
            consola.append(f"La tabla {updateinst.id} no puede actualizarse, el campo no existe\n")
            exceptions.append(f"Error semantico-42703- 42703	undefined_column, el campo no existe -{updateinst.fila}-{updateinst.columna}")

            return []
    else:
        print('error')
        consola.append(f"La tabla {updateinst.id} no puede actualizarse, where no contemplado semanticamente\n")
        exceptions.append(
            f"Error semantico-42883- 42883	undefined_function, where no contemplado semanticamente -{updateinst.fila}-{updateinst.columna}")

        return []


def Filtrar(tabla, indice, operador, expre) -> list:
    nueva = []
    for tupla in tabla:
        if operador == '=' or operador == '==':
            if tupla[indice] == expre:
                nueva.append(tupla)
        elif operador == '<':
            if tupla[indice] < expre:
                nueva.append(tupla)
        elif operador == '<=':
            if tupla[indice] <= expre:
                nueva.append(tupla)
        elif operador == '>':
            if tupla[indice] > expre:
                nueva.append(tupla)
        elif operador == '>=':
            if tupla[indice] >= expre:
                nueva.append(tupla)
        elif operador == '!=':
            if tupla[indice] != expre:
                nueva.append(tupla)

    return nueva

def AndManual(tf1, tf2) -> list:
    unif = []
    if len(tf1) != 0 and len(tf2) != 0:
        for t1 in tf1:
            for t2 in tf2:
                if t1 == t2:
                    unif.append(t1)
    return unif