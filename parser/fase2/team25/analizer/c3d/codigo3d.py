import re

class Codigo3d:
    """
    esta clase almacena el codigo de 3 direcciones y posee metodos para la generacion del archivo .py
    - tambien lleva el control de el temporal correspondiente
    """

    def __init__(self):
        self.count_temporal = 0
        self.count_label = 0
        self.listaCode3d = []
        self.principal = []
        self.tabulaciones = 1




    def restart(self) -> None:
        """
        limpia las variables
        """
        self.count_temporal = 0
        self.listaCode3d.clear()
        self.count_label = 0
        self.tabulaciones = 1

    def getTabulaciones(self) -> str:
        tab = ''
        for i in range(self.tabulaciones):
            tab += '\t'
        return tab

    def addToCode(self, nuevaLinea_de_codigo) -> None:
        self.listaCode3d.append(nuevaLinea_de_codigo+"\n")

    def addToMain(self, nuevaLinea_de_codigo) -> None:
        self.principal.append(nuevaLinea_de_codigo+"\n")

    def showCode(self):
        print(self.getCodigo())




    def getNewTemporal(self) -> str:
        """
        retorna una cadena con el temporal correspondiente 'Tn t1,t2'
        """

        temporal = "t" + str(self.count_temporal)
        self.count_temporal += 1
        return temporal

    def getNewLabel(self)->str:
        """ retonra una etoqueta L1,L2,L3 ...Ln correspondiente
        """
        etiqueta = "L" + str(self.count_label)
        self.count_label += 1
        return etiqueta





    def asegurarIntruccion(self, instruccion :str , goToMain : bool , quitarParentesisFinal = False):
        '''Limpia de comentarios y se asegura que inicie con una palabra reservada de la fase 1 como USE , INSERT , SELECT , UPDATE '''
        tn_previos = ''
        instruccion += "\n"
        instruccion = instruccion.lower()
        instruccion = re.sub('\-\-(.*)\n|/\*(.|\n)*?\*/' ,"",instruccion)
        instruccion = re.sub('create\s+(function|procedure)' ,"",instruccion)# quito unos create que podrian dar problemas
        instruccion = instruccion[0:len(instruccion)-1]
        instruccion = instruccion.replace("\n", " ")
        lexema = ""
        indiceInicial = 0
        tipoFuncion = ''
        for x in range(len(instruccion)):
            if instruccion[x] == " ":
                lexema = ""
            else:
                lexema += instruccion[x]

            tipoFuncion = lexema.lower()
            if lexema.lower() == "use":
                indiceInicial = x-2
                break
            elif lexema.lower() == "select" or lexema.lower() == "insert" or lexema.lower() == "update" or lexema.lower() == "delete" or lexema.lower() == "create":
                indiceInicial = x-5
                break
            elif lexema.lower() == "truncate":
                indiceInicial = x-7
                break
            elif lexema.lower() == "(select":
                indiceInicial = x-5
                break

            elif lexema.lower() == "alter":
                indiceInicial = x-4
                break
            elif lexema.lower() == "show" or lexema.lower() == "drop":
                indiceInicial = x-3
                break
        instruccionOK = ''
        while(indiceInicial < len(instruccion)):
            instruccionOK+=instruccion[indiceInicial]
            indiceInicial +=1
        lexema = ""
        if tipoFuncion  =="(select":
                    instruccionOK = quitarParentesisSubquery(instruccionOK)
                    quitarParentesisFinal = False
                    tipoFuncion ="select"
        if tipoFuncion == "select":
            if quitarParentesisFinal:
                instruccionOK = quitarParentesisSubquery(instruccionOK)

            aux = re.sub('select' ,"",instruccionOK)
            aux =  aux.strip()

            auxParams = ''
            for x in aux:
                auxParams += x
                if x == " ":
                    lexema = ""
                else:
                    lexema += x.lower()
                if lexema == "from" or lexema == ";": # paro de buscar con un from o un punto y coma
                    break
            auxParams = re.sub('from' ,"",auxParams)
            auxParams = re.sub(';' ,"",auxParams)
            auxParams = auxParams.strip()
            parametros = mi_split(auxParams)
            parametros = quitarEspacios(parametros)


            patron = '[a-zA-Z_][a-zA-Z_0-9]*\s*[(].*[)]'
            for parametro in parametros:
                if re.match(patron,parametro):
                        objPattern = re.search(patron , parametro)
                        coincidencia = objPattern.string[objPattern.span()[0] : objPattern.span()[1]]
                        #  Y REEMPLAZO EL CODIGO 3D como un str(tn)
                        if coincidencia == 'count(*)':
                            continue
                        if getOnlyId(coincidencia).upper() in funcionesDefinidas:
                            # es de la fase 1 asi que se queda normal
                            pass
                        else:# REPLACE
                                tn = self.getNewTemporal()
                                salida = f'\t{coincidencia}\n\t{tn} = RETURN[0]'
                                if goToMain:
                                    self.addToMain(salida)
                                else:
                                    tn_previos+= salida+'\n'
                                instruccionOK = instruccionOK.replace(coincidencia,f'\"+str({tn})+\"')



        elif tipoFuncion == "insert":
            aux = instruccionOK
            aux =  aux.strip()
            auxParams = ''
            for x in aux:

                if x == " ":
                    lexema = ""
                elif x == ";":
                    break
                else:
                    lexema += x.lower()
                    auxParams+=x

                if lexema == "values":
                    auxParams = ""

                elif auxParams =="values(":
                    auxParams=""+"("
            auxParams = auxParams.strip()
            auxParams = auxParams[1: len(auxParams)-1]# LE QUITO LOS PARENTESIS
            parametros = mi_split(auxParams)
            parametros = quitarEspacios(parametros)
            patron = '[a-zA-Z_][a-zA-Z_0-9]*\s*[(].*[)]'
            for parametro in parametros:
                if re.match(patron,parametro):
                        objPattern = re.search(patron , parametro)
                        coincidencia = objPattern.string[objPattern.span()[0] : objPattern.span()[1]]
                        # VERIFICO SI EXISTE EN LA ESTRUCUTRA  Y REEMPLAZO EL CODIGO 3D como un str(tn)
                        if getOnlyId(coincidencia).upper() in funcionesDefinidas:
                            pass # no se traduce
                        else:# REPLACE
                            # * SI SALE TODO BIEN
                            tn = self.getNewTemporal()
                            salida = f'\t{coincidencia}\n\t{tn} = RETURN[0]'
                            if goToMain:
                                self.addToMain(salida)
                            else:
                                tn_previos+= salida+'\n'
                            instruccionOK = instruccionOK.replace(coincidencia,f'\"+str({tn})+\"')
                                #va adentro de  un procedure o funcion

        if goToMain:
            return instruccionOK
        else:
            tn = self.getNewTemporal()
            tres = self.getNewTemporal()#TEMPORAL RESULTANTE
            instruccionOK = tn_previos +f'\t{tn} = "{instruccionOK}"'
            instruccionOK += f'\n\tstack.push({tn})'
            instruccionOK += f"\n\t{tres} = funcionIntermedia()"
            return [instruccionOK,tres]



    def generarArchivoEjecucion(self) -> None:
        """
        ESTE METODO GENERA UN ARCHIVO .PY PARA PODER EJECUTAR EL CODIGO 3 DIRECCIONES QUE SE ADJUNTO
        """
        RUTA = './analizer/'
        with open(F"{RUTA}SALIDA_C3D.py", "w") as archivo:
            # librerias
            archivo.write(self.getCodigo())
            archivo.close()

    def getCodigo(self):
        cadena = ''
        cadena+=("from goto import with_goto" + "\n")
        cadena+=("from interpreter import execution"+"\n")
        cadena+=("from c3d.stack import Stack"+"\n")
        cadena+=('\nstack = Stack()\nRETURN=[None]\n')
        # Funciones
        for inst in self.listaCode3d:
            cadena+=(inst)
        cadena+=("\n\n\n@with_goto\n")
        cadena+=("def principal():\n")
        for inst in self.principal:
            cadena += (inst)
        cadena+=('\n\n\ndef funcionIntermedia():\n')
        cadena+=("\treturn execution(stack.pop())\n")
        cadena+=("principal()")
        return cadena



