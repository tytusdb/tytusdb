# Package:      C3D Gen
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Team 01

import os 
import json
import temporalesp as temposg

tempos = temposg.temporalesp()

path = 'c3d/'

#dataPath = path + 'databases'
   
##################
# Databases CRUD #
##################

# CREATE a database checking their existence
def createDatabaseC3D(database: str) -> int:
    try:
        if not database.isidentifier():
            raise Exception()
        ilabel = tempos.incTemporal() 
        
        
        f = open("./c3d/codigo3Dgenerado.py", "a")
        
        f.write("   t" + str(ilabel) + "='" + database + "'\n")
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "= createDB(" + "t" + str(ilabel-1) + "" + ")\n")
        f.write("   \n")
        
        
        f.close()
        return 0
    except:
        return 1


# CREATE a database checking their existence
def useC3D(database: str) -> int:
    try:
        if not database.isidentifier():
            raise Exception()
        ilabel = tempos.incTemporal()  
        f = open("./c3d/codigo3Dgenerado.py", "a")
      
        f.write("   t" + str(ilabel) + "='" + database + "'\n")
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "= useDatabase(" + "t" + str(ilabel-1) + "" + ")\n")
        f.write("   \n")
        
        
        f.close()
        return 0
    except:
        return 1
###############
# Tables CRUD #
###############

# CREATE a table checking their existence
def createTableC3D(database: str, table: str, numberColumns: int, cadenaE : str) -> int:
    try:

        if not database.isidentifier() or not table.isidentifier() or not isinstance(numberColumns, int):
            raise Exception()
        
        cadenaCreate = cadenaE.split('TABLE')
        cadenaTabla = cadenaCreate[1].split('(',1)
        cadenaCampos = cadenaTabla[1].split(',')
        ultimoCampo = cadenaCampos[len(cadenaCampos)-1]
        ultimoCampo = ultimoCampo.replace(')','')
        ultimoCampo = ultimoCampo.replace(';','')
        cadenaCampos[len(cadenaCampos)-1] = ultimoCampo
        
        listaTablas = []
        cadenaWhere = None
        
                

        ilabel = tempos.incTemporal()  
        f = open("./c3d/codigo3Dgenerado.py", "a")
       
        

        f.write("   t" + str(ilabel) + "='" + database + "'\n")
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "='" + table + "'\n")
        
        
        contadorCol = 0
        
        ilabel = tempos.incTemporal()          
        f.write("   t" + str(ilabel) + "=[]\n")
        
        for camposel in cadenaCampos:            
            f.write("   t" + str(ilabel) + ".append('" + camposel.strip() + "')\n")            
            contadorCol += 1
        
        
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "= createTbl(" + "t" + str(ilabel-3) + ",t" + str(ilabel-2) + ",t" + str(ilabel-1)  + ")\n")
        f.write("   \n")
       
        #f.write("main()\n")
        f.close()
        return 0
    except:
        return 1


def insertC3D(database: str, table: str, register: list, posIdentado: str) -> int:
    try:
        if not database.isidentifier() or not table.isidentifier() :
            raise Exception()
        
        ilabel = tempos.incTemporal()  
        f = open("./c3d/codigo3Dgenerado.py", "a")
       
        f.write(posIdentado + "t" + str(ilabel) + "='" + database + "'\n")
        ilabel = tempos.incTemporal() 
        f.write(posIdentado + "t" + str(ilabel) + "='" + table + "'\n")
        contadorCol = 0
        
        ilabel = tempos.incTemporal() 
        #f.write("   t" + str(ilabel) + "='" + str(register) + "'\n")
        
        ilabel = tempos.incTemporal() 
            
        for valInsert in register :
            if contadorCol==0 :
                f.write(posIdentado + "t" + str(ilabel) + "=[]" "\n")
            
            if es_numero(valInsert):
                f.write(posIdentado + "t" + str(ilabel) + ".append(" + str(valInsert) + ")\n")
            else:                    
               f.write(posIdentado + "t" + str(ilabel) + ".append('" + str(valInsert) + "')\n")
            
            contadorCol +=1
        
        ilabel = tempos.incTemporal() 
        f.write(posIdentado + "t" + str(ilabel) + "=t" + str(ilabel-1) + "\n")
        
        ilabel = tempos.incTemporal() 
        f.write(posIdentado + "t" + str(ilabel) + "= existTableC3D(" + "t" + str(ilabel-5) + ",t" + str(ilabel-4) + ")\n")
        f.write(posIdentado + "if t" + str(ilabel) + " is False :\n")
        f.write(posIdentado + "    goto .labelt" + str(ilabel+1) + " \n")
        f.write(posIdentado + "else :\n")
        f.write(posIdentado + "    goto .labelt" + str(ilabel) + " \n")
        f.write(posIdentado + "label .labelt" + str(ilabel) + "\n")        
        ilabel = tempos.incTemporal() 
        f.write(posIdentado + "t" + str(ilabel) + "= insertC3D(" + "t" + str(ilabel-6) + ",t" + str(ilabel-5) + ",t" + str(ilabel-2)  + ")\n")
        f.write(posIdentado + "label .labelt" + str(ilabel) + "\n")        
        f#.write("   print(t" + str(ilabel-1) + ")   \n")
        f.write("   \n")
        
        #f.write("main()\n")
        f.close()
        return 0
    except:
        return 1



