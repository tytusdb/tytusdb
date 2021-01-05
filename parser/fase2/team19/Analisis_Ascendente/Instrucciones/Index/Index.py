from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS

class Index(Instruccion):
    ''' #1 Index normal
        #2 Index hash
        #3 Inder Unique
        #4 Index order
        #5 Index Lower '''

    def __init__(self, caso,id, tabla, columnref, where,order, fila, columna):
        self.caso = caso
        self.id = id
        self.tabla = tabla
        self.columnref = columnref
        self.where = where
        self.order = order
        self.fila = fila
        self.columna = columna

    def ejecutar(Index, ts, consola, exceptions):
        bdactual = ts.buscar_sim("usedatabase1234")
        BD = ts.buscar_sim(bdactual.valor)
        entornoBD = BD.Entorno

        print(Index.caso)
        listaId = []
        try:
            if entornoBD.validar_sim(Index.tabla) == 1:

                if Index.caso == 1:
                    for idcito in Index.columnref:
                        print(idcito.id)
                        listaId.append(idcito.id)
                        print(str(listaId))
                    sim = TS.Simbolo(TS.TIPO_DATO.INDEX_SIMPLE,Index.id,None,str(listaId)[1:-1],None)
                    entornoBD.agregar_sim(sim)
                elif Index.caso == 2:
                    for idcito in Index.columnref:
                        print(idcito.id)
                        listaId.append(idcito.id)
                        print(str(listaId))
                    sim = TS.Simbolo(TS.TIPO_DATO.INDEX_HASH, Index.id, None, str(listaId)[1:-1], None)
                    entornoBD.agregar_sim(sim)
                elif Index.caso == 3:
                    for idcito in Index.columnref:
                        print(idcito.id)
                        listaId.append(idcito.id)
                        print(str(listaId))
                    sim = TS.Simbolo(TS.TIPO_DATO.INDEX_UNIQUE, Index.id, None, str(listaId)[1:-1], None)
                    entornoBD.agregar_sim(sim)
                elif Index.caso == 4:
                    sim = TS.Simbolo(TS.TIPO_DATO.INDEX_ORDER, Index.id, Index.order,Index.columnref, None)
                    entornoBD.agregar_sim(sim)
                else:
                    sim = TS.Simbolo(TS.TIPO_DATO.INDEX_LOWER, Index.id, None,Index.columnref, None)
                    entornoBD.agregar_sim(sim)


                consola.append(f"Index {Index.id} se ha creado exitosamente\n")

            else:
                consola.append(f"	42P01 :	undefined_table {Index.tabla}\n")

                return
        except:
            consola.append("XX000 : internal_error")


