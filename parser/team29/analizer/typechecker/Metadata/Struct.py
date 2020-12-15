from TypeChecker.Metadata import File    

Databases = []
# --------------------------------------Database-----------------------------------------------
def createDatabase(name,mode,owner):
    database = {}
    database['name']=name
    database['mode']=mode
    database['owner']=owner
    database['tables']=[]
    Databases = File.importFile()
    Databases.append(database)
    File.exportFile(Databases)

def alterDatabase(databaseOld, databaseNew):
    Databases = File.importFile()
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
    Databases = File.importFile()
    for data in Databases:
       if data['name'] == name:
            element = data       
            break

    if element !={}:
        Databases.remove(element)
        print("Drop database")
        File.exportFile(Databases)
        return 
    print("Database not found")
    return 
    
def replaceDatabase(name,mode,owner):
    dropDatabase(name)
    createDatabase(name,mode,owner)
    print("Replace database")
# --------------------------------------Tables-----------------------------------------------

def insertTable(dbName,tableName,columns):
    createTable(dbName,tableName)
    insertColumns(dbName,tableName,columns)
    
    
def createTable (dbName, tableName):
    table={}
    table['name']=tableName
    table['colmns']= []
    Databases = File.importFile()
    for db in Databases:
        if db['name']==dbName:
            db['tables'].append(table)
            break
    File.exportFile(Databases)

#def showTables (basededatos):

def alterTable(dbName, tableOld, tableNew):
    Databases = File.importFile()
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
    Databases = File.importFile()
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
    col['DEFAULT']=inc
    return col

def insertColumns(dbName, tName,columns):
    Databases = File.importFile()
    for db in Databases:
        if db['name'] == dbName:
            for table in db['tables']:
                if table['name']==tName: 

                    for column in columns:
                        table['colmns'].append(getCol(column))                    
                    break
    File.exportFile(Databases)


def getCol(col):
    name = col[0]
    type_ = col[1][0]
    #name,category,type_,pk,fk,nn,df,size
    pk=False
    fk=None
    nn=False
    df=None
    size = col[1][1][0]
    category = getCategory(type_)
    campos=col[2]
    if campos !=None:
        for campo in campos:
            if campo[0]=='PRIMARY':
                pk = campo[1]
            elif campo[0]=='FOREIGN':
                fk = campo[1]
            elif campo[0]=='NULL':
                nn = campo[1]
            elif campo[0]=='DEFAULT':
                df = campo[1]

    col = createCol(name,category,type_,pk,fk,nn,df,size)
    return col

def getCategory(type_):
    return 0

def alterDrop(dbName, tableName, colName):
    clm={}
    Databases = File.importFile()
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
    Databases = File.importFile()
    for db in Databases:
        if db['name'] == dbName:
            for table in db['tables']:
                if table['name']==tableName:  
                    for col in  table['colmns']:
                        if col['name']==colName:
                            return col
                    return None


def extractTable(dbName, tableName):
   for db in Databases:
        if db['name'] == dbName:
            for table in db['tables']:
                if table['name']==tableName:  
                    return table
            return None