def updateC3D(database: str, table: str, register: dict, columns: list) -> int:
    try:
        if not database.isidentifier() or not table.isidentifier() :
            raise Exception()
        
        ilabel = tempos.incTemporal()  
        f = open("./c3d/codigo3Dgenerado.py", "a")
       
        f.write("   t" + str(ilabel) + "='" + database + "'\n")
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "='" + table + "'\n")
        contadorCol = 0
        
        ilabel = tempos.incTemporal() 
        #f.write("   t" + str(ilabel) + "='" + str(register) + "'\n")
        
        ilabel = tempos.incTemporal() 
            
        for valInsert in register :
            if contadorCol==0 :
                f.write("   t" + str(ilabel) + "={}" "\n")
            
            if es_numero(register[valInsert]):
                f.write("   t" + str(ilabel) + "[" + str(valInsert) + "] = " + str(register[valInsert]) + "\n")
            else:                    
               f.write("   t" + str(ilabel) + "[" + str(valInsert) + "] = '" + str(register[valInsert]) + "'\n")
            
            contadorCol +=1
        
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "=t" + str(ilabel-1) + "\n")
        

        ilabel = tempos.incTemporal() 
        contadorCol=0    
        for valInsert in columns :
            if contadorCol==0 :
                f.write("   t" + str(ilabel) + "=[]" "\n")
            
            if es_numero(valInsert):
                f.write("   t" + str(ilabel) + ".append(" + str(valInsert) + ")\n")
            else:                    
               f.write("   t" + str(ilabel) + ".append('" + str(valInsert) + "')\n")
            
            contadorCol +=1
    
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "=t" + str(ilabel-1) + "\n")
        
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "= existTableC3D(" + "t" + str(ilabel-7) + ",t" + str(ilabel-6) + ")\n")
        f.write("   if t" + str(ilabel) + " is False :\n")
        f.write("       goto .labelt" + str(ilabel+1) + " \n")
        f.write("   else :\n")
        f.write("       goto .labelt" + str(ilabel) + " \n")
        f.write("   label .labelt" + str(ilabel) + "\n")        
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "= updateC3D(" + "t" + str(ilabel-8) + ",t" + str(ilabel-7) + ",t" + str(ilabel-4) + ",t" + str(ilabel-2) + ")\n")
        f.write("   label .labelt" + str(ilabel) + "\n")        
        f#.write("   print(t" + str(ilabel-1) + ")   \n")
        f.write("   \n")
        
        #f.write("main()\n")
        f.close()
        return 0
    except:
        return 1

