from instruccion import *
from funcionesTS import *
from expresiones import *
from conexionDB import *
from VerificarDatos import *
from funcionesNativas import * 



class crearTablas():

    def __init__(self, tablaActual, baseActual, conectar, ts , listaTablas):
        self.conectar = conectar
        self.ts  = ts
        self.tablaActual = tablaActual
        self.baseActual = baseActual
        self.listaTablas = listaTablas
    
    
    
    def crearTabla(self,instru) :     
            instIfnot = instru.instru.ifNot
            instColTabla = instru.instru.colTabla
            instFinTabla = instru.instru.finTabla
            #obtener list de campos coltabla , obtener finTabla
            
            idtabla = ''
            errorExiste = 1
            
            if isinstance(instIfnot , ids):
                idtabla = instIfnot.ids
            elif isinstance(instIfnot, IfExist2):
                idtabla = instIfnot.identificador
                if instIfnot.existe == valido.invalido:
                   errorExiste = verificarTablaDuplicada(idtabla, self.baseActual)
                if instIfnot.existe == True:
                    errorExiste = verificarTablaDuplicada(idtabla, self.baseActual)
                    
            elif isinstance(instIfnot, modo):
                idtabla = instIfnot.identificador
                if instIfnot.existe == True:
                    errorExiste = verificarTablaDuplicada(idtabla, self.baseActual)
                elif instIfnot.existe == valido.invalido:
                    errorExiste = verificarTablaDuplicada(idtabla, self.baseActual)
            
            elif isinstance(instIfnot, IfExist):
                idtabla = instIfnot.identificador
                if instIfnot.existe == True:
                    errorExiste = verificarTablaDuplicada(idtabla, self.baseActual)
                elif instIfnot.existe == valido.invalido:
                    errorExiste = verificarTablaDuplicada(idtabla, self.baseActual)
                
            #obtener campos
            if errorExiste == 1:
                errorExiste = verificarTablaDuplicada(idtabla , self.tablaActual)
                if errorExiste == 1:
                    listllaves = []
                    contador = 0
                    listaCampos = []
                    listaForeignKeys =[]
                    for camp in instColTabla:
                        if isinstance(camp, propCol):
                            contador = contador + 1 
                            idCol = camp.identificador
                            tipoCol = camp.tipo
                            param = camp.propiedades
                            if isinstance(param, valido):
                                if tipoCol.num == valido.invalido:
                                    nuevCamp = campo(idCol, tipoCol.tipo, '','','','','')
                                    listaCampos.append(nuevCamp)
                                else:
                                    nuevCamp = campo(idCol, tipoCol.tipo,'','','','','')
                                    nuevCamp.setDimension(tipoCol.num)
                                    listaCampos.append(nuevCamp)
                            else:
                                varprop = self.getPropiedades(camp.propiedades)
                                if tipoCol.num == valido.invalido:
                                    nuevCamp = campo(idCol, tipoCol.tipo, varprop.isLlave, varprop.hasCheck, varprop.isIdentity, varprop.setNull, varprop.setConstraint)
                                    listaCampos.append(nuevCamp)
                                else:
                                    nuevCamp = campo(idCol, tipoCol.tipo, varprop.isLlave, varprop.hasCheck, varprop.isIdentity, varprop.setNull, varprop.setConstraint)
                                    nuevCamp.setDimension(tipoCol.num)
                                    listaCampos.append(nuevCamp)
                        elif isinstance(camp,foreingKey):   
                            listaForeignKeys = self.getListIds(camp.identificador)
                        elif isinstance(camp, primaryKey):
                            listllaves= self.getListIds(camp.propiedades)

                    if isinstance(instFinTabla, Empty):
                        self.conectar.cmd_createTable(self.baseActual, idtabla, contador)
                        if verificarTablaDuplicada(idtabla, self.baseActual) == 0:
                            tablaNueva = TablaB(idtabla,listaCampos,listaForeignKeys,listllaves)
                            self.listaTablas.append(tablaNueva)
                            self.tablaActual = idtabla
                            for elem in listaCampos:
                                self.conectar.cmd_agregarCont(elem)


                            print('ingreso de tabla')
                           

                    elif isinstance(instFinTabla, inherencia):
                        #lleva inherits
                        print('hacer herencia')
                        for elementos in self.listaTablas:
                            if elementos.nombre == instFinTabla.ids:
                                for elementos2 in elementos.listCampos:
                                    listaCampos.append(elementos2)
                                    contador = contador+1

                                for elementos2 in  elementos.listLlavesForeign:
                                    listaForeignKeys.append(elementos2)
                                for elementos2 in elementos.listLlavesPrimary:
                                    listllaves.append(elementos2)
                        
                        self.conectar.cmd_createTable(self.baseActual, idtabla, contador)
                        if verificarTablaDuplicada(idtabla, self.baseActual) == 0:
                            tablaNueva = TablaB(idtabla,listaCampos,listaForeignKeys,listllaves)
                            self.listaTablas.append(tablaNueva)
                            self.tablaActual = idtabla

                            for elem in listaCampos:
                                self.conectar.cmd_agregarCont(elem)
                        
                    
                else: 
                    print('Error de tabla duplicada'+ idtabla)
            else:
                print('error no se debe reportar ')

    def getPropiedades(self, instru):
        if isinstance(instru, propiedad):
            if isinstance(instru.var2, propiedad):
                props  = self.getPropiedades(instru.propiedades)
                if instru.var1 == 'identity':
                    if props.isIdentity =='':
                        return campo('',props.tipo,props.isLlave,props.hasCheck,valoresCampo.IDENTITY,props.setNull,props.setConstraint)
                    else:
                        print('error usted ya declaro identity')
                elif instru.var1 == 'null':
                    if props.isNull =='':
                        return campo('',props.tipo,props.isLlave,props.hasCheck,props.isIdentity,valoresCampo.NUll,props.setConstraint)
                    else:
                        print('error usted ya declaro null o notNull')
                elif instru.var1 == 'notNull':
                    if props.isNull =='':
                        return campo('',props.tipo,props.isLlave,props.hasCheck,props.isIdentity,valoresCampo.notNUll,props.setConstraint)
                    else:
                        print('error usted ya declaro null o notNull')
                else:
                    print('Error de parametros campo' + instru.var2)

            elif instru.var2 == valido.invalido:
                if instru.var == 'identity':
                    return campo('','','','',valoresCampo.IDENTITY,'','')
                elif instru.var == 'null':
                    return campo('','','','','',valoresCampo.NUll,'')
                elif instru.var == 'notNull':
                    return campo('','','','','',valoresCampo.notNUll,'')
                else:
                    print('Error de parametros campo' + instru.var2)

        elif isinstance(instru, primaryKey):
            var = instru.propiedades
            if var == valido.invalido:
                return campo('','',valoresCampo.PRIMARY,'','','','')
            else:
                props  = self.getPropiedades(instru.propiedades)
                hasCheck = props.hasCheck
                isIdentity = props.isIdentity
                setNull = props.setNulll
                setConstraint = props.setConstraint
                if props.isLlave !='':
                    return campo('','',valoresCampo.PRIMARY, hasCheck, isIdentity, setNull, setConstraint)
                else:
                    print('error ')

    def getListIds(self, instru):
        listaIdss = []
        for ident  in instru:
            if isinstance(ident, ids):
                listaIdss.append(ident.ids)

        return listaIdss


    def getBaseActual(self):
        return self.baseActual

    def getTablaActual(self):
        return self.tablaActual

