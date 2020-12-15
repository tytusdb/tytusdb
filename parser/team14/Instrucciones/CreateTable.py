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
        tam = len(self.listaDef)
        print (tam)
        nuevaTabla = Simbolo(TipoSimbolo.TABLA,self.id)
        listaColumnas = []
        for x in range(0,tam,1):
            tt = self.listaDef[x]
            if tt.tipo == AtributosColumna.COLUMNA_SIMPLE:
                self.numColumnas += 1
                nuevaColumna = Simbolo(tt.tipoDato,tt.identificador)
                listaColumnas.append(nuevaColumna)
        
        nuevaTabla.valor = listaColumnas
        dbActual = ent.getDataBase()
        if dbActual != None:
            estado = DBMS.createTable(dbActual,self.id, self.numColumnas)
            if estado == 0: 
                nuevaTabla.baseDatos = dbActual
                ent.nuevoSimbolo(nuevaTabla)
                print("Tabla Creada")
                DBMS.showCollection()
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