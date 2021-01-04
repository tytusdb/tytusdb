from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Sql_create.Tipo_Constraint import Tipo_Constraint, Tipo_Dato_Constraint
from Instrucciones.Excepcion import Excepcion


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
    
    def analizar(self, tabla, arbol):
        pass
    
    def traducir(self, tabla, arbol):
        #ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PUNTO_COMA
        cadena = "\"alter table "
        if(self.tabla):
            cadena += self.tabla
        cadena += " alter column "
        if(self.col):
            cadena += self.col
        cadena += " set not null"          
        cadena += ";\""

        arbol.addComen("Asignar cadena")
        temporal1 = tabla.getTemporal()
        arbol.addc3d(f"{temporal1} = { cadena }")

        arbol.addComen("Entrar al ambito")
        temporal2 = tabla.getTemporal()
        arbol.addc3d(f"{temporal2} = P+2")
        temporal3 = tabla.getTemporal()
        arbol.addComen("parametro 1")
        arbol.addc3d(f"{temporal3} = { temporal2}+1")
        arbol.addComen("Asignacion de parametros")
        arbol.addc3d(f"Pila[{temporal3}] = {temporal1}")

        arbol.addComen("Llamada de funcion")
        arbol.addc3d(f"P = P+2")
        arbol.addc3d(f"funcionintermedia()")
        
        arbol.addComen("obtener resultado")
        temporalX = tabla.getTemporal()
        arbol.addc3d(f"{temporalX} = P+2")
        temporalR = tabla.getTemporal()
        arbol.addc3d(f"{temporalR} = Pila[{ temporalX }]")

        arbol.addComen("Salida de funcion")
        arbol.addc3d(f"P = P-2")

