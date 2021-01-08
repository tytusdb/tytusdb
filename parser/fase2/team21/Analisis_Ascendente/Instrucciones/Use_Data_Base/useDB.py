from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
import tytus.parser.fase2.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
from tytus.parser.fase2.team21.Analisis_Ascendente.storageManager.jsonMode import *

#from Instrucciones.instruccion import Instruccion
#import Tabla_simbolos.TablaSimbolos as TS
#from storageManager.jsonMode import *

#USE
class Use(Instruccion):
    def __init__(self, id,concatena):
        self.id = id
        self.concatena = concatena

    def ejecutar(use,ts,consola,exceptions):

            if ts.validar_sim("usedatabase1234") == -1:

                lb = showDatabases()
                for bd in lb:

                    if bd == str(use.id):
                        simbolo_use = TS.Simbolo(TS.TIPO_DATO.USE, "usedatabase1234", None, use.id, None)
                        ts.agregar_sim(simbolo_use)
                        consola.append(f"Seleccionando {simbolo_use.valor} base de datos\n")
                        return

                consola.append(f"La Base de Datos {use.id} no existe\n")
            else:

                lb = showDatabases()
                for bd in lb:
                    if bd == use.id:
                        use_anterior = ts.buscar_sim("usedatabase1234")
                        simbolo_use = TS.Simbolo(TS.TIPO_DATO.USE, "usedatabase1234", None, use.id, None)
                        ts.actualizar_sim(simbolo_use)
                        consola.append(f"Cambiando use de {use_anterior.valor} ahora el actual es: {simbolo_use.valor}\n")
                        return

                consola.append(f"La Base de Datos {use.id} no existe\n")

    def traducir(use,consola,tv):

        #iniciar traduccion
        info = "" #info contiene toda el string a mandar como parametros
        print("concatena \n")
        print(use.concatena)
        for data in use.concatena:
            info += " " +data

        contador = tv.Temp()
        consola.append(f"\n\t{contador} = \"{info}\"")
        contador2 = tv.Temp()
        consola.append(f"\n\t{contador2} = T({contador})")
        consola.append(f"\n\tT1 = T3({contador2})")
        consola.append(f"\n\tstack.append(T1)\n")