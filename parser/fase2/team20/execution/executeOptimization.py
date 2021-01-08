def optimize(pila): 
        #Obtener codigo 3D
        #archivo = open("C3D.py", 'r')
        #lines = archivo.readlines()
        #optimizedCode = line
        #optimizedCode = optimizationRules(12,optimizedCode)

        #Obtener cuadruplos solo expresiones
        test = [] #Sustituir esto con PILA
        diccionario = {'resultado':'t0','argumento1':'t0','argumento2':'0','operacion':'+'}
        test.append(diccionario)
        diccionario = {'resultado':'t0','argumento1':'t0','argumento2':'1','operacion':'+'}
        test.append(diccionario)
        diccionario = {'resultado':'t0','argumento1':'t0','argumento2':'0','operacion':'-'}
        test.append(diccionario)
        diccionario = {'resultado':'t0','argumento1':'t0','argumento2':'1','operacion':'*'}
        test.append(diccionario)
        diccionario = {'resultado':'t0','argumento1':'t0','argumento2':'1','operacion':'/'}
        test.append(diccionario)
        diccionario = {'resultado':'t0','argumento1':'t1','argumento2':'0','operacion':'+'}
        test.append(diccionario)

        diccionario = {'resultado':'t0','argumento1':'t1','argumento2':'0','operacion':'-'}
        test.append(diccionario)
        diccionario = {'resultado':'t0','argumento1':'t1','argumento2':'1','operacion':'*'}
        test.append(diccionario)
        diccionario = {'resultado':'t0','argumento1':'t1','argumento2':'1','operacion':'/'}
        test.append(diccionario)
        diccionario = {'resultado':'t0','argumento1':'t1','argumento2':'2','operacion':'*'}
        test.append(diccionario)
        diccionario = {'resultado':'t0','argumento1':'t1','argumento2':'0','operacion':'*'}
        test.append(diccionario)
        diccionario = {'resultado':'t0','argumento1':'0','argumento2':'t1','operacion':'/'}
        test.append(diccionario)

        test = optimizationRules(8,test)
        test = optimizationRules(9,test)
        test = optimizationRules(10,test)
        test = optimizationRules(11,test)
        test = optimizationRules(12,test)
        test = optimizationRules(13,test)
        test = optimizationRules(14,test)
        test = optimizationRules(15,test)
        test = optimizationRules(16,test)
        test = optimizationRules(17,test)
        test = optimizationRules(18,test)
        print(test)
        #pila = optimizationRules(8,pila)
        #return pila 
        #i = 0
        #for line in pila:
            #print(line['resultado'])
            #optimizationRules(i,line)
            #i++

def optimizationRules(rule,pila):
    if(rule == 8):
        return rule8(pila)
    elif(rule == 9):
        return rule9(pila)
    elif(rule == 10):
        return rule10(pila)
    elif(rule == 11):
        return rule11(pila)
    elif(rule == 12):
        return rule12(pila)
    elif(rule == 13):
        return rule13(pila)
    elif(rule == 14):
        return rule14(pila)
    elif(rule == 15):
        return rule15(pila)
    elif(rule == 16):
        return rule16(pila)
    elif(rule == 17):
        return rule17(pila)
    elif(rule == 18):
        return rule18(pila)
    else:
        return pila

#Rules
def rule8(pila):
    optimizedStack = []
    for line in pila:
        if(line['argumento2'] != None):
            if(line['operacion'] == '+'):
                if(line['argumento2'] == '0'):
                    if(line['resultado'] == line['argumento1']):
                        print('Rule 8, Instruccion: '+str(line['resultado'])+'='+str(line['argumento1'])+str(line['operacion'])+str(line['argumento2']) +' Optimizacion: Se elimina la instrucción')
                    else:
                        optimizedStack.append(line) 
                else:
                    optimizedStack.append(line) 
            else:
                optimizedStack.append(line) 
        else:
            optimizedStack.append(line) 
    return optimizedStack

def rule9(pila):
    optimizedStack = []
    for line in pila:
        if(line['argumento2'] != None):
            if(line['operacion'] == '-'):
                if(line['argumento2'] == '0'):
                    if(line['resultado'] == line['argumento1']):
                        print('Rule 9, Instruccion: '+str(line['resultado'])+'='+str(line['argumento1'])+str(line['operacion'])+str(line['argumento2']) +' Optimizacion: Se elimina la instrucción')
                    else:
                        optimizedStack.append(line) 
                else:
                    optimizedStack.append(line) 
            else:
                optimizedStack.append(line) 
        else:
            optimizedStack.append(line) 
    return optimizedStack

def rule10(pila):
    optimizedStack = []
    for line in pila:
        if(line['argumento2'] != None):
            if(line['operacion'] == '*'):
                if(line['argumento2'] == '1'):
                    if(line['resultado'] == line['argumento1']):
                        print('Rule 10, Instruccion: '+str(line['resultado'])+'='+str(line['argumento1'])+str(line['operacion'])+str(line['argumento2']) +' Optimizacion: Se elimina la instrucción')
                    else:
                        optimizedStack.append(line) 
                else:
                    optimizedStack.append(line) 
            else:
                optimizedStack.append(line) 
        else:
            optimizedStack.append(line) 
    return optimizedStack

def rule11(pila):
    optimizedStack = []
    for line in pila:
        if(line['argumento2'] != None):
            if(line['operacion'] == '/'):
                if(line['argumento2'] == '1'):
                    if(line['resultado'] == line['argumento1']):
                        print('Rule 11, Instruccion: '+str(line['resultado'])+'='+str(line['argumento1'])+str(line['operacion'])+str(line['argumento2']) +' Optimizacion: Se elimina la instrucción')
                    else:
                        optimizedStack.append(line) 
                else:
                    optimizedStack.append(line) 
            else:
                optimizedStack.append(line) 
        else:
            optimizedStack.append(line) 
    return optimizedStack

