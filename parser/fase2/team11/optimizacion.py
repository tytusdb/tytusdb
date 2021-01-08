from datetime import date
from datetime import datetime

class Optimizacion:
    def __init__(self, arreglo_traduccion = [], contenido = []):
        reporte = []
        cont = 1
        self.contenido = contenido
        self.arreglo_traduccion = arreglo_traduccion
        if arreglo_traduccion != None:
            linea = 0
            r1_a = ''
            r1_b = ''
            for inst in arreglo_traduccion:
                valor1 = ''
                valor2 = ''
                valor3 = ''
                pos = 1
                tipo_validacion = ''
                encontrado = False
                if '+' not in inst and '-' not in inst and '*' not in inst and '/' not in inst and '%' not in inst and '^' not in inst and ('=' in inst or '<' in inst or '>' in inst):
                    for char in inst:
                        if char != ' ' and char != '\t' and char != '\n':
                            if char == '=':
                                tipo_validacion += '='
                                pos = 2
                            elif char == '<' or char == '>' or char == '!':
                                #print("----", char)
                                tipo_validacion += char
                                pos = 2
                            else:
                                if pos == 1:
                                    valor1 += char
                                if pos == 2:    
                                    valor2 += char
                    # print(r1_a,'*', valor2 ,'--------------', r1_b, '*', valor1)            
                    if r1_a == valor2 and r1_b == valor1:
                        #print('Se  regla 1: ', inst)
                        print("Regla 1")
                        reporte.append(cont)
                        reporte.append('1' )
                        reporte.append(inst)
                        reporte.append('Codigo eliminado')
                        reporte.append(linea)
                        cont += 1        
                    else:
                        # DEMAS REGLAS
                        condicion_A = valor1.replace("if", "")
                        condicion_B = ''

                        condicion_B = valor2.replace("==", "").split(":")

                        son_condiciones_int = False
                        try:
                            condicion_A = int(condicion_A.replace(" ", ""))
                            condicion_B = int(condicion_B[0].replace(" ", ""))
                            son_condiciones_int = True
                        except:
                            son_condiciones_int = False

                        # print(condicion_A, "<->", condicion_B, ">>", son_condiciones_int)

                        if son_condiciones_int:
                            #print(tipo_validacion)
                            if tipo_validacion == '==':
                                if condicion_A == condicion_B:
                                    # AQUI OBTENGO EL 'goto' CUANDO ES VERDADERO, HACER APPEND AL ACTUAL EL 'result'
                                    result = valor2.replace("==", "").split(":")[1].replace(" ", "").replace("goto", "goto ")
                                    #print(" Regla 4: ", inst, ', cambia a: ', result)
                                    print("Regla 4")
                                    contenido.append("\t"+result)
                                    reporte.append(cont)
                                    reporte.append('4' )
                                    reporte.append(inst)
                                    reporte.append(result)
                                    reporte.append(linea)
                                    cont += 1    
                                    # AQUI BUSCO EL INDICE DEL ACTUAL Y ELIMINO EL SIGUIENTE CON POP(INDICE)
                                    eliminar = arreglo_traduccion.index(inst) + 1
                                    arreglo_traduccion.pop(eliminar)
                                else:
                                    eliminar = arreglo_traduccion.index(inst) + 1
                                    result = arreglo_traduccion.pop(eliminar)
                                    print(" Regla 5: ", inst, ', cambia a: ', result)
                                    contenido.append(result)
                                    reporte.append(cont)
                                    reporte.append('5' )
                                    reporte.append(inst)
                                    reporte.append(result)
                                    reporte.append(linea)
                                    cont += 1                                       
                                    print('ELIMINO: ', inst)

                            elif tipo_validacion == '>=':
                                if condicion_A >= condicion_B:

                                    # AQUI OBTENGO EL 'goto' CUANDO ES VERDADERO, HACER APPEND AL ACTUAL EL 'result'
                                    result = valor2.replace("==", "").split(":")[1].replace(" ", "").replace("goto", "goto ")
                                    #print(" Regla 4: ", inst, ', cambia a: ', result)
                                    print("Regla 4")
                                    contenido.append("\t"+result)
                                    reporte.append(cont)
                                    reporte.append('4' )
                                    reporte.append(inst)
                                    reporte.append(result)
                                    reporte.append(linea)
                                    cont += 1    

                                    # AQUI BUSCO EL INDICE DEL ACTUAL Y ELIMINO EL SIGUIENTE CON POP(INDICE)
                                    eliminar = arreglo_traduccion.index(inst) + 1
                                    arreglo_traduccion.pop(eliminar)                                
                                else:

                                    eliminar = arreglo_traduccion.index(inst) + 1
                                    result = arreglo_traduccion.pop(eliminar)
                                    print(" Regla 5: ", inst, ', cambia a: ', result)
                                    contenido.append(result)
                                    reporte.append(cont)
                                    reporte.append('5' )
                                    reporte.append(inst)
                                    reporte.append(result)
                                    reporte.append(linea)
                                    cont += 1                 
                                    print('ELIMINO: ', inst)

                            elif tipo_validacion == '<=':
                                if condicion_A <= condicion_B:
                                    # AQUI OBTENGO EL 'goto' CUANDO ES VERDADERO, HACER APPEND AL ACTUAL EL 'result'
                                    result = valor2.replace("==", "").split(":")[1].replace(" ", "").replace("goto", "goto ")
                                    #print(" Regla 4: ", inst, ', cambia a: ', result)
                                    print("Regla 4")
                                    contenido.append("\t"+result)
                                    reporte.append(cont)
                                    reporte.append('4' )
                                    reporte.append(inst)
                                    reporte.append(result)
                                    reporte.append(linea)
                                    cont += 1    

                                    # AQUI BUSCO EL INDICE DEL ACTUAL Y ELIMINO EL SIGUIENTE CON POP(INDICE)
                                    eliminar = arreglo_traduccion.index(inst) + 1
                                    arreglo_traduccion.pop(eliminar)
                               
                                else:

                                    eliminar = arreglo_traduccion.index(inst) + 1
                                    result = arreglo_traduccion.pop(eliminar)
                                    print(" Regla 5: ", inst, ', cambia a: ', result)
                                    contenido.append(result)
                                    reporte.append(cont)
                                    reporte.append('5' )
                                    reporte.append(inst)
                                    reporte.append(result)
                                    reporte.append(linea)
                                    cont += 1                 
                                    print('ELIMINO: ', inst)

                            elif tipo_validacion == '!=':
                                if condicion_A != condicion_B:
                                    # AQUI OBTENGO EL 'goto' CUANDO ES VERDADERO, HACER APPEND AL ACTUAL EL 'result'
                                    result = valor2.replace("==", "").split(":")[1].replace(" ", "").replace("goto", "goto ")
                                    #print(" Regla 4: ", inst, ', cambia a: ', result)
                                    print("Regla 4")
                                    contenido.append("\t"+result)
                                    reporte.append(cont)
                                    reporte.append('4' )
                                    reporte.append(inst)
                                    reporte.append(result)
                                    reporte.append(linea)
                                    cont += 1    

                                    # AQUI BUSCO EL INDICE DEL ACTUAL Y ELIMINO EL SIGUIENTE CON POP(INDICE)
                                    eliminar = arreglo_traduccion.index(inst) + 1
                                    arreglo_traduccion.pop(eliminar)
                               
                                else:

                                    eliminar = arreglo_traduccion.index(inst) + 1
                                    result = arreglo_traduccion.pop(eliminar)
                                    print(" Regla 5: ", inst, ', cambia a: ', result)
                                    contenido.append(result)
                                    reporte.append(cont)
                                    reporte.append('5' )
                                    reporte.append(inst)
                                    reporte.append(result)
                                    reporte.append(linea)
                                    cont += 1                 
                                    print('ELIMINO: ', inst)

                            elif tipo_validacion == '>':
                                if condicion_A > condicion_B:
                                    # AQUI OBTENGO EL 'goto' CUANDO ES VERDADERO, HACER APPEND AL ACTUAL EL 'result'
                                    result = valor2.replace("==", "").split(":")[1].replace(" ", "").replace("goto", "goto ")
                                    #print(" Regla 4: ", inst, ', cambia a: ', result)
                                    print("Regla 4")
                                    contenido.append("\t"+result)
                                    reporte.append(cont)
                                    reporte.append('4' )
                                    reporte.append(inst)
                                    reporte.append(result)
                                    reporte.append(linea)
                                    cont += 1    

                                    # AQUI BUSCO EL INDICE DEL ACTUAL Y ELIMINO EL SIGUIENTE CON POP(INDICE)
                                    eliminar = arreglo_traduccion.index(inst) + 1
                                    arreglo_traduccion.pop(eliminar)
                               
                                else:

                                    eliminar = arreglo_traduccion.index(inst) + 1
                                    result = arreglo_traduccion.pop(eliminar)
                                    print(" Regla 5: ", inst, ', cambia a: ', result)
                                    contenido.append(result)
                                    reporte.append(cont)
                                    reporte.append('5' )
                                    reporte.append(inst)
                                    reporte.append(result)
                                    reporte.append(linea)
                                    cont += 1                 
                                    print('ELIMINO: ', inst)

                            elif tipo_validacion == '<':
                                if condicion_A < condicion_B:
                                    # AQUI OBTENGO EL 'goto' CUANDO ES VERDADERO, HACER APPEND AL ACTUAL EL 'result'
                                    result = valor2.replace("==", "").split(":")[1].replace(" ", "").replace("goto", "goto ")
                                    #print(" Regla 4: ", inst, ', cambia a: ', result)
                                    print("Regla 4")
                                    contenido.append("\t"+result)
                                    reporte.append(cont)
                                    reporte.append('4' )
                                    reporte.append(inst)
                                    reporte.append(result)
                                    reporte.append(linea)
                                    cont += 1    

                                    # AQUI BUSCO EL INDICE DEL ACTUAL Y ELIMINO EL SIGUIENTE CON POP(INDICE)
                                    eliminar = arreglo_traduccion.index(inst) + 1
                                    arreglo_traduccion.pop(eliminar)                             
                                else:

                                    eliminar = arreglo_traduccion.index(inst) + 1
                                    result = arreglo_traduccion.pop(eliminar)
                                    #print(" Regla 5: ", inst, ', cambia a: ', result)
                                    print("Regla 5")
                                    contenido.append(result)
                                    reporte.append(cont)
                                    reporte.append('5' )
                                    reporte.append(inst)
                                    reporte.append(result)
                                    reporte.append(linea)
                                    cont += 1                 
                                    #print('ELIMINO: ', inst)

                        else:
                            contenido.append(inst)    # YA NO SE INGRESA DIRECTAMENTE 

                    if valor1 != '' and valor2 != '':
                        r1_a = valor1
                        r1_b = valor2      


    def reporteOptimizacion(self, reporte):
        now = datetime.now()
        fecha = 'Fecha: '+str(now.day)+'/'+str(now.month)+'/'+str(now.year)
        hora = 'Hora: '+str(now.hour)+':'+str(now.minute)
        header = '<html><head><br><title>REPORTE DE OPTIMIZACION</title></head><body>\n<H1 ALIGN=CENTER><b><font face="Roboto" color="#1f253d">REPORTE DE OPTIMIZACION</font></b></H1>\n<H4 ALIGN=CENTER><b><font face="Roboto" color="#1f253d">'+fecha+' | '+hora+'</font></b></H4>\n'
        tbhead = '<table align="center" cellpadding="20" cellspacing="0"  style="border:2px solid #1f253d">\n'
        tbhead += '<tr>\n'
        tbhead += '<td bgcolor="#2d48b5" width="150" style="text-align:center"><font face="Roboto" color="white" size="4">No.</font></td>\n'
        tbhead += '<td bgcolor="#2d48b5" width="150" style="text-align:center"><font face="Roboto" color="white" size="4">TIPO DE OPTIMIZACION</font></td>\n'
        tbhead += '<td bgcolor="#2d48b5" width="100" style="text-align:center"><font face="Roboto" color="white" size="4">REGLA DE OPTIMIZACION APLICADA</font></td>\n'
        tbhead += '<td bgcolor="#2d48b5" width="50" style="text-align:center"><font face="Roboto" color="white" size="4">CODIGO ELIMINADO</font></td>\n'
        tbhead += '<td bgcolor="#2d48b5" width="50" style="text-align:center"><font face="Roboto" color="white" size="4">CODIGO AGREGADO</font></td>\n'
        tbhead += '</tr>\n'
        cont = ''
        template = open("reporteOptimizacion.html", "w")      
        i = 0
        for elemento in reporte:
            if i == 0:
                cont += '<tr>\n'
                cont += '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+ str(elemento) +'</font></td>\n'
                cont += '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="gray" size="3">Mirilla</font></td>\n'
            elif i == 1:
                regla = elemento
                cont += '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="gray" size="3">Regla '+str(regla)+'</font></td>\n'
            elif i == 2:
                old = elemento
                cont += '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+str(old)+'</font></td>\n'
            elif i == 3:
                new = elemento
                cont += '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+str(new)+'</font></td>\n'
            elif i == 4:
                linea = elemento
                cont += '</tr>\n'
                i = -1
            i += 1
        template.write(header)
        template.write(tbhead)
        template.write(cont)
        template.write("</table> \n</body> \n</html>")
        template.close()
























            