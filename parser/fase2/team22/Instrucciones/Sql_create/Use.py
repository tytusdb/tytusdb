from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion
from storageManager.jsonMode import *
from Instrucciones.Tablas.BaseDeDatos import BaseDeDatos
from Optimizador.C3D import *
from Instrucciones.TablaSimbolos import Instruccion3D as c3d

class Use(Instruccion):
    def __init__(self, id, strGram ,linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.valor = id

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #SE OBTIENE LA LISTA DE BD
        arbol.lRepDin.append(self.strGram)
        lb=showDatabases()
        #SE RECORRE LA BD PARA VERIFICAR QUE NO EXISTA
        for bd in lb:
            if bd== self.valor:
                #SI SE ENCUENTRA LA BD SE TERMINA EL RECORRIDO
                arbol.setBaseDatos(self.valor)
                #llenar la base de datos
                if(arbol.existeBd(self.valor) == 0):
                    nueva = BaseDeDatos(self.valor)
                    arbol.setListaBd(nueva)
                    arbol.llenarTablas(nueva)
                arbol.consola.append(f"Se selecciono la BD: {self.valor} correctamente.")
                return
        error = Excepcion("100","Semantico",f"No existe la BD: {self.valor}",self.linea,self.columna)
        arbol.excepciones.append(error)
        arbol.consola.append(error.toString())
        #print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))

    def generar3D(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append(c3d.asignacionH())
        code.append(c3d.aumentarP())
        t0 = c3d.getTemporal()
        code.append(c3d.asignacionString(t0, "USE " + self.valor + ';'))
        code.append(c3d.asignacionTemporalStack(t0))
        code.append(c3d.LlamFuncion('call_funcion_intermedia'))

        return code

'''
instruccion = Use("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''