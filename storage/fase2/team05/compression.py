import zlib

import storageManager as u
compression_levels=[1,2,3,4,5,6,7,8,9,-1]

class Compression:
    #def __init__(self):
        #tests={}

    def alterDatabaseCompress(self, database: str, level: int) -> int:
        if database in u.showDatabases():
            if level in compression_levels:
                try:

                    lista_tables=u.showTables(database)
                    for t in lista_tables:
                        self.alterTableCompress(database,t,level)
                    return 0
                except:
                    return 1
                
            else:
                return 3
        else:
            return 2
        

    def alterDatabaseDecompress(self, database: str) -> int:
        if database in u.showDatabases():
            try:
                lista_tables=u.showTables(database)
                for t in lista_tables:
                    self.alterTableDecompress(database,t)
                return 0
            except:
                return 1
            
        else:
            return 2
        

    def alterTableCompress(self, database: str, table: str, level: int) -> int:
        #modo=u.getModoBaseDatos(database)
        if database in u.showDatabases():
            if table in u.showTables(database):
                if level in compression_levels:
                    try:
                        extract=u.extractTable(database,table)
                        if len(extract)>0:
                            #print('Lista mayor a 0 elementos')
                            #recorrido 
                            for i in range(0,len(extract)):
                                fila=extract[i]
                                for j in range(0,len(fila)):
                                    tupla=fila[j]
                                    if type(tupla)==str:
                                        tupla=zlib.compress(bytes(tupla.encode()),level)
                                    elif type(tupla)==bytes:
                                        #tupla=zlib.compress(tupla,level)
                                        tupla=tupla
                                    
                                    fila[j]=tupla
                                extract[i]=fila
                        
                        u.truncate(database,table)
                        #print('compressed:',u.alterAddColumn(database,table,'Compressed'))
                        
                        for element in extract:
                            #print('ingresa element: '+str(element))
                            u.insert(database,table,element)
                            #insert_true=False

                        return 0
                    except:
                        return 1
                else:
                    return 4
            else:
                return 3
        else:
            return 2
        

    def alterTableDecompress(self, database: str, table: str) -> int:
        codificacion=u.getCodificacionDatabase(database)
        if database in u.showDatabases():
            if table in u.showTables(database):
                try:
                    extract=u.extractTable(database,table)
                    if len(extract)>0:
                        #print('Lista mayor a 0 elementos')
                        #recorrido
                        #last_col=-1
                        for i in range(0,len(extract)):
                            fila=extract[i]
                            for j in range(0,len(fila)):
                                try:
                                    tupla=fila[j]
                                    tupla=zlib.decompress(tupla)
                                    fila[j]=tupla.decode(codificacion)
                                except:
                                    return 4
                            extract[i]=fila
                            #last_col=len(fila)
                            #print('lastcol: ',last_col)
                        

                    u.truncate(database,table)
                    
                    for element in extract:
                        u.insert(database,table,element)

                    
                    return 0
                except:
                    return 1
            else:
                return 3
        else:
            return 2


#iniciliazicaicon de compresion
comp=Compression()


#print('Antes de Comprimir-------------------------')
#extra=u.extractTable('BD5','Curso')
#extra=u.extractTable('BD5','Curso')
#for t in extra:
#    print(t)
#print('Despues de comprimir-------------------------')
#print(comp.alterTableCompress('BD5','Curso',1))
#extra=u.extractTable('BD5','Curso')
#for t in extra:
#    print(t)

#print('Despues de comprimir 2vez-------------------------')
#print(comp.alterTableCompress('BD5','Curso',1))
#extra=u.extractTable('BD5','Curso')
#for t in extra:
#    print(t)

#print('Despues de comprimir 3vez-------------------------')
#print(comp.alterTableCompress('BD5','Curso',1))
#extra=u.extractTable('BD5','Curso')
#for t in extra:
#    print(t)

#input('Despues de descomprimir-------------------------')
#print(comp.alterTableDecompress('BD5','Curso'))
#extra=u.extractTable('BD5','Curso')
#for t in extra:
#    print(t)

#print(comp.alterDatabaseCompress('BD5',9))
#print(comp.alterDatabaseDecompress('BD5'))
#print(comp.alterDatabaseDecompress('BD5'))
