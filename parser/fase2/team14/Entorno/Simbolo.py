from Entorno.TipoSimbolo import TipoSimbolo


class Simbolo:
    def __init__(self, tipo="", nombre="", valor=None, linea=0):
        self.tipo = tipo
        self.nombre = nombre
        self.valor = valor
        self.linea = linea
        self.atributos = {}
        self.baseDatos = ""
        self.tabla = ""
        self.indexId = ""

    def toString(self):
        cadena: str = ""
        # nombre,tipoSym,baseDatos,tabla,valor
        if self.nombre != None:
            if self.tipo == TipoSimbolo.TABLA:
                columnas: Simbolo = []
                columnas = self.valor
                cadena += "<TR><TD rowspan='" + str(len(columnas)) + "'>" + self.nombre.split('_')[
                    0] + "</TD><TD rowspan='" + str(len(columnas)) + "'>TABLA</TD><TD rowspan='" + str(
                    len(columnas)) + "'>" + self.baseDatos + "</TD><TD rowspan='" + str(len(columnas)) + "'>"
                cadena += self.tabla + "</TD><TD>" + columnas[0].nombre + ":" + columnas[0].tipo.tipo + "</TD></TR>\n"
                for col in range(1, len(columnas), 1):
                    cadena += "<TR><TD>" + columnas[col].nombre + ":" + columnas[col].tipo.tipo + "</TD></TR>\n"

            elif self.tipo == TipoSimbolo.CONSTRAINT_UNIQUE:
                cadena += "<TR><TD>" + self.nombre + "</TD><TD>UNIQUE</TD><TD>" + self.baseDatos + "</TD><TD>"
                cadena += self.tabla + "</TD><TD>" + self.valor + "</TD></TR>\n\n"

            elif self.tipo == TipoSimbolo.CONSTRAINT_CHECK:
                cond: str = self.valor.simbolo
                if cond in ">":
                    cond = cond.replace(">", "&#62;")
                if cond in "<":
                    cond = cond.replace("<", "&#60;")
                if cond in "<=":
                    cond = cond.replace("<=", "&#60;&#61;")
                if cond in ">=":
                    cond = cond.replace(">=", "&#62;&#61;")
                if cond in "<>":
                    cond = cond.replace(">=", "&#60;&#62;")

                cadena += "<TR><TD>" + self.nombre + "</TD><TD>CONSTRAINT CHECK</TD><TD>" + self.baseDatos + "</TD><TD>"
                cadena += self.tabla + "</TD><TD>" + str(self.valor.exp1.valor) + " " + cond + " " + str(
                    self.valor.exp2.valor) + "</TD></TR>\\n"
            elif self.tipo == TipoSimbolo.CONSTRAINT_FOREIGN:
                cadena += "<TR><TD>" + self.nombre + "</TD><TD>CONSTRAINT FORANEA</TD><TD>" + self.baseDatos + "</TD><TD>"
                cadena += self.tabla + "</TD><TD></TD></TR>"
            elif self.tipo == TipoSimbolo.CONSTRAINT_PRIMARY:
                cadena += "<TR><TD>" + self.nombre + "</TD><TD>CONSTRAINT PRIMARIA</TD><TD>" + self.baseDatos + "</TD><TD>"
                cadena += self.tabla + "</TD><TD>" + str(self.valor) + "</TD></TR>"
            elif self.tipo == TipoSimbolo.TYPE_ENUM:
                columnas: Simbolo = []
                columnas = self.valor
                cadena += "<TR><TD rowspan='" + str(len(columnas)) + "'>" + self.nombre.split('_')[
                    2] + "</TD><TD rowspan='" + str(len(columnas)) + "'>ENUM</TD><TD rowspan='" + str(
                    len(columnas)) + "'>" + self.baseDatos + "</TD><TD rowspan='" + str(len(columnas)) + "'>"
                cadena += self.tabla + "</TD><TD>" + columnas[0].valor + "</TD></TR>\n"
                for col in range(1, len(columnas), 1):
                    cadena += "<TR><TD>" + columnas[col].valor + "</TD></TR>\n"

            elif self.tipo == TipoSimbolo.INDEX:
                un = self.valor.get('unique')
                orden = self.valor.get('orden')
                hsh = self.valor.get('hash')
                tam: int = 1
                aux: str = ""
                if un != None:
                    tam += 1
                    aux += "<TR><TD>unique</TD></TR>\n"

                if orden != None:
                    tam += 1
                    aux += "<TR><TD>orden: " + orden + "</TD></TR>\n"

                if hsh != None:
                    tam += 1
                    aux += "<TR><TD>using hash</TD></TR>\n"

                cadena += "<TR><TD rowspan='" + str(tam) + "'>" + self.valor['id'] + "</TD><TD rowspan='" + str(
                    tam) + "'>INDEX</TD><TD rowspan='" + str(tam) + "'>" + self.baseDatos + "</TD><TD rowspan='" + str(
                    tam) + "'>"
                cadena += self.tabla + "</TD><TD> columna : " + self.valor['columna'] + "</TD></TR>\n"
                cadena += aux
            elif self.nombre[:2] == "_f":
                parametros = self.valor[0]
                if parametros!=None:
                    tamano = len(parametros)
                    cadena += "<TR><TD rowspan='" + str(tamano) + "'>" + self.nombre[2:] + "</TD><TD rowspan='" + str(tamano) + "'>FUNCION : " + str(self.tipo.tipo) + "</TD><TD rowspan='" + str(tamano) + "'></TD><TD rowspan='" + str(tamano) + "'>"
                    cadena += "</TD><TD>" + str(parametros[0].nombre) + ":" + str(parametros[0].tipo.tipo) + "</TD></TR>\n"
                    for x in range(1,len(parametros),1):
                        cadena += "<TR><TD>" + str(parametros[x].nombre) + ":" + str(parametros[x].tipo.tipo) + "</TD></TR>\n"
                else:
                    cadena += "<TR><TD>" + self.nombre[2:] + "</TD><TD>FUNCION : " + str(self.tipo.tipo) + "</TD><TD></TD><TD>"
                    cadena += "</TD><TD></TD></TR>\n"

        return cadena

    def proc(self):
        cadena: str = ""
        if self.nombre != None:
            if self.nombre[:2] == "_P":
                parametros = self.valor[0]
                if parametros!=None:
                    tamano = len(parametros)
                    cadena += "<TR><TD rowspan='" + str(tamano) + "'>" + self.nombre[2:] + "</TD><TD rowspan='" + str(tamano) + "'>PROCEDURE</TD><TD rowspan='" + str(tamano) + "'></TD><TD rowspan='" + str(tamano) + "'>"
                    cadena += "</TD><TD>" + str(parametros[0].nombre) + ":" + str(parametros[0].tipo.tipo) + "</TD></TR>\n"
                    for x in range(1,len(parametros),1):
                        cadena += "<TR><TD>" + str(parametros[x].nombre) + ":" + str(parametros[x].tipo.tipo) + "</TD></TR>\n"
                else:
                    cadena += "<TR><TD>" + self.nombre[2:] + "</TD><TD>PROCEDURE</TD><TD></TD><TD>"
                    cadena += "</TD><TD></TD></TR>\n"
        return cadena