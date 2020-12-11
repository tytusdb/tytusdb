import AST.Nodo as Node
from TablaSimbolos.Tipos import *
from Errores.Nodo_Error import *


class Aritmetica(Node.Nodo):
    def __init__(self, Exp1, Exp2, op, fila, col):
        self.Exp1 = Exp1
        self.Exp2 = Exp2
        self.op = op
        self.fila = fila
        self.columna = col

    def analizar(self, TS, Errores):
        tipo1 = self.Exp1.analizar(TS, Errores)
        tipo2 = self.Exp2.analizar(TS, Errores)

        if self.op == '+':

            if (
                    tipo1 == TIPO_DATOS.INT or tipo1 == TIPO_DATOS.CHAR or tipo1 == TIPO_DATOS.FLOAT or tipo1 == TIPO_DATOS.DOUBLE) and (
                    tipo2 == TIPO_DATOS.CHAR or tipo2 == TIPO_DATOS.INT or tipo2 == TIPO_DATOS.FLOAT or tipo2 == TIPO_DATOS.DOUBLE):
                if tipo1 == TIPO_DATOS.INT and tipo2 == TIPO_DATOS.INT:
                    return TIPO_DATOS.FLOAT
                elif tipo1 == TIPO_DATOS.CHAR or tipo2 == TIPO_DATOS.CHAR:
                    return TIPO_DATOS.INT
                return TIPO_DATOS.FLOAT
            else:
                return TIPO_DATOS.CHAR

        elif self.op == '-' or self.op == '*':
            if (
                    tipo1 == TIPO_DATOS.INT or tipo1 == TIPO_DATOS.CHAR or tipo1 == TIPO_DATOS.FLOAT or tipo1 == TIPO_DATOS.DOUBLE) and (
                    tipo2 == TIPO_DATOS.CHAR or tipo2 == TIPO_DATOS.INT or tipo2 == TIPO_DATOS.FLOAT or tipo2 == TIPO_DATOS.DOUBLE):
                if tipo1 == TIPO_DATOS.INT and tipo2 == TIPO_DATOS.INT:
                    return TIPO_DATOS.INT
                elif tipo1 == TIPO_DATOS.CHAR or tipo2 == TIPO_DATOS.CHAR:
                    return TIPO_DATOS.INT
                return TIPO_DATOS.FLOAT
            else:
                Errores.insertar(
                    Nodo_Error("Semantico", "No es posible operacion entre " + str(tipo1.name) + ' ' + self.op
                               + ' ' + str(tipo2.name), self.fila, self.columna))
                return TIPO_DATOS.ERROR

        elif self.op == '/':
            if (
                    tipo1 == TIPO_DATOS.INT or tipo1 == TIPO_DATOS.CHAR or tipo1 == TIPO_DATOS.FLOAT or tipo1 == TIPO_DATOS.DOUBLE) and (
                    tipo2 == TIPO_DATOS.CHAR or tipo2 == TIPO_DATOS.INT or tipo2 == TIPO_DATOS.FLOAT or tipo2 == TIPO_DATOS.DOUBLE):
                return TIPO_DATOS.FLOAT
            else:
                Errores.insertar(
                    Nodo_Error("Semantico", "No es posible operacion entre " + str(tipo1.nombre) + ' ' + self.op
                               + ' ' + str(tipo2.nombre), self.fila, self.columna))
                return TIPO_DATOS.ERROR
        elif self.op == '%':
            if (tipo1 == TIPO_DATOS.INT or tipo1 == TIPO_DATOS.CHAR) and (
                    tipo2 == TIPO_DATOS.CHAR or tipo2 == TIPO_DATOS.INT):
                return TIPO_DATOS.INT
            else:
                Errores.insertar(
                    Nodo_Error("Semantico", "No es posible operacion entre " + str(tipo1.nombre) + ' ' + self.op
                               + ' ' + str(tipo2.nombre), self.fila, self.columna))
                return TIPO_DATOS.ERROR

    def getC3D(self, TS):
        codigo = ""

        codigo += self.Exp1.getC3D(TS)
        codigo += self.Exp2.getC3D(TS)
        temp = TS.getTemp()
        self.temporal = temp
        codigo += TS.make3d(temp, self.Exp1.temporal, self.op, self.Exp2.temporal)
        return codigo

    def graficarasc(self, padre, grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Exp'))
        grafica.edge(padre, nombrehijo)
        if self.Exp1 is not None:
            self.Exp1.graficarasc(nombrehijo, grafica)
        grafica.node('NodeE1' + str(id(self)), label=(str(self.op)))
        grafica.edge(nombrehijo, 'NodeE1' + str(id(self)))
        if self.Exp2 is not None:
            self.Exp2.graficarasc(nombrehijo, grafica)


class Relacional(Node.Nodo):
    def __init__(self, Exp1, Exp2, op, fila, col):
        self.Exp1 = Exp1
        self.Exp2 = Exp2
        self.op = op
        self.fila = fila
        self.columna = col

    def analizar(self, TS, Errores):
        tipo1 = self.Exp1.analizar(TS, Errores)
        tipo2 = self.Exp2.analizar(TS, Errores)

        if (
                tipo1 == TIPO_DATOS.STRING or tipo1 == TIPO_DATOS.INT or tipo1 == TIPO_DATOS.CHAR or tipo1 == TIPO_DATOS.FLOAT or tipo1 == TIPO_DATOS.DOUBLE) and (
                tipo2 == TIPO_DATOS.STRING or tipo2 == TIPO_DATOS.INT or tipo2 == TIPO_DATOS.CHAR or tipo2 == TIPO_DATOS.FLOAT or tipo2 == TIPO_DATOS.DOUBLE):
            return TIPO_DATOS.INT
        else:
            Errores.insertar(
                Nodo_Error("Semantico", "No es posible operacion entre " + str(tipo1) + ' ' + self.op
                           + ' ' + str(tipo2), self.fila, self.columna))
            return TIPO_DATOS.ERROR

    def getC3D(self, TS):
        codigo = ""
        codigo += self.Exp1.getC3D(TS)
        codigo += self.Exp2.getC3D(TS)
        temp = TS.getTemp()
        self.temporal = temp
        codigo += TS.make3d(temp, self.Exp1.temporal, self.op, self.Exp2.temporal)
        return codigo

    def graficarasc(self, padre, grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Exp'))
        grafica.edge(padre, nombrehijo)
        if self.Exp1 is not None:
            self.Exp1.graficarasc(nombrehijo, grafica)
        grafica.node('NodeE1' + str(id(self)), label=(str(self.op)))
        grafica.edge(nombrehijo, 'NodeE1' + str(id(self)))
        if self.Exp2 is not None:
            self.Exp2.graficarasc(nombrehijo, grafica)


class primitivo(Node.Nodo):
    def __init__(self, Valor, fila, col, tipo):
        self.fila = fila
        self.columna = col
        self.valor = Valor
        self.temporal = ""
        if tipo == "decimal":
            self.tipo = TIPO_DATOS.FLOAT
        elif tipo == "entero":
            self.tipo = TIPO_DATOS.INT
        elif tipo == "char":
            self.tipo = TIPO_DATOS.CHAR
        elif tipo == "string":
            self.tipo = TIPO_DATOS.STRING

    def analizar(self, TS, Errores):
        return self.tipo

    def getC3D(self, TS):
        if self.tipo == TIPO_DATOS.CHAR:
            self.temporal = '\'' + str(self.valor) + '\''
        elif self.tipo == TIPO_DATOS.STRING:
            self.temporal = '\"' + str(self.valor) + '\"'
        else:
            self.temporal = str(self.valor)
        return ""

    def graficarasc(self, padre, grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Exp'))
        grafica.edge(padre, nombrehijo)
        grafica.node('NodeV' + str(id(self)), label=(str(self.valor)))
        grafica.edge(nombrehijo, 'NodeV' + str(id(self)))


class variable(Node.Nodo):
    def __init__(self, nombre, fila, col):
        self.fila = fila
        self.columna = col
        self.nombre = nombre
        self.temporal = ""

    def analizar(self, TS, Errores):
        simbolo = TS.obtener(self.nombre)
        if simbolo is None:
            Errores.insertar(
                Nodo_Error("Semantico", "No existe variable " + self.nombre, self.fila, self.columna))
            return TIPO_DATOS.ERROR
        return simbolo.tipo

    def getC3D(self, TS):
        codigo = ""
        simbolo = TS.obtener(self.nombre)
        self.temporal = simbolo.posicion
        return codigo

    def graficarasc(self, padre, grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Exp'))
        grafica.edge(padre, nombrehijo)
        grafica.node('NodeI' + str(id(self)), label=(str(self.nombre)))
        grafica.edge(nombrehijo, 'NodeI' + str(id(self)))


class bitabit(Node.Nodo):
    def __init__(self, Exp1, Exp2, op, fila, col):
        self.fila = fila
        self.columna = col
        self.Exp1 = Exp1
        self.Exp2 = Exp2
        self.op = op
        self.temporal = ""

    def analizar(self, TS, Errores):
        tipo1 = self.Exp1.analizar(TS, Errores)
        tipo2 = self.Exp2.analizar(TS, Errores)

        if (
                tipo1 == TIPO_DATOS.INT or tipo1 == TIPO_DATOS.CHAR) and (
                tipo2 == TIPO_DATOS.INT or tipo2 == TIPO_DATOS.CHAR):
            return TIPO_DATOS.INT
        else:
            Errores.insertar(
                Nodo_Error("Semantico", "No es posible operacion entre " + str(tipo1.nombre) + ' ' + self.op
                           + ' ' + str(tipo2.nombre), self.fila, self.columna))
            return TIPO_DATOS.ERROR

    def getC3D(self, TS):
        codigo = ""
        codigo += self.Exp1.getC3D(TS)
        codigo += self.Exp2.getC3D(TS)
        temp = TS.getTemp()
        self.temporal = temp
        codigo += TS.make3d(temp, self.Exp1.temporal, self.op, self.Exp2.temporal)
        return codigo

    def graficarasc(self, padre, grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Exp'))
        grafica.edge(padre, nombrehijo)
        if self.Exp1 is not None:
            self.Exp1.graficarasc(nombrehijo, grafica)
        grafica.node('NodeE1' + str(id(self)), label=(str(self.op)))
        grafica.edge(nombrehijo, 'NodeE1' + str(id(self)))
        if self.Exp2 is not None:
            self.Exp2.graficarasc(nombrehijo, grafica)


class logica(Node.Nodo):
    def __init__(self, Exp1, Exp2, op, fila, col):
        self.fila = fila
        self.columna = col
        self.Exp1 = Exp1
        self.Exp2 = Exp2
        self.op = op

    def analizar(self, TS, Errores):
        tipo1 = self.Exp1.analizar(TS, Errores)
        tipo2 = self.Exp2.analizar(TS, Errores)

        if (
                tipo1 == TIPO_DATOS.INT or tipo1 == TIPO_DATOS.CHAR or tipo1 == TIPO_DATOS.FLOAT or tipo1 == TIPO_DATOS.DOUBLE) and (
                tipo2 == TIPO_DATOS.INT or tipo2 == TIPO_DATOS.CHAR or tipo2 == TIPO_DATOS.FLOAT or tipo2 == TIPO_DATOS.DOUBLE):
            return TIPO_DATOS.INT
        else:
            Errores.insertar(
                Nodo_Error("Semantico", "No es posible operacion entre " + str(tipo1.nombre) + ' ' + self.op
                           + ' ' + str(tipo2.nombre), self.fila, self.columna))
            return TIPO_DATOS.ERROR

    def getC3D(self, TS):
        codigo = ""
        codigo += self.Exp1.getC3D(TS)
        codigo += self.Exp2.getC3D(TS)
        temp = TS.getTemp()
        self.temporal = temp
        codigo += TS.make3d(temp, self.Exp1.temporal, self.op, self.Exp2.temporal)
        return codigo

    def graficarasc(self, padre, grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Exp'))
        grafica.edge(padre, nombrehijo)
        if self.Exp1 is not None:
            self.Exp1.graficarasc(nombrehijo, grafica)
        grafica.node('NodeE1' + str(id(self)), label=(str(self.op)))
        grafica.edge(nombrehijo, 'NodeE1' + str(id(self)))
        if self.Exp2 is not None:
            self.Exp2.graficarasc(nombrehijo, grafica)


class incremento(Node.Nodo):
    def __init__(self, Exp1, op, primero, fila, col):
        self.fila = fila
        self.columna = col
        self.Exp1 = Exp1
        self.primero = primero
        self.op = op

    def analizar(self, TS, Errores):
        tipo = self.Exp1.analizar(TS, Errores)
        if tipo == TIPO_DATOS.INT or tipo == TIPO_DATOS.CHAR or tipo == TIPO_DATOS.FLOAT or tipo == TIPO_DATOS.DOUBLE:
            return tipo
        else:
            Errores.insertar(
                Nodo_Error("Semantico", "No es posible incremento/decremento", self.fila, self.columna))
            return TIPO_DATOS.ERROR

    def getC3D(self, TS):
        codigo = ""
        if self.op == '++':
            operador = '+'
        else:
            operador = '-'
        if self.primero:
            codigo += self.Exp1.getC3D(TS)
            temporal = self.Exp1.temporal
            codigo += TS.make3d(temporal, temporal, operador, 1)
            self.temporal = temporal
            return codigo
        else:
            codigo += self.Exp1.getC3D(TS)
            temporal = self.Exp1.temporal
            temporal2 = TS.getTemp()
            codigo += temporal2 + '=' + temporal + ';\n'
            codigo += TS.make3d(temporal, temporal, operador, 1)
            self.temporal = temporal2

            return codigo

    def graficarasc(self, padre, grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Exp'))
        grafica.edge(padre, nombrehijo)
        if self.primero:
            grafica.node('NodeE1' + str(id(self)), label=(str(self.op)))
            grafica.edge(nombrehijo, 'NodeE1' + str(id(self)))
            self.Exp1.graficarasc(nombrehijo, grafica)
        else:
            self.Exp1.graficarasc(nombrehijo, grafica)
            grafica.node('NodeE1' + str(id(self)), label=(str(self.op)))
            grafica.edge(nombrehijo, 'NodeE1' + str(id(self)))


class unario(Node.Nodo):
    def __init__(self, Exp, op, fila, col):
        self.fila = fila
        self.columna = col
        self.Exp = Exp
        self.op = op

    def analizar(self, TS, Errores):
        tipo = self.Exp.analizar(TS, Errores)
        if self.op == '~':
            if tipo == TIPO_DATOS.INT or tipo == TIPO_DATOS.CHAR:
                return TIPO_DATOS.INT
            else:
                Errores.insertar(
                    Nodo_Error("Semantico", "No es posible operador unario " + self.op + ' con tipo de dato ' +
                               str(tipo.nombre), self.fila, self.columna))
                return TIPO_DATOS.ERROR
        else:
            if tipo == TIPO_DATOS.INT or tipo == TIPO_DATOS.CHAR or tipo == TIPO_DATOS.DOUBLE or tipo == TIPO_DATOS.FLOAT:
                return TIPO_DATOS.INT
            else:
                Errores.insertar(
                    Nodo_Error("Semantico", "No es posible operador unario " + self.op + ' con tipo de dato ' +
                               str(tipo.nombre), self.fila, self.columna))
                return TIPO_DATOS.ERROR

    def getC3D(self, TS):
        codigo = ""
        codigo += self.Exp.getC3D(TS)
        temp = TS.getTemp()
        self.temporal = temp
        codigo += self.temporal + ' = ' + str(self.op) + ' ' + self.Exp.temporal + '; \n'
        return codigo

    def graficarasc(self, padre, grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Exp'))
        grafica.edge(padre, nombrehijo)
        grafica.node('NodeE1' + str(id(self)), label=(str(self.op)))
        grafica.edge(nombrehijo, 'NodeE1' + str(id(self)))
        if self.Exp is not None:
            self.Exp.graficarasc(nombrehijo, grafica)


class ternario(Node.Nodo):
    def __init__(self, Cond, Exp1, Exp2, fila, col):
        self.fila = fila
        self.columna = col
        self.Cond = Cond
        self.Exp1 = Exp1
        self.Exp2 = Exp2

    def analizar(self, TS, Errores):
        tipo = self.analizar(TS, Errores)
        if not (
                tipo == TIPO_DATOS.INT or tipo == TIPO_DATOS.CHAR or tipo == TIPO_DATOS.DOUBLE or tipo == TIPO_DATOS.FLOAT):
            Errores.insertar(
                Nodo_Error("Semantico", "La el tipo de condicion no es valido en ternario ", self.fila, self.columna))
            return TIPO_DATOS.ERROR
        tipo2 = self.Exp1.analizar(TS, Errores)
        tipo3 = self.Exp2.analizar(TS, Errores)
        if tipo == TIPO_DATOS.ERROR or tipo2 == TIPO_DATOS.ERROR or tipo3 == TIPO_DATOS.ERROR:
            return TIPO_DATOS.ERROR

    def getC3D(self, TS):
        codigo = ""
        V = TS.getEtq()
        F = TS.getEtq()
        S = TS.getEtq()
        self.temporal = TS.getTemp()
        codigo += self.Cond.getC3D(TS)
        codigo += 'if (' + str(self.Cond.temporal) + ') goto ' + V + ';\n'
        codigo += 'goto ' + F + ';\n'
        codigo += V + ':\n'
        codigo += self.Exp1.getC3D(TS)
        codigo += self.temporal + '=' + str(self.Exp1.temporal) + ';\n'
        codigo += 'goto ' + S + ';\n'
        codigo += F + ':\n'
        codigo += self.Exp1.getC3D(TS)
        codigo += self.temporal + '=' + str(self.Exp1.temporal) + ';\n'
        codigo += 'goto ' + S + ';\n'
        codigo += S + ':\n'
        return codigo

    def graficarasc(self, padre, grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Exp'))
        self.Cond.graficarasc(nombrehijo, grafica)
        grafica.node('NodeE1' + str(id(self)), label="?")
        grafica.edge(nombrehijo, 'NodeE1' + str(id(self)))
        self.Exp1.graficarasc(nombrehijo, grafica)
        grafica.node('NodeE2' + str(id(self)), label=":")
        grafica.edge(nombrehijo, 'NodeE2' + str(id(self)))
        self.Exp2.graficarasc(nombrehijo, grafica)


class casteo(Node.Nodo):
    def __init__(self, Cast, Exp, fila, col):
        self.fila = fila
        self.columna = col
        self.Exp = Exp
        self.cast = Cast

    def analizar(self, TS, Errores):
        self.Exp.analizar(TS, Errores)
        if self.cast == "char":
            self.tipo = TIPO_DATOS.CHAR
        elif self.cast == "int":
            self.tipo = TIPO_DATOS.INT
        elif self.cast == "float":
            self.tipo = TIPO_DATOS.FLOAT

    def getC3D(self, TS):
        codigo = ""
        codigo += self.Exp.getC3D(TS)
        temp = TS.getTemp()
        codigo += temp + '= (' + self.cast + ')' + self.Exp.temporal + ';\n'
        self.temporal = temp

        return codigo;

    def graficarasc(self, padre, grafica):
        pass


class sizeof(Node.Nodo):
    def __init__(self, Exp, fila, col):
        self.fila = fila
        self.columna = col
        self.Exp = Exp

    def analizar(self, TS, Errores):
        return

    def getC3D(self, TS):
        self.temporal = "3"
        return ""

    def graficarasc(self, padre, grafica):
        return
