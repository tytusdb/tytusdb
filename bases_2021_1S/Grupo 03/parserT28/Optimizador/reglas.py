from parserT28.Optimizador.clases3d import AsignacionID, Goto, LabelIF, Relop, ifStatement
from parserT28.controllers.optimization_controller import OptimizationController


def regla1(result, list_instrucciones, index):
    if isinstance(result, AsignacionID):
        id1 = result.id
        value = result.value
        if index + 1 > len(list_instrucciones) - 1:
            pass
        else:
            index = index + 1
            if isinstance(list_instrucciones[index], AsignacionID):
                id2 = list_instrucciones[index].id
                value2 = list_instrucciones[index].value
                if id1 == value2 and value == id2:
                    codigo_viejo = f'{id1} = {value}\n {id2} = {value2}'
                    codigo_nuevo = f'{id1} = {value}\n'
                    OptimizationController().add(codigo_viejo, codigo_nuevo, "Regla 1")


def regla2(result, list_instrucciones, index):
    isRule2 = False
    if isinstance(result, Goto):
        label = result.labelDestino
        index = index + 1
        while True:
            if index > len(list_instrucciones) - 1:
                break
            if isinstance(list_instrucciones[index], LabelIF):
                if list_instrucciones[index].idLabel != label:
                    isRule2 = True
                if list_instrucciones[index].idLabel == label:
                    if not isRule2:
                        codigo_viejo = f'goto . {label}\n --instrucciones--\n label . {label}\n'
                        OptimizationController().add(
                            codigo_viejo, f'{label}', "Regla 2")
                        print('vamos a optimizar la regla 2')
                        break
            index = index + 1


def regla3(result, list_instrucciones, index):
    if isinstance(result, AsignacionID):
        if isinstance(result.value, Relop):
            value1 = result.value.value1
            value2 = result.value.value2
            operador = result.value.operator
            index = index + 1
            while True:
                if index > len(list_instrucciones) - 1:
                    break
                if isinstance(list_instrucciones[index], ifStatement):
                    label = list_instrucciones[index].gotoLabel.labelDestino
                    if index + 1 > len(list_instrucciones) - 1:
                        break
                    if isinstance(list_instrucciones[index+1], Goto):
                        label2 = list_instrucciones[index+1].labelDestino
                        operador1 = negar_simbolos(operador)
                        codigo_viejo = f'if ({value1} {operador} {value2}): goto . {label}\n goto . {label2}\n  label . {label}\n --instrucciones--\n label . {label2}\n'
                        codigo_nuevo = f'if ({value1} {operador1} {value2}): goto . {label2}\n --instrucciones--\n label . {label2}\n'
                        OptimizationController().add(codigo_viejo, codigo_nuevo, "Regla 3")
                        break
                index = index + 1
        else:
            return


def regla4y5(result, list_instrucciones, index):
    if isinstance(result, AsignacionID):
        if isinstance(result.value, Relop):
            value1 = result.value.value1
            value2 = result.value.value2
            operador = result.value.operator
            index = index + 1
            if (type(value1) == int and type(value2) == int) or (type(value1) == float and type(value2) == float):
                if process_compacion(value1, value2, operador):
                    while True:
                        if index > len(list_instrucciones) - 1:
                            break
                        if isinstance(list_instrucciones[index], ifStatement):
                            label = list_instrucciones[index].gotoLabel.labelDestino
                            if index + 1 > len(list_instrucciones) - 1:
                                break
                            if isinstance(list_instrucciones[index+1], Goto):
                                label2 = list_instrucciones[index +
                                                            1].labelDestino
                                operador = simbolos(operador)
                                codigo_viejo = f'if ({value1} {operador} {value2}): goto . {label}\n goto . {label2}\n'
                                codigo_nuevo = f'goto .{label}'
                                OptimizationController().add(codigo_viejo, codigo_nuevo, "Regla 4")
                                break
                        index = index + 1
                else:
                    while True:
                        if index > len(list_instrucciones) - 1:
                            break
                        if isinstance(list_instrucciones[index], ifStatement):
                            label = list_instrucciones[index].gotoLabel.labelDestino
                            if index + 1 > len(list_instrucciones) - 1:
                                break
                            if isinstance(list_instrucciones[index+1], Goto):
                                label2 = list_instrucciones[index +
                                                            1].labelDestino
                                operador = simbolos(operador)
                                codigo_viejo = f'if ({value1} {operador} {value2}): goto . {label}\n goto . {label2}\n'
                                codigo_nuevo = f'goto .{label2}'
                                OptimizationController().add(codigo_viejo, codigo_nuevo, "Regla 5")
                                break
                        index = index + 1


