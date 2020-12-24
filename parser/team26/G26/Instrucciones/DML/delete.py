import sys
sys.path.append('../G26/Instrucciones')
sys.path.append('../G26/Librerias/storageManager')
sys.path.append('../G26/Utils')

from instruccion import *
from Error import *
from jsonMode import *

from TablaSimbolos import *

class Delete(Instruccion):

    def __init__(self, tableid, condiciones):
        self.tableid = tableid
        self.condiciones = condiciones

    def execute(self, data):

        tables = showTables(str(data.databaseSeleccionada))
        if not self.tableid.table.upper() in tables :
            error = Error('Semántico', 'Error(???): La tabla no existe.', 0, 0)
            return error
        
        #mandar a condiciones
        # Send to execute condition
        filas = extractTable(data.databaseSeleccionada, self.tableid.table.upper())
        #print(filas)
        if filas == None :
            error = Error('Semántico', 'Error(???): no existe la tabla ' + self.tableid.table.upper(), 0, 0)
            return error
        elif filas == [] :
            error = Error('Semántico', 'Error(???): La tabla ' + self.tableid.table.upper()+' está vacía.', 0, 0)
            return error

        pks = []
        contp = 0
        for col in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][self.tableid.table.upper()]['columns'] :
            if col.pk != None :
                if col.pk.val :
                    pks.append(contp)
            contp += 1



        if self.condiciones == None :
            'Se cambian todas los campos que vienen'
            index = 0
            for fila in filas :
                rowlistp = []
                if not pks == [] :
                    for pk in pks :
                        rowlistp.append(fila[pk])
                else :
                    rowlistp.append(index)
                    index += 1

                print(rowlistp)

            index = 0
            for fila in filas :
                rowlistp = []
                if not pks == [] :
                    for pk in pks :
                        rowlistp.append(fila[pk])
                else :
                    rowlistp.append(index)
                    index += 1
                

                if rowlistp == [] :
                    print('Operación exitosa')

                reto = delete(data.databaseSeleccionada, self.tableid.table.upper(), rowlistp)

                if reto == 0:
                    ''
                    print('Operación exitosa')
                elif reto == 1:
                    error = Error('Storage', 'Error(1): Error en la operación', 0, 0)
                    return error
                elif reto == 2:
                    error = Error('Storage', 'Error(2): Database no existente', 0, 0)
                    return error
                elif reto == 3:
                    error = Error('Storage', 'Error(3): Table no existente', 0, 0)
                    return error
                elif reto == 4:
                    error = Error('Storage', 'Error(4): Llave primaria inexistente', 0, 0)
                    return error

        
        else : 
            #diccionario para mandar a condiciones:
            #dicciPrueba = {'NombreTabla1': {'fila': [1, 3, "f"], 'alias': 'nombre'}, 'NombreTabla2': {'fila': [], 'alias': None}}
            index = 0
            for fila in filas :
                condObj = {self.tableid.table.upper() : {'fila' : fila, 'alias':''}}
                #print(condObj)
                
                toadd = self.condiciones.execute(data, condObj)
                if isinstance(toadd, Error):
                    return toadd

                rowlistp = []
                if toadd :
                    if not pks == [] :
                        for pk in pks :
                            rowlistp.append(fila[pk])
                    else :
                        rowlistp.append(index)

                    print(rowlistp)

                index += 1


            index = 0
            for fila in filas :
                condObj = {self.tableid.table.upper() : {'fila' : fila, 'alias':''}}
                print(condObj)
                
                toadd = self.condiciones.execute(data, condObj)
                if isinstance(toadd, Error):
                    return toadd

                # Send to delete function
                rowlistp = []
                if toadd :
                    if not pks == [] :
                        for pk in pks :
                            rowlistp.append(fila[pk])
                    else :
                        rowlistp.append(index)

                    if rowlistp == [] :
                        print('Operación exitosa')

                    reto = delete(data.databaseSeleccionada, self.tableid.table.upper(), rowlistp)

                    if reto == 0:
                        ''
                        print('Operación exitosa')
                    elif reto == 1:
                        error = Error('Storage', 'Error(1): Error en la operación', 0, 0)
                        return error
                    elif reto == 2:
                        error = Error('Storage', 'Error(2): Database no existente', 0, 0)
                        return error
                    elif reto == 3:
                        error = Error('Storage', 'Error(3): Table no existente', 0, 0)
                        return error
                    elif reto == 4:
                        error = Error('Storage', 'Error(4): Llave primaria inexistente', 0, 0)
                        return error
                
                index += 1

        return self.tableid

    def __repr__(self):
        return str(self.__dict__)
