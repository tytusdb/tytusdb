
Databases = []
# --------------------------------------Database-----------------------------------------------
def createDatabase(name,mode):
    database = {}
    database['name']=name
    database['mode']=mode
    database['tables']=[]
    Databases.append(database)

def alterDatabase (databaseOld, databaseNew):
    for data in Databases:
        if data['name'] == databaseOld:
            data['name']=databaseNew
            print("Alter database")
            return 
    print("Database not found")
    return 

def showDatabases():
    for data in Databases:
        print("Name: ",data['name'])
        print("Mode: ",data['mode'])

def dropDatabase(name):
    element ={}
    for data in Databases:
       if data['name'] == name:
            element = data       
            break

    if element !={}:
        Databases.remove(element)
        print("Drop database")
        return 
    print("Database not found")
    return 
    

# --------------------------------------Tables-----------------------------------------------

def createTable (dbName, tableName):
    table={}
    table['name']=tableName
    table['colmns']= []
    for db in Databases:
        if db['name']==dbName:
            db['tables'].append(table)
            break

#def showTables (basededatos):

def alterTable(dbName, tableOld, tableNew):
    for db in Databases:
        if db['name']==dbName:
            for table in db['tables']:
                if table['name']==tableOld:
                    table['name']=tableNew
                    print("Alter table")
                    break
            break



def dropTable (dbName, tableName):
    tbl ={}
    for db in Databases:
        if db['name'] == dbName:
            for table in db['tables']:
                if table['name']==tableName:  
                    tbl=table  
            if tbl !={}:
                db['tables'].remove(tbl)
                print("Drop Table")
        break

# --------------------------------------Columns-----------------------------------------------                    
def createCol(name,category,type_,pk,fk,nn,inc,size):
    col={}
    col['name']=name
    #TODO: agregar enum para category y type
    col['category']=category
    col['type']=type_
    #TODO : validar precicion y escala no sobrepasen los limites de los tipos decimal y numerico
    col['size']=size
    col['PK']=pk
    col['FK']=fk
    col['NN']=nn
    col['AI']=inc
    return col

def addCol(dbName, tName,name,category,type_,pk,fk,nn,inc,size):
    col = createCol(name,category,type_,pk,fk,nn,inc,size)
    for db in Databases:
        if db['name'] == dbName:
            for table in db['tables']:
                if table['name']==tName:  
                    table['colmns'].append(col)
                    break


def alterDrop(dbName, tableName, colName):
    clm={}
    for db in Databases:
        if db['name'] == dbName:
            for table in db['tables']:
                if table['name']==tableName:  
                    for col in  table['colmns']:
                        if col['name']==colName:
                            clm = col
                    if clm != {}:
                        table['colmns'].remove(clm)
                        print("Drop Table")
                    return
        

def extractColmn(dbName, tableName, colName):
   for db in Databases:
        if db['name'] == dbName:
            for table in db['tables']:
                if table['name']==tableName:  
                    for col in  table['colmns']:
                        if col['name']==colName:
                            return col
                    return None