def selectC3D(database: str, table: str, cadenaE: str, posIdentado: str ) -> int:
    try:        
        cadenaSelect = cadenaE.split('SELECT')
        
        listaTablas = []
        cadenaWhere = None
        cadenaCampos = cadenaSelect[1].split('FROM')
        listacampos = cadenaCampos[0].split(',')        
        if len(cadenaCampos)>1:   
                cadenaTablas = cadenaCampos[1].split('WHERE')
                listaTablas = cadenaTablas[0].split(',')
                if len(cadenaTablas)>1:
                    cadenaWhere = cadenaTablas[1]
                
        
        
        f = open("./c3d/codigo3Dgenerado.py", "a")
        ilabel = tempos.incTemporal() 
        f.write(posIdentado + "t" + str(ilabel) + "='" + database + "'\n")
        
        contadorCol = 0
        
        ilabel = tempos.incTemporal()          
        f.write(posIdentado + "t" + str(ilabel) + "=[]\n")
                 
        for camposel in listacampos:            
            f.write(posIdentado + "t" + str(ilabel) + ".append('" + camposel.strip() + "')\n")            
            contadorCol += 1
        
        contadorTablas = 0
        ilabel = tempos.incTemporal()          
            
        f.write(posIdentado + "t" + str(ilabel) + "=[]\n")
        for tabsel in listaTablas:
            f.write(posIdentado + "t" + str(ilabel) + ".append('" + tabsel.strip() + "')\n")                        
            contadorTablas += 1
                               
        ilabel = tempos.incTemporal() 
        if cadenaWhere == None:
            f.write(posIdentado + "t" + str(ilabel) + "=''\n")        
        else:
            fexpar=cadenaWhere.find('STR')
            cadenaPar = ''
            if fexpar>=0:
                cadenaWheres = cadenaWhere.split('STR')
                cadenaPar = cadenaWheres[1].replace(')','')
                cadenaPar = cadenaWheres[1].replace('(','')
                cadenaWhere = cadenaWheres[0].strip()
                f.write(posIdentado + "t" + str(ilabel) + "='" + cadenaWhere.strip() + "' + str(" + str(cadenaPar) + "\n")        
            else:
                f.write(posIdentado + "t" + str(ilabel) + "='" + cadenaWhere.strip() + "'\n")        
        
        ilabel = tempos.incTemporal() 
        f.write(posIdentado + "t" + str(ilabel) + "= existTableC3D(" + "t" + str(ilabel-4) + ",t" + str(ilabel-2) + "[0])\n")
        f.write(posIdentado + "if t" + str(ilabel) + " is False :\n")
        f.write(posIdentado + "   goto .labelt" + str(ilabel+1) + " \n")
        f.write(posIdentado + "else :\n")
        f.write(posIdentado + "   goto .labelt" + str(ilabel) + " \n")
        f.write(posIdentado + "label .labelt" + str(ilabel) + "\n")        
        ilabel = tempos.incTemporal() 
        f.write(posIdentado + "t" + str(ilabel) + "= selectC3D(" + "t" + str(ilabel-5)  + ",t" + str(ilabel-4) + ",t" + str(ilabel-3) + ",t" + str(ilabel-2) + ")\n")
        f.write(posIdentado + "label .labelt" + str(ilabel) + "\n")        
        #f.write(posIdentado + "print(t" + str(ilabel-1) + ")   \n")
        f.write("   \n")
        
        #f.write("main()\n")
        f.close()
        return 0
    except:
        return 1