def regla6(result, list_instrucciones, index):
    isRule6 = False
    if isinstance(result, Goto):
        label = result.labelDestino
        index = index + 1
        while True:
            if index > len(list_instrucciones) - 1:
                break
            if isinstance(list_instrucciones[index], LabelIF):
                if list_instrucciones[index].idLabel != label:
                    pass
                if list_instrucciones[index].idLabel == label:
                    if index + 1 > len(list_instrucciones) - 1:
                        break
                    if isinstance(list_instrucciones[index+1], Goto):
                        label2 = list_instrucciones[index+1].labelDestino
                        codigo_viejo = f'goto . {label}\n --instrucciones--\n label . {label}\n goto . {label2}'
                        codigo_nuevo = f'goto . {label2}\n --instrucciones--\n label . {label}\n goto . {label2}'
                        OptimizationController().add(codigo_viejo, codigo_nuevo, "Regla 6")
                    break
            index = index + 1


def regla7(result, list_instrucciones, index):
    isRule6 = False
    if isinstance(result, AsignacionID):
        if isinstance(result.value, Relop):
            value1 = result.value.value1
            value2 = result.value.value2
            operador = result.value.operator
            index = index + 1
            if isinstance(list_instrucciones[index], ifStatement):
                label = list_instrucciones[index].gotoLabel.labelDestino
                index = index + 1
                while True:
                    if index > len(list_instrucciones) - 1:
                        break

                    if isinstance(list_instrucciones[index], LabelIF):
                        if list_instrucciones[index].idLabel != label:
                            pass
                        if list_instrucciones[index].idLabel == label:
                            if index + 1 > len(list_instrucciones) - 1:
                                break
                            if isinstance(list_instrucciones[index+1], Goto):
                                label2 = list_instrucciones[index +
                                                            1].labelDestino
                                operador = simbolos(operador)
                                codigo_viejo = f'if ({value1} {operador} {value2}) goto . {label}\n --instrucciones--\n label . {label}\n goto . {label2}'
                                codigo_nuevo = f'if ({value1} {operador} {value2}) goto . {label2}\n --instrucciones--\n label . {label}\n goto . {label2}'
                                OptimizationController().add(codigo_viejo, codigo_nuevo, "Regla 7")
                                break
                    index = index + 1


def process_compacion(value1, value2, operador):
    if operador == "==":
        if value1 == value2:
            return True
        else:
            return False
    elif operador == "!=":
        if value1 != value2:
            return True
        else:
            return False
    elif operador == ">":
        if value1 > value2:
            return True
        else:
            return False
    elif operador == "<":
        if value1 < value2:
            return True
        else:
            return False
    elif operador == ">=":
        if value1 >= value2:
            return True
        else:
            return False
    elif operador == "<=":
        if value1 <= value2:
            return True
        else:
            return False


def negar_simbolos(simbol):
    if simbol == "==":
        simbol = "NOT_EQUALS"
    elif simbol == "!=":
        simbol = "EQUALS"
    elif simbol == ">":
        simbol = "MENOR"
    elif simbol == "<":
        simbol = "MAYOR"
    elif simbol == "<=":
        simbol = "MAYOR_IGUAL"
    elif simbol == ">=":
        simbol = "MENOR_IGUAL"
    return simbol


def simbolos(simbol):
    if simbol == "==":
        simbol = "EQUALS"
    elif simbol == "!=":
        simbol = "NOT_EQUALS"
    elif simbol == ">":
        simbol = "MAYOR"
    elif simbol == "<":
        simbol = "MENOR"
    elif simbol == "<=":
        simbol = "MENOR_IGUAL"
    elif simbol == ">=":
        simbol = "MAYOR_IGUAL"
    return simbol
