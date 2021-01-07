class ejeShow():
    def __init__(self, tablaActual, baseActual, conectar, ts , listaTablas):
        self.conectar = conectar
        self.ts  = ts
        self.tablaActual = tablaActual
        self.baseActual = baseActual
        self.listaTablas = listaTablas


    def iniciarShow(self, instru):
        obShow = instru.show_cont
        self.conectar.cmd_showDatabases(obShow)