# CREACION DE FUNCIONES
def createFunctionC3D(database: str, nombre : str, arg1: any, arg2 : any, arg3 : any, arg4 : any, cuerpo : any) -> int:
    try:

        if not database.isidentifier():
            raise Exception()

        
        listaparamf = []
        listaparamVars=[]
 
        contadorParam = 0;
        ilabel = tempos.incTemporal() 
        for parametrof in arg2:
            paramf = {}
            paramf['nombre'] = parametrof.table.upper()
            listaparamVars.append(parametrof.table.upper())
            parTipoUp = parametrof.column['ast'].type.upper()
            parTipo = parTipoUp.find("TEXT") 
            if parTipo >=0 :
                paramf['tipo'] = 'str'                
            else :
                parTipo = parTipoUp.find("VARCHAR") 
                if parTipo >=0:
                    paramf['tipo'] = 'str'     
                else:
                    parTipo = parTipoUp.find("INTEGER") 
                    if parTipo >=0:
                        paramf['tipo'] = 'int'     
                    else:
                        paramf['tipo'] = parTipoUp
            
            paramf['temporal'] = "pt" + str(ilabel)
            listaparamf.append(paramf)
        
        cadenaE = arg3
         
        f = open("./c3d/codigo3Dgenerado.py", "a")
        
        ilabel = tempos.incTemporal() 
        f.write("   @with_goto \n" )        
        f.write("   def " + nombre + "(" )
        contadorParam = 0
        for prm in listaparamf:
            if contadorParam==0:
                f.write(str(prm['nombre']) + ":" + str(prm['tipo']))
            else:
                f.write("," + str(prm['nombre']) + ":" + str(prm['tipo']))
            contadorParam+=1
        f.write("):\n")
        

        # cadenaBloque1 = cadenaE.split('BEGIN')
        # cadenaBloque2 = cadenaBloque1[1].rsplit('END')
        # cadenabloque= cadenaBloque2[0].upper()
        # cadenabloque= cadenabloque.replace('\n','')
        # cadenabloque="["+ str(cadenabloque) +"]"
        # operaciones = json.loads(cadenabloque)

   
        # for operacion in operaciones:
        #     if(operacion['BLOQUE']=='RETURN'):
        #         varReturn = operacion['CADENA'].replace('RETURN','')
        #         varReturn = varReturn.replace(';','')
        #         varReturn = varReturn.strip()

        #         ilabel = tempos.incTemporal() 
        #         f.write("       t" + str(ilabel) + "=" + str(varReturn) + "\n")     
        #         f.write("       return t" + str(ilabel) + "\n")   
            

        for operacion in cuerpo.instrucciones:
            if hasattr(operacion,'paramReturn'):
                ilabel = tempos.incTemporal() 
                f.write("       t" + str(ilabel) + "=" + str(operacion.paramArg.column.upper()) + "\n")     
                f.write("       return t" + str(ilabel) + "\n")   
            else:
                if hasattr(operacion[0].asignaciones,'operador'):
                    x = 'peracion[0].variable.column'
                    cadenaS = operacion[0].asignaciones.operador.arg1.upper() 
                    cadenaS = cadenaS.strip()

                    cadenaConParams = cadenaS

                    for cadPar in listaparamVars:
                        cadenaConParamslist = cadenaConParams.split(cadPar)
                        
                        #for rcad in cadenaConParamslist                            
                        ipar = 0
                        while ipar<(len(cadenaConParamslist)-1):
                            cadenaConParams = cadenaConParamslist[ipar] + " str(" + cadPar + ") " + cadenaConParamslist[ipar+1]
                            ipar+=1
                            cadenaConParamslist[ipar] = cadenaConParams

                    f.write("\n")
                    f.close()
                    valRetSel = selectC3D(database, 'tabla', cadenaConParams.upper(), '       ')     

                    f = open("./c3d/codigo3Dgenerado.py", "a")
                    ilabel = tempos.incTemporal() 
                    f.write("       " + str(operacion[0].variable.column.upper()) + "=t" + str(ilabel-1) + "\n")     
                    f.write("\n")
                    
                else:
                    if (hasattr(operacion[0].asignaciones.leftOperator,'column') or hasattr(operacion[0].asignaciones.leftOperator,'val')) and (hasattr(operacion[0].asignaciones.rightOperator,'column') or hasattr(operacion[0].asignaciones.rightOperator,'val')) :
                        ilabel = tempos.incTemporal() 
                        #if es_numero(operacion[0].asignaciones.leftOperator.column):
                        if 1==1:
                            if hasattr(operacion[0].asignaciones.leftOperator,'column'):
                                f.write("       t" + str(ilabel) + "=" + str(operacion[0].asignaciones.leftOperator.column.upper()) + "\n")     
                            else:
                                f.write("       t" + str(ilabel) + "=" + str(operacion[0].asignaciones.leftOperator.val) + "\n")     
                        else:
                            if hasattr(operacion[0].asignaciones.leftOperator,'column'):
                                f.write("       t" + str(ilabel) + "=" + str(operacion[0].asignaciones.leftOperator.column.upper()) + "\n") 
                            else:
                                f.write("       t" + str(ilabel) + "=" + str(operacion[0].asignaciones.leftOperator.val) + "\n") 
                    
                        ilabel = tempos.incTemporal() 
                        #if es_numero(operacion[0].asignaciones.rightOperator.column):
                        if 1==1:
                            if hasattr(operacion[0].asignaciones.rightOperator,'column'):
                                f.write("       t" + str(ilabel) + "=" + str(operacion[0].asignaciones.rightOperator.column.upper()) + "\n")     
                            else:
                                f.write("       t" + str(ilabel) + "=" + str(operacion[0].asignaciones.rightOperator.val) + "\n")     

                        else:
                            if hasattr(operacion[0].asignaciones.rightOperator,'column'):
                                f.write("       t" + str(ilabel) + "=" + str(operacion[0].asignaciones.rightOperator.column.upper()) + "\n")     
                            else:
                                f.write("       t" + str(ilabel) + "=" + str(operacion[0].asignaciones.rightOperator.val) + "\n")     
                    
                        ilabel = tempos.incTemporal() 
                        f.write("       t" + str(ilabel) + "=t" + str(ilabel-2) + " " + operacion[0].asignaciones.sign + " t" + str(ilabel-1) + "\n")     
                        f.write("       " + str(operacion[0].variable.column.upper()) + "=t" + str(ilabel) + "\n")     
                    else:
                        if hasattr(operacion[0].asignaciones.leftOperator,'column'):
                            ilabel = tempos.incTemporal() 
                            if es_numero(operacion[0].asignaciones.leftOperator.column):
                                f.write("       t" + str(ilabel) + "=" + str(operacion[0].asignaciones.leftOperator.column.upper()) + "\n")     
                            else:
                                f.write("       t" + str(ilabel) + "=" + str(operacion[0].asignaciones.leftOperator.column.upper()) + "\n") 
                        else:
                            if hasattr(operacion[0].asignaciones.leftOperator.leftOperator,'column'):
                                ilabel = tempos.incTemporal() 
                                if es_numero(operacion[0].asignaciones.leftOperator.leftOperator.column):
                                    f.write("       t" + str(ilabel) + "=" + str(operacion[0].asignaciones.leftOperator.leftOperator.column.upper()) + "\n")     
                                else:
                                    f.write("       t" + str(ilabel) + "=" + str(operacion[0].asignaciones.leftOperator.leftOperator.column.upper()) + "\n") 

                                ilabel = tempos.incTemporal() 
                                
                                if es_numero(operacion[0].asignaciones.leftOperator.rightOperator.column):
                                    f.write("       t" + str(ilabel) + "=" + str(operacion[0].asignaciones.leftOperator.rightOperator.column.upper()) + "\n")     
                                else:
                                    f.write("       t" + str(ilabel) + "=" + str(operacion[0].asignaciones.leftOperator.rightOperator.column.upper()) + "\n")     
                            
                                ilabel = tempos.incTemporal() 
                                f.write("       t" + str(ilabel) + "=t" + str(ilabel-2) + " " + operacion[0].asignaciones.leftOperator.sign + " t" + str(ilabel-1) + "\n")     
                                #f.write("       " + str(operacion[0].leftOperator.variable.column.upper()) + "=t" + str(ilabel) + "\n")     

                        if hasattr(operacion[0].asignaciones.rightOperator,'tipofuncionTrigonometrica'):
                            ilabel = tempos.incTemporal() 
                            #f.write("       t" + str(ilabel) + "=" + str(operacion[0].asignaciones.rightOperator.tipofuncionTrigonometrica.upper()) + "(" + str(operacion[0].asignaciones.rightOperator.arg1.val) + ")\n")     
                            f.write("       t" + str(ilabel) + "=" + str(operacion[0].asignaciones.rightOperator.arg1.val) + "\n")     



                        # operador operacion
                        ilabel = tempos.incTemporal() 
                        f.write("       t" + str(ilabel) + "=t" + str(ilabel-2) + " " + operacion[0].asignaciones.sign + " t" + str(ilabel-1) + "\n")     
                        f.write("       " + str(operacion[0].variable.column.upper()) + "=t" + str(ilabel) + "\n")     




        f.write("\n")
        
        f.close()
        return 0
    except:
        return 1



