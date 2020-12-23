import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
sys.path.append('../tytus/parser/team27/G-27/execution/querie')
sys.path.append('../tytus/storage')
sys.path.append('../tytus/parser/team27/G-27/TypeChecker')
from querie import * 
from environment import *
from table import *
from column import *
from typ import *
from storageManager import jsonMode as admin
from checker import check

class Insert(Querie):
    '''
     row = numero de fila(int)
     column = numero de columna(int)
     tableName = nombre de la tabla a la que deseamos insertar datos(cadena)
     valueList = una lista de objetos tipo Literal
     idList = una lista de ids, es decir una lista de tipo string, puede ser None, depende de el formato del insert
    '''
    def __init__(self, tableName,valueList,idList, row, column):
        Querie.__init__(self, row, column)
        self.tableName = tableName
        self.idList = idList
        self.valueList = valueList

    def execute(self, environment):
        if not isinstance(self.tableName,str):
            return {'Error': 'El nombre indicado de la tabla no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        
        if self.idList == None:

            db_name = environment.getActualDataBase()
            database = environment.readDataBase(db_name)
            table = database.getTable(self.tableName)

            if len(table.columns) != len(self.valueList):
                return {'Error': 'El numero de valores a insertar es diferente que el numero de columnas de la tabla: '+self.tableName, 'Fila':self.row, 'Columna': self.column }
            
            for i in range(len(self.valueList)):
                columna = table.columns[i]
                valor = self.valueList[i].execute(environment)
                res = check(columna.tipo,valor['typ'], valor['value'],columna.lenght)
                if not isinstance(res,bool):
                    return {'Error':res, 'Fila':self.row, 'Columna': self.column}

            for index in range(len(self.valueList)):
                nombreVariable = table.columns[index].name
                valorVariable = self.valueList[index].execute(environment)
                environment.guardarVariable(nombreVariable,valorVariable['typ'],valorVariable['value'], None)
            
            for item in table.constraint:
                if item['type'] == 'primary':
                    var = environment.buscarVariable(item['value'], None)
                    if var == None:
                        return{'Error':'Variable no encontrada', 'Fila':self.row, 'Columna': self.column }
                    if var['tipo'] == Type.NULL:
                        return{'Error':'La primary key no puede ser nula', 'Fila':self.row, 'Columna': self.column }

                elif item['type'] == 'foreign':
                    #no hay validaciones por el momento
                    print('foreign')

                elif item['type'] == 'not null':
                    var = environment.buscarVariable(item['value'],None)
                    if var == None:
                        return{'Error':'Variable no encontrada', 'Fila':self.row, 'Columna': self.column }
                    if var['tipo']== Type.NULL:
                        return{'Error':'El campo: '+var['name']+' no puede ser nulo', 'Fila':self.row, 'Columna': self.column }
                
                elif item['type'] == 'check':
                    var = item['value'].execute(environment)
                    if var['typ'] != Type.BOOLEAN:
                        return{'Error':'La condicion del check, no es booleana', 'Fila':self.row, 'Columna': self.column }
                    if var['value'] != True:
                        return{'Error':'No se cumple con la restriccion: '+item['name'], 'Fila':self.row, 'Columna': self.column }

                elif item['type'] == 'unique':
                    val = admin.extractTable(db_name, self.tableName)
                    if val == None:
                        return{'Error':'La base de datos o la tabla a la que desea hacer referencia no existe.', 'Fila':self.row, 'Columna': self.column }
                    elif len(val) == 0:
                        #pasa de largo porque no hay registros
                        print('')
                    elif len(val) > 0:
                        aux = -1
                        for i in range(len(table.columns)):
                            if table.columns[i].name == item['value']:
                                    aux = i
                                    break
                        if aux == -1:
                                return{'Error':'No se encontro la columna: '+item['value'], 'Fila':self.row, 'Columna': self.column}
                        
                        searched = environment.buscarVariable(item['value'],None)
                        for tupla in val:
                            if tupla[aux] == searched['value']:
                                if isinstance(searched['value'],int):
                                    return{'Error':'Ya existe un registro con el valor: '+str(searched['value'])+' en la columna: '+item['value']+' lo cual viola la restriccion unique', 'Fila':self.row, 'Columna': self.column}
                                else:
                                    return{'Error':'Ya existe un registro con el valor: '+searched['value']+' en la columna: '+item['value']+' lo cual viola la restriccion unique', 'Fila':self.row, 'Columna': self.column}
                    else:
                            return{'Error':'Error desconocido al insertar.', 'Fila':self.row, 'Columna': self.column }
            
            #guardando en el storage
            listaValores=[]
            for item in self.valueList:
                valorLista = item.execute(environment)
                listaValores.append(valorLista['value'])
            valorRetorno = admin.insert(db_name, self.tableName, listaValores)

            if valorRetorno == 0:
                return'Se ha insertado con exito la tupla '+str(listaValores)+' en la tabla: '+self.tableName               
            elif valorRetorno == 1:
                return{'Error':'Error en la operación insertar.', 'Fila':self.row, 'Columna': self.column }
            elif valorRetorno == 2:
                return{'Error':'La base de datos a la que desea referenciar no existe', 'Fila':self.row, 'Columna': self.column }
            elif valorRetorno == 3:
                return{'Error':'La tabla en la que desea insertar registros no existe', 'Fila':self.row, 'Columna': self.column }
            elif valorRetorno == 4:
                return{'Error':'Llave primaria duplicada', 'Fila':self.row, 'Columna': self.column }
            elif valorRetorno == 5:
                return{'Error':'columna fuera de limites', 'Fila':self.row, 'Columna': self.column }
            else:
                return{'Error':'Error desconocido al insertar registros', 'Fila':self.row, 'Columna': self.column }

        else:
            # aqui es el segundo formato de insert
            db_name = environment.getActualDataBase()
            database = environment.readDataBase(db_name)
            table = database.getTable(self.tableName)

            if len(table.columns) < len(self.idList):
                return {'Error': 'El numero de columnas indicadas es mayor al numero de columnas de la tabla: '+self.tableName, 'Fila':self.row, 'Columna': self.column }
           
            if len(self.valueList) != len(self.idList):
                return {'Error': 'El numero de registros a insertar difiere del numero de columnas indicadas: '+self.tableName, 'Fila':self.row, 'Columna': self.column }
            
            #TODO verificar tipos
            for i in range(len(self.valueList)):
                columna = table.readColumn(self.idList[i])
                valor = self.valueList[i].execute(environment)
                res = check(columna.tipo,valor['typ'], valor['value'],columna.lenght)
                if not isinstance(res,bool):
                    return {'Error':res, 'Fila':self.row, 'Columna': self.column}


            # verificar que el id list coincida con los nombres de las columnas
            for item in self.idList:
                exist = False
                for col in table.columns:
                    if col.name == item:
                        exist = True
                if exist == False:
                    return {'Error': 'La columna: '+item+' no existe en la tabla: '+self.tableName, 'Fila':self.row, 'Columna': self.column }


            for index in range(len(self.valueList)):
                nombreVariable = self.idList[index]
                valorVariable = self.valueList[index].execute(environment)
                environment.guardarVariable(nombreVariable,valorVariable['typ'],valorVariable['value'], None)

            for item in table.columns:
                var = environment.buscarVariable(item.name, None)
                if var == None:
                    if item.default == None:
                        nombreVariable = item.name
                        valorVariable = 'null'
                        tipoVariable = Type.NULL
                        environment.guardarVariable(nombreVariable,tipoVariable,valorVariable, None)
                    else:
                        nombreVariable = item.name
                        valorVariable = item.default
                        tipoVariable = item.tipo
                        environment.guardarVariable(nombreVariable,tipoVariable,valorVariable, None)
          
            for item in table.constraint:
                if item['type'] == 'primary':
                    var = environment.buscarVariable(item['value'], None)
                    if var == None:
                        return{'Error':'Variable no encontrada', 'Fila':self.row, 'Columna': self.column }
                    if var['tipo'] == Type.NULL:
                        return{'Error':'La primary key no puede ser nula', 'Fila':self.row, 'Columna': self.column }

                elif item['type'] == 'foreign':
                    #no hay validaciones por el momento
                    print('foreign')

                elif item['type'] == 'not null':
                    var = environment.buscarVariable(item['value'],None)
                    if var == None:
                        return{'Error':'Variable no encontrada', 'Fila':self.row, 'Columna': self.column }
                    if var['tipo']== Type.NULL:
                        return{'Error':'El campo: '+var['name']+' no puede ser nulo', 'Fila':self.row, 'Columna': self.column }
                
                elif item['type'] == 'check':
                    var = item['value'].execute(environment)
                    if var['typ'] != Type.BOOLEAN:
                        return{'Error':'La condicion del check, no es booleana', 'Fila':self.row, 'Columna': self.column }
                    if var['value'] != True:
                        return{'Error':'No se cumple con la restriccion: '+item['name'], 'Fila':self.row, 'Columna': self.column }

                elif item['type'] == 'unique':
                    val = admin.extractTable(db_name, self.tableName)
                    if val == None:
                        return{'Error':'La base de datos o la tabla a la que desea hacer referencia no existe.', 'Fila':self.row, 'Columna': self.column }
                    elif len(val) == 0:
                        #pasa de largo porque no hay registros
                        print('')
                    elif len(val) > 0:
                        aux = -1
                        for i in range(len(table.columns)):
                            if table.columns[i].name == item['value']:
                                    aux = i
                                    break
                        if aux == -1:
                                return{'Error':'No se encontro la columna: '+item['value'], 'Fila':self.row, 'Columna': self.column}
                        
                        searched = environment.buscarVariable(item['value'], None)
                        for tupla in val:
                            if tupla[aux] == searched['value']:
                                if isinstance(searched['value'],int):
                                    return{'Error':'Ya existe un registro con el valor: '+str(searched['value'])+' en la columna: '+item['value']+' lo cual viola la restriccion unique', 'Fila':self.row, 'Columna': self.column}
                                else:
                                    return{'Error':'Ya existe un registro con el valor: '+searched['value']+' en la columna: '+item['value']+' lo cual viola la restriccion unique', 'Fila':self.row, 'Columna': self.column}
                    else:
                            return{'Error':'Error desconocido al insertar.', 'Fila':self.row, 'Columna': self.column }
            
            #ordenar la lista de valores
            #guardando en el storage
            valOrden =[]
            for item in table.columns:
                var = environment.buscarVariable(item.name, None)
                if var == None:
                    return{'Error':'Error desconocido al insertar 2.', 'Fila':self.row, 'Columna': self.column }
                valOrden.append(var['value'])
            valorRetorno = admin.insert(db_name, self.tableName, valOrden)

            if valorRetorno == 0:
                return'Se ha insertado con exito la tupla '+str(valOrden)+' en la tabla: '+self.tableName               
            elif valorRetorno == 1:
                return{'Error':'Error en la operación insertar.', 'Fila':self.row, 'Columna': self.column }
            elif valorRetorno == 2:
                return{'Error':'La base de datos a la que desea referenciar no existe', 'Fila':self.row, 'Columna': self.column }
            elif valorRetorno == 3:
                return{'Error':'La tabla en la que desea insertar registros no existe', 'Fila':self.row, 'Columna': self.column }
            elif valorRetorno == 4:
                return{'Error':'Llave primaria duplicada', 'Fila':self.row, 'Columna': self.column }
            elif valorRetorno == 5:
                return{'Error':'columna fuera de limites', 'Fila':self.row, 'Columna': self.column }
            else:
                return{'Error':'Error desconocido al insertar registros', 'Fila':self.row, 'Columna': self.column }

            
        