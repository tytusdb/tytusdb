import os
import sys
import reportes as h





def optimizacion_de_codigo(entra):
    #script_dir = os.path.dirname(os.path.abspath(__file__))
    #direction = script_dir + "\\codigo3D.py"
    #archivo= open(direction, "r")
    #cadena=archivo.read()
    cadena=entra
    print(cadena)
    pasada=purgarCadena(cadena)
    pasada=regla5(pasada)
    pasada=regla8(pasada)
    pasada=regla9(pasada)
    pasada=regla10(pasada)
    pasada=regla11(pasada)
    pasada=regla12(pasada)
    pasada=regla13(pasada)
    pasada=regla14(pasada)
    pasada=regla15(pasada)
    pasada=regla16(pasada)
    pasada=regla17(pasada)
    pasada=regla18(pasada)
    a=construir_cadena(pasada)
    print(a)
    escribir3DOptimizado(a)
    h.textosalida+="--------------------INICIO DE LA OPTIMIZACION--------------------\n"
    h.textosalida+=a
    h.textosalida+="--------------------FIN DE LA OPTIMIZACION--------------------\n"
    return h.textosalida

def purgarCadena(cadena):
    resultado=cadena.splitlines()
    linea=""
    analizar=[]
    analizarString=""
    #print(resultado)
    for line in range(0,len(resultado)):
        print("linea normal: ",resultado[line])
        linea=resultado[line].split(" ")
        if '' in linea:
            print("si esta")
            print("linea spliteada: ",linea)
            linea.remove('')
            print("linea sin espacio: ",linea)
            analizar.append(linea)
        else:
            print("no esta")
            print("linea spliteada: ",linea)

            analizar.append(linea)
    print("-------------------------- la salida PARA optimizar es -------------------------")
    for line in range(0,len(analizar)):
        #salidaString
        print(analizar[line])
    return analizar

#-------------------------------------------------------------------------------------------------------------------
#                       REGLA DE OPTIMIZACION 12 X= Y + 0 => 
def regla12(entrada):
    for line in range(0,len(entrada)):
        #salidaString
        #print(entrada[line])
        if len(entrada[line])>=5:
            if entrada[line][2]=="0" and entrada[line][3]=="+" and entrada[line][4]!="0":
                a=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])+" "+str(entrada[line][3])+" "+str(entrada[line][4])
                del(entrada[line][2])
                del(entrada[line][2])
                b=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
                h.reportitoOptimizado+="<tr><td>N. 12</td><td>x= y + 0</td><td>"+a+"</td><td>"+b+"</td></tr>\n"
            elif entrada[line][2]!="0" and entrada[line][3]=="+" and entrada[line][4]=="0":
                print("LA SALIDA NORMAL SERIA: ", entrada[line])
                a=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])+" "+str(entrada[line][3])+" "+str(entrada[line][4])
                del(entrada[line][3])
                del(entrada[line][3])
                b=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
                h.reportitoOptimizado+="<tr><td>N. 12</td><td>x= y + 0</td><td>"+a+"</td><td>"+b+"</td></tr>\n"
            else:
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
        else:
            print("LA SALIDA normal SERIA: ", entrada[line])
    print("cadena regla 12:\n",entrada)
    return entrada

#-------------------------------------------------------------------------------------------------------------------
#                       REGLA DE OPTIMIZACION 13 X= Y - 0 => 
def regla13(entrada):
    for line in range(0,len(entrada)):
        #salidaString
        #print(entrada[line])
        if len(entrada[line])>=5:
            if entrada[line][2]=="0" and entrada[line][3]=="-" and entrada[line][4]!="0":
                a=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])+" "+str(entrada[line][3])+" "+str(entrada[line][4])
                del(entrada[line][2])
                del(entrada[line][2])
                b=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])
                h.reportitoOptimizado+="<tr><td>N. 13</td><td>x= y - 0</td><td>"+a+"</td><td>"+b+"</td></tr>\n"
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
            elif entrada[line][2]!="0" and entrada[line][3]=="-" and entrada[line][4]=="0":
                a=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])+" "+str(entrada[line][3])+" "+str(entrada[line][4])
                print("LA SALIDA NORMAL SERIA: ", entrada[line])
                del(entrada[line][3])
                del(entrada[line][3])
                b=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])
                h.reportitoOptimizado+="<tr><td>N. 13</td><td>x= y - 0</td><td>"+a+"</td><td>"+b+"</td></tr>\n"
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
            else:
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
        else:
            print("LA SALIDA normal SERIA: ", entrada[line])
    print("cadena regla 13:\n",entrada)
    return entrada


