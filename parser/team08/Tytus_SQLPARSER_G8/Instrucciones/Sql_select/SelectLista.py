from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion

class SelectLista(Instruccion):
    def __init__(self, lista, linea, columna):
        Instruccion.__init__(self,None,linea,columna)
        self.lista = lista

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        columnas = []
        valores = []
        for ins in self.lista:
            if isinstance(ins, Alias):
                resultado = ins.expresion.ejecutar(tabla, arbol)
                if isinstance(resultado, Excepcion):
                    return resultado
                valores.append(str(resultado))
                columnas.append(ins.id)
            else:
                resultado = ins.ejecutar(tabla, arbol)
                if isinstance(resultado, Excepcion):
                    return resultado
                valores.append(str(resultado))
                columnas.append('col')
        valores = [valores]
        lf = []
        for i in range(0,len(columnas)):
            temporal = []
            temporal.append(len(columnas[i]))
            for l in valores:
                temporal.append(len(str(l[i])))
            lf.append(max(temporal))

        # Encabezado
        cad = ''
        for s in range(0,len(lf)):
            cad += '+---'+'-'*lf[s]
        cad += '+\n'    
        for s in range(0,len(lf)):
            cad += '| ' +str(columnas[s]) + ' ' *((lf[s]+4)-(2+len(str(columnas[s]))))
        cad += '|\n'
        cad += '|'
        for s in range(0,len(lf)):
            cad += '---'+'-'*lf[s]+ '+'
        size = len(cad)
        cad = cad[:size - 1] + "|\n"

        # Valores
        for i in valores:
            for j in range(0,len(lf)):
                cad += '| ' + str(i[j]) + ' ' *((lf[j]+4)-(2+len(str(i[j]))))
            cad += "|\n"
        # Línea final
        for s in range(0,len(columnas)):
            cad += '+---'+'-'*lf[s]
        cad += '+\n' 
        
        arbol.consola.append(cad)

class Alias():
    def __init__(self, id, expresion):
        self.id = id
        self.expresion = expresion