# CREACION DE PROCEDIMIENTOS
def createProcedureC3D(database: str, nombre : str, arg2 : any, cuerpo : any) -> int:
    try:

        if not database.isidentifier():
            raise Exception()

        
        listaparamf = []
 
        if arg2 == None:
            arg2 = []

        contadorParam = 0;
        ilabel = tempos.incTemporal() 
        for parametrof in arg2:
            paramf = {}
            paramf['nombre'] = parametrof.table.upper()
            parTipoUp = parametrof.column['ast'].type.upper()
            parTipo = parTipoUp.find("TEXT") 
            if parTipo >=0 :
                paramf['tipo'] = 'str'
            else :
                parTipo = parTipoUp.find("VARCHAR") 
                if parTipo >=0:
                    paramf['tipo'] = 'str'     
                else:
                    parTipo = parTipoUp.find("INTEGER") 
                    if parTipo >=0:
                        paramf['tipo'] = 'int'     
                    else:
                        paramf['tipo'] = parTipoUp
            
            paramf['temporal'] = "pt" + str(ilabel)
            listaparamf.append(paramf)
        
        
         
        f = open("./c3d/codigo3Dgenerado.py", "a")
        
        ilabel = tempos.incTemporal() 
        f.write("   @with_goto \n" )        
        f.write("   def " + nombre + "(" )
        contadorParam = 0
        for prm in listaparamf:
            if contadorParam==0:
                f.write(str(prm['nombre']) + ":" + str(prm['tipo']))
            else:
                f.write("," + str(prm['nombre']) + ":" + str(prm['tipo']))
            contadorParam+=1
        f.write("):\n")
        

        # cadenaBloque1 = cadenaE.split('BEGIN')
        # cadenaBloque2 = cadenaBloque1[1].rsplit('END')
        # cadenabloque= cadenaBloque2[0].upper()
        # cadenabloque= cadenabloque.replace('\n','')
        # cadenabloque="["+ str(cadenabloque) +"]"
        # operaciones = json.loads(cadenabloque)

   
        # for operacion in operaciones:
        #     if(operacion['BLOQUE']=='RETURN'):
        #         varReturn = operacion['CADENA'].replace('RETURN','')
        #         varReturn = varReturn.replace(';','')
        #         varReturn = varReturn.strip()

        #         ilabel = tempos.incTemporal() 
        #         f.write("       t" + str(ilabel) + "=" + str(varReturn) + "\n")     
        #         f.write("       return t" + str(ilabel) + "\n")   
            

        for operacion in cuerpo.instrucciones:
            if operacion.arg0.upper() == 'RETURN':
                ilabel = tempos.incTemporal() 
                returnVal = operacion.arg1.upper().split('RETURN')
                returnVal = returnVal[1].strip()
                returnVal = returnVal.replace(';','')
                f.write("       t" + str(ilabel) + "=" + str(returnVal) + "\n")     
                f.write("       return t" + str(ilabel) + "\n")   
            else:
                if operacion.arg0.upper() == 'INSERT':
                    x = 'peracion[0].variable.column'

                    listaCamposIns = []
                    for lscamp in operacion.values:
                        if hasattr(lscamp,'tipofuncionfehca'):
                            listaCamposIns.append(lscamp.tipofuncionfehca.upper()+"()")
                        else:
                            listaCamposIns.append(lscamp.val)
                    
                    # cadenaS = operacion.arg1.upper() 
                    # cadenaS = 'INSERT ' + cadenaS
                    # cadenaS = cadenaS.strip()
                    f.write("\n")
                    f.close()
                    insertC3D(database, operacion.tableid.upper(), listaCamposIns, '       ')     

                    f = open("./c3d/codigo3Dgenerado.py", "a")
                    ilabel = tempos.incTemporal() 
                    #f.write("       " + str(operacion[0].variable.column.upper()) + "=t" + str(ilabel-1) + "\n")     
                    f.write("\n")
                    
                



        f.write("\n")
        
        f.close()
        return 0
    except:
        return 1