#-------------------------------------------------------------------------------------------------------------------
#                       REGLA DE OPTIMIZACION 14 X= Y * 1 => 
def regla14(entrada):
    for line in range(0,len(entrada)):
        #salidaString
        #print(entrada[line])
        if len(entrada[line])>=5:
            if entrada[line][2]=="1" and entrada[line][3]=="*" and entrada[line][4]!="1":
                a=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])+" "+str(entrada[line][3])+" "+str(entrada[line][4])
                del(entrada[line][2])
                del(entrada[line][2])
                b=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])
                h.reportitoOptimizado+="<tr><td>N. 14</td><td>x= y * 1</td><td>"+a+"</td><td>"+b+"</td></tr>\n"
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
            elif entrada[line][2]!="1" and entrada[line][3]=="*" and entrada[line][4]=="1":
                a=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])+" "+str(entrada[line][3])+" "+str(entrada[line][4])
                print("LA SALIDA NORMAL SERIA: ", entrada[line])
                del(entrada[line][3])
                del(entrada[line][3])
                b=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])
                h.reportitoOptimizado+="<tr><td>N. 14</td><td>x= y * 1 </td><td>"+a+"</td><td>"+b+"</td></tr>\n"
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
            else:
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
        else:
            print("LA SALIDA normal SERIA: ", entrada[line])
    print("cadena regla 14:\n",entrada)
    return entrada

#-------------------------------------------------------------------------------------------------------------------
#                       REGLA DE OPTIMIZACION 15 X= Y / 1 => 
def regla15(entrada):
    for line in range(0,len(entrada)):
        #salidaString
        #print(entrada[line])
        if len(entrada[line])>=5:
            if entrada[line][2]=="1" and entrada[line][3]=="/" and entrada[line][4]!="1":
                a=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])+" "+str(entrada[line][3])+" "+str(entrada[line][4])
                del(entrada[line][2])
                del(entrada[line][2])
                b=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])
                h.reportitoOptimizado+="<tr><td>N. 15</td><td>x= y / 1</td><td>"+a+"</td><td>"+b+"</td></tr>\n"
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
            elif entrada[line][2]!="1" and entrada[line][3]=="/" and entrada[line][4]=="1":
                a=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])+" "+str(entrada[line][3])+" "+str(entrada[line][4])
                print("LA SALIDA NORMAL SERIA: ", entrada[line])
                del(entrada[line][3])
                del(entrada[line][3])
                b=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])
                h.reportitoOptimizado+="<tr><td>N. 15</td><td>x= y / 1</td><td>"+a+"</td><td>"+b+"</td></tr>\n"
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
            else:
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
        else:
            print("LA SALIDA normal SERIA: ", entrada[line])
    print("cadena regla 15:\n",entrada)
    return entrada

