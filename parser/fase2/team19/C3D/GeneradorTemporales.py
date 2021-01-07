_numero_temporal = 1

def resetar_numero_temporal():
    global _numero_temporal
    _numero_temporal = 1


def nuevo_temporal():
    global _numero_temporal
    temporal = _numero_temporal
    _numero_temporal += 1
    return 't%s' % temporal