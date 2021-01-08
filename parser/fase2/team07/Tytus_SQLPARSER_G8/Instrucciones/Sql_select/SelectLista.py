from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Sql_select.Select import Select
from Instrucciones.Tablas.Tablas import Tablas
from Instrucciones.TablaSimbolos.Simbolo3D import Simbolo3d


class SelectLista(Instruccion):
    def __init__(self, lista, strGram, linea, columna, strSent):
        Instruccion.__init__(self,Tipo("",Tipo_Dato.QUERY),linea,columna,strGram,strSent)
        self.lista = lista

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        columnas = []
        valores = []
        selectEncontrado = 0
        for ins in self.lista:
            if isinstance(ins, Alias):
                resultado = ins.expresion.ejecutar(tabla, arbol)
                if isinstance(resultado, Excepcion):
                    return resultado
                valores.append(str(resultado))
                columnas.append(ins.id)
            elif isinstance(ins, Select):
                resultado = ins.ejecutar(tabla, arbol)
                if isinstance(resultado, Excepcion):
                    return resultado
                valores = resultado
                columnas = ins.devolverColumnas(tabla,arbol)
                if isinstance(columnas, Excepcion):
                    return columnas
                selectEncontrado = 1
            else:
                resultado = ins.ejecutar(tabla, arbol)
                if isinstance(resultado, Excepcion):
                    return resultado
                valores.append(str(resultado))
                columnas.append('col')
        #print("COLUMNAS-------------------------->",columnas)
        #print("VALORES-------------------------->",valores)
        if(selectEncontrado == 0):
            valores = [valores]
            
            if(arbol.getRelaciones() == False):
                arbol.getMensajeTabla(columnas,valores)
            else:
                n = Tablas("tabla",None)
                n.data = valores
                n.lista_de_campos = columnas
                return n
        else:
            if(arbol.getRelaciones() == False):
                arbol.getMensajeTabla(columnas,valores)
            else:
                n = Tablas("tabla",None)
                n.lista_de_campos = columnas
                n.data = valores
                return n
    
    def traducir(self,tabla,arbol,cadenaTraducida):
        temporal1 = arbol.generaTemporal()
        codigo = "\t" + temporal1 + " = " + "\"" + self.strSent + "\"\n"
        temporal = arbol.generaTemporal()
        codigo += "\t" + temporal + " = FuncionesPara3D.ejecutarsentecia(" + temporal1 + ")\n\n"
        return Simbolo3d(Tipo("",Tipo_Dato.INTEGER), temporal, codigo, None, None)



class Alias():
    def __init__(self, id, expresion, strSent):
        self.id = id
        self.expresion = expresion
        self.tipo = None
        self.strSent = strSent