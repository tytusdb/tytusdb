import salto_incodicional as si
import salto_condicional as sc
import reglas as r


class Instrucciones():

    def __init__(self, instrucciones):
        self.instrucciones = instrucciones
    
    def optimizacion(self, reglas, pendiente):
        ins = self.instrucciones
        i = 0
        for i in range(len(ins)):
            #print('el valor de inst[i] es ->\n' + str(ins[i]))
            if ins[i][0] == 'sc':

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

                    cond = sc.Salto_con(ins[i][1], ins[i][2], ins[i][3]).optimizacion(reglas, pendiente)
                    incond =  si.Salto_in(sig_incon[1]).optimizacion()
                    

                    #Si las 2 reglas siguen siendo true
                    if r.Reglas.regla4 and r.Reglas.regla5:

                        codigo = cond + '\n' + incond
                        pendiente.append(codigo)
                    
                    #Si solo la regla4 es true
                    elif r.Reglas.regla4:
                        nuevo = 'goto ' + ins[i][2]
                        codigo_regla4 = '#Se cumple la regla 4\n' + nuevo 
                        pendiente.append(codigo_regla4)

                        anterior = cond + '<br>' + incond + '<br>'
                        linea = ''

                        if cond[0] == 'sc':
                            linea = cond[3]
                        elif cond[0] == 'sin' or cond[0] == 'salto':
                            linea = cond[2] 

                        regla = '4,'+anterior+','+nuevo+','+linea
                        reglas.append(regla)
                
                    #Si sola la regla5 es true
                    elif r.Reglas.regla5:
                        codigo_regla5 = '#Se cumple la regla 5 \n'+ incond + '\n'
                        pendiente.append(codigo_regla5)

                        anterior = cond + '<br>' + incond
                        linea = ''

                        if cond[0] == 'sc':
                            linea = cond[3]
                        elif cond[0] == 'sin' or cond[0] == 'salto':
                            linea = cond[2]

                        regla = '5,'+anterior+','+incond+','+linea
                        reglas.append(regla)


                    
