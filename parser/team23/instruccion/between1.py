from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *
from error.errores import *
from tools.tabla_simbolos import *
from abstract.retorno import *
from storage import jsonMode as funciones

class between1(instruccion):
    def __init__(self,expresiones1,between,expresiones2,operador,expresiones3, line, column, num_nodo):
        super().__init__(line,column)
        self.expresiones1=expresiones1
        self.expresiones2=expresiones2
        self.expresiones3=expresiones3

        self.between=between
        self.operador=operador

        #Nodo AST Between
        self.nodo = nodo_AST(between,num_nodo)
        self.nodo.hijos.append(expresiones1.nodo)
        self.nodo.hijos.append(nodo_AST(between, num_nodo+1))
        self.nodo.hijos.append(expresiones2.nodo) 
        self.nodo.hijos.append(nodo_AST(operador, num_nodo+2))
        self.nodo.hijos.append(expresiones3.nodo) 

        #Gramatica
        self.grammar_ = '<TR><TD> EXPRESSION ::= EXPRESSION1 ' + between + ' EXPRESSION2 AND EXPRESSION3 </TD><TD> EXPRESSION = new between1(EXPRESSION1, ' + between + ', EXPRESSION2, EXPRESSION3); </TD></TR>'
        self.grammar_ += expresiones1.grammar_ + '\n'
        self.grammar_ += expresiones2.grammar_ + '\n'
        self.grammar_ += expresiones3.grammar_ + '\n'

    def ejecutar(self, list_id):
        #try:
        id_db = get_actual_use()

        indice_inferior = self.expresiones2.ejecutar(list_id)
        if indice_inferior.tipo == tipo_primitivo.ERROR:
            errores.append(nodo_error(self.line, self.column, 'ERROR - No puedes validar este tipo', 'Semántico'))
            add_text('ERROR - No puedes validar este tipo\n')
            return retorno(-1, tipo_primitivo.ERROR)

        indice_superior = self.expresiones3.ejecutar(list_id)
        if indice_superior.tipo == tipo_primitivo.ERROR:
            errores.append(nodo_error(self.line, self.column, 'ERROR - No puedes validar este tipo', 'Semántico'))
            add_text('ERROR - No puedes validar este tipo\n')
            return retorno(-1, tipo_primitivo.ERROR)

        evaluar = self.expresiones1.ejecutar(list_id)
        if evaluar.tipo == tipo_primitivo.ERROR:
            errores.append(nodo_error(self.line, self.column, 'ERROR - No puedes validar este tipo', 'Semántico'))
            add_text('ERROR - No puedes validar este tipo\n')
            return retorno(-1, tipo_primitivo.ERROR)

        registros_resultado = []

        #CONOCER SI ES LISTA DE REGISTROS 
        #EVALUAR ES UNA TABLA
        if evaluar.query == True:
            #BETWEEN
            if self.between.lower() == 'between':
                for registro in evaluar.valor:
                    try:
                        #ANALIZAR LIMITE INFERIOR
                        #LIMITE INFERIOR ES UNA TABLA
                        if indice_inferior.query == True:
                            if indice_inferior.valor[indice_inferior.index_col] > registro:
                                #LIMITE SUPERIOR ES UNA TABLA
                                if indice_superior.query == True:
                                    if registro < indice_superior.valor[indice_superior.index_col]:
                                        registros_resultado.append(registro)
                                #LIMITE SUPERIOR NO ES UNA TABLA
                                else:
                                    if registro < indice_superior.valor:
                                        registros_resultado.append(registro)
                        #LIMITE INFERIOR NO ES UNA TABLA
                        else:
                            
                            if indice_inferior.valor > registro:
                                #LIMITE SUPERIOR ES UNA TABLA
                                if indice_superior.query == True:
                                    if registro < indice_superior.valor[indice_superior.index_col]:
                                        registros_resultado.append(registro)
                                #LIMITE SUPERIOR NO ES UNA TABLA
                                else:
                                    print("superior no es tabla")
                                    if registro < indice_superior.valor:
                                        print("encontramos dato")
                                        registros_resultado.append(registro)
                    except:
                        pass
            #NOT BETWEEN
            else:
                for registro in evaluar.valor:
                    try:
                        #ANALIZAR LIMITE INFERIOR
                        #LIMITE INFERIOR ES UNA TABLA
                        if indice_inferior.query == True:
                            if indice_inferior.valor[indice_inferior.index_col] < registro:
                                registros_resultado.append(registro)
                            else:
                                #LIMITE SUPERIOR ES UNA TABLA
                                if indice_superior.query == True:
                                    if registro > indice_superior.valor[indice_superior.index_col]:
                                        registros_resultado.append(registro)
                                #LIMITE SUPERIOR NO ES UNA TABLA
                                else:
                                    if registro > indice_superior.valor:
                                        registros_resultado.append(registro)
                        #LIMITE INFERIOR NO ES UNA TABLA
                        else:
                            if indice_inferior.valor < registro:
                                registros_resultado.append(registro)
                            else:
                                #LIMITE SUPERIOR ES UNA TABLA
                                if indice_superior.query == True:
                                    if registro > indice_superior.valor[indice_superior.index_col]:
                                        registros_resultado.append(registro)
                                #LIMITE SUPERIOR NO ES UNA TABLA
                                else:
                                    if registro > indice_superior.valor:
                                        registros_resultado.append(registro)
                    except:
                        pass
        #EVALUAR NO ES TABLA
        else:
                            
            #BETWEEN
            if self.between.lower() == 'between':
                #ANALIZAR LIMITE INFERIOR
                #LIMITE INFERIOR ES UNA TABLA
                if indice_inferior.query == True:
                    errores.append(nodo_error(self.line, self.column, 'ERROR - No puedes validar este tipo', 'Semántico'))
                    add_text('ERROR - No puedes validar este tipo\n')
                    return retorno(-1, tipo_primitivo.ERROR)
                #LIMITE INFERIOR NO ES UNA TABLA
                else:
                    if indice_inferior.valor > registro:
                        #LIMITE SUPERIOR ES UNA TABLA
                        if indice_superior.query == True:
                            errores.append(nodo_error(self.line, self.column, 'ERROR - No puedes validar este tipo', 'Semántico'))
                            add_text('ERROR - No puedes validar este tipo\n')
                            return retorno(-1, tipo_primitivo.ERROR)
                        #LIMITE SUPERIOR NO ES UNA TABLA
                        else:
                            if registro < indice_superior.valor:
                                registros_resultado.append(registro)
            
            #NOT BETWEEN
            else:
                #ANALIZAR LIMITE INFERIOR
                #LIMITE INFERIOR ES UNA TABLA
                if indice_inferior.query == True:
                    errores.append(nodo_error(self.line, self.column, 'ERROR - No puedes validar este tipo', 'Semántico'))
                    add_text('ERROR - No puedes validar este tipo\n')
                    return retorno(-1, tipo_primitivo.ERROR)
                #LIMITE INFERIOR NO ES UNA TABLA
                else:
                    if indice_inferior.valor < registro:
                        registros_resultado.append(registro)
                    else:
                        #LIMITE SUPERIOR ES UNA TABLA
                        if indice_superior.query == True:
                            errores.append(nodo_error(self.line, self.column, 'ERROR - No puedes validar este tipo', 'Semántico'))
                            add_text('ERROR - No puedes validar este tipo\n')
                            return retorno(-1, tipo_primitivo.ERROR)
                        #LIMITE SUPERIOR NO ES UNA TABLA
                        else:
                            if registro > indice_superior.valor:
                                registros_resultado.append(registro)

        return registros_resultado
            
        #except:
        #    errores.append(nodo_error(self.line, self.column, 'ERROR - No se puede ejecutar la expresión between.', 'Semántico'))
        #    add_text('ERROR - No se puede ejecutar la expresión between.\n')
        #    return retorno(-1, tipo_primitivo.ERROR)

    def castear_dato(self, dato, tipo):
        if tipo == tipo_primitivo.BIGINT or tipo == tipo_primitivo.INTEGER or tipo_primitivo.SMALLINT:
            return int(dato)
        elif tipo == tipo_primitivo.DECIMAL or tipo == tipo_primitivo.DOUBLE_PRECISION or tipo == tipo_primitivo.MONEY or tipo_primitivo.REAL:
            return float(dato)