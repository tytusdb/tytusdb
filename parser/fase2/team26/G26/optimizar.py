reporte = ""
def optimizar(texto):
    texto = optimizarr12(texto)
    texto = optimizarr13(texto)
    texto = optimizarr14(texto)
    texto = optimizarr15(texto)
    texto = optimizarr16(texto)
    texto = optimizarr17(texto)
    texto = optimizarr18(texto)
    return texto

#Optimizaciones----------------------------

def optimizarr12(texto):
    optimizacion = ""
    texto = texto.split("\n")
    for linea in texto:
        if "(" not in linea:
            try:
                optimizacion += regla12(linea) + "\n"
            except:
                optimizacion += linea + "\n"
        else:
            optimizacion += linea + "\n"
    return optimizacion

def optimizarr13(texto):
    optimizacion = ""
    texto = texto.split("\n")
    for linea in texto:
        if "(" not in linea:
            try:
                optimizacion += regla13(linea) + "\n"
            except:
                optimizacion += linea + "\n"
        else:
            optimizacion += linea + "\n"
    return optimizacion

def optimizarr14(texto):
    optimizacion = ""
    texto = texto.split("\n")
    for linea in texto:
        if "(" not in linea:
            try:
                optimizacion += regla14(linea) + "\n"
            except:
                optimizacion += linea + "\n"
        else:
            optimizacion += linea + "\n"
    return optimizacion

def optimizarr15(texto):
    optimizacion = ""
    texto = texto.split("\n")
    for linea in texto:
        if "(" not in linea:
            try:
                optimizacion += regla15(linea) + "\n"
            except:
                optimizacion += linea + "\n"
        else:
            optimizacion += linea + "\n"
    return optimizacion

def optimizarr16(texto):
    optimizacion = ""
    texto = texto.split("\n")
    for linea in texto:
        if "(" not in linea:
            try:
                optimizacion += regla16(linea) + "\n"
            except:
                optimizacion += linea + "\n"
        else:
            optimizacion += linea + "\n"
    return optimizacion

def optimizarr17(texto):
    optimizacion = ""
    texto = texto.split("\n")
    for linea in texto:
        if "(" not in linea:
            try:
                optimizacion += regla17(linea) + "\n"
            except:
                optimizacion += linea + "\n"
        else:
            optimizacion += linea + "\n"
    return optimizacion

def optimizarr18(texto):
    optimizacion = ""
    texto = texto.split("\n")
    for linea in texto:
        if "(" not in linea:
            try:
                optimizacion += regla18(linea) + "\n"
            except:
                optimizacion += linea + "\n"
        else:
            optimizacion += linea + "\n"
    return optimizacion


#Metodos para optimizar-----------------------
def operandos(texto):
    newText = ""
    flag = False
    for i in texto:
        if i == "=":
            flag = True
        if flag and i !="=":
            if i != " ":
                newText += i
    return newText


def operandosr8(texto):
    newText = ""
    flag = True
    for i in texto:
        if i == "=":
            flag = False
        if flag and i != "=" and i!=" ":
                newText += i
    return newText

def regla8(linea):
    rep = linea
    opIzq = operandosr8(linea)
    linea = operandos(linea)
    operacion = linea.split("+")
    if opIzq == operacion[0] and  operacion[1] == "0":
        reporteRegla8(rep)
        return False
    elif opIzq == operacion[1] and  operacion[0] == "0":
        reporteRegla8(rep)
        return False
    else:
        return True

def reporteRegla8(l):
    global reporte
    reporte += "Regla 8:\nSe elimino: "+ l  + "\n"

def reporteRegla9(l):
    global reporte
    reporte += "Regla 9:\nSe elimino: "+ l  + "\n"

def reporteRegla10(l):
    global reporte
    reporte += "Regla 10:\nSe elimino: "+ l  + "\n"

def reporteRegla11(l):
    global reporte
    reporte += "Regla 11:\nSe elimino: "+ l  + "\n"

def regla9(linea):
    rep = linea
    opIzq = operandosr8(linea)
    linea = operandos(linea)
    operacion = linea.split("-")
    if opIzq == operacion[0] and  operacion[1] == "0":
        reporteRegla9(rep)
        return False
    else:
        return True

def regla10(linea):
    rep = linea
    opIzq = operandosr8(linea)
    linea = operandos(linea)
    operacion = linea.split("*")
    if opIzq == operacion[0] and  operacion[1] == "1":
        reporteRegla10(rep)
        return False
    elif opIzq == operacion[1] and  operacion[0] == "1":
        reporteRegla10(rep)
        return False
    else:
        return True

