from .storageManager import jsonMode
from .storageManager.TypeChecker import TCcreateDatabase,TCSearchDatabase,TCdropDatabase,TCgetDatabase,TCcreateTable,TCcreateType,TCaddCheckTable,TCaddPrimaryKey,TCaddUnique,TCgetToInherit,TCcreateIndex
from .executeExpression import executeExpression,Relational
from .AST.sentence import ColumnId,ColumnCheck,ColumnConstraint,ColumnUnique,ColumnPrimaryKey,ColumnForeignKey
from .AST.error import * 

import os 
import json

import sys
sys.path.append("../")
from console import * 

def executeCreateDatabase(self, database):
    # crear en base a la condicion FALTA AGREGAR REPLACE Y OWNERMODE
    mode=1
    if(database.OwnerMode[1]!= None):
        res = executeExpression(self,database.OwnerMode[1])
        if(isinstance(res,Error)): 
            print_error("SEMANTIC ERROR",res.toString(),2)
        else: mode = res.value
        
    if(database.ifNotExistsFlag and not(database.OrReplace)):
        if mode==1:
            return jsonMode.createDatabase(database.name)
        elif mode==2:
            return jsonMode.createDatabase(database.name)
        elif mode==3:
            return jsonMode.createDatabase(database.name)
        elif mode==4:
            return jsonMode.createDatabase(database.name)
        else:
            print_error("SEMANTIC ERROR",'Mode between 1-5',2)
            return 1

    elif(database.ifNotExistsFlag and database.OrReplace):
        res=TCSearchDatabase(database.name)

        if(res==8):
            mode=1
            if(database.OwnerMode[1]!= None ):
                res = executeExpression(self,database.OwnerMode[1])
                if(isinstance(res,Error)): 
                    print_error("SEMANTIC ERROR",res.toString(),2)
                else: mode = res.value
            if mode==1:
                return jsonMode.createDatabase(database.name)
            elif mode==2:
                return jsonMode.createDatabase(database.name)
            elif mode==3:
                return jsonMode.createDatabase(database.name)
            elif mode==4:
                return jsonMode.createDatabase(database.name)
            else:
                print_error("SEMANTIC ERROR",'Mode between 1-5',2)
                return 1
        else:
            TCdropDatabase(database.name)
            if res==1:
                jsonMode.dropDatabase(database.name)
            elif res==2:
                jsonMode.dropDatabase(database.name)
            elif res==3:
                jsonMode.dropDatabase(database.name)
            elif res==4:
                jsonMode.dropDatabase(database.name)
            else:
                print_error("SEMANTIC ERROR",'Mode between 1-5',2)
                return 1
            
            mode=1
            if(database.OwnerMode[1]!= None ):
                res = executeExpression(self,database.OwnerMode[1])
                if(isinstance(res,Error)): 
                    print_error("SEMANTIC ERROR",res.toString(),2)
                else: mode = res.value
            if mode==1:
                return jsonMode.createDatabase(database.name)
            elif mode==2:
                return jsonMode.createDatabase(database.name)
            elif mode==3:
                return jsonMode.createDatabase(database.name)
            elif mode==4:
                return jsonMode.createDatabase(database.name)
            else:
                print_error("SEMANTIC ERROR",'Mode between 1-5',2)
                return 1

    elif(not(database.ifNotExistsFlag) and not(database.OrReplace)):
       
        if mode==1:
            return jsonMode.createDatabase(database.name)
        elif mode==2:
            return jsonMode.createDatabase(database.name)
        elif mode==3:
            return jsonMode.createDatabase(database.name)
        elif mode==4:
            return jsonMode.createDatabase(database.name)
        else:
            print_error("SEMANTIC ERROR",'Mode between 1-5',2)
            return 1

    else:
        res=TCSearchDatabase(database.name)

        if(res==8):            
            if mode==1:
                return jsonMode.createDatabase(database.name)
            elif mode==2:
                return jsonMode.createDatabase(database.name)
            elif mode==3:
                return jsonMode.createDatabase(database.name)
            elif mode==4:
                return jsonMode.createDatabase(database.name)
            else:
                print_error("SEMANTIC ERROR",'Mode between 1-5',2)
                return 1
        else:
            TCdropDatabase(database.name)
            if res==1:
                jsonMode.dropDatabase(database.name)
            elif res==2:
                jsonMode.dropDatabase(database.name)
            elif res==3:
                jsonMode.dropDatabase(database.name)
            elif res==4:
                jsonMode.dropDatabase(database.name)
            else:
                print_error("SEMANTIC ERROR",'Mode between 1-5',2)
                return 1
            
            if mode==1:
                return jsonMode.createDatabase(database.name)
            elif mode==2:
                return jsonMode.createDatabase(database.name)
            elif mode==3:
                return jsonMode.createDatabase(database.name)
            elif mode==4:
                return jsonMode.createDatabase(database.name)
            else:
                print_error("SEMANTIC ERROR",'Mode between 1-5',2)
                return 1

    return 1

