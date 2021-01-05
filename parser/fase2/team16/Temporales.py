from random import *

class Temporales:
    def __init__(self, tablaSimbolos={}, variables={}, funciones={}, temp= 0, etiqueta = 0, parametro=0, funcion = 1, retorno = 0):
        self.variables = variables.copy()
        self.parametro = parametro
        self.funciones = funciones.copy()
        self.tablaSimbolos = tablaSimbolos.copy()
        self.temp = temp
        self.etiqueta = etiqueta
        self.funcion = funcion
        self.retorno = retorno

    def limpiar(self):
        self.temp = 0
        self.parametro = 0
        self.etiqueta = 0

    def varTemporal(self):
        variable = "t" + str(self.temp)
        self.temp += 1
        return str(variable)

    def varParametro(self):
        variable = "p" + str(self.parametro)
        self.parametro += 1
        return str(variable)

    def varRetorno(self):
        variable = "r" + str(self.retorno)
        self.retorno += 1
        return str(variable)

    def varFuncion(self):
        variable = "F" + str(self.funcion)
        self.funcion += 1
        return str(variable)

    def varFuncionAnterior(self):
        variable = self.funcion
        return variable

    def etiquetaT(self):
        variable = "L" + str(self.etiqueta)
        self.etiqueta += 1
        return variable

    def agregarVar(self, varT, variableObjeto):
        self.variables[varT] = variableObjeto

    def agregarSimbolo(self, simbolo):
        rand = randint(1, 25000)
        self.tablaSimbolos[str(simbolo.nombre)+str(rand)] = simbolo

    def obtenerSimbolo(self, simbolo):
        if not simbolo in self.tablaSimbolos:
            pass
            return None
        else:
            return self.tablaSimbolos[simbolo]

    def actualizarSimbolo(self, simbolo, nuevoSi):
        if not simbolo in self.tablaSimbolos:
            print("Si se actualizo.")
            pass
        else:
            self.tablaSimbolos[simbolo] = nuevoSi

class tipoSimbolo():
    def __init__(self, temporal, nombre, tipo, tam, pos, rol, ambito):
        self.temporal = temporal
        self.nombre = nombre
        self.tipo = tipo
        self.tam = tam
        self.pos = pos
        self.rol = rol
        self.ambito = ambito