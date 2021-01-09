import storageManager as uni

def verificaCodificacion(columnas: list, database: str):
    try:
        codificacion = uni.getCodificacionDatabase(database)
        if codificacion is not None:
            for x in columnas:
                str(x).encode(codificacion, "strict")
        return True
    except UnicodeEncodeError:
        return False
