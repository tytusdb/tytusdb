def crearReporte(raiz) :
    file = open("ReporteEjecucion.md", "w")
    file.write('## GRUPO #11 \n'
               + '# *REPORTE GRAMATICAL DE LA EJECUCION*\n\n')
    file.write(recorrerAST(raiz))
    file.close()

def recorrerAST(nodo):
    bnf = ""
    contador = 1
    for hijo in nodo.hijos: 
        bnf += '### Instruccion #'+str(contador)+' \n'
        bnf += '```bnf\n'
        bnf += hijo.gramatica + '\n'
        bnf += recorrerHijo(hijo)
        bnf += '```\n\n'
        contador += 1
    return bnf

def recorrerHijo(nodo):
    bnf = ""
    for hijo in nodo.hijos: 
        if hijo.gramatica != '':
            bnf += hijo.gramatica + '\n'
        bnf += recorrerHijo(hijo)
    return bnf