from abc import abstractmethod
from parserT28.controllers.optimization_controller import OptimizationController


class Instruction:
    '''Clase abstracta'''
    @abstractmethod
    def process(self):
        ''' metodo para la ejecucion '''
        pass

    @abstractmethod
    def compile(self):
        ''' metodo para la ejecucion '''
        pass

    @abstractmethod
    def optimizate(self):
        ''' metodo para la optimizacion'''
        pass

# =============================================================================================================
# =============================================================================================================


class Relop(Instruction):
    '''
    Relop contiene los operadores logicos
    == != >= ...
    Devuelve un valor booleano
    '''

    def __init__(self, value1, operator, value2):
        self.value1 = value1
        self.operator = operator
        self.value2 = value2

    def __repr__(self):
        return str(vars(self))

    def process(self, expression):
        pass


# =============================================================================================================
# =============================================================================================================
class Temporal(Instruction):
    '''
    Temporal tiene los t1,t2,tn....
    '''

    def __init__(self, alias):
        self.alias = alias

    def __repr__(self):
        return str(vars(self))

    def process(self, expression):
        pass


# =============================================================================================================
# =============================================================================================================
class StackAccess(Instruction):
    '''
    StackAcces tiene el acceso a la pila
    '''

    def __init__(self, positionAccess):
        self.positionAccess = positionAccess

    def __repr__(self):
        return str(vars(self))

    def process(self, expression):
        pass


# =============================================================================================================
# =============================================================================================================
class LabelIF(Instruction):
    '''
    Label contiene el identificador de este label
    '''

    def __init__(self, idLabel):
        self.idLabel = idLabel

    def __repr__(self):
        return str(vars(self))

    def process(self, expression):
        return self


# =============================================================================================================
# =============================================================================================================
class Goto(Instruction):
    '''
    Goto contiene la etiqueta destino
    '''

    def __init__(self, labelDestino):
        self.labelDestino = labelDestino

    def __repr__(self):
        return str(vars(self))

    def process(self, expression):
        return self


# =============================================================================================================
# =============================================================================================================
class PrimitiveData(Instruction):
    """
    Esta clase contiene los tipos primitivos
    de datos como STRING, NUMBER, BOOLEAN
    """

    def __init__(self, data_type, value):
        self.data_type = data_type
        self.value = value

        # if self.data_type == DATA_TYPE.STRING:
        #     self.alias = "\'" + self.alias + "\'"

    def __repr__(self):
        return str(vars(self))

    def process(self, expression):
        return self


# =============================================================================================================
# =============================================================================================================
class ArithmeticBinaryOperation(Instruction):
    '''
        Una operacion binaria recibe, sus dos operandos y el operador
    '''

    def __init__(self, value1, value2, operador):
        self.value1 = value1
        self.value2 = value2
        self.operador = operador

    def __repr__(self):
        return str(vars(self))

    def process(self, expression):
        pass


