from datetime import date
from datetime import datetime

def now():
    """Obtener FECHA Y HORA ACTUAL

    Retorna el valor de fecha y hora actual del sistea

    Args:
        No hay valor de entrada

    Returns:
        DATE
    """
    return datetime.now()

def extract(source, value):
    """Extrear de Fecha

    Retorna el valor extraido de fecha

    Args:
        source(STRING): el valor deseado a extraer de una fecha
        value(DATE): fecha

    Returns:
        NUMBER
    """
    if isinstance(source,str) and isinstance(value,datetime):
        datestr = str(value).split(" ")

        if source == 'YEAR':
            return int(datestr[0][0:4])
        if source == 'MONTH':
            return int(datestr[0][5:7])
        if source == 'DAY':
            return int(datestr[0][8:10])
        
        if source == 'HOUR':
            return int(datestr[1][0:2])
        if source == 'MINUTE':
            return int(datestr[1][3:5])
        if source == 'SECOND':
            return int(datestr[1][6:8])
        return -2
            
    return -1


def date_part(source, value):
    """Extrear de Fecha

    Retorna el valor extraido de fecha

    Args:
        source(STRING): el valor deseado a extraer de una fecha
        value(DATE): fecha

    Returns:
        NUMBER
    """
    source = source.upper()
    if isinstance(source,str):
        datestr = str(value).split(" ")
        if isinstance(value,datetime):
            if source == 'YEAR':
                return int(datestr[0][0:4])
            if source == 'MONTH':
                return int(datestr[0][0:4])
            if source == 'DAY':
                return int(datestr[0][0:4])
            
            if source == 'HOUR':
                return int(datestr[1][0:2])
            if source == 'MINUTE':
                return int(datestr[1][3:5])
            if source == 'SECOND':
                return int(datestr[1][6:8])
            return -2
    
        if isinstance(value,str):
            value = value.upper().split(" ")
            if source[len(source)-1] != 'S':
                source += 'S'
            if source in value:
                return int(value[value.index(source)-1])
            return -2
    return -1

def current_date():
    """Obtener fecha actual

    Retorna la fecha actual

    Args:
        Sin argumentos

    Returns:
        DATE
    """
    return datetime.now().date()

def current_time():
    """Obtener fecha actual

    Retorna la fecha actual

    Args:
        Sin argumentos

    Returns:
        DATE
    """
    return datetime.now().time()

try:
    fechatexto = '0001-01-01'
    fecha = datetime.strptime(fechatexto,'%Y-%m-%d')
except ValueError:
    print('time data ' + fechatexto + ' does not match format %d-%m-%Y')
    fecha = datetime(1,1,1,0,0,0)


ARR = fechatexto.split(" ")

hora = '4 hours 3 minutes 15 seconds'

ob = current_time()
print(fecha)