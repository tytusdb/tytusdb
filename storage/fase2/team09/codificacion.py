def cod_iso(cadena: str) -> str:
    try:
        return cadena.encode('iso-8859-1')
    except:
        print("Error de codificacion ISO")
        return None



def toASCII(cadena)-> str:
    try:
        return cadena.encode('ascii', errors='ignore')
    except:
        print('Error en codificacion ascci')
        return None

def utf(cadena: str) -> str:
    try:
        return cadena.encode('utf-8')
    except:
        print("Error de codificacion ISO")
        return None