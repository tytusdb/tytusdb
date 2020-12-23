from graphviz import Graph
class Gramatical:
    def __init__(self):
        self.gramatica = {}
        self.terminal = []
        self.no_terminal = []
        self.id = []

    def agregarGramatical(self,gramatica,reg_gramatical,terminal,no_terminal,id):
        if id in self.gramatica:
            aux_gramatica = self.gramatica[id][0]
            aux_regla = self.gramatica[id][1]
            if gramatica.find("::=") >= 0:
                id_reemplazar = '<' + id + '>'
                aux_parametro = gramatica.replace("::=",'|').replace(id_reemplazar,'',1)
                if gramatica not in aux_gramatica and reg_gramatical not in aux_regla:
                    self.gramatica[id] = [aux_gramatica + '\n' + aux_parametro, aux_regla + reg_gramatical]
            else:
                if gramatica not in aux_gramatica and reg_gramatical not in aux_regla:
                    self.gramatica[id] = [aux_gramatica + '\n' + gramatica, aux_regla + reg_gramatical]
        else:
            if gramatica.find("::=") >= 0:
                self.gramatica[id] = [gramatica,reg_gramatical]
            else:
                if gramatica.find('|') >= 0:
                    self.gramatica[id] = ['<' + id + '>' + gramatica.replace('|',"::=",1),reg_gramatical]

        for term in terminal:
            if term not in self.terminal:
                self.terminal.append(term)

        for no_term in no_terminal:
            if no_term not in self.no_terminal:
                self.no_terminal.append(no_term)

        if id not in self.id:
            self.id.append(id)

    def obtenerGramatical(self):
        dot = Graph()
        dot.attr(pad = '0.5', nodesep = '0.5', ranksep = '2')
        dot.node_attr.update(shape = 'plain', rankdir = 'TB')
        tb_precedence ="<<table border = '0' cellborder = '1' cellspacing = '0' ALIGN = 'LEFT'>\n"
        tb_precedence += "<tr><td bgcolor='/rdylgn11/6:/rdylgn11/9'><i>Precedencia</i></td></tr>\n"
        tb_terminales = "<<table border = '0' cellborder = '1' cellspacing = '0' ALIGN = 'LEFT'>\n"
        tb_terminales += "<tr><td bgcolor='/rdylgn11/6:/rdylgn11/9'><i>Terminal</i></td></tr>\n"
        tb_no_terminales = "<<table border = '0' cellborder = '1' cellspacing = '0' ALIGN = 'LEFT'>\n"
        tb_no_terminales += "<tr><td bgcolor='/rdylgn11/6:/rdylgn11/9'><i>No Terminal</i></td></tr>\n"
        tb_semantica = "<<table border = '0' cellborder = '1' cellspacing = '0' ALIGN = 'LEFT'>\n"
        tb_semantica += "<tr><td bgcolor='/rdylgn11/6:/rdylgn11/9'><i>Produccion</i></td><td bgcolor='/rdylgn11/6:/rdylgn11/9'><i>Regla Semantica</i></td></tr>\n"
        
        tb_precedence += "<tr><td>(left : CONCAT), (left : MENOR,MAYOR,IGUAL,MENORIGUAL,MAYORIGUAL,DIFERENTE), (left : MAS,MENOS),"
        tb_precedence += "(left : POR,DIVISION,MODULO),\n(left : EXP)</td></tr>"

        for term in self.terminal:
            tb_terminales += "<tr><td>" + term + "</td></tr>\n"

        for index in self.no_terminal:
            aux = index.replace('<','(').replace('>',')') or index
            tb_no_terminales += "<tr><td>" + aux + "</td></tr>\n"

        for id in self.id:
            if id in self.gramatica:
                prod = self.gramatica[id][0].replace('<','(').replace('>',')') or self.gramatica[id][0]
                regla = self.gramatica[id][1].replace('<','(').replace('>',')') or self.gramatica[id][1]
                tb_semantica += "<tr><td>" + prod + "</td><td>" + regla + "</td></tr>\n"

        tb_precedence += "</table>>\n"
        tb_terminales += "</table>>\n"
        tb_no_terminales += "</table>>\n"
        tb_semantica += "</table>>\n"
        dot.node("Prece",tb_precedence)
        dot.node("Term",tb_terminales)
        dot.node("NoTerm",tb_no_terminales)
        dot.node("Grama",tb_semantica)
        dot.view("gramatical")