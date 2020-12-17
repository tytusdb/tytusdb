from datetime import datetime


def validateTimeStamp(val):
    try:
        if "-" in val:
            dateTime = datetime.strptime(val, "%Y-%m-%d %H:%M:%S")
        else:
            dateTime = datetime.strptime(val, "%Y/%m/%d %H:%M:%S")
        print("Date:", dateTime.date())
        return None
    except:
        return {"Type": "timeStamp", "Descripción": "Formato desconocido"}


def validateDate(val):
    try:
        if "-" in val:
            dateTime = datetime.strptime(val, "%Y-%m-%d")
        else:
            dateTime = datetime.strptime(val, "%Y/%m/%d")
        print("Date:", dateTime.date())
        return None
    except:
        return {"Type": "date", "Descripción": "Formato desconocido"}


def validateTime(val):
    try:
        if "-" in val:
            dateTime = datetime.strptime(val, "%H:%M:%S")
        else:
            dateTime = datetime.strptime(val, "%H:%M:%S")
        print("Date:", dateTime.time())
        return None
    except:
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
        print(i)
        try:
            if not lst[i].isdigit() or not typeInterval(lst[i + 1]):
                error.append(
                    {"Type": "interval", "Descripción": "Parametro desconocido"}
                )
        except:
            # save err
            error.append({"Type": "interval", "Descripción": "Parametro invalido"})
    return error
