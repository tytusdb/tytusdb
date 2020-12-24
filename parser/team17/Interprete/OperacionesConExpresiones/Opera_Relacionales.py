from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from Interprete.SELECT.indexador_auxiliar import indexador_auxiliar
from Interprete.SELECT.indexador_auxiliar import IAT
from Interprete.simbolo import Simbolo
from Interprete.Meta import Meta
from Interprete.Manejo_errores.ErroresSemanticos import ErroresSemanticos
from Interprete.Manejo_errores import ErroresSintacticos

class Opera_Relacionales(NodoArbol):

    def __init__(self, izq, der, tipoOperaRelacional, line, coliumn):
        super().__init__(line, coliumn)
        self.izq = izq
        self.der = der
        self.tipoOperaRelacional = tipoOperaRelacional

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        izquierdo:indexador_auxiliar = self.izq
        derecho:Valor = self.der.execute(entorno, arbol)

        if self.tipoOperaRelacional == "=":
            if entorno.varibaleExiste("TablaResult"):
                TablaResult:Valor = entorno.obtener_varibale("TablaResult")
                TablaResult.inicializarPrettybabe()
                TablaResult.filtrarWhere("=", izquierdo.referencia, derecho.data)
                simbol:Simbolo = Simbolo("TablaResult", 0, TablaResult)
                entorno.insertar_variable(simbol)
                retorno:bool = not(TablaResult.matriResult_isEmpty())
                arbol.console.append("\n" + TablaResult.inicializarPrettybabe() + "\n")
                print(str(retorno) + " <--------------")
                return Valor(3,retorno)
            else:
                # Codigo de Pablo
                # Se crea una lista que contendra o no las llaves primarias que cumplan la condicion
                registers = []
                '''
                    Se obtiene la tabla, el indice de la columna que especifica el lado izquierdo de la operacion 
                    relacional y las llaves primarias
                '''
                table = entorno.gettable()
                pks = Meta.getPksIndex(table[0])
                column = Meta.getNumberColumnByName(izquierdo.get_origen(), table[0])
                # Si la columna existe
                if column != -1:
                    # Se recorre cada uno de los registros de la tabla
                    for row in range(len(table)):
                        # Si el registro coincide con el valor
                        if table[row][column] == derecho.data:
                            # Si no hay llaves primarias en la tabla
                            if not pks:
                                registers.append(str([row]))
                            # Si hay llaves primarias en la tabla
                            else:
                                inner = []
                                for pk in pks:
                                    inner.append(str(table[row][pk]) + '|')
                                registers.append(inner)
                # Se devuelven los valores de las llaves primarias de las filas que cumplen la condicion o es vacia
                    return registers
                # Si la columna no existe
                else:
                    '''
                      ______ _____  _____   ____  _____  
                     |  ____|  __ \|  __ \ / __ \|  __ \ 
                     | |__  | |__) | |__) | |  | | |__) |
                     |  __| |  _  /|  _  /| |  | |  _  / 
                     | |____| | \ \| | \ \| |__| | | \ \ 
                     |______|_|  \_\_|  \_\\____/|_|  \_\
                    Descripcion: La columna especificada izquierdo.get_origen() no existe.
                    '''
                    Error: ErroresSemanticos = ErroresSemanticos("XX01: La columna especificada izquierdo.get_origen() no existe", self.linea,
                                                                 self.columna,
                                                                 'Operaciones Relacionales')
                    arbol.ErroresSemanticos.append(Error)
                    print('La columna especificada izquierdo.get_origen() no existe')
                    return None

        elif self.tipoOperaRelacional == "u:=":
            return {izquierdo: self.der}
