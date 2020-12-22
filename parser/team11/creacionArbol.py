from Ast import Nodo

# Función que crea el Nodo para la producción Alter Table
def getAlterTableNode(t):
    childs = []
    g = '<alter_instr> ::= ALTER TABLE ID '
    if len(t) == 5:
        g += '<list_alter_column>\n'
        childs.append(Nodo('Operacion','ALTER COLUMN',t[4],t.lexer.lineno,0,g))
    elif len(t) == 7:
        g += str(t[4])+' COLUMN <listtablas>\n'
        childs.append(Nodo('Operacion',t[4]+' '+t[5],t[6],t.lexer.lineno,0,g))
    elif len(t) == 9:
        if str(t[4]).upper() == 'RENAME':
            g += '\"RENAME\" COLUMN ID TO ID\n'
            n1 = Nodo('ID',t[6],[],t.lexer.lineno)
            n2 = Nodo('ID',t[8],[],t.lexer.lineno)
            childs.append(Nodo('Operacion',t[4]+' '+t[5],[n1,n2],t.lexer.lineno,0,g))
        else:
            g += '\"ADD\" \"CHECK\" \"PARIZQ\" <condicion> \"PARDER\"\n'  
            childs.append(Nodo('Operacion',t[4]+' '+t[5],[t[7]],t.lexer.lineno,0,g))
    elif len(t) == 11:
        g += '\"ADD\" \"CONSTRAINT\" ID \"UNIQUE\" \"PARIZQ\" ID \"PARDER\"\n'
        n1 = Nodo('ID',t[6],[],t.lexer.lineno)
        n2 = Nodo('ID',t[9],[],t.lexer.lineno)
        childs.append(Nodo('Operacion',t[4]+' '+t[5],[n1,n2],t.lexer.lineno,0,g))
    elif len(t) == 12:
        g += '\"ADD\" \"FOREIGN\" \"KEY\" \"PARIZQ\" ID \"PARDER\" \"REFERENCES\" ID\n'
        n1 = Nodo('Columna',t[8],[],t.lexer.lineno)
        n2 = Nodo('Referencia',t[11],[],t.lexer.lineno)
        childs.append(Nodo('Operacion',t[4]+' '+t[5]+' '+t[6],[n1,n2],t.lexer.lineno,0,g))
    elif len(t) == 10:
        g += '\"ALTER\" \"COLUMN\" ID \"SET\" \"NOT\" \"NULL\"\n'
        n = Nodo('Columna',t[6],[],t.lexer.lineno)
        childs.append(Nodo('Operacion',t[7]+' '+t[8]+' '+t[9],[n],t.lexer.lineno,0,g))
    else:
        childs.append(Nodo('Error','getAlterTable',[],t.lexer.lineno)) 
    return  Nodo('ALTER TABLE',t[3],childs,t.lexer.lineno)

# Función para crear el Nodo del tipo de la Columna
def getColumnTypeNode(t):
    if len(t) == 2:
        return Nodo('Tipo', t[1], [], t.lexer.lineno)
    elif len(t) == 3:
        return Nodo('Tipo', t[1], [t[2]], t.lexer.lineno)
    elif len(t) == 5:
        n = Nodo('Limite',str(t[3]),[],t.lexer.lineno)
        return Nodo('Tipo', t[1], [n], t.lexer.lineno)
    elif len(t) == 6:
        n = Nodo('Limite',str(t[4]),[],t.lexer.lineno)
        return Nodo('Tipo', t[1]+' '+t[2], [n], t.lexer.lineno)
    elif len(t) == 7:
        n1 = Nodo('Digitos',str(t[3]),[],t.lexer.lineno)
        n2 = Nodo('Cifras',str(t[5]),[],t.lexer.lineno)
        return Nodo('Tipo',t[1],[n1,n2],t.lexer.lineno)
    else:
        return Nodo('Error','getColumType',[],t.lexer.lineno)