# =============================================================================================================
# =============================================================================================================
class AsignacionID(Instruction):

    def __init__(self, id, value):
        self.id = id
        self.value = value

    def __repr__(self):
        return str(vars(self))

    #   De la forma opA = opB
    #   donde opA =  id(temporal) | Stack[n] | relop | aritmeticBinary
    #   para la regla 8 en adelante solo nos interesa id = id op number
    #   donde op     = + | - | * | /
    #         number =  0 | 1 | 2

    def process(self, expression):
        #
        if isinstance(self.value, ArithmeticBinaryOperation):
            idAss = self.id
            opIzq = self.value.value1
            opDer = self.value.value2
            operador = self.value.operador
            if self.id == opIzq:
                if operador == '+' and opDer == 0:
                    codigo_viejo = f'{idAss} = {opIzq} {operador} {opDer}'
                    OptimizationController().add(codigo_viejo, "# Se elimina la instruccion", "Regla 8")
                elif operador == '-' and opDer == 0:
                    codigo_viejo = f'{idAss} = {opIzq} {operador} {opDer}'
                    OptimizationController().add(codigo_viejo, "# Se elimina la instruccion", "Regla 9")
                elif operador == '*' and opDer == 1:
                    codigo_viejo = f'{idAss} = {opIzq} {operador} {opDer}'
                    OptimizationController().add(codigo_viejo, "# Se elimina la instruccion", "Regla 10")
                elif operador == "/" and opDer == 1:
                    codigo_viejo = f'{idAss} = {opIzq} {operador} {opDer}'
                    OptimizationController().add(codigo_viejo, "# Se elimina la instruccion", "Regla 11")
            elif self.id == self.value.value2:
                if operador == '+' and opIzq == 0:
                    codigo_viejo = f'{idAss} = {opIzq} {operador} {opDer}'
                    OptimizationController().add(codigo_viejo, "# Se elimina la instruccion", "Regla 8")
                elif operador == '*' and opIzq == 1:
                    codigo_viejo = f'{idAss} = {opIzq} {operador} {opDer}'
                    OptimizationController().add(codigo_viejo, "# Se elimina la instruccion", "Regla 10")
            else:
                if isinstance(opDer, int) or isinstance(opDer, float) and isinstance(opIzq, str):

                    if operador == "+" and opDer == 0:
                        codigo_viejo = f'{idAss} = {opIzq} {operador} {opDer}'
                        OptimizationController().add(
                            codigo_viejo, f'{idAss} = {opIzq}', "Regla 12")
                    elif operador == "*" and opDer == 1:
                        codigo_viejo = f'{idAss} = {opIzq} {operador} {opDer}'
                        OptimizationController().add(
                            codigo_viejo, f'{idAss} = {opIzq}', "Regla 14")
                    elif operador == "-" and opDer == 0:
                        codigo_viejo = f'{idAss} = {opIzq} {operador} {opDer}'
                        OptimizationController().add(
                            codigo_viejo, f'{idAss} = {opIzq}', "Regla 13")
                    elif operador == "/" and opDer == 1:
                        codigo_viejo = f'{idAss} = {opIzq} {operador} {opDer}'
                        OptimizationController().add(
                            codigo_viejo, f'{idAss} = {opIzq}', "Regla 15")
                    elif operador == "*" and opDer == 2:
                        codigo_viejo = f'{idAss} = {opIzq} {operador} {opDer}'
                        OptimizationController().add(
                            codigo_viejo, f'{idAss} = {opIzq} + {opIzq}', "Regla 16")
                    elif operador == "*" and opDer == 0:
                        codigo_viejo = f'{idAss} = {opIzq} {operador} {opDer}'
                        OptimizationController().add(codigo_viejo, f'0', "Regla 17")

                elif isinstance(opIzq, int) or isinstance(opIzq, float) and isinstance(opDer, str):
                    if operador == "+" and opIzq == 0:
                        codigo_viejo = f'{idAss} = {opIzq} {operador} {opDer}'
                        OptimizationController().add(
                            codigo_viejo, f'{idAss} = {opDer}', "Regla 12")
                    elif operador == "*" and opIzq == 1:
                        codigo_viejo = f'{idAss} = {opIzq} {operador} {opDer}'
                        OptimizationController().add(
                            codigo_viejo, f'{idAss} = {opDer}', "Regla 14")
                    elif operador == "*" and opIzq == 2:
                        codigo_viejo = f'{idAss} = {opIzq} {operador} {opDer}'
                        OptimizationController().add(
                            codigo_viejo, f'{idAss} = {opDer} + {opDer}', "Regla 16")
                    elif operador == "*" and opIzq == 0:
                        codigo_viejo = f'{idAss} = {opIzq} {operador} {opDer}'
                        OptimizationController().add(codigo_viejo, f'0', "Regla 17")
                    elif operador == "/" and opIzq == 0:
                        codigo_viejo = f'{idAss} = {opIzq} {operador} {opDer}'
                        OptimizationController().add(codigo_viejo, f'0', "Regla 18")

                else:
                    return
        elif isinstance(self.value, Relop):
            return self
        elif isinstance(self.value, str):
            return self


# =============================================================================================================
# =============================================================================================================
class impresion(Instruction):

    def __init__(self, valorAImprimir):
        self.valorAImprimir = valorAImprimir

    def __repr__(self):
        return str(vars(self))

    def process(self, expression):
        pass
# =============================================================================================================
# =============================================================================================================


class ifStatement(Instruction):

    def __init__(self, condition, gotoLabel):
        self.condition = condition
        self.gotoLabel = gotoLabel

    def __repr__(self):
        return str(vars(self))

    def process(self, expression):
        return self
# RELOP
# TEMPORAL
# STACK_ACCESS
# LABEL
# GOTO
# PRIMITIVE_DATA
# ArithmeticBinaryOperation
# ASIGNACION_ID
# IMPRESION
# IF_STATEMENT
