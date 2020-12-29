from ReporteTS import *

errorsem = []

tipoTexto = ['varchar', 'char', 'text', 'character', 'varying']
tipoNumero = ['integer', 'real', 'bigint', 'decimal', 'numeric', 'real', 'double', 'money', 'int']
tipoFecha = 'date'
tipoBool = 'boolean'


def tipoColumna(nombreCol, tabla, valor, base):
    # verificar recibe:
    #   1-numerico
    #   2-texto
    #   3-fecha
    #   4-bool

    verificar = 0

    # print("Comprobando tipos de columna " + nombre)

    noexisteCampo = 0

    for i in tsgen:
        if str(tsgen[i]['declarada_en']) == str(tabla) and str(tsgen[i]['nombre']) == str(nombreCol) and str(
                tsgen[i]['ambito']) == str(base):
            noexisteCampo = 0
            break

        else:
            noexisteCampo = 1

    if noexisteCampo == 1:
        errorsem.append("Error, no existe el campo en la tabla y base indicada")
        print("Error, no existe el campo en la tabla y base indicada")

    else:
        for i in tsgen:
            # print("Comparando " + tsgen[i]['declarada_en'] + " - " +tsgen[i]['nombre'] + " con " + tabla + " - " + nombre)

            if str(tsgen[i]['declarada_en']) == str(tabla) and str(tsgen[i]['nombre']) == str(nombreCol) and str(
                    tsgen[i]['ambito']) == str(base):
                # print("Variable encontrada")

                # Comprobando tipo de entrada
                for k in tipoNumero:
                    if str(tsgen[i]['tipo']).__contains__(k):
                        verificar = 1

                for j in tipoTexto:
                    if str(tsgen[i]['tipo']).__contains__(str(j)):
                        verificar = 2

                if str(tsgen[i]['tipo']).__contains__(tipoFecha):
                    verificar = 3

                if str(tsgen[i]['tipo']).__contains__(tipoBool):
                    verificar = 4

                if verificar == 1:
                    print("Si es numero")

                    if isNumber(valor):
                        if str(valor).__contains__("."):
                            print("Es decimal")
                        else:
                            print("Es integer")

                    else:
                        errorsem.append(
                            "Error de tipos en \"" + valor + "\". Se esperaba tipo " + str(tsgen[i]['tipo']))
                        print("Error de tipos en " + valor + ". Se esperaba tipo " + str(tsgen[i]['tipo']))

                elif verificar == 2:
                    print("No es numero")

                    if not isNumber(valor):
                        if str(tsgen[i]['tipo']).__contains__("("):
                            print("Tiene parentesis")
                            tipo = str(tsgen[i]['tipo']).split("(")
                            tipo2 = tipo[1].split(")")
                            tamTipo = tipo2[0]

                            if len(valor) == int(tamTipo):
                                print("Son del mismo tam")
                            else:
                                errorsem.append(
                                    "Error longitud en \"" + valor + "\". Se esperaba longitud de " + tamTipo + ". \r Se esperaba tipo " + str(
                                        tsgen[i]['tipo']))
                                print("Error de longitud en \"" + valor + "\". Se esperaba longitud de " + tamTipo)

                        else:
                            print("Es tipo texto")

                    else:
                        errorsem.append(
                            "Error de tipos en \"" + str(valor) + "\". Se esperaba tipo " + str(tsgen[i]['tipo']))
                        print("Error de tipos en \"" + str(valor) + "\". Se esperaba tipo " + str(tsgen[i]['tipo']))

                elif verificar == 3:
                    print("Es fecha")

                    if not isNumber(valor):
                        print(str(valor))
                        if str(valor).__contains__("/") or str(valor).__contains__("-") or str(valor).__contains__(
                                "now()"):
                            print("Es una fecha")
                        else:
                            errorsem.append("Invalid Datetime Format. Msg 22007. Error de tipos en \"" + str(
                                valor) + "\". Se esperaba tipo " + str(tsgen[i]['tipo']))
                            print("Error de tipos en \"" + str(valor) + "\". Se esperaba tipo " + str(tsgen[i]['tipo']))

                elif verificar == 4:
                    print("Es bool")

                    if isNumber(valor):

                        if valor == 1 or valor == 0:
                            print("Todo bien con el bool")
                        else:
                            errorsem.append(
                                "Error de tipos en \"" + str(valor) + "\". Se esperaba tipo " + str(tsgen[i]['tipo']))
                            print("Error de tipos en \"" + str(valor) + "\". Se esperaba tipo " + str(tsgen[i]['tipo']))

                    else:

                        if str(valor) == "true" or str(valor) == "false" or str(valor) == "yes" or str(
                                valor) == "no" or str(valor) == "on" or str(valor) == "off":
                            print("Todo bien con el bool")
                        else:
                            errorsem.append(
                                "Error de tipos en \"" + str(valor) + "\". Se esperaba tipo " + str(tsgen[i]['tipo']))
                            print("Error de tipos en \"" + str(valor) + "\". Se esperaba tipo " + str(tsgen[i]['tipo']))


def isNumber(valor):
    try:
        valor = valor % 1
        return 1
    except:
        return 0