def executeCreateTable(self, table): 
    database=TCgetDatabase()
    array={}
    NColumns=0
    ids={}
    primary=0

    primaryskey=[]

    if(table.columns!= None):
        for node in table.columns:
            if isinstance(node,ColumnId):
                null=0
                notnull=0
                default=0
                constrains1={}
                constrains2=[]
                array1={}
                NColumns+=1
                new1={'TYPE':node.type[0]}
                constrains1.update(new1)
                if (len(node.type)==2):
                    new={'MAXLENGTH':node.type[1]}
                    constrains1.update(new)
                if(node.options!=None):
                    if'primary' in node.options:
                        primary+=1
                        new={'PRIMARY':node.options['primary']}
                        primaryskey.append(NColumns-1)
                        constrains1.update(new)
                    if 'default' in node.options:
                        default+=1
                        va= executeExpression(self,node.options['default'])   
                        new={'DEFAULT':va.value}
                        constrains1.update(new)
                    if 'null' in node.options:
                        if(node.options['null']==True):
                            null+=1
                        else:
                            notnull+=1

                        new={'NULL':node.options['null']}
                        constrains1.update(new)
                    if 'unique' in node.options:
                        new={'UNIQUE':node.options['unique']}
                        constrains1.update(new)
                    if 'references' in node.options:
                        '''val= TCValidateReference(database,table.name)
                        if(val==0):
                            print("ERROR:no sirve")
                        if(val==1):
                            print("ERROR:no sirve")
                        if(val==2):
                            print("ERROR:no sirve")
                        if(val==3):
                            print("ERROR:no sirve")'''
                    if 'check' in node.options:
                        if isinstance(node.options['check'],Relational):
                            lacolumna=0
                            if(node.options['check'].value1.type!=4):
                                lacolumna=node.options['check'].value1.value
                            elif(node.options['check'].value2.type!=4):
                                lacolumna=node.options['check'].value2.value
                            constrains2.append({'OP':node.options['check'].type,'VALUE':lacolumna})
                        else:
                            print_error("SEMANTIC ERROR",'Only relational operations acept check',2)
                            return 1 
            
                if(node.name in ids):
                    print_error("SEMANTIC ERROR",'column '+node.name+' specified more than once SQL state: 42701',2)
                    return 1
                ids.update({node.name:node.name})
                array.update({node.name:{'CONST':constrains1,'CHECKS':constrains2}})
        
    if(table.columns!= None):
        for node in table.columns:        
            if isinstance(node,ColumnCheck):
                if isinstance(node.expression,Relational):
                    lacolumna=0
                    valor=0
                    if(node.expression.value1.type==4):
                        lacolumna=node.expression.value1.value
                        valor=node.expression.value2.value
                    elif(node.expression.value2.type==4):
                        lacolumna=node.expression.value2.value
                        valor=node.expression.value1.value
                    array[lacolumna]['CHECKS'].append({'OP':node.expression.type,'VALUE':valor})
                    #print(TCaddCheckTable(database,table.name,lacolumna,valor,node.expression.type))
                else:
                    print_error("SEMANTIC ERROR",'Only relational operations acept check',2)
                    return 1
            if isinstance(node,ColumnConstraint):
                if isinstance(node.expression,Relational):
                    lacolumna=0
                    valor=0
                    if(node.expression.value1.type==4):
                        lacolumna=node.expression.value1.value
                        valor=node.expression.value2.value
                    elif(node.expression.value2.type==4):
                        lacolumna=node.expression.value2.value
                        valor=node.expression.value1.value
                    array[lacolumna]['CHECKS'].append({'OP':node.expression.type,'VALUE':valor})
                    #print(TCaddCheckTable(database,table.name,lacolumna,valor,node.expression.type))
                else:
                    print_error("SEMANTIC ERROR",'Only relational operations acept check',2)
                    return 1
            if isinstance(node,ColumnUnique):
                for x in node.columnslist:
                    new={'UNIQUE':True}
                    if x in array:
                        array[x]['CONST'].update(new)
                    else:
                        print_error("SEMANTIC ERROR",'column '+x+' does not exist ',2)
                        return 1
                    #constrains1.update(new)
                    #TCaddUnique(database,table.name,x,True)
            if isinstance(node,ColumnPrimaryKey):
                primary+=1
                
                for x in node.columnslist:
                    new={'PRIMARY':True}
                    if x in array:
                        array[x]['CONST'].update(new)
                        primaryskey.append(list(array).index(x))
                    else:
                        print_error("SEMANTIC ERROR",'column '+x+' does not exist ',2)
                        return 1
                    #constrains1.update(new)
                    #TCaddPrimaryKey(database,table.name,x,True)
        
    if(table.inherits!=None):
        n=TCgetToInherit(database,table.inherits)
        if(bool(n)): 
            array.update(n)
            for i in n:
                if i in ids:
                    print_error("SEMANTIC ERROR",'column '+i+' specified more than once SQL state: 42701',2)
                    return 1
                NColumns+=1
                if 'PRIMARY' in n[i]['CONST']:
                    primaryskey.append(NColumns-1)
                #array.update(i)

    if(primary>1):
        print_error("SEMANTIC ERROR",'multiple primary keys for table '+ table.name+' are not allowed SQL state: 42P16',2)
        return 1

    
    result=TCcreateTable(database,table.name,array)
    if(result!=0):
        return result
            
    mode=TCSearchDatabase(database)
    
    if(mode==1):
        res= jsonMode.createTable(database,table.name,NColumns)
        if res==0 and primary>0:
            jsonMode.alterAddPK(database, table.name, primaryskey)
        return res
    elif(mode==2):
        res= jsonMode.createTable(database,table.name,NColumns)
        if res==0 and primary>0:
            jsonMode.alterAddPK(database, table.name, primaryskey)
        return res
    elif(mode==3):
        res= jsonMode.createTable(database,table.name,NColumns)
        if res==0 and primary>0:
            jsonMode.alterAddPK(database, table.name, primaryskey)
        return res
    elif(mode==5):
        res= jsonMode.createTable(database,table.name,NColumns)
        if res==0 and primary>0:
            jsonMode.alterAddPK(database, table.name, primaryskey)
        return res
    else:
        print_error("SEMANTIC ERROR",'Mode between 1-5',2)
        return 1
            
            
          
    
    #{"Type":,type,"Name":,"MaxLength":,"DefaultFlag":,"PrimaryKeyFlag":,"NullFlag":,"Constrains":[]}
    #
        
