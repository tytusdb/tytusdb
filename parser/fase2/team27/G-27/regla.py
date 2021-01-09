from Optimizacion.Asignaciones.temporal import *
from Optimizacion.Asignaciones.asignacion import *
from Optimizacion.Instrucciones.funcion import *
from Optimizacion.Instrucciones.ins_if import *
from Optimizacion.Asignaciones.label import *
from Optimizacion.Asignaciones.goto_label import *

RepOptimizacion = []

def regla1(arreglo):
    print('inicio regla1')
    j=0
    while j < len(arreglo): #RECORRE ARREGLO DE FUNCIONES
        funcion = arreglo[j].execute().get('func',[])

        i=0
        while i < (len(funcion)): #RECORRE INSTRUCCIONES DE CADA FUNCIÓN
            temporal = funcion[i]  #TEMPORAL DENTRO DE LAS INSTRUCCIONES

            if isinstance(temporal,Asignacion) and len(temporal.execute()) == 2 : #VERIFICACIÓN DE INSTRUCCIÓN DE ASIGNACIÓN
                
                k=i+1
                while k < (len(funcion)): # RECORRER INSTRUCCIONES DELANTE DEL TEMPORAL
                    temporal2 = funcion[k]

                    if isinstance(temporal2,Asignacion) and len(temporal2.execute()) == 2 :
                        if temporal.execute()['temp'] == temporal2.execute()['val'] and  temporal.execute()['val'] == temporal2.execute()['temp'] :
                            RepOptimizacion.append({'antiguo': temporal2.toString(0), 'regla': '1', 'nuevo': 'SE ELIMINA INSTRUCCION'})
                            funcion.pop(k)
                            break
                        else:
                            if temporal.execute()['temp'] == temporal2.execute()['temp']:
                                #print('REASIGNAR: NO OPTIMIZAR REGLA 1', temporal.execute()['temp'])
                                break
                    elif isinstance(temporal2,Label) :
                        #print('LABEL: NO OPTIMIZAR REGLA 1', temporal.execute()['temp'])
                        break
                    k+=1
            i+=1
        j+=1
                 
def regla2(arreglo):
    print('inicio regla2')
    j = 0
    while j < (len(arreglo)): #RECORRE ARREGLO DE FUNCIONES
        funcion = arreglo[j].execute().get('func',[])

        i = 0
        while i < (len(funcion)): #RECORRE INSTRUCCIONES DE CADA FUNCIÓN
            goto = funcion[i]  #TEMPORAL DENTRO DE LAS INSTRUCCIONES

            if isinstance(goto,Goto_Label): #VERIFICACIÓN DE INSTRUCCIÓN DE ASIGNACIÓN
                
                k = i+1
                while k < (len(funcion) ): # RECORRER INSTRUCCIONES DELANTE DEL TEMPORAL
                    label = funcion[k]

                    if isinstance(label,Label): # SI LA INSTRCCIÓN ES UN LABEL
                        if label.execute()['label'] == goto.execute()['goto']:  # LABEL IGUALES
                            antiguo = ''
                            for l in range(i,k):
                                antiguo += '\n'+ funcion[l].toString(0)
                                funcion.pop(i)
                            i=k-i

                            RepOptimizacion.append({'antiguo': antiguo, 'regla': '2', 'nuevo': label.toString(0)})
                            #print('OPTIMIZAR: REGLA 2', goto.execute()['goto'])
                            break
                        else:
                            #print('LABEL: NO OPTIMIZAR', goto.execute()['goto'], label.execute()['label'])
                            break
                    k+=1
            i+=1
        j+=1

def regla3(arreglo):
    print('inicio regla3')
    j = 0
    while j < (len(arreglo)): #RECORRE ARREGLO DE FUNCIONES
        funcion = arreglo[j].execute().get('func',[])

        i = 0
        while i < (len(funcion)): #RECORRE INSTRUCCIONES DE CADA FUNCIÓN
            ins_if = funcion[i]  #TEMPORAL DENTRO DE LAS INSTRUCCIONES

            if isinstance(ins_if,Ins_if):
                if isinstance(funcion[i+1],Goto_Label):
                    
                    antiguo = ''
                    for l in range(i-1,i+3):
                        antiguo += '\n' + funcion[l].toString(0)

                    ins_if.setGoto(funcion[i+1].getGoto())
                    
                    operacion = funcion[i-1].getOperacion()
                    if operacion == '==':
                        funcion[i-1].setOperacion('!=')
                    elif operacion == '!=':
                        funcion[i-1].setOperacion('==')
                    elif operacion == '<':
                        funcion[i-1].setOperacion('>=')
                    elif operacion == '>':
                        funcion[i-1].setOperacion('<=')
                    elif operacion == '<=':
                        funcion[i-1].setOperacion('>')
                    elif operacion == '>=':
                        funcion[i-1].setOperacion('<')
                        
                    funcion.pop(i+1)
                    
                    nuevo = ''
                    for l in range(i-1,i+1):
                        nuevo += '\n' + funcion[l].toString(0)

                    RepOptimizacion.append({'antiguo': antiguo, 'regla': '3', 'nuevo': nuevo})
            i+=1

        j+=1

