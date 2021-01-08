from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion

import tytus.parser.fase2.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS

class AlterIndex(Instruccion):
    def __init__(self,idindex,idantiguo,idnuevo,fila,columna):
        self.idindex = idindex
        self.idantiguo = idantiguo
        self.idnuevo = idnuevo
        self.fila = fila
        self.columna = columna


    def ejecutar(elemento, ts, consola, exceptions):

        if ts.validar_sim(elemento.idindex) == 1:

            anterior = ts.buscar_sim(elemento.idindex)

            print(anterior.id,"simon")
            datos = anterior.valor
            print("holahola",datos)
            bandera = False
            i = 0
            concatena = []
            for data in datos:
                if data == elemento.idantiguo:
                    print("sisi ",data)
                    bandera = True
                    break

                i = i + 1


            if not bandera:
                consola.append(f"22005	error_in_assignment,No existe la columna en {elemento.idantiguo} index {elemento.idindex}\n")
                exceptions.append(
                    f"Error semantico-22005-	error_in_assignment-ALTER {elemento.idindex}-{elemento.fila}-{elemento.columna}\n")
            else:
                consola.append(f"\nAlter-{elemento.idindex} ejecutado exitosamente")
                print("aqui elemento nuevo ",elemento.idnuevo)
                print("aqui anterior valor [i] ",anterior.valor[i])

                anterior.valor[i]=elemento.idnuevo

                print("anterior valor :", anterior.valor)
                nueva = anterior.valor
                print("nueva ,", nueva)
                ts.eliminar_sim(elemento.idindex)
                nuevo = TS.Simbolo(anterior.categoria,anterior.id,anterior.tipo,nueva,anterior.Entorno)
                ts.agregar_sim(nuevo)
                print("agregada")
        else:

            consola.append(f"22005	error_in_assignment,No existe {elemento.idindex}\n")
            exceptions.append(f"Error semantico-22005-	error_in_assignment-ALTER {elemento.idindex}-{elemento.fila}-{elemento.columna}\n")

    def traducir(elemento,ts,consola,Exception,tv):

        #iniciar traduccion
        info = f"ALTER INDEX {elemento.idindex} ALTER COLUMN {elemento.idantiguo} {elemento.idnuevo} ;" #info contiene toda el string a mandar como parametros


        contador = tv.Temp()
        consola.append(f"\n\t{contador} = \"{info}\"")
        contador2 = tv.Temp()
        consola.append(f"\n\t{contador2} = T({contador})")
        consola.append(f"\n\tT1 = T3({contador2})")
        consola.append(f"\n\tstack.append(T1)\n")
