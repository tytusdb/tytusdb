from team29.analizer import grammar as g
import ply
from team29.analizer import variables


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
    variables.bnfgrammar = cad