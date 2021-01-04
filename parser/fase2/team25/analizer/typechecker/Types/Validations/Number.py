Error = None
syntaxPostgreErrors = []


def validateInteger(n, val, x):
    global Error
    s = str(val)
    if s.isdecimal() or s[1:].isdecimal():
        li = -(2 ** n)
        ls = (2 ** n) + x
        if li <= val and val <= ls:
            Error = None
            return True
        else:
            syntaxPostgreErrors.append("Error: 22003: el valor esta fuera del rango")
            Error = "El valor está fuera del rango"
            return False
    Error = "El valor no es un numero entero"
    syntaxPostgreErrors.append(
        "Error: 22P02: sintaxis de entrada no válida para el tipo entero"
    )
    return False


def beforePointD(max, val):
    s = str(val)
    min = -max
    if val < 0:
        s = s[1:]
    if min <= len(s) and len(s) <= max:
        return True
    return False


def beforePointN(max, val):
    s = str(val)
    if val < 0:
        s = s[1:]
    if max == len(s):
        return True
    return False


def afterPoint(max, val):
    s = str(val)
    if len(s) <= max:
        return True
    return False


def validateDecimal(col, val):
    global Error
    n = str(val)
    try:
        if col["size"] != None:
            p = col["size"][0]
            s = col["size"][1]
            if "." in n:
                lts = n.split(".")
                x = beforePointD(p - s, int(lts[0]))
                y = afterPoint(s, int(lts[1]))
                if x and y:
                    Error = None
                    return True
                else:
                    syntaxPostgreErrors.append(
                        "Error: 22003: el valor no cumple con la precision"
                    )
                    Error = "No cumple con la precisión"
                    return False
            else:
                if beforePointD(p - s, val):
                    Error = None
                    return True
                else:
                    syntaxPostgreErrors.append(
                        "Error: 22003: el valor no cumple con la precision"
                    )
                    Error = "No cumple con la presición"
                    return False
        else:
            if "." in n:
                lts = n.split(".")
                x = beforePointD(131072, int(lts[0]))
                y = afterPoint(16383, int(lts[1]))
                if x and y:
                    Error = None
                    return True
                else:
                    syntaxPostgreErrors.append(
                        "Error: 22003: el valor no cumple con la precision"
                    )
                    Error = "No cumple con la precisión"
                    return False
            else:
                if beforePointD(131072, val):
                    Error = None
                    return True
                else:
                    syntaxPostgreErrors.append(
                        "Error: 22003: el valor no cumple con la precision"
                    )
                    Error = "No cumple con la presición"
                    return False
    except:
        Error = "El valor no es un decimal"
        syntaxPostgreErrors.append(
            "Error: 22P02: sintaxis de entrada no válida para el tipo decimal"
        )
        return False


def validateNumeric(col, val):
    global Error
    n = str(val)
    try:
        if col["size"] != None:
            p = col["size"][0]
            s = col["size"][1]
            if "." in n:
                lts = n.split(".")
                x = beforePointN(p - s, int(lts[0]))
                y = afterPoint(s, int(lts[1]))
                if x and y:
                    Error = None
                    return True
                else:
                    syntaxPostgreErrors.append(
                        "Error: 22003: el valor no cumple con la precision"
                    )
                    Error = "No cumple con la precisión"
                    return False
            else:
                if beforePointD(p - s, val):
                    Error = None
                    return True
                else:
                    syntaxPostgreErrors.append(
                        "Error: 22003: el valor no cumple con la precision"
                    )
                    Error = "No cumple con la presición"
                    return False
        else:
            if "." in n:
                lts = n.split(".")
                x = beforePointN(131072, int(lts[0]))
                y = afterPoint(16383, int(lts[1]))
                if x and y:
                    Error = None
                    return True
                else:
                    syntaxPostgreErrors.append(
                        "Error: 22003: el valor no cumple con la precision"
                    )
                    Error = "No cumple con la precisión"
                    return False
            else:
                if beforePointD(131072, val):
                    Error = None
                    return True
                else:
                    syntaxPostgreErrors.append(
                        "Error: 22003: el valor no cumple con la precision"
                    )
                    Error = "No cumple con la presición"
                    return False
    except:
        syntaxPostgreErrors.append(
            "Error: 22P02: sintaxis de entrada no válida para el tipo entero"
        )
        Error = "El valor no es un numero"
        return False


def validateReal(col, val):
    global Error
    n = str(val)
    # p = col['size']
    try:
        if "." in n:
            lts = n.split(".")
            x = validateInteger(31, int(lts[0]), 0)
            y = afterPoint(6, int(lts[1]))
            if x and y:
                Error = None
                return True
            else:
                syntaxPostgreErrors.append(
                    "Error: 22003: el valor esta fuera del rango establecido"
                )
                Error = "Valor real fuera del rango establecido"
                return False
        else:
            if validateInteger(31, int(val), 0):
                Error = None
                return True
            else:
                syntaxPostgreErrors.append(
                    "Error: 22003: el valor esta fuera del rango establecido"
                )
                Error = "Valor real fuera del rango establecido"
                return False
    except:
        syntaxPostgreErrors.append(
            "Error: 22P02: sintaxis de entrada no válida para el tipo entero"
        )
        Error = "El valor no es un numero"
        return False


def validateDouble(col, val):
    global Error
    n = str(val)
    # p = col['size']
    try:
        if "." in n:
            lts = n.split(".")
            x = validateInteger(63, int(lts[0]), 0)
            y = afterPoint(15, int(lts[1]))

            if x and y:
                Error = None
                return True
            else:
                syntaxPostgreErrors.append(
                    "Error: 22003: el valor double esta fuera del rango establecido"
                )
                Error = "Valor double fuera del rango establecido"
                return False
        else:
            if validateInteger(63, int(val), 0):
                Error = None
                return True
            else:
                syntaxPostgreErrors.append(
                    "Error: 22003: el valor  double esta fuera del rango establecido"
                )
                Error = "Valor double fuera del rango establecido"
                return False
    except:
        syntaxPostgreErrors.append(
            "Error: 22P02: sintaxis de entrada no válida para el tipo entero"
        )
        Error = "El valor no es un numero"
        return False


def validateMoney(value):
    global Error
    max = 2 ** 63 + 0.07
    min = -(2 ** 63 + 0.08)
    try:
        val = int(value)
        if min <= val and val <= max:
            Error = None
            return True
        else:
            syntaxPostgreErrors.append(
                "Error: 22003: el valor  money esta fuera del rango establecido"
            )
            Error = "Valor money fuera del rango establecido"
            return False
    except:
        syntaxPostgreErrors.append(
            "Error: 22P02: sintaxis de entrada no válida para el tipo entero"
        )
        Error = "El valor no es un numero"
        return False