#-------------------------------------------------------------------------------------------------------------------
#                       REGLA DE OPTIMIZACION 16 X= Y *2 => 
def regla16(entrada):
    for line in range(0,len(entrada)):
        #salidaString
        #print(entrada[line])
        if len(entrada[line])>=5:
            if entrada[line][2]=="2" and entrada[line][3]=="*" and entrada[line][4]!="2":
                a=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])+" "+str(entrada[line][3])+" "+str(entrada[line][4])
                entrada[line][3]="+"
                entrada[line][2]=entrada[line][4]
                b=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])+" "+str(entrada[line][3])+" "+str(entrada[line][4])
                h.reportitoOptimizado+="<tr><td>N. 16</td><td>x= y * 2</td><td>"+a+"</td><td>"+b+"</td></tr>\n"
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
            elif entrada[line][2]!="2" and entrada[line][3]=="*" and entrada[line][4]=="2":
                a=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])+" "+str(entrada[line][3])+" "+str(entrada[line][4])
                print("LA SALIDA NORMAL SERIA: ", entrada[line])
                entrada[line][3]="+"
                entrada[line][4]=entrada[line][2]
                b=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])+" "+str(entrada[line][3])+" "+str(entrada[line][4])
                h.reportitoOptimizado+="<tr><td>N. 16</td><td>x= y * 2 </td><td>"+a+"</td><td>"+b+"</td></tr>\n"
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
            else:
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
        else:
            print("LA SALIDA normal SERIA: ", entrada[line])
    print("cadena regla 14:\n",entrada)
    return entrada

#-------------------------------------------------------------------------------------------------------------------
#                       REGLA DE OPTIMIZACION 17 X= Y * 0 => 
def regla17(entrada):
    for line in range(0,len(entrada)):
        #salidaString
        #print(entrada[line])
        if len(entrada[line])>=5:
            if entrada[line][2]=="0" and entrada[line][3]=="*" and entrada[line][4]!="0":
                a=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])+" "+str(entrada[line][3])+" "+str(entrada[line][4])
                del(entrada[line][3])
                del(entrada[line][3])
                b=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])
                h.reportitoOptimizado+="<tr><td>N. 17</td><td>x= y * 0</td><td>"+a+"</td><td>"+b+"</td></tr>\n"
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
            elif entrada[line][2]!="0" and entrada[line][3]=="*" and entrada[line][4]=="0":
                a=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])+" "+str(entrada[line][3])+" "+str(entrada[line][4])
                print("LA SALIDA NORMAL SERIA: ", entrada[line])
                entrada[line][2]="0"
                del(entrada[line][3])
                del(entrada[line][3])
                b=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])
                h.reportitoOptimizado+="<tr><td>N. 17</td><td>x= y * 0</td><td>"+a+"</td><td>"+b+"</td></tr>\n"
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
            else:
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
        else:
            print("LA SALIDA normal SERIA: ", entrada[line])
    print("cadena regla 17:\n",entrada)
    return entrada

#-------------------------------------------------------------------------------------------------------------------
#                       REGLA DE OPTIMIZACION 18 X= 0 / Y => 
def regla18(entrada):
    for line in range(0,len(entrada)):
        #salidaString
        #print(entrada[line])
        if len(entrada[line])>=5:
            if entrada[line][2]=="0" and entrada[line][3]=="/" and entrada[line][4]!="0":
                a=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])+" "+str(entrada[line][3])+" "+str(entrada[line][4])
                del(entrada[line][3])
                del(entrada[line][3])
                b=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])
                h.reportitoOptimizado+="<tr><td>N. 18</td><td>x= 0 / y</td><td>"+a+"</td><td>"+b+"</td></tr>\n"
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
            else:
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
        else:
            print("LA SALIDA normal SERIA: ", entrada[line])
    print("cadena regla 17:\n",entrada)
    return entrada