def regla4(arreglo):
    print('inicio regla4')
    j = 0
    while j < (len(arreglo)): #RECORRE ARREGLO DE FUNCIONES
        funcion = arreglo[j].execute().get('func',[])

        i = 0
        while i < (len(funcion)): #RECORRE INSTRUCCIONES DE CADA FUNCIÓN
            ins_if = funcion[i]  #TEMPORAL DENTRO DE LAS INSTRUCCIONES

            if isinstance(ins_if,Ins_if):
                temporal = funcion[i-1]
                goto  = funcion[i+1]
                if isinstance(temporal,Asignacion) and isinstance(goto,Goto_Label):
                    if temporal.getIzquierda() == temporal.getDerecha() and temporal.getOperacion() == '==':
                        antiguo = ''
                        for l in range(i-1, i+2):
                            antiguo += '\n' + funcion[l].toString(0)
                        funcion.insert(i-1,Goto_Label(funcion[i].getGoto()))
                        funcion.pop(i)
                        funcion.pop(i)
                        funcion.pop(i)
                        i-=1

                        nuevo = funcion[i].toString(0)
                        RepOptimizacion.append({'antiguo': antiguo, 'regla': '4', 'nuevo': nuevo})

            i+=1        
        j+=1

def regla5(arreglo):
    print('inicio regla5')
    j = 0
    while j < (len(arreglo)): #RECORRE ARREGLO DE FUNCIONES
        funcion = arreglo[j].execute().get('func',[])

        i = 0
        while i < (len(funcion)): #RECORRE INSTRUCCIONES DE CADA FUNCIÓN
            ins_if = funcion[i]  #TEMPORAL DENTRO DE LAS INSTRUCCIONES

            if isinstance(ins_if,Ins_if):
                temporal = funcion[i-1]
                goto  = funcion[i+1]
                if isinstance(temporal,Asignacion) and isinstance(goto,Goto_Label):
                    if temporal.getIzquierda() != temporal.getDerecha() and temporal.getOperacion() == '==':
                        antiguo = ''
                        for l in range(i-1, i+2):
                            antiguo += '\n' + funcion[l].toString(0)
                        funcion.pop(i-1)
                        funcion.pop(i-1)
                        i-=1

                        nuevo = funcion[i].toString(0)
                        RepOptimizacion.append({'antiguo': antiguo, 'regla': '5', 'nuevo': nuevo})

            i+=1        
        j+=1

def regla6(arreglo):
    print('inicio regla6')
    j = 0
    while j < (len(arreglo)): #RECORRE ARREGLO DE FUNCIONES
        funcion = arreglo[j].execute().get('func',[])

        i = 0
        while i < (len(funcion)): #RECORRE INSTRUCCIONES DE CADA FUNCIÓN
            goto = funcion[i]  #TEMPORAL DENTRO DE LAS INSTRUCCIONES

            if isinstance(goto,Goto_Label): #VERIFICACIÓN DE INSTRUCCIÓN DE ASIGNACIÓN
                
                k = i+1
                while k < (len(funcion) ): # RECORRER INSTRUCCIONES DELANTE DEL TEMPORAL
                    label = funcion[k]

                    if isinstance(label,Label): # SI LA INSTRCCIÓN ES UN LABEL
                        if label.execute()['label'] == goto.execute()['goto']:  # LABEL IGUALES
                            if (k+1) < len(funcion) and isinstance(funcion[k+1],Goto_Label): #SI LA INSTRUCCIÓN SIGUIENTE ES UN GOTO
                                antiguo = ''
                                antiguo += '\n'+ goto.toString(0)
                                antiguo += '\n'+ label.toString(0)
                                antiguo += '\n'+ funcion[k+1].toString(0)
                                
                                goto.setGoto(funcion[k+1].getGoto())

                                nuevo = ''
                                nuevo += '\n'+ goto.toString(0)
                                nuevo += '\n'+ label.toString(0)
                                nuevo += '\n'+ funcion[k+1].toString(0)
                                RepOptimizacion.append({'antiguo': antiguo, 'regla': '6', 'nuevo': nuevo})
                                #print('OPTIMIZAR: REGLA 2', goto.execute()['goto'])
                            break
                        else:
                            #print('LABEL: NO OPTIMIZAR', goto.execute()['goto'], label.execute()['label'])
                            break
                    k+=1
            i+=1
        j+=1

