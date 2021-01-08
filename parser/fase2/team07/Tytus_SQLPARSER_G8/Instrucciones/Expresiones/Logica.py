from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion
from Instrucciones.TablaSimbolos.Simbolo3D import Simbolo3d

class Logica(Instruccion):
    def __init__(self, opIzq, opDer, operador, strGram, linea, columna, strSent):
        Instruccion.__init__(self,Tipo("",Tipo_Dato.BOOLEAN),linea,columna,strGram,strSent)
        self.opIzq = opIzq
        self.opDer = opDer
        self.operador = operador

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        # Operación con dos operadores
        if(self.opDer != None):
            # Si existe algún error en el operador izquierdo, retorno el error.
            resultadoIzq = self.opIzq.ejecutar(tabla, arbol)
            if isinstance(resultadoIzq, Excepcion):
                return resultadoIzq
            # Si existe algún error en el operador derecho, retorno el error.
            resultadoDer = self.opDer.ejecutar(tabla, arbol)
            if isinstance(resultadoDer, Excepcion):
                return resultadoDer
            # Comprobamos el tipo de operador
            if self.operador == 'OR':
                if self.opIzq.tipo.tipo == Tipo_Dato.BOOLEAN and self.opDer.tipo.tipo == Tipo_Dato.BOOLEAN:
                    return resultadoIzq or resultadoDer
                else:
                    error = Excepcion('42804',"Semántico","El argumento de OR debe ser de tipo boolean",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            elif self.operador == 'AND':
                if self.opIzq.tipo.tipo == Tipo_Dato.BOOLEAN and self.opDer.tipo.tipo == Tipo_Dato.BOOLEAN:
                    return resultadoIzq and resultadoDer
                else:
                    error = Excepcion('42804',"Semántico","El argumento de AND debe ser de tipo boolean",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            else:
                error = Excepcion('42804',"Semántico","Operador desconocido.",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        # Operación unaria
        else:
            # Si existe algún error en el operador izquierdo, retorno el error.
            resultadoIzq = self.opIzq.ejecutar(tabla, arbol)
            if isinstance(resultadoIzq, Excepcion):
                return resultadoIzq
            if self.operador == 'NOT':
                if self.opIzq.tipo.tipo == Tipo_Dato.BOOLEAN:
                    return resultadoIzq and resultadoDer
                else:
                    error = Excepcion('42804',"Semántico","Tipo de datos incorrectos en la operación lógica not",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            else:
                error = Excepcion('42804',"Semántico","Operador desconocido.",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
    
    # **********************************************************************************************
    # ************************************ TRADUCCIÓN **********************************************
    # **********************************************************************************************

    def traducir(self,tabla,arbol,cadenaTraducida):
        super().ejecutar(tabla,arbol)
        # Operación con dos operadores
        if(self.opDer != None):
            # Si existe algún error en el operador izquierdo, retorno el error.
            resultadoIzq = self.opIzq.traducir(tabla, arbol,cadenaTraducida)
            if isinstance(resultadoIzq, Excepcion):
                return resultadoIzq
            # Si existe algún error en el operador derecho, retorno el error.
            resultadoDer = self.opDer.traducir(tabla, arbol,cadenaTraducida)
            if isinstance(resultadoDer, Excepcion):
                return resultadoDer

            # Comprobamos el tipo de operador
            if self.operador == 'OR':
                if resultadoIzq.tipo.tipo == Tipo_Dato.BOOLEAN and resultadoDer.tipo.tipo == Tipo_Dato.BOOLEAN:
                    codigo = ""
                    etiquetaV = ""
                    etiquetaF = ""
                    
                    # operador Izquierdo
                    if resultadoIzq.temporal != "":
                        etiqueta1 = arbol.generaEtiqueta()
                        etiqueta2 = arbol.generaEtiqueta()
                        resultadoIzq.codigo += "\tif("+resultadoIzq.temporal+"==true): \n\t\tgoto ."+etiqueta1+" \n"
                        resultadoIzq.codigo += "\tgoto ."+etiqueta2+" \n"
                        resultadoIzq.etiquetaV = "\t."+etiqueta1+"\n"
                        resultadoIzq.etiquetaF = "\t."+etiqueta2+"\n"

                    codigo += resultadoIzq.codigo
                    codigo += "label " + resultadoIzq.etiquetaF + "\n\n"

                    # operador Derecho
                    if resultadoDer.temporal != "":
                        etiqueta1 = arbol.generaEtiqueta()
                        etiqueta2 = arbol.generaEtiqueta()
                        resultadoDer.codigo += "\tif("+resultadoDer.temporal+"==true): \n\t\tgoto ."+etiqueta1+ "\n"
                        resultadoDer.codigo += "\tgoto ."+etiqueta2+" \n"
                        resultadoDer.etiquetaV = "\t."+etiqueta1+"\n"
                        resultadoDer.etiquetaF = "\t."+etiqueta2+"\n"

                    codigo += resultadoDer.codigo
                    etiquetaV = resultadoIzq.etiquetaV + resultadoDer.etiquetaV
                    etiquetaF = resultadoDer.etiquetaF


                    nuevo = Simbolo3d(Tipo("",Tipo_Dato.BOOLEAN),"",codigo,etiquetaV,etiquetaF)
                    return nuevo       
                elif resultadoIzq.tipo.tipo == Tipo_Dato.ID or resultadoDer.tipo.tipo == Tipo_Dato.ID:
                    codigo = ""
                    etiquetaV = ""
                    etiquetaF = ""
                    
                    # operador Izquierdo
                    if resultadoIzq.temporal != "":
                        etiqueta1 = arbol.generaEtiqueta()
                        etiqueta2 = arbol.generaEtiqueta()
                        resultadoIzq.codigo += "\tif("+resultadoIzq.temporal+"==true): \n\t\tgoto ."+etiqueta1+" \n"
                        resultadoIzq.codigo += "\tgoto ."+etiqueta2+" \n"
                        resultadoIzq.etiquetaV = "\t."+etiqueta1+"\n"
                        resultadoIzq.etiquetaF = "\t."+etiqueta2+"\n"

                    codigo += resultadoIzq.codigo
                    codigo += "label " + resultadoIzq.etiquetaF + "\n\n"

                    # operador Derecho
                    if resultadoDer.temporal != "":
                        etiqueta1 = arbol.generaEtiqueta()
                        etiqueta2 = arbol.generaEtiqueta()
                        resultadoDer.codigo += "\tif("+resultadoDer.temporal+"==true): \n\t\tgoto ."+etiqueta1+ "\n"
                        resultadoDer.codigo += "\tgoto ."+etiqueta2+" \n"
                        resultadoDer.etiquetaV = "\t."+etiqueta1+"\n"
                        resultadoDer.etiquetaF = "\t."+etiqueta2+"\n"

                    codigo += resultadoDer.codigo
                    etiquetaV = resultadoIzq.etiquetaV + resultadoDer.etiquetaV
                    etiquetaF = resultadoDer.etiquetaF


                    nuevo = Simbolo3d(Tipo("",Tipo_Dato.ID),"",codigo,etiquetaV,etiquetaF)
                    return nuevo                                  
                else:
                    error = Excepcion('42804',"Semántico","El argumento de OR debe ser de tipo boolean",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            elif self.operador == 'AND':
                if resultadoIzq.tipo.tipo == Tipo_Dato.BOOLEAN and resultadoDer.tipo.tipo == Tipo_Dato.BOOLEAN:
                    codigo = ""
                    etiquetaV = ""
                    etiquetaF = ""

                    #operador Izquierdo
                    if resultadoIzq.temporal != "":
                        etiqueta1 = arbol.generaEtiqueta()
                        etiqueta2 = arbol.generaEtiqueta()
                        resultadoIzq.codigo += "\tif("+resultadoIzq.temporal+"==true): \n\t\tgoto ."+etiqueta1+" \n"
                        resultadoIzq.codigo += "\tgoto ."+etiqueta2+" \n"
                        resultadoIzq.etiquetaV =  "\t."+etiqueta1+"\n"
                        resultadoIzq.etiquetaF = "\t."+etiqueta2+"\n"

                    codigo += resultadoIzq.codigo
                    codigo += "label "+resultadoIzq.etiquetaV +"\n"

                    #Operador Derecho
                    if resultadoDer.temporal != "":
                        etiqueta1 = arbol.generaEtiqueta()
                        etiqueta2 = arbol.generaEtiqueta()
                        resultadoDer.codigo += "\tif("+resultadoDer.temporal+"==true): \n\t\tgoto ."+etiqueta1+" \n"
                        resultadoDer.codigo += "\tgoto ."+etiqueta2+" \n"
                        resultadoDer.etiquetaV = "\t."+etiqueta1+"\n"
                        resultadoDer.etiquetaF = "\t."+etiqueta2+"\n"

                    codigo += resultadoDer.codigo
                    etiquetaV = resultadoDer.etiquetaV
                    etiquetaF = resultadoIzq.etiquetaF + resultadoDer.etiquetaF

                    nuevo = Simbolo3d(Tipo("",Tipo_Dato.BOOLEAN),"",codigo,etiquetaV,etiquetaF)
                    return nuevo  
                elif resultadoIzq.tipo.tipo == Tipo_Dato.ID or resultadoDer.tipo.tipo == Tipo_Dato.ID:
                    codigo = ""
                    etiquetaV = ""
                    etiquetaF = ""

                    #operador Izquierdo
                    if resultadoIzq.temporal != "":
                        etiqueta1 = arbol.generaEtiqueta()
                        etiqueta2 = arbol.generaEtiqueta()
                        resultadoIzq.codigo += "\tif("+resultadoIzq.temporal+"==true): \n\t\tgoto ."+etiqueta1+" \n"
                        resultadoIzq.codigo += "\tgoto ."+etiqueta2+" \n"
                        resultadoIzq.etiquetaV =  "\t."+etiqueta1+"\n"
                        resultadoIzq.etiquetaF = "\t."+etiqueta2+"\n"

                    codigo += resultadoIzq.codigo
                    codigo += "label "+resultadoIzq.etiquetaV +"\n"

                    #Operador Derecho
                    if resultadoDer.temporal != "":
                        etiqueta1 = arbol.generaEtiqueta()
                        etiqueta2 = arbol.generaEtiqueta()
                        resultadoDer.codigo += "\tif("+resultadoDer.temporal+"==true): \n\t\tgoto ."+etiqueta1+" \n"
                        resultadoDer.codigo += "\tgoto ."+etiqueta2+" \n"
                        resultadoDer.etiquetaV = "\t."+etiqueta1+"\n"
                        resultadoDer.etiquetaF = "\t."+etiqueta2+"\n"

                    codigo += resultadoDer.codigo
                    etiquetaV = resultadoDer.etiquetaV
                    etiquetaF = resultadoIzq.etiquetaF + resultadoDer.etiquetaF

                    nuevo = Simbolo3d(Tipo("",Tipo_Dato.ID),"",codigo,etiquetaV,etiquetaF)
                    return nuevo  
                else:
                    error = Excepcion('42804',"Semántico","El argumento de AND debe ser de tipo boolean",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            else:
                error = Excepcion('42804',"Semántico","Operador desconocido.",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        # Operación unaria
        else:
            # Si existe algún error en el operador izquierdo, retorno el error.
            resultadoIzq = self.opIzq.traducir(tabla, arbol,cadenaTraducida)
            if isinstance(resultadoIzq, Excepcion):
                return resultadoIzq

            if self.operador == 'NOT':
                if resultadoIzq.tipo.tipo == Tipo_Dato.BOOLEAN:
                    
                    if resultadoIzq.temporal != "":
                        etiqueta1 = arbol.generaEtiqueta()
                        etiqueta2 = arbol.generaEtiqueta()
                        resultadoIzq.codigo += "\tif("+resultadoIzq.temporal+"==true): \n\t\tgoto ."+etiqueta1+"\n"
                        resultadoIzq.codigo += "\tgoto ."+etiqueta2+"\n"
                        resultadoIzq.etiquetaV = "\tt\t."+etiqueta1+"\n"
                        resultadoIzq.etiquetaF = "\t."+etiqueta2+"\n"

                    
                    veradadera = resultadoIzq.etiquetaV
                    falsa = resultadoIzq.etiquetaF

                    resultadoIzq.etiquetaV = falsa
                    resultadoIzq.etiquetaF = veradadera

                    return resultadoIzq
                
                elif resultadoIzq.tipo.tipo == Tipo_Dato.ID:
                    if resultadoIzq.temporal != "":
                        etiqueta1 = arbol.generaEtiqueta()
                        etiqueta2 = arbol.generaEtiqueta()
                        resultadoIzq.codigo += "\tif("+resultadoIzq.temporal+"==true): \n\t\tgoto ."+etiqueta1+"\n"
                        resultadoIzq.codigo += "\tgoto ."+etiqueta2+"\n"
                        resultadoIzq.etiquetaV = "\tt\t."+etiqueta1+"\n"
                        resultadoIzq.etiquetaF = "\t."+etiqueta2+"\n"

                    
                    veradadera = resultadoIzq.etiquetaV
                    falsa = resultadoIzq.etiquetaF

                    resultadoIzq.etiquetaV = falsa
                    resultadoIzq.etiquetaF = veradadera

                    return resultadoIzq
                else:
                    error = Excepcion('42804',"Semántico","Tipo de datos incorrectos en la operación lógica not",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            else:
                error = Excepcion('42804',"Semántico","Operador desconocido.",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error