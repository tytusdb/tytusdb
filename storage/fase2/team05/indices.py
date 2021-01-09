import storageManager as uni

#Creación y eliminación de llaves foráneas

#Agrega un índice de llave foranea
def alterTableAddFK(database: str, table: str, indexName: str, columns: list, tableRef: str, columnsRef: list) -> int:
    if database not in uni.showDatabases():
        return 2

    if table not in uni.showTables(database) or tableRef not in uni.showTables(database):
        return 3

    if (len(columns) < 1) or (len(columnsRef) < 1) or (len(columns) != len(columnsRef)):
        return 4

    for col in columns:
        if len(uni.extractRangeTable(database, table, col, 0, 1)) == None:
            return 1

    for refCol in columnsRef:
        if len(uni.extractRangeTable(database, table, refCol, 0, 1)) == None:
            return 1

    if len(uni.extractTable(database, table)) == 0 and len(uni.extractTable(database, tableRef)) == 0:
        if uni.createTable(database, table + '_FK', 3) != 0:
            return 1
        
        if uni.alterAddPK(database, table + '_FK', [0]) != 0:
            return 1

        if uni.insert(database, table + '_FK', [indexName, tableRef, columnsRef]) != 0:
            return 1
    elif len(uni.extractTable(database, table)) > 0 and len(uni.extractTable(database, table)) == 0:
        return 5
    else:
        tableRefValues = uni.extractTable(database, tableRef)
        tableValues = uni.extractTable(database, table)
        notFoundValues = []
        indiceCol = 0

        while indiceCol < len(columns):
            for values in tableValues:
                if values[columns[indiceCol]] not in notFoundValues:
                    notFoundValues.append(values[columns[indiceCol]])
            indiceCol += 1
                
        indiceCol = 0
        while indiceCol < len(columnsRef):
            for refValues in tableRefValues:
                if refValues[columnsRef[indiceCol]] in notFoundValues:
                    notFoundValues.remove(refValues[columnsRef[indiceCol]])
            indiceCol += 1

        if len(notFoundValues) == 0:
            if uni.createTable(database, table + '_FK', 3) != 0:
                return 1

            if uni.alterAddPK(database, table + '_FK', [0]) != 0:
                return 1

            if uni.insert(database, table + '_FK', [indexName, tableRef, columnsRef]) != 0:
                return 1
        else:
            return 5
    return 0

#Destruye el índice tanto como metadato como la estructura adicional
def alterTableDropFK(database: str, table: str, indexName: str) -> int:
    if database not in uni.showDatabases():
        return 2

    if table not in uni.showTables(database):
        return 3

    if len(uni.extractRow(database, table, [indexName])) == 0:
        return 4

    if uni.dropTable(database, table + '_FK') != 0:
        return 1
    return 0

#Creación y eliminación de índices únicos

#Agrega un índice único, creando una estructura adicional con el modo indicado en la bd
def alterTableAddUnique(database: str, table: str, indexName: str, columns: list) -> int:
    if database not in uni.showDatabases():
        return 2

    if table not in uni.showTables(database):
        return 3

    if (len(columns) < 1):
        return 4
    
    for col in columns:
        if len(uni.extractRangeTable(database, table, col, 0, 1)) == None:
            return 1
        
    if len(uni.extractTable(database, table)) == 0:
        if uni.createTable(database, table + '_UNIQUE', 2) != 0:
            return 1
        
        if uni.alterAddPK(database, table + '_UNIQUE', [0]) != 0:
            return 1

        if uni.insert(database, table + '_UNIQUE', [indexName, columns]) != 0:
            return 1
    else:
        tuplas = uni.extractTable(database, table)
        indiceCol = 0
        encontrados = []

        while indiceCol < len(columns):
            for values in tuplas:
                if values[columns[indiceCol]] not in encontrados:
                    encontrados.append(values[columns[indiceCol]])
                else:
                    return 5
            indiceCol += 1

        if uni.createTable(database, table + '_UNIQUE', 2) != 0:
            return 1
        
        if uni.alterAddPK(database, table + '_UNIQUE', [0]) != 0:
            return 1

        if uni.insert(database, table + '_UNIQUE', [indexName, columns]) != 0:
            return 1
    return 0

#Destruye el índice tanto como metatadato como la estructura adicional
def alterTableDropUnique(database: str, table: str, indexName: str) -> int:
    if database not in uni.showDatabases():
        return 2

    if table not in uni.showTables(database):
        return 3

    if len(uni.extractRow(database, table, [indexName])) == 0:
        return 4

    if uni.dropTable(database, table + '_UNIQUE') != 0:
        return 1
    return 0

#Creación y eliminación de índices

#Agrga un índice, creando una estructura adicional con el modo indicado para la base de datos
def alterTableAddIndex(database: str, table: str, indexName: str, columns: list) -> int:
    if database not in uni.showDatabases():
        return 2

    if table not in uni.showTables(database):
        return 3

    if (len(columns) < 1):
        return 4
    
    for col in columns:
        if len(uni.extractRangeTable(database, table, col, 0, 1)) == None:
            return 1
        
    if uni.createTable(database, table + '_INDEX', 2) != 0:
        return 1
    
    if uni.alterAddPK(database, table + '_INDEX', [0]) != 0:
        return 1

    if uni.insert(database, table + '_INDEX', [indexName, columns]) != 0:
        return 1
    
    return 0

#Destruye el índice tanto como metadato de la tabla como la estructura adicional creada
def alterTableDropIndex(database: str, table: str, indexName: str) -> int:
    if database not in uni.showDatabases():
        return 2

    if table not in uni.showTables(database):
        return 3

    if len(uni.extractRow(database, table, [indexName])) == 0:
        return 4

    if uni.dropTable(database, table + '_INDEX') != 0:
        return 1
    return 0

