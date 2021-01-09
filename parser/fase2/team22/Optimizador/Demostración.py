import SintRecolectorC3D

def Demostracion():
    ArchivoEntrada = '''
    L1:
    inicio = 'INICIO DE ARCHIVO'
    goto L2
    texto = 'adios vaquero'
    tm = texto + ' recuerdameee'
    t0 = 0
    L2:
    if t0 >= 18 goto L3
    t0 = t0 + 1
    t1 = 19 + 0
    t2 = t1 - 0
    t3 = t2 / 1
    t1 = t2
    t3 = t1
    t3 = t3 * 2
    t4 = 18 / 1
    goto L2
    L3:
    if 5 != 0 goto L4
    goto L5
    L4:
    if 5 == 0 goto L6
    goto L7
    L5:
    funcion()
    L6:
    t5 = 128 * 0
    L7:
    if 1 == 1 goto L8
    goto L9
    L8:
    t4 = 'yo'
    L9:
    t6 = 'FINAL DEL ARCHIVO YAY'
    t7 = 18 * 2
    t8 = 99 + t7
    t9 = 19 - t8
    t10 = t5 / t9
    '''
    print(SintRecolectorC3D.ejecutarEscaneo(ArchivoEntrada))

Demostracion()