def regla11(linea):
    rep = linea
    opIzq = operandosr8(linea)
    linea = operandos(linea)
    operacion = linea.split("/")
    if opIzq == operacion[0] and  operacion[1] == "1":
        reporteRegla11(rep)
        return False
    else:
        return True

def regla12(linea):
    l = linea
    global reporte
    opIzq = operandosr8(linea)
    linea = operandos(linea)
    operacion = linea.split("+")
    if operacion[0] == "0":
        reporte += "Regla 12:\nSe sustituyo: "+ l +"    por ->     "  + opIzq + " = " + operacion[1] + "\n"
        return "    " + opIzq + " = " + operacion[1]
    elif operacion[1] == "0":
        reporte += "Regla 12:\nSe sustituyo: "+ l +"    por ->     "  + opIzq + " = " + operacion[1] + "\n"
        return "    " + opIzq + " = " + operacion[0]
    else:
        return "    " + opIzq + " = " + operacion[0] + "+" + operacion[1]

def regla13(linea):
    global reporte
    l =  linea
    opIzq = operandosr8(linea)
    linea = operandos(linea)
    operacion = linea.split("-")
    if operacion[1] == "0":
        reporte += "Regla 13:\nSe sustituyo: "+ l +"    por ->     "  + opIzq + " = " + operacion[1] + "\n"
        return "    " + opIzq + " = " + operacion[0]
    else:
        return "    " + opIzq + " = " + operacion[0] + " - "+ operacion[1]

def regla14(linea):
    global reporte
    l = linea
    opIzq = operandosr8(linea)
    linea = operandos(linea)
    operacion = linea.split("*")
    if operacion[0] == "1":
        reporte += "Regla 14:\nSe sustituyo: "+ l +"    por ->     "  + opIzq + " = " + operacion[1] + "\n"
        return "    " + opIzq + " = " + operacion[1]
    elif operacion[1] == "1":
        reporte += "Regla 14:\nSe sustituyo: "+ l +"    por ->     "  + opIzq + " = " + operacion[1] + "\n"
        return "    " + opIzq + " = " + operacion[0]
    else:
        return "    " + opIzq + " = " + operacion[0] + "*" + operacion[1]

def regla15(linea):
    global reporte
    l = linea
    opIzq = operandosr8(linea)
    linea = operandos(linea)
    operacion = linea.split("/")
    if operacion[1] == "1":
        reporte += "Regla 15:\nSe sustituyo: "+ l +"    por ->     "  + opIzq + " = " + operacion[1] + "\n"
        return "    " + opIzq + " = " + operacion[0]
    else:
        return "    " + opIzq + " = " + operacion[0] + " / " + operacion[1]

def regla16(linea):
    global reporte
    l = linea
    opIzq = operandosr8(linea)
    linea = operandos(linea)
    operacion = linea.split("*")
    if operacion[0] == "2":
        reporte += "Regla 16:\nSe sustituyo: "+ l +"    por ->     "  + opIzq + " = " + operacion[1] + "\n"
        return "    " + opIzq + " = " + operacion[1] + " + " + operacion[1]
    elif operacion[1] == "2":
        reporte += "Regla 16:\nSe sustituyo: "+ l +"    por ->     "  + opIzq + " = " + operacion[1] + "\n"
        return "    " + opIzq + " = " + operacion[0]  + " + " + operacion[0]
    else:
        return "    " + opIzq + " = " + operacion[0] + "*" + operacion[1]

def regla17(linea):
    global reporte
    l = linea
    opIzq = operandosr8(linea)
    linea = operandos(linea)
    operacion = linea.split("*")
    if operacion[0] == "0":
        reporte += "Regla 17:\nSe sustituyo: "+ l +"    por ->     "  + opIzq + " = " + operacion[1] + "\n"
        return "    " + opIzq + " = 0" 
    elif operacion[1] == "0":
        reporte += "Regla 17:\nSe sustituyo: "+ l +"    por ->     "  + opIzq + " = " + operacion[1] + "\n"
        return "    " + opIzq + " = 0" 
    else:
        return "    " + opIzq + " = " + operacion[0] + "*" + operacion[1]

def regla18(linea):
    global reporte
    l = linea
    opIzq = operandosr8(linea)
    linea = operandos(linea)
    operacion = linea.split("/")
    if operacion[0] == "0":
        reporte += "Regla 18:\nSe sustituyo: "+ l +"    por ->     "  + opIzq + " = " + operacion[1] + "\n"
        return "    " + opIzq + " = 0" 
    else:
        return "    " + opIzq + " = " + operacion[0] + "/" + operacion[1]

def getreporte():
    return reporte
