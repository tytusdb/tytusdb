reglasOpt = []
codOpt = ''
indice = 0
def optimizar(pOpt):
    global codOpt, indice
    listaOp = pOpt
    size = len(listaOp)
    for indice in range(size):
        valor = listaOp[indice]
        if "=" in valor:
            if "+" in valor:
                suma = valor.split('+')
                if str(suma[1]).strip() == '0':
                    operador = suma[0].split('=')
                    if str(operador[0]).strip() == str(operador[1]).strip():
                        reglasOpt.append("Regla 8:" + str(valor) +'. Se elimina.')
                    else:
                        val = str(suma[0]) + '\n'
                        reglasOpt.append ( "Regla 12:" + str ( valor ) +'. Se optimiza por: ' + val)
                        codOpt += val
                else:
                    codOpt += valor + '\n'
            elif "-" in valor:
                resta = valor.split("-")
                if str(resta[1]).strip() == '0':
                    operador = resta[0].split('=')
                    if str(operador[0]).strip() == str(operador[1]).strip():
                        reglasOpt.append("Regla 9:" + str(valor) + '. Se elimina.')
                    else:
                        val = str(resta[0]) + ';\n'
                        reglasOpt.append ( "Regla 13:" + str ( valor ) + '. Se optimiza por: ' + str(val).strip() )
                        codOpt += val
                else:
                    codOpt += valor + '\n'
            elif "/" in valor:
                div = valor.split("/")
                if str(div[1]).strip() == '1':
                    operador = div[0].split('=')
                    if str(operador[0]).strip() == str(operador[1]).strip():
                        reglasOpt.append("Regla 11:" + str(valor) + '. Se elimina.')
                    else:
                        val = str(div[0]) + '\n'
                        reglasOpt.append ( "Regla 15:" + str ( valor ) + '. Se optimiza por: ' + str(val).strip() )
                        codOpt += val
                else:
                    operador = div[0].split('=')
                    if str(operador[1]).strip() == '0':
                        val = str(div[0]) + '\n'
                        reglasOpt.append( "Regla 18:" + str(valor) + '. Se optimiza por: ' + str(val).strip())
                        codOpt += val
                    else:
                        codOpt += valor + '\n'
            elif "*" in valor:
                mult = valor.split("*")
                if str(mult[1]).strip() == '1':
                    operador = mult[0].split('=')
                    if str(operador[0]).strip() == str(operador[1]).strip():
                        reglasOpt.append("Regla 10:" + str(valor) + '. Se elimina.')
                    else:
                        val = str(mult[0]) + '\n'
                        reglasOpt.append ( "Regla 14:" + str ( valor ) + '. Se optimiza por: ' + str(val).strip() )
                        codOpt += val
                elif str(mult[1]).strip() == '2':
                    opt = mult[0].split('=')
                    val = str(opt[0]) + ' = ' + str(opt[1]) + '+' + str(opt[1])
                    reglasOpt.append("Regla 16:" + valor +'. Se optimiza por: ' + str(val).strip())
                elif str(mult[1]).strip() == '0':
                    operador = mult[0].split('=')
                    val =  str(operador[0]).strip() + ' = 0'
                    reglasOpt.append("Regla 17:" + valor + '.Se optimiza por: '+str(val).strip())
                    codOpt += val
                else:
                    codOpt += valor + '\n'
            elif 'if ' in valor:
                vIf = valor.split(':')
                vIf[0] = vIf[0].replace("if","")
                operador = vIf[0].split('==')
                a = str(operador[0]).strip()
                b = str(operador[1]).strip()
                if (a.isnumeric() and  b.isnumeric()) or ( "\"" in a and "\"" in b):
                    if a == b:
                        indiceA = indice + 1
                        val = str(vIf[1])
                        reglasOpt.append("Regla 4: " + valor + '\n' + str(listaOp[indiceA]) + '. Se optimiza por: ' + str(val))
                        listaOp[indiceA] = ''
                        codOpt += val
                    else:
                        indiceB = indice + 1
                        val = str(listaOp[indiceB])
                        reglasOpt.append("Regla 5: " + valor + '<br>' + str(listaOp[indiceB]) + '<br> Se optimiza por: ' + str(val))
                        listaOp[indiceB] = ''
                        codOpt += val
                else:
                    indiceIf = indice + 1
                    if2 = listaOp[indiceIf]
                    if 'goto ' in if2:
                        vLab1 = valor.split('goto .')
                        vLab2 = vLab1[0].replace('==','!=')
                        vLab3 = if2
                        vLab4 = vLab2 + vLab3
                        optimizado = 'Regla 3: ' + str(valor) + '<br>' + str(if2) + '<br' + str(listaOp[indiceIf + 1]) + '<br> se optimiza por: <br> ' + str(vLab4) + '<br>' + str(listaOp[indiceIf + 2] + '')
                        reglasOpt.append(optimizado)
                        listaOp[indiceIf] = ''
                        listaOp[indiceIf + 1] = ''
                        codOpt += str(vLab4) + str(listaOp[indiceIf + 2])

                    else:
                        codOpt += valor

            else:
                indiceAsig = indice + 1
                asig2 = listaOp[indiceAsig]
                if '=' in asig2:
                    asig = valor.split('=')
                    asig2 = asig2.split('=')
                    if (str(asig[0]).strip() == str(asig2[1]).strip()) and (str(asig[1]).strip() == str(asig2[0]).strip()):
                        reglasOpt.append("Regla 1: <br>" + valor + '<br>' +str(listaOp[indiceAsig]) + '. <br> Se optimiza por: ' + valor )
                        listaOp[indiceAsig] = ''
                        codOpt += valor
                    else:
                        codOpt += valor
                else:
                    codOpt += valor
        else:
            codOpt += valor + '\n'

def retornoOpt():
    return codOpt