def regla7(arreglo):
    print('inicio regla7')
    j = 0
    while j < (len(arreglo)): #RECORRE ARREGLO DE FUNCIONES
        funcion = arreglo[j].execute().get('func',[])

        i = 0
        while i < (len(funcion)): #RECORRE INSTRUCCIONES DE CADA FUNCIÓN
            ins_if = funcion[i]

            if isinstance(ins_if,Ins_if):  #IF DENTRO DE LAS INSTRUCCIONES
                k = i+1
                while k < (len(funcion)): # RECORRER INSTRUCCIONES DELANTE DEL TEMPORAL
                    label = funcion[k]

                    if isinstance(label,Label): # SI LA INSTRCCIÓN ES UN LABEL
                        if ins_if.getGoto() == label.getLabel():  # LABEL IGUALES
                            if (k+1) < len(funcion) and isinstance(funcion[k+1],Goto_Label): #SI LA INSTRUCCIÓN SIGUIENTE ES UN GOTO
                                antiguo = ''
                                antiguo += '\n'+ ins_if.toString(0)
                                antiguo += '\n'+ label.toString(0)
                                antiguo += '\n'+ funcion[k+1].toString(0)
                                
                                ins_if.setGoto(funcion[k+1].getGoto())

                                nuevo = ''
                                nuevo += '\n'+ ins_if.toString(0)
                                nuevo += '\n'+ label.toString(0)
                                nuevo += '\n'+ funcion[k+1].toString(0)
                                RepOptimizacion.append({'antiguo': antiguo, 'regla': '7', 'nuevo': nuevo})
                                #print('OPTIMIZAR: REGLA 2', goto.execute()['goto'])
                                break
                    k+=1
            i+=1        
        j+=1

