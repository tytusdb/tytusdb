from enum import Enum

class TIPO_DE_DATO(Enum) :
    NUMERO = 1
    FLOTANTE=2
    CARACTER=3
    #ir agregando los tipos faltantes para la comprobacion de tipos en las operacioens

class Simbolo() :
    'Esta clase representa un simbolo dentro de nuestra tabla de simbolos'

    def __init__(self, id, nombre,tipo,tamanoCadena,BD,tabla,obligatorio,pk,FK,ReferenciaTablaFK,ReferenciaCampoFK,unique,idUnique,check,condicionCheck,idCheck,valor,default) :
        self.id = id
        self.nombre = nombre
        self.tipo = tipo    
        self.tamanoCadena = tamanoCadena
        self.BD = BD
        self.tabla = tabla
        self.obligatorio = obligatorio
        self.pk = pk
        self.FK = FK
        self.referenciaTablaFK = ReferenciaTablaFK
        self.referenciaCampoFK = ReferenciaCampoFK
        self.unique = unique
        self.idUnique = idUnique
        self.check = check
        self.condicionCheck = condicionCheck
        self.idCheck = idCheck
        self.valor = valor
        self.default = default
        


class TablaDeSimbolos() :
    'Esta clase representa la tabla de simbolos'

    def __init__(self, simbolos = {}) :
        self.simbolos = simbolos

    def agregar(self, simbolo) :
        self.simbolos[simbolo.id] = simbolo
    
    def obtener(self, id) :
        print("a este entra")
        if not id in self.simbolos :
            print('Error1: variable ', id, ' no definida.')
            return("no definida")
        return self.simbolos[id]
    
    def obtener2(self, id) :
        print("a este entra")
        if not id in self.simbolos :
            print('Error1: variable ', id, ' no definida.')
            return 0
        return self.simbolos[id]

    def actualizar(self, simbolo) :
        if not simbolo.id in self.simbolos :
            print('Error2: variable ', simbolo.id, ' no definida.')
        else :
            self.simbolos[simbolo.id] = simbolo

    def mostrar(self,var):
        print(str(var))
        for x in self.simbolos:
            print(x)


    def destruir(self,simbolo):
        print("########################### simbolos>",str(simbolo.id))
        if not simbolo.id in self.simbolos :
            print('Error3: variable ', simbolo.id, ' no definida.')
        else :
            self.simbolos[simbolo.id] = simbolo
            del self.simbolos[simbolo.id]
            print("si lo elimina")

    #-----------------------------------------------------------------------------------------------------------------------
    def obtenerDato(self, nombre):
        print("a este entra")
        if not nombre in self.simbolos :
            print('Error1: variable ', nombre, ' no definida.')
            return("no definida")
        return self.simbolos[nombre]

    #-----------------------------------------------------------------------------------------------------------------------
    def agregarnuevTablaBD(self,simbolo):
        clave = str(simbolo.nombre)+str(simbolo.BD)
        self.simbolos[clave] = simbolo

    def validarTabla(self,nombre,BD):
        clave = str(nombre)+str(BD)
        if not clave in self.simbolos:
            return 0
        return 1

    def obtenerTablaBD(self, nombre):
        print("a este entra")
        if not nombre in self.simbolos :
            print('Error: La tabla: ', nombre, ' no definida.')
            return 0
        return self.simbolos[nombre]

    #-----------------------------------------------------------------------------------------------------------------------
    #Inicia creacion de tabla
    def agregarnuevaColumna(self,simbolo):
        clave = str(simbolo.nombre) + str(simbolo.BD) + str(simbolo.tabla)
        self.simbolos[clave] = simbolo

    def verificarcolumnaBD(self,nombre,BD,tabla):
        clave = str(nombre) + str(BD) + str(tabla)
        if not clave in self.simbolos :
            print('Error: La tabla: ', nombre, ' no definida.')
            return 0
        return 1


    def actualizauniqueColumna(self,nombre,BD,tabla):
        clave = str(nombre) + str(BD) + str(tabla)
        for simb in self.simbolos:
            if simb == clave:
                if self.simbolos[simb].nombre == nombre and self.simbolos[simb].BD == BD and self.simbolos[simb].tabla == tabla:
                    self.simbolos[simb].unique = 1
                    print("se actualizao restriccion unique en columna")
                    return    
            #print(self.simbolos[simb].id," ",self.simbolos[simb].nombre," ",self.simbolos[simb].BD," ",self.simbolos[simb].tabla)
        print("la columna no existe")
        return 0

    def actualizarcheckColumna(self,nombre,BD,tabla,idchk,condchk):
        clave = str(nombre) + str(BD) + str(tabla)
        for simb in self.simbolos:
            if simb == clave:
                if self.simbolos[simb].nombre == nombre and self.simbolos[simb].BD == BD and self.simbolos[simb].tabla == tabla:
                    self.simbolos[simb].check = 1
                    self.simbolos[simb].condCheck = condchk
                    self.simbolos[simb].idCheck = idchk
                    print("se actualizo restricion check en columna")
                    return
            #print(self.simbolos[simb].id," ",self.simbolos[simb].nombre," ",self.simbolos[simb].BD," ",self.simbolos[simb].tabla)
        print("la columna no existe")
        return 0

    def actualizapkcolumna(self,nombre,BD,tabla):
        clave = str(nombre) + str(BD) + str(tabla)
        for simb in self.simbolos:
            if simb == clave:
                if self.simbolos[simb].nombre == nombre and self.simbolos[simb].BD == BD and self.simbolos[simb].tabla == tabla:
                    self.simbolos[simb].pk = 1
                    print("se actualizo restricion llave primaria en columna")
                    return
            #print(self.simbolos[simb].id," ",self.simbolos[simb].nombre," ",self.simbolos[simb].BD," ",self.simbolos[simb].tabla)
        print("la columna no existe")
        return 0
    
    def actualizafkcolumna(self,nombre,BD,tabla,idrefcolumna,idreftabla):
        clave = str(nombre) + str(BD) + str(tabla)
        for simb in self.simbolos:
            if simb == clave:
                if self.simbolos[simb].nombre == nombre and self.simbolos[simb].BD == BD and self.simbolos[simb].tabla == tabla:
                    self.simbolos[simb].fk = 1
                    self.simbolos[simb].referenciaCampoFK = idrefcolumna
                    self.simbolos[simb].referenciaTablaFK = idreftabla
                    print("se actualizo columna como llave foranea")
                    return
            #print(self.simbolos[simb].id," ",self.simbolos[simb].nombre," ",self.simbolos[simb].BD," ",self.simbolos[simb].tabla)
        print("la columna no existe")
        return 0
    
    #-----------------------------------------------------------------------------------------------------------------------
    #Inicia Insert en Tabla


    def printcontsimbolos(self):
        tm = 0
        for simb in self.simbolos:
            print("----------Columna ",tm,"----------")
            print(self.simbolos[simb].id)
            print(self.simbolos[simb].nombre)
            print(self.simbolos[simb].tipo)
            print(self.simbolos[simb].tamanoCadena)
            print(self.simbolos[simb].BD)
            print(self.simbolos[simb].tabla)
            print(self.simbolos[simb].obligatorio)
            print(self.simbolos[simb].pk)
            print(self.simbolos[simb].FK)
            print(self.simbolos[simb].referenciaTablaFK)
            print(self.simbolos[simb].referenciaCampoFK)
            print(self.simbolos[simb].unique)
            print(self.simbolos[simb].idUnique)
            print(self.simbolos[simb].check)
            print(self.simbolos[simb].condicionCheck)
            print(self.simbolos[simb].idCheck)
            print(self.simbolos[simb].valor)
            tm=tm+1
        return 0
