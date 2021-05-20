from utilities.analisys_parser.analizer import grammar as g
import ply


def grammarReport():
    rep = g.getRepGrammar()
    cad = ""
    for r1 in rep:
        for r2 in r1:
            if isinstance(r2, ply.lex.LexToken):
                cad += str(r2.type) + " "
            else:
                cad += "<" + str(r2) + "> "
                if r2 == r1[0]:
                    cad += "::= "
        cad += "\n"
    crearArchivo(cad)


def crearArchivo(cad):
    file = open("ReporteGramatica.bnf", "w")
    file.write(cad)
    file.close()