class crearBases():
    def __init__(self, tablaActual, baseActual, conectar, ts , listaTablas):
        self.conectar = conectar
        self.ts  = ts
        self.tablaActual = tablaActual
        self.baseActual = baseActual
        self.listaTablas = listaTablas
    
    def obIfNot(self, instru, conectar):
        #se 
        instIfnot = instru.instru.ifNot
        idtabla = ''
        errorExiste = 1
        if isinstance(instIfnot , ids):
            idtabla = instIfnot.ids
            conectar.cmd_createdatabase(idtabla)
            self.baseActual = idtabla
        elif isinstance(instIfnot, IfExist2):
            idtabla = instIfnot.identificador
            if instIfnot.existe == valido.invalido:
                errorExiste = verificarTablaDuplicada(idtabla, self.tablaActual)
            if instIfnot.existe == True:
                errorExiste = verificarTablaDuplicada(idtabla, self.tablaActual)
            conectar.cmd_createdatabase(idtabla)
            if errorExiste == 1:
                self.baseActual = idtabla
        elif isinstance(instIfnot, modo):
            idtabla = instIfnot.identificador
            if instIfnot.existe == True:
                errorExiste = verificarTablaDuplicada(idtabla, self.tablaActual)
            elif instIfnot.existe == valido.invalido:
                errorExiste = verificarTablaDuplicada(idtabla, self.tablaActual)
            conectar.cmd_createdatabase(idtabla)
            if errorExiste == 1:
                self.baseActual = idtabla
        elif isinstance(instIfnot, IfExist):
            idtabla = instIfnot.identificador
            if instIfnot.existe == True:
                errorExiste = verificarTablaDuplicada(idtabla, self.tablaActual)
            elif instIfnot.existe == valido.invalido:
                errorExiste = verificarTablaDuplicada(idtabla, self.tablaActual)
            conectar.cmd_createdatabase(idtabla)
            if errorExiste == 1:
                self.baseActual = idtabla

        print('verificacion basetabla')


    def getBaseActual(self):
        return self.baseActual

