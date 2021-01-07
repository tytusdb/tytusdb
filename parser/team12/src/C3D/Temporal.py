class temporal():    

    def __init__(self):
        self.temporalActual = 1
    
    def getTemporal(self):
        getTemporalActual = 't' + str(self.temporalActual)
        self.temporalActual += 1
        return getTemporalActual

instanceTemporal = temporal()