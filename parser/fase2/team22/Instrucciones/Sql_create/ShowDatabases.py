from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from storageManager.jsonMode import *
from Instrucciones.Tablas.BaseDeDatos import BaseDeDatos
from Optimizador.C3D import *
from Instrucciones.TablaSimbolos import Instruccion3D as c3d

class ShowDatabases(Instruccion):
    def __init__(self, id, tipo, strGram ,linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = id

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        listaBD = showDatabases()
        arbol.lRepDin.append(self.strGram)
        lista = []
        columna = ['Database']
        iteracion = 1  
        #arbol.consola.append("Show Databases:")      
        for bd in listaBD:
            if self.valor:
                # Para ver que contenga el string 
                if self.valor in str(bd):
                    lista.append([f"{iteracion}. {bd}"])
                    #arbol.consola.append(f"\t{iteracion}. {bd}")
                    iteracion += 1
            else:
                lista.append([f"{iteracion}. {bd}"])
                #arbol.consola.append(f"\t{iteracion}. {bd}")
                iteracion += 1
            #aqui se van a agregar las bases de datos
            if(arbol.existeBd(bd) == 0):
                nueva = BaseDeDatos(bd)
                arbol.setListaBd(nueva)
            
        #arbol.consola.append("\n")
        print(lista)
        arbol.getMensajeTabla(columna,lista)
        #print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))


    def generar3D(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append(c3d.asignacionH())
        code.append(c3d.aumentarP())
        t0 = c3d.getTemporal()
        code.append(c3d.asignacionString(t0, "SHOW DATABASES"))
        t1 = c3d.getTemporal()
        if self.valor != None:
            code.append(c3d.operacion(t1, Identificador(t0), Valor("\" LIKE " + "\\'" + self.valor + "\\'\" ", "STRING"), OP_ARITMETICO.SUMA))
            t0 = t1
            t1 = c3d.getTemporal()
        code.append(c3d.operacion(t1, Identificador(t0), Valor("\";\"", "STRING"), OP_ARITMETICO.SUMA))
        code.append(c3d.asignacionTemporalStack(t1))
        code.append(c3d.LlamFuncion('call_funcion_intermedia'))

        return code
'''
instruccion = ShowDatabases("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''