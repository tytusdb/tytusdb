from goto import with_goto

@with_goto
def ejecutar():
    t1 = 2 * 2
    t2 = 5 #base potencia
    t3 = 1  #contador de potencia
    label .L3
    if(t3 < t1):
        goto .L1

    goto .L2
    label .L1
    t2 = t2 * 5
    t3 = t3+ 1
    goto .L3
    label .L2

    
    print('resultado = ' + str(t2))


ejecutar()