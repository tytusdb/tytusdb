from Instrucciones.Sql_create.Tipo_Constraint import Tipo_Constraint, Tipo_Dato_Constraint
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Declaracion import Declaracion
from Instrucciones.TablaSimbolos.Tabla import Tabla
from Instrucciones.Excepcion import Excepcion
from Instrucciones.TablaSimbolos import Instruccion3D as c3d
#from storageManager.jsonMode import *

class AlterTableAddCheck(Instruccion):
    def __init__(self, tabla, condicion, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.tabla = tabla
        self.condicion = condicion

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        # Ambito para la tabla
        tablaLocal = Tabla(tabla)
        if arbol.bdUsar != None:
            objetoTabla = arbol.devolviendoTablaDeBase(self.tabla)
            if objetoTabla != 0:
                for columnas in objetoTabla.lista_de_campos:
                    arbol.comprobacionCreate = True
                    objeto = Declaracion(columnas.nombre, columnas.tipo, None)
                    objeto.ejecutar(tablaLocal, arbol)
                resultado = self.condicion.ejecutar(tablaLocal,arbol)
                if isinstance(resultado, Excepcion):
                    return resultado
                # Buscamos el nombre del constraint
                col = None
                for columnas in objetoTabla.lista_de_campos:
                        if columnas.nombre == arbol.columnaCheck:
                            col = columnas
                            break
                nombre = ''
                if col.constraint != None:
                    for const in columnas.constraint:
                        if const.tipo == Tipo_Dato_Constraint.CHECK:
                            nombre = const.id
                    last_char = nombre[-1]
                    sinNumero = nombre[:-1]
                    nuevo = sinNumero + str(int(last_char)+1)
                    col.constraint.append(Tipo_Constraint(nuevo, Tipo_Dato_Constraint.CHECK, self.condicion))                   
                else:
                    col.constraint = []
                    col.constraint.append(Tipo_Constraint(self.tabla+"_"+arbol.columnaCheck+"_check1", Tipo_Dato_Constraint.CHECK, self.condicion))
                arbol.comprobacionCreate = False
                arbol.columnaCheck = None
                arbol.consola.append("Consulta devuelta correctamente.")
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
        code.append(t2 + ' = "' + str(self.condicion) + '"')
        code.append('heap[h] = ' + t2)
        code.append('p = h')
        code.append('call_alterTable_addCheck()')
        
        return code    