reglasOpt = []
codOpt = ''
def optimizar(pOpt):
    global codOpt
    listaOp = pOpt.split('\n')
    size = len(listaOp)
    for indice in range(size):
        valor = listaOp[indice]
        if "=" in valor:
            if "+" in valor:
                suma = valor.split('+')
                if suma[1] == '0;':
                    val = str(suma[0]) + ';\n'
                    reglasOpt.append("Regla 8:" + str(valor) +'. Se elimina.')
                    codOpt += val
                    reglasOpt.append ( "Regla 12:" + str ( valor ) +'. Se optimiza por: ' + val)
                else:
                    codOpt += valor + '\n'
            elif "-" in valor:
                resta = valor.split("-")
                if resta[1] == '0;':
                    reglasOpt.append("Regla 9:" + str(valor) + '. Se elimina.')
                    val = str(resta[0]) + ';\n'
                    reglasOpt.append ( "Regla 13:" + str ( valor ) + '. Se optimiza por: ' + val )
                    codOpt += val
                else:
                    codOpt += valor + '\n'
            elif "/" in valor:
                div = valor.split("/")
                if div[1] == '1;':
                    reglasOpt.append("Regla 11:" + str(valor) + '. Se elimina.')
                    val = str(div[0]) + ';\n'
                    reglasOpt.append ( "Regla 15:" + str ( valor ) + '. Se optimiza por: ' + val )
                    codOpt += val
                else:
                    codOpt += valor + '\n'
            elif "*" in valor:
                mult = valor.split("*")
                if mult[1] == '1;':
                    reglasOpt.append("Regla 10:" + str(valor) + '. Se elimina.')
                    val = str(mult[0]) + ';\n'
                    reglasOpt.append ( "Regla 14:" + str ( valor ) + '. Se optimiza por: ' + val )
                    codOpt += val
                elif mult[1] == '2;':
                    opt = mult[0].split('=')
                    val = str(opt[0]) + str(opt[1]) + '+' + str(opt[1])
                    reglasOpt.append("Regla 16:" + valor +'. Se optimiza por: ' + val)
                elif mult[1] == '0;':
                    val = ' 0;\n'
                    reglasOpt.append("Regla 17:" + valor + '.Se optimiza por: '+val)
                    codOpt += val
                else:
                    codOpt += valor + '\n'
            else:
                codOpt += valor +'\n'
        else:
            codOpt += valor + '\n'