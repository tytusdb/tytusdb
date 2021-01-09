from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Sql_select.Select import Select
from Instrucciones.Tablas.Tablas import Tablas
from Instrucciones.TablaSimbolos import Instruccion3D as c3d
from Optimizador.C3D import Valor as ClassValor
from Optimizador.C3D import OP_ARITMETICO as ClassOP_ARITMETICO
from Optimizador.C3D import Identificador as ClassIdentificador

class SelectLista(Instruccion):
    def __init__(self, lista, strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.QUERY),linea,columna,strGram)
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

    def generar3D(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append(c3d.asignacionH())
        code.append(c3d.aumentarP())
        t0 = c3d.getTemporal()
        code.append(c3d.asignacionString(t0, "SELECT "))

        sizeCol = len(self.lista)
        contador = 1
        for el in self.lista:
            code += el.generar3D(tabla, arbol)
            if contador != sizeCol:
                t0 = c3d.getLastTemporal()
                t1 = c3d.getTemporal()
                code.append(c3d.operacion(t1, ClassIdentificador(t0), ClassValor("\", \"", "STRING"), ClassOP_ARITMETICO.SUMA))
            contador += 1

        t0 = c3d.getLastTemporal()
        t1 = c3d.getTemporal()
        code.append(c3d.operacion(t1, ClassIdentificador(t0), ClassValor("\";\"", "STRING"), ClassOP_ARITMETICO.SUMA))
        
        code.append(c3d.asignacionTemporalStack(t1))
        code.append(c3d.LlamFuncion('call_funcion_intermedia'))

        return code


class Alias():
    def __init__(self, id, expresion):
        self.id = id
        self.expresion = expresion
        self.tipo = None