#-------------------------------------------------------------------------------------------------------------------
#                       REGLA DE OPTIMIZACION 11 X= 0 / Y => 
def regla11(entrada):
    eliminada=[]
    for line in range(0,len(entrada)):
        if len(entrada[line])>=5:
            if entrada[line][0]==entrada[line][2] and entrada[line][3]=="/" and entrada[line][4]=="1":
                a=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])+" "+str(entrada[line][3])+" "+str(entrada[line][4])
                eliminada.append(str(entrada[line][0]))
                print(eliminada)
                #del(entrada[line])
                h.reportitoOptimizado+="<tr><td>N. 11</td><td>x= x / 1</td><td>"+a+"</td><td> Se elimina la produccion</td></tr>\n"
                #print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
            else:
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
        else:
            print("LA SALIDA normal SERIA: ", entrada[line])
    for x in range(0,len(eliminada)):
        val=len(entrada)
        line=0
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", eliminada[x])
        while val>0: 
            print(entrada[line])
            if eliminada[x] in entrada[line]:
                if eliminada[x] ==entrada[line][0]:
                    print("ENCUENTRA: ", eliminada[x])
                    del(entrada[line])
                    val -=2
                elif entrada[line][2]==eliminada[x] and entrada[line][4]!=eliminada[x]:
                    print("viene en posicion 2")
                    del(entrada[line][2])
                    del(entrada[line][2])
                    val-=1
                    line+=1
                elif entrada[line][2]!=eliminada[x] and entrada[line][4]==eliminada[x]:
                    print("viene en posicion 4")
                    del(entrada[line][3])
                    del(entrada[line][3])
                    val-=1
                    line+=1
                else:
                    val-=1
                    line+=1
            else:
                val-=1
                line+=1
    return entrada

#-------------------------------------------------------------------------------------------------------------------
#                       REGLA DE OPTIMIZACION 10 X= 0 * Y => 
def regla10(entrada):
    eliminada=[]
    for line in range(0,len(entrada)):
        if len(entrada[line])>=5:
            if entrada[line][0]==entrada[line][2] and entrada[line][3]=="*" and entrada[line][4]=="1":
                a=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])+" "+str(entrada[line][3])+" "+str(entrada[line][4])
                eliminada.append(str(entrada[line][0]))
                print(eliminada)
                #del(entrada[line])
                h.reportitoOptimizado+="<tr><td>N. 10</td><td>x= x * 1</td><td>"+a+"</td><td> Se elimina la produccion</td></tr>\n"
                #print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
            else:
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
        else:
            print("LA SALIDA normal SERIA: ", entrada[line])
    for x in range(0,len(eliminada)):
        val=len(entrada)
        line=0
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", eliminada[x])
        while val>0: 
            print(entrada[line])
            if eliminada[x] in entrada[line]:
                if eliminada[x] ==entrada[line][0]:
                    print("ENCUENTRA: ", eliminada[x])
                    del(entrada[line])
                    val -=2
                elif entrada[line][2]==eliminada[x] and entrada[line][4]!=eliminada[x]:
                    print("viene en posicion 2")
                    del(entrada[line][2])
                    del(entrada[line][2])
                    val-=1
                    line+=1
                elif entrada[line][2]!=eliminada[x] and entrada[line][4]==eliminada[x]:
                    print("viene en posicion 4")
                    del(entrada[line][3])
                    del(entrada[line][3])
                    val-=1
                    line+=1
                else:
                    val-=1
                    line+=1
            else:
                val-=1
                line+=1
    return entrada
#-------------------------------------------------------------------------------------------------------------------
#                       REGLA DE OPTIMIZACION 9 X= 0 - Y => 
def regla9(entrada):
    eliminada=[]
    for line in range(0,len(entrada)):
        if len(entrada[line])>=5:
            if entrada[line][0]==entrada[line][2] and entrada[line][3]=="-" and entrada[line][4]=="0":
                a=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])+" "+str(entrada[line][3])+" "+str(entrada[line][4])
                eliminada.append(str(entrada[line][0]))
                print(eliminada)
                #del(entrada[line])
                h.reportitoOptimizado+="<tr><td>N. 9</td><td>x= x * 1</td><td>"+a+"</td><td> Se elimina la produccion</td></tr>\n"
                #print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
            else:
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
        else:
            print("LA SALIDA normal SERIA: ", entrada[line])
    for x in range(0,len(eliminada)):
        val=len(entrada)
        line=0
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", eliminada[x])
        while val>0: 
            print(entrada[line])
            if eliminada[x] in entrada[line]:
                if eliminada[x] ==entrada[line][0]:
                    print("ENCUENTRA: ", eliminada[x])
                    del(entrada[line])
                    val -=2
                elif entrada[line][2]==eliminada[x] and entrada[line][4]!=eliminada[x]:
                    print("viene en posicion 2")
                    del(entrada[line][2])
                    del(entrada[line][2])
                    val-=1
                    line+=1
                elif entrada[line][2]!=eliminada[x] and entrada[line][4]==eliminada[x]:
                    print("viene en posicion 4")
                    del(entrada[line][3])
                    del(entrada[line][3])
                    val-=1
                    line+=1
                else:
                    val-=1
                    line+=1
            else:
                val-=1
                line+=1
    return entrada

