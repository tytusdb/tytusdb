from Instrucciones.Instruccion import Instruccion
from Instrucciones.AtrColumna import AtributosColumna
from storageManager import jsonMode as DBMS
from Entorno.Entorno import Entorno
from Entorno.Simbolo import Simbolo
from Entorno.TipoSimbolo import TipoSimbolo

class CreateTable(Instruccion):
    def __init__(self, id:str, listaDef):
        self.id = id
        self.listaDef = listaDef
        self.numColumnas = 0

    def ejecutar(self, ent:Entorno):
        dbActual = ent.getDataBase()
        tam = len(self.listaDef)
        print (tam)
        nuevaTabla = Simbolo(TipoSimbolo.TABLA,self.id)
        listaColumnas = []
        for x in range(0,tam,1):
            tt = self.listaDef[x]
            if tt.tipo == AtributosColumna.COLUMNA_SIMPLE:
                self.numColumnas += 1
                nuevaColumna = Simbolo(tt.tipoDato,tt.identificador)
                if tt.lista != None: #aca se mete si viene por ejemplo: columna1 integer references tabla2
                    tamano = len(tt.lista)
                    for y in range(tamano):
                        atrColumna = tt.lista[y]
                        if atrColumna.tipo == AtributosColumna.UNICO:
                            nuevoUnico = Simbolo(TipoSimbolo.CONSTRAINT_UNIQUE,atrColumna.valor)
                            nuevoUnico.baseDatos = dbActual
                            nuevoUnico.tabla = self.id
                            ent.nuevoSimbolo(nuevoUnico)
                            nuevaColumna.atributos.update({'unique':atrColumna.valor})
                        elif atrColumna.tipo == AtributosColumna.CHECK:
                            nuevoCheck = Simbolo(TipoSimbolo.CONSTRAINT_CHECK,atrColumna.valor)
                            nuevoCheck.baseDatos = dbActual
                            nuevoCheck.tabla = self.id
                            ent.nuevoSimbolo(nuevoCheck)
                            nuevaColumna.atributos.update({'check':atrColumna.valor})
                        elif atrColumna.tipo == AtributosColumna.DEFAULT:
                            nuevaColumna.atributos.update({'default':atrColumna.valor})
                        elif atrColumna.tipo == AtributosColumna.NO_NULO:
                            nuevaColumna.atributos.update({'not null':True})
                        elif atrColumna.tipo == AtributosColumna.NULO:
                            nuevaColumna.atributos.update({'null':True})
                        elif atrColumna.tipo == AtributosColumna.PRIMARY:
                            nuevaPrimaria = Simbolo(TipoSimbolo.CONSTRAINT_PRIMARY,str("PK_" + self.id))
                            nuevaPrimaria.baseDatos = dbActual
                            nuevaPrimaria.tabla = self.id
                            ent.nuevoSimbolo(nuevaPrimaria)
                            nuevaColumna.atributos.update({'primary':str("PK_" + self.id)})
                        elif atrColumna.tipo == AtributosColumna.REFERENCES:
                            rr = DBMS.extractTable(dbActual,atrColumna.valor)
                            if rr == []:
                                return str("La tabla \'" + atrColumna.valor + "\' a la que está referenciando, no existe")
                            else:
                                nuevaForanea = Simbolo(TipoSimbolo.CONSTRAINT_FOREIGN,str("FK_" + self.id))
                                nuevaForanea.baseDatos = dbActual
                                nuevaForanea.tabla = self.id
                                ent.nuevoSimbolo(nuevaForanea)
                                nuevaColumna.atributos.update({'foreign':str("FK_" + self.id)})
                
                listaColumnas.append(nuevaColumna)

        #considerar la situacion de cuando no se haya creado la tabla pero ya se hayan 
        #agregado los constraint a la tabla de simbolos 
        nuevaTabla.valor = listaColumnas
        if dbActual != None:
            estado = DBMS.createTable(dbActual,self.id, self.numColumnas)
            if estado == 0: 
                nuevaTabla.baseDatos = dbActual
                ent.nuevoSimbolo(nuevaTabla)
                
                DBMS.showCollection()
                return str("Tabla " + nuevaTabla.nombre + " creada exitosamente")
            #elif estado == 1: 

class Check(CreateTable):
    def __init__(self, condiciones):
        self.condiciones = condiciones
        self.tipo = AtributosColumna.CHECK

class Unique(CreateTable):
    def __init__(self, unicos):
        self.unicos = unicos
        self.tipo = AtributosColumna.UNICO

class Foranea(CreateTable):
    def __init__(self, foraneas, tabla:str, ref_lista):
        self.foraneas = foraneas
        self.tabla = tabla
        self.ref_lista = ref_lista
        self.tipo = AtributosColumna.REFERENCES

class Primaria(CreateTable):
    def __init__(self,primarias):
        self.primarias = primarias
        self.tipo = AtributosColumna.PRIMARY

class Atributo(CreateTable):
    def __init__(self,tipo:AtributosColumna,valor = None, exp = None):
        self.tipo = tipo
        self.valor = valor
        self.exp = exp

class Constraint(CreateTable):
    def __init__(self,identificador:str,objeto):
        self.id = identificador
        self.contenido = objeto
        self.tipo = AtributosColumna.CONSTRAINT

class Columna(CreateTable):
    def __init__(self,identificador:str,tipoDato,lista = None):
        self.identificador = identificador
        self.lista = lista #este recibe una lista
        self.tipoDato = tipoDato
        self.tipo = AtributosColumna.COLUMNA_SIMPLE