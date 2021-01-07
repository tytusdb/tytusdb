from goto import with_goto
#from InstruccionesDGA import tabla
import InstruccionesDGA as dga
import storage as s
from enum import Enum
import tablaDGA as TAS
import reportError as errores


@with_goto
def range(start, stop):
    i = start  #la variable start se guarda en i
    result = []  #se crear una lista para guardar los resultados

    label .begin #con label se crea cualquier etiqueta en esta caso aqui le pusieron begin pero se puede llamar de cualquier forma
    if i == stop: #se comprueba que i es igual a stop
        goto .end #si se entra a este if saltamos a la etiqueta .end que esta en la linea 21

    result.append(i) # se va a pushear i cuando no saltemos a la etiqueta end
    i += 1 # como no entramos en el if tambien se incremanta i+1
    goto .begin # nuevamente saltamos a la etiqueta begin es decir en este punto regresamos a la linera 13

    label .end # esta etiqueta end se invoca cuando entra en el if y continuamos con la lineas de abajo
    return result # finalmente se devuelde el arreglo

#guardar en tabla de simbolo
@with_goto
def save_func(id):
    i = ix  #la variable start se guarda en i
    if tabla.existe_id(i):
        goto .error
    else: 
        goto .save

    label .error
    #creacion de error y retorno del error
    e = errores.CError(0,0,"Error funcion",'Semantico') 
    errores.insert_error(e)
    goto .end


    label .save
    #Guardo en tabla de simbolo
    ambitoFuncion = dga.NombreDB
    NuevoSimbolo = TAS.Simbolo(dga.cont,id,TAS.TIPO.FUNCTION,ambitoFuncion,None, None, None, None, None, None, None ,None,None,None,None,False) 
    dga.tabla.agregar(NuevoSimbolo)
    goto .end

    label .end # esta etiqueta end se invoca cuando entra en el if y continuamos con la lineas de abajo
    return 1


@with_goto
def save_decla(id):
    i = ix  #la variable start se guarda en i
    if tabla.existe_id(i):
        goto .funcionseletc
    else: 
        goto .save

    label .error
    #creacion de error y retorno del error
    e = errores.CError(0,0,"Error funcion",'Semantico') 
    errores.insert_error(e)
    return e
    goto .end


    label .save
    
    #Guardo en tabla de simbolo
    ambitoFuncion = dga.NombreDB
    NuevoSimbolo = TAS.Simbolo(dga.cont,id,TAS.TIPO.FUNCTION,ambitoFuncion,None, None, None, None, None, None, None ,None,None,None,None,False) 
    dga.tabla.agregar(NuevoSimbolo)
    goto .end

    label .end # esta etiqueta end se invoca cuando entra en el if y continuamos con la lineas de abajo
    return 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(range(2,7))


