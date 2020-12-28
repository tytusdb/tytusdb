from datetime import datetime

syntaxPostgreSQL = []


def validateTimeStamp(val):
    try:
        if "-" in val:
            dateTime = datetime.strptime(val, "%Y-%m-%d %H:%M:%S")
        else:
            dateTime = datetime.strptime(val, "%Y/%m/%d %H:%M:%S")

        return None
    except:
        syntaxPostgreSQL.append("Error: 22007: Formato de fecha invalido " + str(val))
        return {"Type": "timeStamp", "Descripción": "Formato desconocido"}


def validateDate(val):
    try:

        if "-" in val:
            dateTime = datetime.strptime(val, "%Y-%m-%d")
        else:
            dateTime = datetime.strptime(val, "%Y/%m/%d")
        return None
    except:
        syntaxPostgreSQL.append("Error: 22007: Formato de fecha invalido " + str(val))
        return {"Type": "date", "Descripción": "Formato desconocido"}


def validateTime(val):
    try:
        if "-" in val:
            dateTime = datetime.strptime(val, "%H:%M:%S")
        else:
            dateTime = datetime.strptime(val, "%H:%M:%S")

        return None
    except:
        syntaxPostgreSQL.append("Error: 22007: Formato de fecha invalido " + str(val))
        return {"Type": "time", "Descripción": "Formato desconocido"}


def typeInterval(val):
    val = val.lower()
    if (
        val == "years"
        or val == "months"
        or val == "days"
        or val == "hours"
        or val == "minutes"
        or val == "seconds"
    ):
        return True
    elif (
        val == "year"
        or val == "month"
        or val == "day"
        or val == "hour"
        or val == "minute"
        or val == "second"
    ):
        return True
    return False


def validateInterval(val):
    val = val.strip()
    lst = val.split(" ")
    r = len(lst)
    error = []
    for i in range(0, r, 2):

        try:
            if not lst[i].isdigit() or not typeInterval(lst[i + 1]):
                error.append(
                    {"Type": "interval", "Descripción": "Parametro desconocido"}
                )
                syntaxPostgreSQL.append(
                    "Error: 22007:sintaxis de entrada no válida para el tipo 'interval' "
                )
        except:
            # save err
            syntaxPostgreSQL.append(
                "Error: 22007:sintaxis de entrada no válida para el tipo 'interval' "
            )
            error.append({"Type": "interval", "Descripción": "Parametro invalido"})
    return error