class replaceBases():
    def __init__(self, tablaActual, baseActual, conectar, ts , listaTablas):
        self.conectar = conectar
        self.ts  = ts
        self.tablaActual = tablaActual
        self.baseActual = baseActual
        self.listaTablas = listaTablas
    
    def obIfNot(self, instru, conectar):
        #se 
        instIfnot = instru.instru.ifNot
        idtabla = ''
        errorExiste = 1
        if isinstance(instIfnot , ids):
            idtabla = instIfnot.ids
            conectar.cmd_dropDatabase(idtabla)
            conectar.cmd_createdatabase(idtabla)
            self.baseActual = idtabla
        elif isinstance(instIfnot, IfExist2):
            idtabla = instIfnot.identificador
            if instIfnot.existe == valido.invalido:
                errorExiste = verificarTablaDuplicada(idtabla, self.tablaActual)
            if instIfnot.existe == True:
                errorExiste = verificarTablaDuplicada(idtabla, self.tablaActual)

            conectar.cmd_dropDatabase(idtabla)
            conectar.cmd_createdatabase(idtabla)
            if errorExiste == 1:
                self.baseActual = idtabla
        elif isinstance(instIfnot, modo):
            idtabla = instIfnot.identificador
            if instIfnot.existe == True:
                errorExiste = verificarTablaDuplicada(idtabla, self.tablaActual)
            elif instIfnot.existe == valido.invalido:
                errorExiste = verificarTablaDuplicada(idtabla, self.tablaActual)
            conectar.cmd_dropDatabase(idtabla)
            conectar.cmd_createdatabase(idtabla)
            if errorExiste == 1:
                self.baseActual = idtabla
        elif isinstance(instIfnot, IfExist):
            idtabla = instIfnot.identificador
            if instIfnot.existe == True:
                errorExiste = verificarTablaDuplicada(idtabla, self.tablaActual)
            elif instIfnot.existe == valido.invalido:
                errorExiste = verificarTablaDuplicada(idtabla, self.tablaActual)
            conectar.cmd_dropDatabase(idtabla)
            conectar.cmd_createdatabase(idtabla)
            if errorExiste == 1:
                self.baseActual = idtabla

        print('verificacion basetabla')


    def getBaseActual(self):
        return self.baseActual

