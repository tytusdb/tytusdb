import encabezado as encabezado
import  op_aritmeticas as aritmetica
import salto_incodicional as si
import salto_condicional as sc
import salto as s
import reglas as r

class ast_op():
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones

    def optimizacion(self):
        print('Entró a la optimización del ast')
        codigo = '#**** CODIGO OPTIMIZADO ****\n'

        ins = self.instrucciones
        i = 0

        for i in range(len(ins)):
            
            sentencia = ins[i]

            if sentencia[0] == 'sc':
                #Salto condicional
                try:
                    sig_incon = ins[i+1]
                except:
                    sig_incon = None
                try:
                    sig_salto = ins[i+2]
                except:
                    sig_salto = None 

                if sig_incon != None and sig_salto != None:
                    if sig_incon[0] == 'sin' and sig_salto[0] == 'salto':
                        #Se cumple la regla 3
                        print('regla3')
                
                if sig_incon[0] == 'sin':
                    #No se sabe que regla es, así que se activan las 2 
                    r.Reglas.regla4 = True
                    r.Reglas.regla5 = True

                    cond = sc.Salto_con(ins[i][1], ins[i][2], ins[i][3]).optimizacion()
                    incond =  si.Salto_in(sig_incon[1]).optimizacion()
                    

                    #Si las 2 reglas siguen siendo true
                    if r.Reglas.regla4 and r.Reglas.regla5:

                        codigo = cond + '\n' + incond + '\n'
                        r.Reglas.optimizado = r.Reglas.optimizado + codigo
                    
                    #Si solo la regla4 es true
                    elif r.Reglas.regla4:
                        nuevo = 'goto ' + ins[i][2]
                        codigo_regla4 = '#Se cumple la regla 4\n' + nuevo + '\n'
                        r.Reglas.optimizado = r.Reglas.optimizado + codigo_regla4

                        anterior = cond + '<br>' + incond + '<br>'

                        regla = '4,'+anterior+','+nuevo+','+str(ins[i][3])
                        r.Reglas.reglas.append(regla)
                
                    #Si sola la regla5 es true
                    elif r.Reglas.regla5:
                        codigo_regla5 = '#Se cumple la regla 5 \n'+ incond + '\n'
                        r.Reglas.optimizado = r.Reglas.optimizado + codigo_regla5

                        anterior = cond + '<br>' + incond

                        regla = '5,'+anterior+','+incond+','+str(ins[i][3])
                        r.Reglas.reglas.append(regla)

                    r.Reglas.condicional_negada = ''
                    r.Reglas.regla4 = False
                    r.Reglas.regla5 = False

                else:
                    self.otros(sentencia)

                    if r.Reglas.pendiente != '':
                        r.Reglas.optimizado = r.Reglas.optimizado + r.Reglas.pendiente
                        r.Reglas.pendiente = ''

            elif sentencia[0] == 'sin':
                #Regla 2
                print('Entro a regla 2')
                try:
                    sig_ins = ins[i+1]
                except:
                    sig_ins = None

                if sig_ins != None:

                    #Si existe otra instrucción después de esta
                    if sig_ins[0] != 'salto' and sig_ins[0] != 'sc':
                        cumple = False
                        etiqueta_sc = sentencia[1]
                        tope = i + 1

                        #Se verifica que si se cumple la regla

                        j = i + 2
                        for j in range(len(ins)):
                            tope = j
                            sig_salto = ins[j]

                            if sig_salto[0] == 'salto':
                                
                                etiqueta_s = sig_salto[1]

                                if etiqueta_sc == etiqueta_s:
                                    tope = j
                                    cumple = True
                                    break 

                                else:
                                    cumple = False
                                    tope = j
                                    break

                        if cumple:
                            print('Si cumple regla 2')
                            codigo_eliminar = ''

                            codigo_regla2 = '#Se cumple la regla 2\n'

                            r.Reglas.regla2 = True
                            codigo_regla2 = codigo_regla2 + 'label ' + etiqueta_sc + '\n'
                            n = 'label ' +  etiqueta_sc + ': <br>'

                            j = i + 1

                            for j in range(tope):
                                print('Entro a for de codigo eliminado')
                                #Concatena el código que se va a eliminar
                                instru = ins[j]

                                self.otros(instru)

                                codigo_eliminar = codigo_eliminar + r.Reglas.pendiente + '<br>'
                                r.Reglas.pendiente = ''

                            print('codigo optimizado hasta el momento :\n' + r.Reglas.optimizado)
                            #El código anterior se elimina 
                            #Se concantena las instrucciones hasta que se encuentro un salto, salto condicional o incondicional
                            r.Reglas.regla2 = False

                            codigo_abajo = ''
                            tope_nuevo = tope

                            print('nuevo tope -> ' + str(tope_nuevo))

                            for j in range(tope + 1, len(ins)):
                                instruc = ins[j]
                                tope_nuevo = j
                                print('nuevo tope -> ' + str(tope_nuevo))

                                print('codigo optimizado hasta el momento :\n' + r.Reglas.optimizado)

                                if instruc[0] != 'sc' and instruc[0] != 'sin' and instruc[0] != 'salto':
                                    self.otros(instruc)

                                    if r.Reglas.pendiente != '' :
                                        n = n + r.Reglas.pendiente + '<br>'
                                        codigo_regla2 = codigo_regla2 + r.Reglas.pendiente
                                        codigo_abajo = codigo_abajo + r.Reglas.pendiente + '<br>'
                                        r.Reglas.pendiente = ''
                                
                                    print('valor de codigo_regla2 despues\n' + codigo_regla2)
                                else:
                                    print('no hay más instrucciones')
                                    break

                            goto = si.Salto_in(sentencia[1]).optimizacion()
                            ant = goto + '<br>'
                            ant = ant + codigo_eliminar + '\n'
                            ant = ant + 'label ' + etiqueta_sc + '<br>'
                            ant = ant + codigo_abajo + '<br>'

                            regla = '2,'+ant+','+n+','+str(ins[i][2])
                            r.Reglas.reglas.append(regla)

                            r.Reglas.condicional_negada = ''
                            r.Reglas.optimizado = r.Reglas.optimizado + codigo_regla2
                            i = tope_nuevo + 1 
                            print('nuevo tope = i -> ' + str(i))
                        else:

                            #No se cumple la regla entonces solo imprime el goto
                            goto = si.Salto_in(sentencia[1]).optimizacion()
                            r.Reglas.optimizado = r.Reglas.optimizado + str(goto) + '\n'

                    else:
                        self.otros(sentencia)
                        if r.Reglas.pendiente != '':
                            r.Reglas.optimizado = r.Reglas.optimizado + r.Reglas.pendiente
                            r.Reglas.pendiente = ''

            else: 
                self.otros(sentencia)
                if r.Reglas.pendiente != '':
                    r.Reglas.optimizado = r.Reglas.optimizado + r.Reglas.pendiente
                    r.Reglas.pendiente = ''

        if r.Reglas.pendiente != '':
            r.Reglas.optimizado = r.Reglas.optimizado + r.Reglas.pendiente
            r.Reglas.pendiente = ''

        return codigo

        
    def otros(self, entrada):

        if entrada[0] == 'encabezado':
            #Encabezado
            encabezado.Encabezado(entrada[1]).optimizacion()

        elif entrada[0] == 'asignacion':
            #Asignacion
            aritmetica.Aritmetica(entrada[1], entrada[2], entrada[3]).optimizacion()