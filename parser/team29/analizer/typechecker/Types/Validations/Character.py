syntaxPostgreErrors = []


def validateVarchar(n, val):
    if 0 <= len(val) and len(val) <= n:
        return None
    syntaxPostgreErrors.append("Error: 22026: Excede el limite de caracteres")
    return {"Type": "varchar", "Descripción": "Excede el limite de caracteres"}


def validateChar(n, val):
    if len(val) == n:
        return None
    syntaxPostgreErrors.append("Error: 22026: Restriccion de caracteres")
    return {"Type": "char", "Descripción": "Restriccion de caracteres"}


def validateBoolean(val):
    s = str(val).lower()
    if s == "true" or s == "false":
        return None
    elif val == 1 or val == 0:
        return None
    syntaxPostgreErrors.append("Error: 22000: Tipo invalido (Boolean)")
    return {"Type": "boolean", "Descripción": "invalido"}
