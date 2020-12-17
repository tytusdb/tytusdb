from .instruccionAbstracta import InstruccionAbstracta


class funcion(InstruccionAbstracta):

    def __init__(self):
        pass

    def funcionTimeExtract(self, VarTime, TipoTiempo, CadenaTiempo):
        self.VarTime = VarTime
        self.TipoTiempo = TipoTiempo
        self.CadenaTiempo = CadenaTiempo

    def funcionTimeDatePart(self, CadenaPart, TipoTiempo, CadenaTiempo):
        self.CadenaPart = CadenaTiempo
        self.TipoTiempo = TipoTiempo
        self.CadenaTiempo = CadenaTiempo

    def funcionTiempoPredefinido(self, TipoLlamada):
        self.TipoLlamada = TipoLlamada

    def funcionMateUnitaria(self, TipoFuncion, Parametro):
        self.TipoFuncion = TipoFuncion
        self.Parametro = Parametro

    def funcionMateBinaria(self, TipoFuncion, Param1, Param2):
        self.TipoFuncion = TipoFuncion
        self.Param1 = Param1
        self.Param2 = Param2

    def funcionMateWidthBucket(self, TipoFuncion, Param1, Param2, Param3, Param4):
        self.TipoFuncion = TipoFuncion
        self.Param1 = Param1
        self.Param2 = Param2
        self.Param3 = Param3
        self.Param4 = Param4

    def funcionTrigonometricaUnitaria(self, TipoFuncion, Parametro):
        self.TipoFuncion = TipoFuncion
        self.Parametro = Parametro

    def funcionTrigonometricaBinaria(self, TipoFuncion, Param1, Param2):
        self.TipoFuncion = TipoFuncion
        self.Param1 = Param1
        self.Param2 = Param2

    def funcionBinariaStrUnitaria(self, TipoFuncion, Parametro):
        self.TipoFuncion = TipoFuncion
        self.Parametro = Parametro

    def funcionTrigonometricaBinaria(self, TipoFuncion, Param1, Param2):
        self.TipoFuncion = TipoFuncion
        self.Param1 = Param1
        self.Param2 = Param2

    def funcionTrigonometricaTriple(self, TipoFuncion, Param1, Param2, Param3):
        self.TipoFuncion = TipoFuncion
        self.Param1 = Param1
        self.Param2 = Param2
        self.Param3 = Param3

    def funcionExprecion(self, TipoFuncion, ListaFunciones):
        self.TipoFuncion = TipoFuncion
        self.ListaFunciones = ListaFunciones

    def funcionAgregacion(self, TipoFuncion, Parametro):
        self.TipoFuncion = TipoFuncion
        self.parametro = Parametro

    def ejecutar(self, tabalSimbolos, listaErrores):

        pass
