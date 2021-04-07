from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
from Instrucciones.TablaSimbolos.Nodo3D import Nodo3D
from Instrucciones.Sql_select.SelectLista import SelectLista2
from Instrucciones.Excepcion import Excepcion

class Asignacion(Instruccion):
    def __init__(self, id, expresion, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.id = id
        self.expresion = expresion

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        pass

    def analizar(self, tabla, arbol):
        super().analizar(tabla,arbol)
        variable = tabla.getSimboloVariable(self.id)
        if variable == None:
            error = Excepcion("42723", "Semantico", f"La variable {self.id} no ha sido declarada", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error 
        
        resultado = self.expresion.analizar(tabla,arbol)
        if not isinstance(resultado, Excepcion):
            self.tipo = resultado

        comprobar = self.comprobarTipo(variable.tipo, resultado, None)

        if not comprobar:
            error = Excepcion('42804',"Semántico",f"La variable {self.id} es de tipo {variable.tipo.toString()} pero la expresión es de tipo {resultado.toString()}.",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
               
        
    def traducir(self, tabla, arbol):
        super().traducir(tabla,arbol)
        retorno = Nodo3D()
        variable = tabla.getSimboloVariable(self.id)
        arbol.addComen(f"Inicia asignación: {self.id}")
        temporal1 = tabla.getTemporal()
        temporal2 = tabla.getTemporal()
        arbol.addc3d(f"{temporal1} = P + {variable.posicion}")
        arbol.addComen("Se obtiene el valor")
        
        if isinstance(self.expresion, SelectLista2):
            arbol.addc3d("arbol.expre_query = True")
            exp = self.expresion.c3d(tabla, arbol)
        else:
            exp = self.expresion.traducir(tabla, arbol)
        
        if variable.tipo.tipo == Tipo_Dato.BOOLEAN and exp.temporalAnterior != "1" and exp.temporalAnterior != "0":
            retorno.imprimirEtiquetDestino(arbol, exp.etiquetaTrue)
            arbol.addc3d(f"{temporal2} = 1")
            etiqueta1 = tabla.getEtiqueta()
            arbol.addc3d(f"goto .{etiqueta1}")
            retorno.imprimirEtiquetDestino(arbol, exp.etiquetaFalse)
            arbol.addc3d(f"{temporal2} = 0")
            arbol.addc3d(f"label .{etiqueta1}")
        else:
            arbol.addc3d(f"{temporal2} = {exp.temporalAnterior}")
        arbol.addc3d(f"Pila[{temporal1}] = {temporal2}")
        if isinstance(self.expresion, SelectLista2):
            arbol.addc3d("arbol.expre_query = False")
        arbol.addComen("Fin Asignación")



    def comprobarTipo(self, tipoColumna, tipoValor, val):
        if tipoValor.tipo == Tipo_Dato.QUERY:
            return True
        if (tipoColumna.tipo == Tipo_Dato.MONEY) and (tipoValor.tipo == Tipo_Dato.CHAR):
            if ',' in val:
                val = val.replace(',','')
            try:
                val = float(val)
            except:
                return False
            return True
        if (tipoColumna.tipo == Tipo_Dato.CHAR or tipoColumna.tipo == Tipo_Dato.VARCHAR or tipoColumna.tipo == Tipo_Dato.VARYING or tipoColumna.tipo == Tipo_Dato.CHARACTER or tipoColumna.tipo == Tipo_Dato.TEXT) and (tipoValor.tipo == Tipo_Dato.CHAR or tipoValor.tipo == Tipo_Dato.VARCHAR or tipoValor.tipo == Tipo_Dato.VARYING or tipoValor.tipo == Tipo_Dato.CHARACTER or tipoValor.tipo == Tipo_Dato.TEXT):
            if tipoColumna.dimension != None:
                pass
            return True
        elif (tipoColumna.tipo == Tipo_Dato.SMALLINT or tipoColumna.tipo == Tipo_Dato.INTEGER or tipoColumna.tipo == Tipo_Dato.BIGINT or tipoColumna.tipo == Tipo_Dato.DECIMAL or tipoColumna.tipo == Tipo_Dato.NUMERIC or tipoColumna.tipo == Tipo_Dato.REAL or tipoColumna.tipo == Tipo_Dato.DOUBLE_PRECISION or tipoColumna.tipo == Tipo_Dato.MONEY) and (tipoValor.tipo == Tipo_Dato.SMALLINT or tipoValor.tipo == Tipo_Dato.INTEGER or tipoValor.tipo == Tipo_Dato.BIGINT or tipoValor.tipo == Tipo_Dato.DECIMAL or tipoValor.tipo == Tipo_Dato.NUMERIC or tipoValor.tipo == Tipo_Dato.REAL or tipoValor.tipo == Tipo_Dato.DOUBLE_PRECISION or tipoValor.tipo == Tipo_Dato.MONEY):
            if tipoColumna.tipo == Tipo_Dato.SMALLINT:
                pass
            elif tipoColumna.tipo == Tipo_Dato.INTEGER:
                pass
            elif tipoColumna.tipo == Tipo_Dato.BIGINT:
                pass
            return True
        elif (tipoColumna.tipo == Tipo_Dato.DATE or tipoColumna.tipo == Tipo_Dato.TIMESTAMP or tipoColumna.tipo == Tipo_Dato.TIME or tipoColumna.tipo == Tipo_Dato.INTERVAL or tipoColumna.tipo == Tipo_Dato.CHAR ) and (tipoValor.tipo == Tipo_Dato.DATE or tipoValor.tipo == Tipo_Dato.TIMESTAMP or tipoValor.tipo == Tipo_Dato.TIME or tipoValor.tipo == Tipo_Dato.INTERVAL or tipoValor.tipo == Tipo_Dato.CHAR):
            return True
        elif (tipoColumna.tipo == Tipo_Dato.BOOLEAN) and (tipoValor.tipo == Tipo_Dato.BOOLEAN):
            return True
        return False