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
def createTableC3D(database: str, table: str, numberColumns: int) -> int:
    try:
        if not database.isidentifier()  \
        or not table.isidentifier() \
        or not isinstance(numberColumns, int):
            raise Exception()
        
        ilabel = tempos.incTemporal()  
        f = open("./c3d/codigo3Dgenerado.py", "a")
       
        f.write("   t" + str(ilabel) + "='" + database + "'\n")
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "='" + table + "'\n")
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "=" + str(numberColumns) + "\n")
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "= createTbl(" + "t" + str(ilabel-3) + ",t" + str(ilabel-2) + ",t" + str(ilabel-1)  + ")\n")
        f.write("   \n")
       
        #f.write("main()\n")
        f.close()
        return 0
    except:
        return 1


def insertC3D(database: str, table: str, register: list) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() :
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
                f.write("   t" + str(ilabel) + "=[]" "\n")
            
            if es_numero(valInsert):
                f.write("   t" + str(ilabel) + ".append(" + str(valInsert) + ")\n")
            else:                    
               f.write("   t" + str(ilabel) + ".append('" + str(valInsert) + "')\n")
            
            contadorCol +=1
        
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "=t" + str(ilabel-1) + "\n")
        
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "= existTableC3D(" + "t" + str(ilabel-5) + ",t" + str(ilabel-4) + ")\n")
        f.write("   if t" + str(ilabel) + " is False :\n")
        f.write("       goto .labelt" + str(ilabel+1) + " \n")
        f.write("   else :\n")
        f.write("       goto .labelt" + str(ilabel) + " \n")
        f.write("   label .labelt" + str(ilabel) + "\n")        
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "= insertC3D(" + "t" + str(ilabel-6) + ",t" + str(ilabel-5) + ",t" + str(ilabel-2)  + ")\n")
        f.write("   label .labelt" + str(ilabel) + "\n")        
        f#.write("   print(t" + str(ilabel-1) + ")   \n")
        f.write("   \n")
        
        #f.write("main()\n")
        f.close()
        return 0
    except:
        return 1



def updateC3D(database: str, table: str, register: dict, columns: list) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() :
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


def selectC3D(database: str, table: str, cadenaE: str) -> int:
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
        f.write("   t" + str(ilabel) + "='" + database + "'\n")
        
        contadorCol = 0
        
        ilabel = tempos.incTemporal()          
        f.write("   t" + str(ilabel) + "=[]\n")
        
        for camposel in listacampos:            
            f.write("   t" + str(ilabel) + ".append('" + camposel.strip() + "')\n")            
            contadorCol += 1
        
        contadorTablas = 0
        ilabel = tempos.incTemporal()          
            
        f.write("   t" + str(ilabel) + "=[]\n")
        for tabsel in listaTablas:
            f.write("   t" + str(ilabel) + ".append('" + tabsel.strip() + "')\n")                        
            contadorTablas += 1
                               
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "='" + cadenaWhere.strip() + "'\n")        
        
        
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "= existTableC3D(" + "t" + str(ilabel-4) + ",t" + str(ilabel-2) + "[0])\n")
        f.write("   if t" + str(ilabel) + " is False :\n")
        f.write("       goto .labelt" + str(ilabel+1) + " \n")
        f.write("   else :\n")
        f.write("       goto .labelt" + str(ilabel) + " \n")
        f.write("   label .labelt" + str(ilabel) + "\n")        
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "= selectC3D(" + "t" + str(ilabel-5)  + ",t" + str(ilabel-4) + ",t" + str(ilabel-3) + ",t" + str(ilabel-2) + ")\n")
        f.write("   label .labelt" + str(ilabel) + "\n")        
        f#.write("   print(t" + str(ilabel-1) + ")   \n")
        f.write("   \n")
        
        #f.write("main()\n")
        f.close()
        return 0
    except:
        return 1

def selectC3D1( instruccionsel : any) -> int:
    try:
        selTable = []
        
        fromData = instruccionsel.fromopcional

        where = fromData.whereopcional
        directorioTablas = {}
        tablasFromTemporales = []
        columnasFromTemporales = {}

        for tablasSeleccionadas in fromData.parametros:
            tablasFromTemporales = []
            tablasFromTemporales.append(tablasSeleccionadas.parametros.operador.upper())
            tablasFromTemporales.append(tablasSeleccionadas.asop)
            selTable.append(tablasFromTemporales)

        


        listaCampos = []
        
        for parametros in  instruccionsel.parametros.listadeseleccion:
            listaCamposTemp = []
            listaCamposTemp.append(parametros.listaseleccionados.column)
            listaCamposTemp.append(parametros.listaseleccionados.table)
            listaCampos.append(listaCamposTemp)


        
        if not database.isidentifier() \
        or not table.isidentifier() :
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
                f.write("   t" + str(ilabel) + "=[]" "\n")
            
            if es_numero(valInsert):
                f.write("   t" + str(ilabel) + ".append(" + str(valInsert) + ")\n")
            else:                    
               f.write("   t" + str(ilabel) + ".append('" + str(valInsert) + "')\n")
            
            contadorCol +=1
        
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "=t" + str(ilabel-1) + "\n")
        
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "= existTableC3D(" + "t" + str(ilabel-5) + ",t" + str(ilabel-4) + ")\n")
        f.write("   if t" + str(ilabel) + " is False :\n")
        f.write("       goto .labelt" + str(ilabel+1) + " \n")
        f.write("   else :\n")
        f.write("       goto .labelt" + str(ilabel) + " \n")
        f.write("   label .labelt" + str(ilabel) + "\n")        
        ilabel = tempos.incTemporal() 
        f.write("   t" + str(ilabel) + "= insertC3D(" + "t" + str(ilabel-6) + ",t" + str(ilabel-5) + ",t" + str(ilabel-2)  + ")\n")
        f.write("   label .labelt" + str(ilabel) + "\n")        
        f#.write("   print(t" + str(ilabel-1) + ")   \n")
        f.write("   \n")
        
        #f.write("main()\n")
        f.close()
        return 0
    except:
        return 1


def es_numero(variable : any):
    try:
        float(variable)
        return True
    except :
        return False