def executeCreateType(self, typeEnum):
    database=TCgetDatabase()
    array={}
    if(typeEnum.expressions!=None):
        i = 0
        for node in typeEnum.expressions:
            res=executeExpression(self,node)
            if(isinstance(res,Error)): 
                print_error("SEMANTIC ERROR",res.toString(),2)
                return 1
            elif(res.type == 3):
                new={str(i):res.value}
                array.update(new)
                i=i+1
            elif(res.type == 5):
                res.value = res.value.replace("'","")
                new={str(i):res.value}
                array.update(new)
                i=i+1
            else:
                return 1
                
        #print(array)
        mode=TCSearchDatabase(database)
        if(mode==1):
            return TCcreateType(database,typeEnum.name,array) 
        elif(mode==2):
            return TCcreateType(database,typeEnum.name,array) 
        elif(mode==3):
            return TCcreateType(database,typeEnum.name,array) 
        elif(mode==4):
            return TCcreateType(database,typeEnum.name,array) 
        elif(mode==8):
            return TCcreateType(database,typeEnum.name,array) 
        else:
            print_error("SEMANTIC ERROR",'Mode between 1-5',2)
            return 1

def executeCreateUnique(self,unique):
    database=TCgetDatabase()
    mode=TCSearchDatabase(database)
    #print(unique.ascdesc)
    ascdesc='ASC'
    '''if(len(unique.ascdesc)==2):
        ascdesc=unique.ascdesc[1]'''
    if(mode==1):
        return TCcreateIndex(database,unique.table,unique.ascdesc,unique.name)
    elif(mode==2):
        return TCcreateIndex(database,unique.table,unique.ascdesc[0],unique.name) 
    elif(mode==3):
        return TCcreateIndex(database,unique.table,unique.ascdesc[0],unique.name) 
    elif(mode==4):
        return TCcreateIndex(database,unique.table,unique.ascdesc[0],unique.name)
    elif(mode==8):
        return TCcreateIndex(database,unique.table,unique.ascdesc[0],unique.name)
    else:
        print_error("SEMANTIC ERROR",'Mode between 1-5',2)
        return 1

    