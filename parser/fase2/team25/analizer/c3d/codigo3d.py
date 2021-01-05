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



    def showCode(self):
        contenido = ""
        for inst in self.listaCode3d:
            contenido+=(inst)
        print(contenido)




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





    def asegurarIntruccion(self, instruccion :str):
        '''Limpia de comentarios y se asegura que inicie con una palabra reservada de la fase 1 como USE , INSERT , SELECT , UPDATE '''
        #
        instruccion += "\n"
        instruccion = re.sub('\-\-(.*)\n|/\*(.|\n)*?\*/' ,"",instruccion)
        instruccion = instruccion[0:len(instruccion)-1]
        instruccion = instruccion.replace("\n", " ")
        lexema = ""
        indiceInicial = 0
        for x in range(len(instruccion)):
            if instruccion[x] == " ":
                lexema = ""
            else:
                lexema += instruccion[x]
            if lexema.lower() == "use":
                indiceInicial = x-2
                break
            elif lexema.lower() == "select" or lexema.lower() == "insert" or lexema.lower() == "update" or lexema.lower() == "delete" or lexema.lower() == "create":
                indiceInicial = x-5
                break
            elif lexema.lower() == "truncate":
                indiceInicial = x-7
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

        return instruccionOK



    def generarArchivoEjecucion(self) -> None:
        """
        ESTE METODO GENERA UN ARCHIVO .PY PARA PODER EJECUTAR EL CODIGO 3 DIRECCIONES QUE SE ADJUNTO
        """
        RUTA = '../analizer/'
        with open(F"{RUTA}SALIDA_C3D.py", "w") as archivo:
            # librerias
            archivo.write(self.getCodigo())
            archivo.close()

    def getCodigo(self):
        cadena = ''
        cadena+=("from goto import with_goto" + "\n")
        cadena+=("from interpreter import execution"+"\n")
        cadena+=("from c3d.stack import Stack"+"\n")
        cadena+=('\nstack = Stack()\n\n')
        cadena+=("\n\n\n@with_goto\n")
        cadena+=("def principal():\n")
        for inst in self.listaCode3d:
            cadena+=(inst)
        cadena+=('\n\n\ndef funcionIntermedia():\n')
        cadena+=("\texecution(stack.pop())\n")
        cadena+=("principal()")
        return cadena




# INSTANCIA PARA CONTROLAS LOS METODOS DE LA CLASE
instancia_codigo3d = Codigo3d()

#instacia auxiliar
# instanciaAux = Codigo3d()