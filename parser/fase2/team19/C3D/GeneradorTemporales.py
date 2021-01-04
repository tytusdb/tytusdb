_numero_temporal = 1

def resetar_numero_etiqueta():
    global _numero_temporal
    _numero_temporal = 1


def nueva_etiqueta():
    global _numero_temporal
    _numero_temporal = _numero_temporal
    _numero_temporal += 1
    return 't%s' % _numero_temporal