def regla8_18(arreglo):
    print('INICIO REGLA 8-18')
    k = 0
    while k < (len(arreglo)):
        if isinstance(arreglo[k],Funcion):

            instruccion = arreglo[k].execute().get('func',[])
            
            i=0
            while i < (len(instruccion)):
                if isinstance(instruccion[i],Asignacion) and len(instruccion[i].execute()) == 4:
                    asignacion = instruccion[i].execute()

                    if asignacion['op'] == '+':

                        if asignacion['temp'] == asignacion['izq']:
                            if asignacion['der'] == 0:
                                RepOptimizacion.append({'antiguo': instruccion[i].toString(0), 'regla': '8', 'nuevo': 'SE ELIMINA INSTRUCCION'})
                                instruccion.pop(i)
                                i-=1
                                continue
                        elif asignacion['temp'] == asignacion['der']:
                            if asignacion['izq'] == 0:
                                RepOptimizacion.append({'antiguo': instruccion[i].toString(0), 'regla': '8', 'nuevo': 'SE ELIMINA INSTRUCCION'})
                                instruccion.pop(i)
                                i-=1
                                continue
                        
                        elif asignacion['izq'] == 0:
                            antiguo = instruccion[i].toString(0)

                            instruccion[i].setIzquierda(asignacion['der'])
                            instruccion[i].setOperacion(None)
                            instruccion[i].setDerecha(None)
                            nuevo = instruccion[i].toString(0)

                            RepOptimizacion.append({'antiguo': antiguo, 'regla': '12', 'nuevo': nuevo})
                            i-=1
                            continue
                        elif asignacion['der'] == 0:
                            antiguo = instruccion[i].toString(0)
                            instruccion[i].setDerecha(None)
                            instruccion[i].setOperacion(None)
                            nuevo = instruccion[i].toString(0)

                            RepOptimizacion.append({'antiguo': antiguo, 'regla': '12', 'nuevo': nuevo})
                            i-=1
                            continue

                    elif instruccion[i].execute()['op'] == '-':
                        
                        if asignacion['temp'] == asignacion['izq']:
                            if asignacion['der'] == 0:
                                RepOptimizacion.append({'antiguo': instruccion[i].toString(0), 'regla': '9', 'nuevo': 'SE ELIMINA INSTRUCCION'})
                                instruccion.pop(i)
                                i-=1
                                continue
                        else:
                            if asignacion['der'] == 0:
                                antiguo = instruccion[i].toString(0)

                                instruccion[i].setOperacion(None)
                                instruccion[i].setDerecha(None)
                                nuevo = instruccion[i].toString(0)

                                RepOptimizacion.append({'antiguo': antiguo, 'regla': '13', 'nuevo': nuevo})
                                i-=1
                                continue

                    elif instruccion[i].execute()['op'] == '*':
                        
                        if asignacion['temp'] == asignacion['izq']:
                            if asignacion['der'] == 1:
                                RepOptimizacion.append({'antiguo': instruccion[i].toString(0), 'regla': '10', 'nuevo': 'SE ELIMINA INSTRUCCION'})
                                instruccion.pop(i)
                                i-=1
                                continue
                        elif asignacion['temp'] == asignacion['der']:
                            if asignacion['izq'] == 1:
                                RepOptimizacion.append({'antiguo': instruccion[i].toString(0), 'regla': '10', 'nuevo': 'SE ELIMINA INSTRUCCION'})
                                instruccion.pop(i)
                                i-=1
                                continue

                        elif asignacion['izq'] == 1:
                            antiguo = instruccion[i].toString(0)

                            instruccion[i].setIzquierda(asignacion['der'])
                            instruccion[i].setOperacion(None)
                            instruccion[i].setDerecha(None)
                            nuevo = instruccion[i].toString(0)

                            RepOptimizacion.append({'antiguo': antiguo, 'regla': '14', 'nuevo': nuevo})
                            i-=1
                            continue
                        elif asignacion['der'] == 1:
                            antiguo = instruccion[i].toString(0)

                            instruccion[i].setOperacion(None)
                            instruccion[i].setDerecha(None)
                            nuevo = instruccion[i].toString(0)

                            RepOptimizacion.append({'antiguo': antiguo, 'regla': '14', 'nuevo': nuevo})
                            i-=1
                            continue
                        elif asignacion['izq'] == 0 or asignacion['der'] == 0:
                            antiguo = instruccion[i].toString(0)

                            instruccion[i].setIzquierda(0)
                            instruccion[i].setOperacion(None)
                            instruccion[i].setDerecha(None)
                            nuevo = instruccion[i].toString(0)

                            RepOptimizacion.append({'antiguo': antiguo, 'regla': '17', 'nuevo': nuevo})
                            i-=1
                            continue
                        else:
                            if asignacion['izq'] == 2:
                                antiguo = instruccion[i].toString(0)

                                instruccion[i].setIzquierda(asignacion['der'])
                                instruccion[i].setOperacion('+')
                                nuevo = instruccion[i].toString(0)

                                RepOptimizacion.append({'antiguo': antiguo, 'regla': '16', 'nuevo': nuevo})
                                i-=1
                                continue
                            elif asignacion['der'] == 2:
                                antiguo = instruccion[i].toString(0)

                                instruccion[i].setDerecha(asignacion['izq'])
                                instruccion[i].setOperacion('+')
                                nuevo = instruccion[i].toString(0)

                                RepOptimizacion.append({'antiguo': antiguo, 'regla': '16', 'nuevo': nuevo})
                                i-=1
                                continue
                        
                    elif instruccion[i].execute()['op'] == '/':

                        if asignacion['temp'] == asignacion['izq']:
                            if asignacion['der'] == 1:
                                RepOptimizacion.append({'antiguo': instruccion[i].toString(0), 'regla': '11', 'nuevo': 'SE ELIMINA INSTRUCCION'})
                                instruccion.pop(i)
                                i-=1
                                continue
                        elif asignacion['der'] == 1:
                            antiguo = instruccion[i].toString(0)

                            instruccion[i].setOperacion(None)
                            instruccion[i].setDerecha(None)
                            nuevo = instruccion[i].toString(0)

                            RepOptimizacion.append({'antiguo': antiguo, 'regla': '15', 'nuevo': nuevo})
                            i-=1
                            continue
                        elif asignacion['izq'] == 0:
                            antiguo = instruccion[i].toString(0)

                            instruccion[i].setIzquierda(0)
                            instruccion[i].setOperacion(None)
                            instruccion[i].setDerecha(None)
                            nuevo = instruccion[i].toString(0)

                            RepOptimizacion.append({'antiguo': antiguo, 'regla': '18', 'nuevo': nuevo})
                            i-=1
                            continue
                i+=1
        k+=1

def limipiarReporte():
    RepOptimizacion.clear()

def Optimizar(arreglo):
    regla1(arreglo)
    regla2(arreglo)
    regla3(arreglo)
    regla4(arreglo)
    regla5(arreglo)
    regla6(arreglo)
    regla7(arreglo)
    regla8_18(arreglo)

    return RepOptimizacion

