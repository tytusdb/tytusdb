from sql.Instrucciones.Sql_create.Tipo_Constraint import Tipo_Constraint, Tipo_Dato_Constraint
from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.Declaracion import Declaracion
from sql.Instrucciones.TablaSimbolos.Tabla import Tabla
from sql.Instrucciones.Excepcion import Excepcion
#from sql.storageManager.jsonMode import *

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
        