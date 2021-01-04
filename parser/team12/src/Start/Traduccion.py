def traduccionSelect(nodoRaiz):

    stringRetornar = "Select "
    cantidadHijos = len(nodoRaiz.hijos)

    if cantidadHijos == 1 :

        expresionTraducir = nodoRaiz.hijos[0]
        
        cantidadHijos = len(expresionTraducir.hijos)
        contador = 1

        for hijo in expresionTraducir.hijos:

            if contador == 1 :
                stringRetornar += ""
            else:
                stringRetornar += ", "
                
            stringRetornar += hijo.getText()
            contador = contador + 1

    elif cantidadHijos == 2:

        expresionTraducir = nodoRaiz.hijos[0]
        tablasTraducir = nodoRaiz.hijos[1]

        if expresionTraducir.nombreNodo == "*":

            stringRetornar += "* "

        else :

            cantidadHijos = len(expresionTraducir.hijos)
            contador = 1

            for hijo in expresionTraducir.hijos:

                if contador == 1 :
                    stringRetornar += ""
                else:
                    stringRetornar += ", "
                
                stringRetornar += hijo.getText()
                contador = contador + 1

        
        stringRetornar += "from "
        cantidadHijos = len(tablasTraducir.hijos)
        contador = 1

        for hijo in tablasTraducir.hijos:

            if contador == 1 :
                stringRetornar += ""
            else:
                stringRetornar += ", "

            if hijo.nombreNodo == 'Identificador':
                stringRetornar += hijo.valor
            
            contador =  contador + 1


    elif cantidadHijos == 3:    
        expresionTraducir = nodoRaiz.hijos[0]
        tablasTraducir = nodoRaiz.hijos[1]
        tercerNodo = nodoRaiz.hijos[2]
    
    stringRetornar += ";\n"
    return stringRetornar