def rule12(pila):
    optimizedStack = []
    for line in pila:
        if(line['argumento2'] != None):
            if(line['operacion'] == '+'):
                if(line['argumento2'] == '0'):
                    print('Rule 12, Instruccion: '+str(line['resultado'])+'='+str(line['argumento1'])+str(line['operacion'])+str(line['argumento2']) +' Optimizacion: '+str(line['resultado'])+'='+str(line['argumento1']))
                    diccionario = {'resultado':str(line['resultado']),'argumento1':str(line['argumento1']),'argumento2':None,'operacion':None}
                    optimizedStack.append(diccionario)
                else:
                    optimizedStack.append(line) 
            else:
                optimizedStack.append(line) 
        else:
            optimizedStack.append(line) 
    return optimizedStack

def rule13(pila):
    optimizedStack = []
    for line in pila:
        if(line['argumento2'] != None):
            if(line['operacion'] == '-'):
                if(line['argumento2'] == '0'):
                    print('Rule 13, Instruccion: '+str(line['resultado'])+'='+str(line['argumento1'])+str(line['operacion'])+str(line['argumento2']) +' Optimizacion: '+str(line['resultado'])+'='+str(line['argumento1']))
                    diccionario = {'resultado':str(line['resultado']),'argumento1':str(line['argumento1']),'argumento2':None,'operacion':None}
                    optimizedStack.append(diccionario)
                else:
                    optimizedStack.append(line) 
            else:
                optimizedStack.append(line) 
        else:
            optimizedStack.append(line) 
    return optimizedStack

def rule14(pila):
    optimizedStack = []
    for line in pila:
        if(line['argumento2'] != None):
            if(line['operacion'] == '*'):
                if(line['argumento2'] == '1'):
                    print('Rule 14, Instruccion: '+str(line['resultado'])+'='+str(line['argumento1'])+str(line['operacion'])+str(line['argumento2']) +' Optimizacion: '+str(line['resultado'])+'='+str(line['argumento1']))
                    diccionario = {'resultado':str(line['resultado']),'argumento1':str(line['argumento1']),'argumento2':None,'operacion':None}
                    optimizedStack.append(diccionario)
                else:
                    optimizedStack.append(line) 
            else:
                optimizedStack.append(line) 
        else:
            optimizedStack.append(line) 
    return optimizedStack

def rule15(pila):
    optimizedStack = []
    for line in pila:
        if(line['argumento2'] != None):
            if(line['operacion'] == '/'):
                if(line['argumento2'] == '1'):
                    print('Rule 15, Instruccion: '+str(line['resultado'])+'='+str(line['argumento1'])+str(line['operacion'])+str(line['argumento2']) +' Optimizacion: '+str(line['resultado'])+'='+str(line['argumento1']))
                    diccionario = {'resultado':str(line['resultado']),'argumento1':str(line['argumento1']),'argumento2':None,'operacion':None}
                    optimizedStack.append(diccionario)
                else:
                    optimizedStack.append(line) 
            else:
                optimizedStack.append(line) 
        else:
            optimizedStack.append(line) 
    return optimizedStack

def rule16(pila):
    optimizedStack = []
    for line in pila:
        if(line['argumento2'] != None):
            if(line['operacion'] == '*'):
                if(line['argumento2'] == '2'):
                    print('Rule 16, Instruccion: '+str(line['resultado'])+'='+str(line['argumento1'])+str(line['operacion'])+str(line['argumento2']) +' Optimizacion: '+str(line['resultado'])+'='+str(line['argumento1'])+str(line['operacion'])+str(line['argumento1']))
                    diccionario = {'resultado':str(line['resultado']),'argumento1':str(line['argumento1']),'argumento2':str(line['argumento1']),'operacion':str(line['operacion'])}
                    optimizedStack.append(diccionario)
                else:
                    optimizedStack.append(line) 
            else:
                optimizedStack.append(line) 
        else:
            optimizedStack.append(line) 
    return optimizedStack

def rule17(pila):
    optimizedStack = []
    for line in pila:
        if(line['argumento2'] != None):
            if(line['operacion'] == '*'):
                if(line['argumento2'] == '0'):
                    print('Rule 17, Instruccion: '+str(line['resultado'])+'='+str(line['argumento1'])+str(line['operacion'])+str(line['argumento2']) +' Optimizacion: '+str(line['resultado'])+'='+str(line['argumento2']))
                    diccionario = {'resultado':str(line['resultado']),'argumento1':str(line['argumento2']),'argumento2':None,'operacion':None}
                    optimizedStack.append(diccionario)
                else:
                    optimizedStack.append(line) 
            else:
                optimizedStack.append(line) 
        else:
            optimizedStack.append(line) 
    return optimizedStack

def rule18(pila):
    optimizedStack = []
    for line in pila:
        if(line['argumento2'] != None):
            if(line['operacion'] == '/'):
                if(line['argumento1'] == '0'):
                    print('Rule 18, Instruccion: '+str(line['resultado'])+'='+str(line['argumento1'])+str(line['operacion'])+str(line['argumento2']) +' Optimizacion: '+str(line['resultado'])+'='+str(line['argumento1']))
                    diccionario = {'resultado':str(line['resultado']),'argumento1':str(line['argumento1']),'argumento2':None,'operacion':None}
                    optimizedStack.append(diccionario)
                else:
                    optimizedStack.append(line) 
            else:
                optimizedStack.append(line) 
        else:
            optimizedStack.append(line) 
    return optimizedStack