# SELECT function
def select_functionC3D(nombre: str, parametros: any) -> int:
    try:

        f = open("./c3d/codigo3Dgenerado.py", "a")        
        ilabel = tempos.incTemporal() 
        
        listadeParametros = []
        contadorParams = 0
        if parametros==None:
            parametros = []
        for parmf in parametros:
            ilabel = tempos.incTemporal() 
            contadorParams += 1
            if str(parmf.type) =='string':
                f.write("   t" + str(ilabel) + "='" + str(parmf.val) + "'\n")
            else:
                f.write("   t" + str(ilabel) + "=" + str(parmf.val) + "\n")
            
        
        
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "= " + nombre + "(")
        
        i=0
        while i < contadorParams :
            if i==0:
                f.write("t" + str(ilabel-contadorParams+i) )
            else:
                f.write(",t" + str(ilabel-contadorParams+i) )
            i += 1
        f.write(")\n")


        f.write("   \n")
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "= print(t" + str(ilabel-1)  + ")\n")
        f.write("   \n")
        
        f.close()
        return 0
    except:
        return 1


# SELECT procedure
def select_procedureC3D(nombre: str, parametros: any) -> int:
    try:

        f = open("./c3d/codigo3Dgenerado.py", "a")        
        ilabel = tempos.incTemporal() 
        
        listadeParametros = []
        contadorParams = 0
        if parametros==None:
            parametros = []

        for parmf in parametros:
            ilabel = tempos.incTemporal() 
            contadorParams += 1
            if str(parmf.type) =='string':
                f.write("   t" + str(ilabel) + "='" + str(parmf.val) + "'\n")
            else:
                f.write("   t" + str(ilabel) + "=" + str(parmf.val) + "\n")
            
        
        
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "= " + nombre + "(")
        
        i=0
        while i < contadorParams :
            if i==0:
                f.write("t" + str(ilabel-contadorParams+i) )
            else:
                f.write(",t" + str(ilabel-contadorParams+i) )
            i += 1
        f.write(")\n")


        f.write("   \n")
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "= print(t" + str(ilabel-1)  + ")\n")
        f.write("   \n")
        
        f.close()
        return 0
    except:
        return 1