# --------------------CREAR, ALTER Y DROP BD---------------------------------------------------------------------
    def agregarCrearBD(self, simbolo) :
        self.simbolos[simbolo.nombre] = simbolo

    
    def verificacionCrearBD(self, nombre) :
        for simb in self.simbolos:            
            if self.simbolos[simb].nombre == nombre and self.simbolos[simb].BD == None and self.simbolos[simb].tabla == None:
                print('Error1: base de datos ', nombre, ' ya definida.')
                return 1
        return 0 

    def verificacionAlterBD(self, nombre) :
        for simb in self.simbolos:            
            if self.simbolos[simb].nombre == nombre and self.simbolos[simb].BD == None and self.simbolos[simb].tabla == None:
                return 1
        return 0

    def actualizarAlterBD(self, old, alter) :
        for simb in self.simbolos:            
            if self.simbolos[simb].nombre == old and self.simbolos[simb].BD == None and self.simbolos[simb].tabla == None:
                print("SIMB",self.simbolos[simb])
                self.simbolos[alter] = self.simbolos.pop(simb)
                self.simbolos[alter].nombre = alter
                return 2
        return 1

    def destruirBD(self,nombre):
        for simb in self.simbolos:
            if self.simbolos[simb].nombre == nombre and self.simbolos[simb].BD == None and self.simbolos[simb].tabla == None:
                print('Se elimino ', nombre)
                self.simbolos.pop(simb)
                return 1
        return 0

    def printBD(self):
        tm = 0
        for simb in self.simbolos:
            print("----------BASE DE DATOS ",tm,"----------")
           # print(self.simbolos[simb].id)
            print(self.simbolos[simb].nombre)
            tm=tm+1
        return 0