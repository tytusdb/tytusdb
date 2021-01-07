from Optimizacion.Asignaciones.temporal import *
from Optimizacion.Asignaciones.asignacion import *
from Optimizacion.Instrucciones.funcion import *
from Optimizacion.Asignaciones.label import *
from Optimizacion.Asignaciones.goto_label import *

def regla1(arreglo):
    print('inicio regla1')
    for j in range(len(arreglo)): #RECORRE ARREGLO DE FUNCIONES
        print(arreglo[j].execute())
        funcion = arreglo[j].execute()['func']

        for i in range(len(funcion)): #RECORRE INSTRUCCIONES DE CADA FUNCIÓN
            temporal = funcion[i]  #TEMPORAL DENTRO DE LAS INSTRUCCIONES

            if isinstance(temporal,Asignacion) and len(temporal.execute()) == 2 : #VERIFICACIÓN DE INSTRUCCIÓN DE ASIGNACIÓN
                
                for k in range(i+1, len(funcion) ): # RECORRER INSTRUCCIONES DELANTE DEL TEMPORAL
                    temporal2 = funcion[k]

                    if isinstance(temporal2,Asignacion) and len(temporal2.execute()) == 2 :
                        if temporal.execute()['temp'] == temporal2.execute()['val'] and  temporal.execute()['val'] == temporal2.execute()['temp'] :
                            print('OPTIMIZAR: REGLA 1', temporal.execute()['temp'])
                            break
                        else:
                            if temporal.execute()['temp'] == temporal2.execute()['temp']:
                                print('REASIGNAR: NO OPTIMIZAR REGLA 1', temporal.execute()['temp'])
                                break
                    elif isinstance(temporal2,Label) :
                        print('LABEL: NO OPTIMIZAR REGLA 1', temporal.execute()['temp'])
                        break


                 
def regla2(arreglo):
    print('inicio regla2')
    for j in range(len(arreglo)): #RECORRE ARREGLO DE FUNCIONES
        print(arreglo[j].execute())
        funcion = arreglo[j].execute()['func']

        for i in range(len(funcion)): #RECORRE INSTRUCCIONES DE CADA FUNCIÓN
            goto = funcion[i]  #TEMPORAL DENTRO DE LAS INSTRUCCIONES

            if isinstance(goto,Goto_Label): #VERIFICACIÓN DE INSTRUCCIÓN DE ASIGNACIÓN
                
                for k in range(i+1, len(funcion) ): # RECORRER INSTRUCCIONES DELANTE DEL TEMPORAL
                    label = funcion[k]

                    if isinstance(label,Label):
                        if label.execute()['label'] == goto.execute()['goto']:
                            print('OPTIMIZAR: REGLA 2', goto.execute()['goto'])
                            break
                        else:
                            print('LABEL: NO OPTIMIZAR', goto.execute()['goto'], label.execute()['label'])
                            break


def regla3(arreglo):
    pass

def regla4(arreglo):
    pass

def regla5(arreglo):
    pass

def regla6(arreglo):
    pass

def regla7(arreglo):
    pass

def regla8_18(arreglo):
    print('regla8')
    index = []
    for item in range(len(arreglo)):
        if isinstance(arreglo[item],Funcion):

            arreglo2 = arreglo[item].execute()['func']
            for item2 in range(len(arreglo2)):

                if( len(arreglo2[item2].execute()) == 4):
                    val = arreglo2[item2].execute()
                    print(val)

                    if val['op'] == '+':

                        if val['temp'] == val['izq']:
                            if val['der'] == 0:
                                print('OPTIMIZACION REGLA 8 ELIMINAR INSTRUCCION')
                        elif val['temp'] == val['der']:
                            if val['izq'] == 0:
                                print('OPTIMIZACION REGLA 8 ELIMINAR INSTRUCCION')
                        
                        elif val['izq'] == 0:
                            print('OPTIMIZACION REGLA 12')
                        elif val['der'] == 0:
                            print('OPTIMIZACION REGLA 12')

                                
                    if arreglo2[item2].execute()['op'] == '-':
                        
                        if val['temp'] == val['izq']:
                            if val['der'] == 0:
                                print('OPTIMIZACION REGLA 9 ELIMINAR INSTRUCCION')
                        else:
                            if val['der'] == 0:
                                print('OPTIMIZACION REGLA 13')

                    if arreglo2[item2].execute()['op'] == '*':
                        
                        if val['temp'] == val['izq']:
                            if val['der'] == 1:
                                print('OPTIMIZACION REGLA 10 ELIMINAR INSTRUCCION')
                        elif val['der'] == 1:
                            print('OPTIMIZACION REGLA 14')
                        elif val['izq'] == 0 or val['der'] == 0:
                            print('OPTIMIZACION REGLA 17')
                        else:
                            if val['izq'] == 2:
                                print('OPTIMIZACION REGLA 16')
                            elif val['der'] == 2:
                                print('OPTIMIZACION REGLA 16')
                        
                    if arreglo2[item2].execute()['op'] == '/':

                        if val['temp'] == val['izq']:
                            if val['der'] == 1:
                                print('OPTIMIZACION REGLA 11 ELIMINAR INSTRUCCION')
                        elif val['der'] == 1:
                            print('OPTIMIZACION REGLA 15')
                        elif val['der'] == 0:
                            print('OPTIMIZACION REGLA 18')



def Optimizar(arreglo):
    regla1(arreglo)

