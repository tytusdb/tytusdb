from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
import C3D.GeneradorTemporales as GeneradorTemporales
import Analisis_Ascendente.reportes.Reportes as Reportes

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

        #print(Index.caso)
        listaId = []
        try:
            if entornoBD.validar_sim(Index.tabla) == 1:
                if entornoBD.validar_sim(Index.id) == 1:
                    consola.append(f"No se puede crear el Index {Index.id} , ya existe en la base de datos \n")
                else:
                    if Index.caso == 1:
                        for idcito in Index.columnref:
                            #print(idcito.id)
                            listaId.append(idcito.id)
                            #print(str(listaId))
                        sim = TS.Simbolo(TS.TIPO_DATO.INDEX_SIMPLE,Index.id,None,str(listaId)[1:-1],None)
                        entornoBD.agregar_sim(sim)
                    elif Index.caso == 2:
                        for idcito in Index.columnref:
                            #print(idcito.id)
                            listaId.append(idcito.id)
                            #print(str(listaId))
                        sim = TS.Simbolo(TS.TIPO_DATO.INDEX_HASH, Index.id, None, str(listaId)[1:-1], None)
                        entornoBD.agregar_sim(sim)
                    elif Index.caso == 3:
                        for idcito in Index.columnref:
                            #print(idcito.id)
                            listaId.append(idcito.id)
                            #print(str(listaId))
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

    def getC3D(self, lista_optimizaciones_C3D):

            etiqueta = GeneradorTemporales.nuevo_temporal()
            instruccion_quemada = 'create'
            if self.caso == 1:
                instruccion_quemada += ' index %s ' % self.id + 'on %s ' % self.tabla
                instruccion_quemada += '( '
                for idcito in self.columnref:
                    instruccion_quemada += '%s ' % idcito.id + ','
                instruccion_quemada = instruccion_quemada[:-1]
                instruccion_quemada += ');'
            elif self.caso == 2:
                instruccion_quemada += ' index %s ' % self.id + 'on %s ' % self.tabla
                instruccion_quemada += ' using hash ( '
                for idcito in self.columnref:
                    instruccion_quemada += '%s ' % idcito.id + ','
                instruccion_quemada = instruccion_quemada[:-1]
                instruccion_quemada += ');'
            elif self.caso == 3:
                instruccion_quemada += ' unique index %s ' % self.id + 'on %s ' % self.tabla + '('
                for idcito in self.columnref:
                    instruccion_quemada += '%s ' % idcito.id + ','
                instruccion_quemada = instruccion_quemada[:-1]
                instruccion_quemada += ');'
            elif self.caso == 4:
                instruccion_quemada += ' index %s ' % self.id + 'on %s ' % self.tabla + '( %s ' % self.columnref + ' %s' % self.order +  ');'
            elif self.caso == 5 :
                instruccion_quemada += ' index %s ' % self.id + 'on %s ' % self.tabla + '( lower ( %s ' % self.columnref + ') );'

            c3d = '''
    # --------- INDEX -----------
    top_stack = top_stack + 1
    %s = "%s"
    stack[top_stack] = %s 

    ''' % (etiqueta, instruccion_quemada, etiqueta)

            '''optimizacion1 = Reportes.ListaOptimizacion("c3d original", "c3d que entra",
                                                       Reportes.TipoOptimizacion.REGLA1)
            lista_optimizaciones_C3D.append(optimizacion1)'''

            return c3d