# def selectC3D1( instruccionsel : any) -> int:
#     try:
#         selTable = []
        
#         fromData = instruccionsel.fromopcional

#         where = fromData.whereopcional
#         directorioTablas = {}
#         tablasFromTemporales = []
#         columnasFromTemporales = {}

#         for tablasSeleccionadas in fromData.parametros:
#             tablasFromTemporales = []
#             tablasFromTemporales.append(tablasSeleccionadas.parametros.operador.upper())
#             tablasFromTemporales.append(tablasSeleccionadas.asop)
#             selTable.append(tablasFromTemporales)

        


#         listaCampos = []
        
#         for parametros in  instruccionsel.parametros.listadeseleccion:
#             listaCamposTemp = []
#             listaCamposTemp.append(parametros.listaseleccionados.column)
#             listaCamposTemp.append(parametros.listaseleccionados.table)
#             listaCampos.append(listaCamposTemp)


        
#         if not database.isidentifier() \
#         or not table.isidentifier() :

#         raise Exception()
        
#         ilabel = tempos.incTemporal()  
#         f = open("./c3d/codigo3Dgenerado.py", "a")
       
#         f.write("   t" + str(ilabel) + "='" + database + "'\n")
#         ilabel = tempos.incTemporal() 
#         f.write("   t" + str(ilabel) + "='" + table + "'\n")
#         contadorCol = 0
        
#         ilabel = tempos.incTemporal() 
#         #f.write("   t" + str(ilabel) + "='" + str(register) + "'\n")
        
#         ilabel = tempos.incTemporal() 
            
#         for valInsert in register :
#             if contadorCol==0 :
#                 f.write("   t" + str(ilabel) + "=[]" "\n")
            
#             if es_numero(valInsert):
#                 f.write("   t" + str(ilabel) + ".append(" + str(valInsert) + ")\n")
#             else:                    
#                f.write("   t" + str(ilabel) + ".append('" + str(valInsert) + "')\n")
            
#             contadorCol +=1
        
#         ilabel = tempos.incTemporal() 
#         f.write("   t" + str(ilabel) + "=t" + str(ilabel-1) + "\n")
        
#         ilabel = tempos.incTemporal() 
#         f.write("   t" + str(ilabel) + "= existTableC3D(" + "t" + str(ilabel-5) + ",t" + str(ilabel-4) + ")\n")
#         f.write("   if t" + str(ilabel) + " is False :\n")
#         f.write("       goto .labelt" + str(ilabel+1) + " \n")
#         f.write("   else :\n")
#         f.write("       goto .labelt" + str(ilabel) + " \n")
#         f.write("   label .labelt" + str(ilabel) + "\n")        
#         ilabel = tempos.incTemporal() 
#         f.write("   t" + str(ilabel) + "= insertC3D(" + "t" + str(ilabel-6) + ",t" + str(ilabel-5) + ",t" + str(ilabel-2)  + ")\n")
#         f.write("   label .labelt" + str(ilabel) + "\n")        
#         f#.write("   print(t" + str(ilabel-1) + ")   \n")
#         f.write("   \n")
        
#         #f.write("main()\n")
#         f.close()
#         return 0
#     except:
#         return 1


def es_numero(variable : any):
    try:
        float(variable)
        return True
    except :
        return False




