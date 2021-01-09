from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
import tytus.parser.fase2.team21.Analisis_Ascendente.ascendente as tr
import tytus.parser.fase2.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS


class DropFunctionProcedure(Instruccion):
    def __init__(self,tipo,id,fila,columna):
        self.tipo = tipo
        self.id = id
        self.fila = fila
        self.columna = columna



    def ejecutar(elemento, ts, consola, exceptions):

        if ts.validar_sim(elemento.id) == 1:

            ts.eliminar_sim(elemento.id)
            consola.append(f"\nDrop-{elemento.tipo} {elemento.id} borrado exitosamente")

        else:
            consola.append(f"22005	error_in_assignment,No existe {elemento.tipo} {elemento.id}\n")
            exceptions.append(f"Error semantico-22005-	error_in_assignment-DROP {elemento.tipo}-{elemento.fila}-{elemento.columna}")

    def traducir(elemento,ts,consola,Exception,tv):

        #iniciar traduccion
        info = f"DROP {elemento.tipo} {elemento.id} ;" #info contiene toda el string a mandar como parametros


        contador = tv.Temp()
        consola.append(f"\n\t{contador} = \"{info}\"")
        contador2 = tv.Temp()
        consola.append(f"\n\t{contador2} = T({contador})")
        consola.append(f"\n\tT1 = T3({contador2})")
        consola.append(f"\n\tstack.append(T1)\n")