class ReplaceTabla():
    def __init__(self, tablaActual, baseActual, conectar, ts , listaTablas):
        self.conectar = conectar
        self.ts  = ts
        self.tablaActual = tablaActual
        self.baseActual = baseActual
        self.listaTablas = listaTablas 
    
    def replaceTabla(self,instru) :     
            instIfnot = instru.instru.ifNot
            instColTabla = instru.instru.colTabla
            instFinTabla = instru.instru.finTabla
            #obtener list de campos coltabla , obtener finTabla
            
            idtabla = ''
            errorExiste = 1
            
            if isinstance(instIfnot , ids):
                idtabla = instIfnot.ids
            elif isinstance(instIfnot, IfExist2):
                idtabla = instIfnot.identificador
                if instIfnot.existe == valido.invalido:
                   errorExiste = verificarTablaDuplicada(idtabla, self.tablaActual)
                if instIfnot.existe == True:
                    errorExiste = verificarTablaDuplicada(idtabla, self.tablaActual)
                    
            elif isinstance(instIfnot, modo):
                idtabla = instIfnot.identificador
                if instIfnot.existe == True:
                    errorExiste = verificarTablaDuplicada(idtabla, self.tablaActual)
                elif instIfnot.existe == valido.invalido:
                    errorExiste = verificarTablaDuplicada(idtabla, self.tablaActual)
            
            elif isinstance(instIfnot, IfExist):
                idtabla = instIfnot.identificador
                if instIfnot.existe == True:
                    errorExiste = verificarTablaDuplicada(idtabla, self.tablaActual)
                elif instIfnot.existe == valido.invalido:
                    errorExiste = verificarTablaDuplicada(idtabla, self.tablaActual)
                
            #obtener campos
            if errorExiste == 1:
                errorExiste = verificarTablaDuplicada(idtabla , self.tablaActual)
                if errorExiste == 1:
                    listllaves = []
                    contador = 0
                    listaCampos = []
                    listaForeignKeys =[]
                    for camp in instColTabla:
                        if isinstance(camp, propCol):
                            contador = contador + 1 
                            idCol = camp.identificador
                            tipoCol = camp.tipo
                            param = camp.propiedades
                            if isinstance(param, valido):
                                if tipoCol.num == valido.invalido:
                                    nuevCamp = campo(idCol, tipoCol.tipo, '','','','','')
                                    listaCampos.append(nuevCamp)
                                else:
                                    nuevCamp = campo(idCol, tipoCol.tipo,'','','','','')
                                    nuevCamp.setDimension(tipoCol.num)
                                    listaCampos.append(nuevCamp)
                            else:
                                varprop = self.getPropiedades(camp.propiedades)
                                if tipoCol.num == valido.invalido:
                                    nuevCamp = campo(idCol, tipoCol.tipo, varprop.isLlave, varprop.hasCheck, varprop.isIdentity, varprop.setNull, varprop.setConstraint)
                                    listaCampos.append(nuevCamp)
                                else:
                                    nuevCamp = campo(idCol, tipoCol.tipo, varprop.isLlave, varprop.hasCheck, varprop.isIdentity, varprop.setNull, varprop.setConstraint)
                                    nuevCamp.setDimension(tipoCol.num)
                                    listaCampos.append(nuevCamp)
                        elif isinstance(camp,foreingKey):   
                            listaForeignKeys = self.getListIds(camp.identificador)
                        elif isinstance(camp, primaryKey):
                            listllaves= self.getListIds(camp.propiedades)

                    if isinstance(instFinTabla, Empty):
                        self.conectar.cmd_dropTable(self.baseActual, idtabla)
                        self.conectar.cmd_createTable(self.baseActual,idtabla, contador)
                        if verificarTablaDuplicada(idtabla, self.baseActual) == 0:
                            tablaNueva = TablaB(idtabla,listaCampos,listaForeignKeys,listllaves)
                            self.listaTablas.append(tablaNueva)
                            self.tablaActual = idtabla
                            print('ingreso de tabla')
                           

                    elif isinstance(instFinTabla, inherencia):
                        #lleva inherits
                        print('hacer herencia')
                        for elementos in self.listaTablas:
                            if elementos.nombre == instFinTabla.ids:
                                for elementos2 in elementos.listCampos:
                                    listaCampos.append(elementos2)
                                    contador = contador+1

                                for elementos2 in  elementos.listLlavesForeign:
                                    listaForeignKeys.append(elementos2)
                                for elementos2 in elementos.listLlavesPrimary:
                                    listllaves.append(elementos2)
                        
                        self.conectar.cmd_dropTable(self.baseActual, idtabla)
                        self.conectar.cmd_createTable(self.baseActual,idtabla, contador)
                        if verificarTablaDuplicada(idtabla, self.baseActual) == 0:
                            tablaNueva = TablaB(idtabla,listaCampos,listaForeignKeys,listllaves)
                            self.listaTablas.append(tablaNueva)
                            self.tablaActual = idtabla
                        
                    
                else: 
                    print('Error de tabla duplicada'+ idtabla)
            else:
                print('error no se debe reportar ')

    def getPropiedades(self, instru):
        if isinstance(instru, propiedad):
            if isinstance(instru.var2, propiedad):
                props  = self.getPropiedades(instru.propiedades)
                if instru.var1 == 'identity':
                    if props.isIdentity =='':
                        return campo('',props.tipo,props.isLlave,props.hasCheck,valoresCampo.IDENTITY,props.setNull,props.setConstraint)
                    else:
                        print('error usted ya declaro identity')
                elif instru.var1 == 'null':
                    if props.isNull =='':
                        return campo('',props.tipo,props.isLlave,props.hasCheck,props.isIdentity,valoresCampo.NUll,props.setConstraint)
                    else:
                        print('error usted ya declaro null o notNull')
                elif instru.var1 == 'notNull':
                    if props.isNull =='':
                        return campo('',props.tipo,props.isLlave,props.hasCheck,props.isIdentity,valoresCampo.notNUll,props.setConstraint)
                    else:
                        print('error usted ya declaro null o notNull')
                else:
                    print('Error de parametros campo' + instru.var2)

            elif instru.var2 == valido.invalido:
                if instru.var == 'identity':
                    return campo('','','','',valoresCampo.IDENTITY,'','')
                elif instru.var == 'null':
                    return campo('','','','','',valoresCampo.NUll,'')
                elif instru.var == 'notNull':
                    return campo('','','','','',valoresCampo.notNUll,'')
                else:
                    print('Error de parametros campo' + instru.var2)

        elif isinstance(instru, primaryKey):
            var = instru.propiedades
            if var == valido.invalido:
                return campo('','',valoresCampo.PRIMARY,'','','','')
            else:
                props  = self.getPropiedades(instru.propiedades)
                hasCheck = props.hasCheck
                isIdentity = props.isIdentity
                setNull = props.setNulll
                setConstraint = props.setConstraint
                if props.isLlave !='':
                    return campo('','',valoresCampo.PRIMARY, hasCheck, isIdentity, setNull, setConstraint)
                else:
                    print('error ')

    def getListIds(self, instru):
        listaIdss = []
        for ident  in instru:
            if isinstance(ident, ids):
                listaIdss.append(ident.ids)

        return listaIdss


