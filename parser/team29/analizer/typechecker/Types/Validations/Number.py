def validateInteger(n, val, x):
    s = str(val)
    if s.isdecimal() or s[1:].isdecimal():
        li = -(2 ** n)
        ls = (2 ** n) + x
        print(li, val, ls)
        if li <= val and val <= ls:
            return None
    return {
        "Type": "numeric",
        "Descripción": "Valor entero fuera del rango establecido",
    }


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
    n = str(val)
    p = col["size"][0]
    s = col["size"][1]
    if "." in n:
        lts = n.split(".")
        x = beforePointD(p - s, int(lts[0]))
        y = afterPoint(s, int(lts[1]))
        print(x, y)
        if x and y:
            return None
    else:
        if beforePointD(p - s, val):
            return None
    return {
        "Type": "numeric",
        "Descripción": "Valor decimal fuera del rango establecido",
    }


def validateNumeric(col, val):
    n = str(val)
    p = col["size"][0]
    s = col["size"][1]
    if "." in n:
        lts = n.split(".")
        x = beforePointN(p - s, int(lts[0]))
        y = afterPoint(s, int(lts[1]))
        print(x, y)
        if x and y:
            return None
    else:
        if beforePointN(p - s, val):
            return None
    return {
        "Type": "numeric",
        "Descripción": "Valor numeric fuera del rango establecido",
    }


def validateReal(col, val):
    n = str(val)
    # p = col['size']
    if "." in n:
        lts = n.split(".")
        x = validateInteger(31, int(lts[0]), 0)
        y = afterPoint(6, int(lts[1]))
        print(x, y)
        if x and y:
            return None
    else:
        if validateInteger(31, int(lts[0]), 0):
            return None
    return {"Type": "numeric", "Descripción": "Valor real fuera del rango establecido"}


def validateDouble(col, val):
    n = str(val)
    # p = col['size']
    if "." in n:
        lts = n.split(".")
        x = validateInteger(63, int(lts[0]), 0)
        y = afterPoint(15, int(lts[1]))
        print(x, y)
        if x and y:
            return None
    else:
        if validateInteger(63, int(lts[0]), 0):
            return None
    return {
        "Type": "numeric",
        "Descripción": "Valor double fuera del rango establecido",
    }


def validateMoney(val):
    max = 2 ** 63 + 0.07
    min = -(2 ** 63 + 0.08)
    if min <= val and val <= max:
        return None
    return {"Type": "numeric", "Descripción": "Valor money fuera del rango establecido"}