funcionesDefinidas = [
    'CONVERT',
    'LENGTH',
    'SUBSTRING',
    'TRIM',
    'MD5',
    'SHA256',
    'SUBSTR',
    'GET_BYTE',
    'SUBSTR',
    'SET_BYTE',
    'CONVERT',
    'GET_BYTE',
    'CONVERT',
    'ENCODE',
    'DECODE',
    'ACOS',
    'ACOSD',
    'ASIN',
    'ASIND',
    'ATAN',
    'ATAND',
    'ATAN2',
    'COS',
    'COSD',
    'COT',
    'COTD',
    'SIN',
    'SIND',
    'TAN',
    'TAND',
    'COSH',
    'SINH',
    'TANH',
    'ACOSH',
    'ASINH',
    'ATANH',
    'ABS',
    'CBRT',
    'CEIL',
    'CEILING',
    'DEGREES',
    'DIV',
    'FACTORIAL',
    'FLOOR',
    'GCD',
    'LN',
    'LOG',
    'EXP',
    'MOD',
    'PI',
    'POWER',
    'RADIANS',
    'ROUND',
    'SIGN',
    'SQRT',
    'WIDTH_BUCKET',
    'TRUNC',
    'RANDOM',
    'NOW',
    'EXTRACT',
    'DATE_PART',
    'SUM',
    'AVG',
    'MAX',
    'MIN',
    'GREATEST',
    'LEAST',
    'COUNT'
]

def quitarEspacios(arreglo)->list:
    for i in range(len(arreglo)):
        arreglo[i] = arreglo[i].strip()
    return arreglo

def mi_split(cadena)->list:
    parametros = []
    separar = 0
    lexema = ''
    for c in cadena:
        if c == "(":
            lexema += c
            separar += 1
        elif c == ")":
            lexema += c
            separar -= 1
        elif  c == "," and separar == 0:
            parametros.append(lexema)
            lexema = ""
        else:
            lexema += c
    parametros.append(lexema)# adjunto el ultimo
    return parametros


def getOnlyId(cadena)->str:
    """
    el parametro tiene que ser una cadena ID()
    """
    id = ''
    for c in cadena:
        if c == '(':
            break
        else:
            id+=c
    return id
def getOnlyParams(cadena)->str:
    i = 0
    for c in range(len(cadena)):
        if c == '(':
            i = c
            break
    x = ''
    while(i < len(cadena)):
        x += cadena[i]
        i+=1
    x.strip()
    return x

def quitarParentesisSubquery(cadena)->str:
    try:
        k = 0
        i = len(cadena)-1
        while( i >= 0):
            if cadena[i] == ")":
                k = i
                print(cadena[i+1])
                break
            i-=1
        if k == 0 : return cadena
        indiceInicial = 0
        salida = ''
        while(indiceInicial < k):
            salida +=cadena[indiceInicial]
            indiceInicial +=1
        salida += ";"
        return salida
    except:
        print('NO SALIO DEL CICLO , NO SE PUDO QUITAR EL PARENTESIS DEL SUBQUERY')
        return cadena


# INSTANCIA PARA CONTROLAS LOS METODOS DE LA CLASE
instancia_codigo3d = Codigo3d()
#instacia auxiliar
# instanciaAux = Codigo3d()