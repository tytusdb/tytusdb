from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS

class Parametro():
    def __init__(self,id,tipo):
        self.id = id
        self.tipo = tipo

class CreateFunction(Instruccion):
    def __init__(self,id,parametros,returns,declare,begin):
        self.id = id
        self.parametros = parametros            #[Parametro(id,tipo),...]
        self.returns = returns.tipo             #returns = Tipo(tipo,longitud,fila,columna)
        self.declare = declare
        self.begin = begin

    def ejecutar(CreateFunction,ts,consola,exceptions):
        bdactual = ts.buscar_sim("usedatabase1234")
        BD = ts.buscar_sim(bdactual.valor)
        entornoBD = BD.Entorno
        try:
            paramcorrectos = True
            if entornoBD.validar_sim(CreateFunction.id) == -1:
                dicci = {}
                for parametro in CreateFunction.parametros:
                    existe = dicci.get(parametro.id,False)
                    if existe == False:
                       dicci[parametro.id] = parametro.tipo.tipo
                    else:
                        consola.append(f"Existe parametros con el mismo nombre en la función: {CreateFunction.id}\n No se pudo crear la función.")
                        paramcorrectos = False
                        break
                if paramcorrectos:
                    entornoFuncion = TS.TablaDeSimbolos({})
                    if CreateFunction.declare != None:
                        simdeclare = TS.Simbolo(TS.TIPO_DATO.DECLARE, "DECLARE", None, CreateFunction.declare, None)
                        entornoFuncion.agregar_sim(simdeclare)
                    #Esto siempre se realiza
                    simbegin = TS.Simbolo(TS.TIPO_DATO.BEGIN, "BEGIN", None, CreateFunction.begin, None)
                    entornoFuncion.agregar_sim(simbegin)
                    #Agregamos las variables de parametros al entorno de la función de una vez
                    for clave,valor in dicci.items():   #id,tipo
                        nuevaVariable = TS.Simbolo(TS.TIPO_DATO.PARAMETRO,clave,valor,None,None)
                        entornoFuncion.agregar_sim(nuevaVariable)

                    #Creamos la nuevafuncion en el entorno global de la base de datos
                    nuevaFuncion = TS.Simbolo(TS.TIPO_DATO.FUNCTION,CreateFunction.id,CreateFunction.returns,None,entornoFuncion)
                    entornoBD.agregar_sim(nuevaFuncion)
                    consola.append(f"Se añadio una nueva funcion llamada: {CreateFunction.id}")
            else:
                consola.append(f"Ya existe esta función en la base de datos")

        except:
            consola.append("XX000 : internal_error")


    #def limpiarFuncion(createFunction):


