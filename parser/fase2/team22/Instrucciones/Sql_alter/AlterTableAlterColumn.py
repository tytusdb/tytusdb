from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Sql_create.Tipo_Constraint import Tipo_Constraint, Tipo_Dato_Constraint
from Instrucciones.Excepcion import Excepcion

from Instrucciones.TablaSimbolos import Instruccion3D as c3d

class AlterTableAlterColumn(Instruccion):
    def __init__(self, tabla, col, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.tabla = tabla
        self.col = col

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if arbol.bdUsar != None:
            objetoTabla = arbol.devolviendoTablaDeBase(self.tabla)
            if objetoTabla != 0:
                existe = None
                for columnas in objetoTabla.lista_de_campos:
                    if columnas.nombre == self.col:
                        existe = columnas
                if existe != None:
                    #print(len(listaUnique),self.tabla, self.id)
                    #Insertar llaves Unique
                    if existe.constraint != None:
                        existe.constraint.append(Tipo_Constraint(None, Tipo_Dato_Constraint.NOT_NULL, None))
                        #print("MÁS DE UNA-----------------",existe.nombre, existe.tipo.toString(),len(existe.constraint))
                    else:
                        existe.constraint = []
                        existe.constraint.append(Tipo_Constraint(None, Tipo_Dato_Constraint.NOT_NULL, None))
                        #print("SOLO UNA-------------",existe.nombre, existe.tipo.toString(),len(existe.constraint)) 
                    arbol.consola.append("Consulta devuelta correctamente.")  
                else:
                    #print(listaNombres,self.lista_col)
                    #print(lista)
                    error = Excepcion('42P01',"Semántico","No existe la columna «"+self.col+"» en la llave",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            else:
                error = Excepcion('42P01',"Semántico","No existe la relación "+self.tabla,self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        else:
            error = Excepcion("100","Semantico","No ha seleccionado ninguna Base de Datos.",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
        
    def generar3DV2(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append('h = p')
        code.append('h = h + 1')
        t0 = c3d.getTemporal()
        bd = arbol.getBaseDatos()
        if bd != None and bd != "":
            code.append(t0 + ' = "' + bd + '"')
        else:
            code.append(t0 + ' = ' + str(None))
        code.append('heap[h] = ' + t0)
        code.append('h = h + 1')
        t1 = c3d.getTemporal()
        code.append(t1 + ' = "' + str(self.tabla) + '"')
        code.append('heap[h] = ' + t1)
        code.append('h = h + 1')
        t2 = c3d.getTemporal()
        code.append(t2 + ' = "' + str(self.col) + '"')
        code.append('heap[h] = ' + t2)
        code.append('p = h')
        code.append('call_alterTable_alterColumn()')
        
        return code