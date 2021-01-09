from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
from Instrucciones.Excepcion import Excepcion

class If(Instruccion):
    '''
        Esta clase representa la instrucción if.
        La instrucción if recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''
    def __init__(self,expLogica,instrucciones,strGram, linea, columna, strSent):
        Instruccion.__init__(self,None,linea,columna,strGram,strSent)
        self.expLogica = expLogica
        self.instrucciones = instrucciones

    def ejecutar(self, tabla, arbol):
        pass

    def traducir(self, tabla, arbol,cadenaTraducida):
        #Si existe algun error en la expresion logica se devuelve el error
        expresion_logica = self.expLogica.traducir(tabla, arbol,cadenaTraducida)
        if isinstance(expresion_logica, Excepcion):
                return expresion_logica
        if expresion_logica.tipo.tipo == Tipo_Dato.BOOLEAN or expresion_logica.tipo.tipo == Tipo_Dato.ID:
            #Inicia traduccion
            codigo = expresion_logica.codigo

            codigo += "\tlabel " + expresion_logica.etiquetaV.replace(":","") + "\n"
            for i in self.instrucciones:
                instruccion_if = i.traducir(tabla, arbol,cadenaTraducida)
                if isinstance(instruccion_if, Excepcion):
                    return instruccion_if
                codigo += instruccion_if
            
            if cadenaTraducida == "":
                codigo += "\tlabel " + expresion_logica.etiquetaF.replace(":","") + "\n"
            else:
                #cadenaTraducida traera la etiqueta de salida si es un elsif
                codigo += "\tgoto " + cadenaTraducida + "\n"
                codigo += "\tlabel " + expresion_logica.etiquetaF.replace(":","") + "\n"
            return codigo
            #   ...
            #   if temporal_logico:
            #       goto L1
            #   goto L2
            #   label L1    
            #   instrucciones_if
            #   label L2
            #   ...
        else:
            error = Excepcion('42804',"Semántico","La expresion logica debe ser de tipo boolean",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error

class Ifelse(Instruccion):
    '''
        Esta clase representa la instrucción if else.
        La instrucción if else recibe como parámetro una expresión lógica y las listas
        de instrucciones a ejecutar si la expresión lógica es verdadera o falsa.
    '''
    def __init__(self,expLogica,instrIfVerdadero,instrIfFalso,strGram, linea, columna, strSent):
        Instruccion.__init__(self,None,linea,columna,strGram,strSent)
        self.expLogica = expLogica
        self.instrIfVerdadero = instrIfVerdadero
        self.instrIfFalso = instrIfFalso
    
    def ejecutar(self, tabla, arbol):
        pass

    def traducir(self, tabla, arbol,cadenaTraducida):
        #Si existe algun error en la expresion logica se devuelve el error
        expresion_logica = self.expLogica.traducir(tabla, arbol,cadenaTraducida)
        if isinstance(expresion_logica, Excepcion):
                return expresion_logica
        if expresion_logica.tipo.tipo == Tipo_Dato.BOOLEAN or expresion_logica.tipo.tipo == Tipo_Dato.ID:
            #Inicia traduccion
            codigo = expresion_logica.codigo

            etiquetaSalida = arbol.generaEtiqueta()

            codigo += "\tlabel " + expresion_logica.etiquetaF.replace(":","") + "\n"
            for inst in self.instrIfFalso:
                instruccion_ifFalso = inst.traducir(tabla, arbol,cadenaTraducida)
                if isinstance(instruccion_ifFalso, Excepcion):
                    return instruccion_ifFalso
                codigo += instruccion_ifFalso
            
            codigo += "\tgoto ." + etiquetaSalida + "\n"
            codigo += "\tlabel " + expresion_logica.etiquetaV.replace(":","") + "\n"
            for i in self.instrIfVerdadero:
                instruccion_if = i.traducir(tabla, arbol,cadenaTraducida)
                if isinstance(instruccion_if, Excepcion):
                    return instruccion_if
                codigo += instruccion_if
            
            codigo += "\tlabel ." + etiquetaSalida + "\n"
            return codigo
            #   ...
            #   if temporal_logico
            #       goto L1
            #   goto L2
            #   label L2
            #   instrucciones_ifFalso
            #   goto L3
            #   label L1
            #   instrucciones_if
            #   label L3
            #   ...
        else:
            error = Excepcion('42804',"Semántico","La expresion logica debe ser de tipo boolean",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error

class IfElseIf(Instruccion):
    '''
        Esta clase representa la instrucción if elseif.
        La instrucción if elseif recibe como parámetro una expresión lógica principal y la lista
        de instrucciones, asi como una lista de elseif que contienen respectiva expresion logica e instrucciones
        a ejecutar.
    '''
    def __init__(self,expLogica,instrIfVerdadero,l_elseif,strGram, linea, columna, strSent):
        Instruccion.__init__(self,None,linea,columna,strGram,strSent)
        self.expLogica = expLogica
        self.instrIfVerdadero = instrIfVerdadero
        self.l_elseif = l_elseif
    
    def ejecutar(self, tabla, arbol):
        pass

    def traducir(self, tabla, arbol,cadenaTraducida):
        #Si existe algun error en la expresion logica se devuelve el error
        expresion_logica = self.expLogica.traducir(tabla, arbol,cadenaTraducida)
        if isinstance(expresion_logica, Excepcion):
                return expresion_logica
        if expresion_logica.tipo.tipo == Tipo_Dato.BOOLEAN or expresion_logica.tipo.tipo == Tipo_Dato.ID:
            #Inicia traduccion
            etiquetaSalida = arbol.generaEtiqueta()
            codigo = expresion_logica.codigo
            codigo += "\tlabel " + expresion_logica.etiquetaF.replace(":","") + "\n"

            #Sentencias elseif
            for s_if in self.l_elseif:
                sentencia_if = s_if.traducir(tabla,arbol,etiquetaSalida)
                if isinstance(sentencia_if, Excepcion):
                    return sentencia_if
                codigo += sentencia_if
            #Label si el primer if es verdadero
            codigo += "\tgoto " + etiquetaSalida + "\n"
            codigo += "\tlabel " + expresion_logica.etiquetaV.replace(":","") + "\n"
            #instrucciones if principal
            for i in self.instrIfVerdadero:
                instruccion_if = i.traducir(tabla, arbol,cadenaTraducida)
                if isinstance(instruccion_if, Excepcion):
                    return instruccion_if
                codigo += instruccion_if
            
            codigo += "\tlabel " + etiquetaSalida + "\n"
            return codigo
            #   ...
            #   if temporal_logico:
            #       goto L1
            #   goto L10
            #   label L10
            #   ................
            #
            #   if temporal_logico2:
            #       goto L3
            #   goto L4
            #   Label L3
            #   instrucciones_elseif
            #   goto L2
            #   label L4
            #
            #   ....................
            #   label L1    
            #   instrucciones_if
            #   label L2
            #   ...
        else:
            error = Excepcion('42804',"Semántico","La expresion logica debe ser de tipo boolean",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error

class IfElseIfElse(Instruccion):
    '''
        Esta clase representa la instrucción if elseif else.
        La instrucción if elseif else recibe como parámetro una expresión lógica principal y la lista
        de instrucciones, asi como una lista de elseif que contienen respectiva expresion logica e instrucciones
        a ejecutar y las instrucciones si todas son falsas.
    '''
    def __init__(self,expLogica,instrIfVerdadero,l_elseif,instrIfFalso,strGram, linea, columna, strSent):
        Instruccion.__init__(self,None,linea,columna,strGram,strSent)
        self.expLogica = expLogica
        self.instrIfVerdadero = instrIfVerdadero
        self.l_elseif = l_elseif
        self.instrIfFalso = instrIfFalso
    
    def ejecutar(self, tabla, arbol):
        pass

    def traducir(self, tabla, arbol,cadenaTraducida):
        #Si existe algun error en la expresion logica se devuelve el error
        expresion_logica = self.expLogica.traducir(tabla, arbol,cadenaTraducida)
        if isinstance(expresion_logica, Excepcion):
                return expresion_logica
        if expresion_logica.tipo.tipo == Tipo_Dato.BOOLEAN or expresion_logica.tipo.tipo == Tipo_Dato.ID:
            #Inicia traduccion
            codigo = expresion_logica.codigo
            etiquetaF = arbol.generaEtiqueta()
            codigo += "\tlabel " + expresion_logica.etiquetaF.replace(":","") + "\n"
            #Sentencias elseif
            for s_if in self.l_elseif:
                sentencia_if = s_if.traducir(tabla,arbol,etiquetaF)
                if isinstance(sentencia_if, Excepcion):
                    return sentencia_if
                codigo += sentencia_if
            #instrucciones si todos son falsos
            for instr in self.instrIfFalso:
                instruccion_falsa = instr.traducir(tabla, arbol,cadenaTraducida)
                if isinstance(instruccion_falsa, Excepcion):
                    return instruccion_falsa
                codigo += instruccion_falsa     
            
            codigo += "\tgoto " + etiquetaF + "\n"
            #Label si el primer if es verdadero
            codigo += "\tlabel " + expresion_logica.etiquetaV.replace(":","") + "\n"
            #instrucciones if principal
            for i in self.instrIfVerdadero:
                instruccion_if = i.traducir(tabla, arbol,cadenaTraducida)
                if isinstance(instruccion_if, Excepcion):
                    return instruccion_if
                codigo += instruccion_if

            codigo += "\tlabel " + etiquetaF + "\n"
            return codigo
            #   ...
            #   if temporal_logico:
            #       goto L1
            #   goto L10
            #   label L10
            #   ................
            #
            #   if temporal_logico2:
            #       goto L3
            #   goto L4
            #   Label L3
            #   instrucciones_elseif
            #   goto L2
            #   label L4
            #
            #   ....................
            #   instrucciones_ifFalso
            #   goto L2  
            #   label L1    
            #   instrucciones_if
            #   label L2
            #   ...
        else:
            error = Excepcion('42804',"Semántico","La expresion logica debe ser de tipo boolean",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error