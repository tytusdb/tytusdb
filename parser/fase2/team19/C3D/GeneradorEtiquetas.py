_numero_etiqueta = 1

def resetar_numero_etiqueta():
    global _numero_etiqueta
    _numero_etiqueta = 1

def nueva_etiqueta():
    global _numero_etiqueta
    etiqueta_temporal = _numero_etiqueta
    _numero_etiqueta += 1
    return 'label%s' % etiqueta_temporal