#-------------------------------------------------------------------------------------------------------------------
#                       REGLA DE OPTIMIZACION 8 X= 0 - Y => 
def regla8(entrada):
    eliminada=[]
    for line in range(0,len(entrada)):
        if len(entrada[line])>=5:
            if entrada[line][0]==entrada[line][2] and entrada[line][3]=="+" and entrada[line][4]=="0":
                a=str(entrada[line][0])+" "+str(entrada[line][1])+" "+str(entrada[line][2])+" "+str(entrada[line][3])+" "+str(entrada[line][4])
                eliminada.append(str(entrada[line][0]))
                print(eliminada)
                #del(entrada[line])
                h.reportitoOptimizado+="<tr><td>N. 8</td><td>x= x * 1</td><td>"+a+"</td><td> Se elimina la produccion</td></tr>\n"
                #print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
            else:
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
        else:
            print("LA SALIDA normal SERIA: ", entrada[line])
    for x in range(0,len(eliminada)):
        val=len(entrada)
        line=0
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", eliminada[x])
        while val>0: 
            print(entrada[line])
            if eliminada[x] in entrada[line]:
                if eliminada[x] ==entrada[line][0]:
                    print("ENCUENTRA: ", eliminada[x])
                    del(entrada[line])
                    val -=2
                elif entrada[line][2]==eliminada[x] and entrada[line][4]!=eliminada[x]:
                    print("viene en posicion 2")
                    del(entrada[line][2])
                    del(entrada[line][2])
                    val-=1
                    line+=1
                elif entrada[line][2]!=eliminada[x] and entrada[line][4]==eliminada[x]:
                    print("viene en posicion 4")
                    del(entrada[line][3])
                    del(entrada[line][3])
                    val-=1
                    line+=1
                else:
                    val-=1
                    line+=1
            else:
                val-=1
                line+=1
    return entrada




def regla5(entrada):
    for line in range(0,len(entrada)):
        #salidaString
        #print(entrada[line])
        if len(entrada[line])>=5:
            if entrada[line][0].upper()=="IF" and entrada[line][3]=="==" and entrada[line][2]=="1" and entrada[line][4]=="1":
                if entrada[line+1][0].uppder()=="GOTO":
                    del(entrada[line])


                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
            else:
                print("LA SALIDA OPTIMIZADA SERIA: ", entrada[line])
        else:
            print("LA SALIDA normal SERIA: ", entrada[line])
    print("cadena regla 5:\n",entrada)
    return entrada





def construir_cadena(entrada):
    salida=""
    for x in range(0,len(entrada)):
        for y in range(0,len(entrada[x])):
            salida+=str(entrada[x][y])+" "
        salida+="\n"
    return salida

def generar_reporte():
    h.reporteOptimizacion()


def escribir3DOptimizado(var3):
    try:
        state_script_dir = os.getcwd()
        report_dir = state_script_dir + "\\codigo3Doptimizado.py"
        with open(report_dir, "w") as f:
            f.write(var3)
            f.closed
        print("Si se escribio el archivo 3D :D!")
    except:
        print("no se genero el archivo :(")
        box_tilte = "Report Error"
        box_msg = "El archivo del codigo no existe"
        messagebox.showinfo(box_tilte, box_msg)