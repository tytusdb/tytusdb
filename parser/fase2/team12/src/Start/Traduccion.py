
import sys, os.path
import json
where_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\Where')
sys.path.append(where_path)
from Where import Where
def traduccionSelect(nodoRaiz):

    stringRetornar = "Select "
    cantidadHijos = len(nodoRaiz.hijos)

    if cantidadHijos == 1 :

        expresionTraducir = nodoRaiz.hijos[0]
        
        cantidadHijos = len(expresionTraducir.hijos)
        contador = 1

        for hijo in expresionTraducir.hijos:

            if contador == 1 :
                stringRetornar += ""
            else:
                stringRetornar += ", "
                
            stringRetornar += hijo.getText()
            contador = contador + 1

    elif cantidadHijos == 2:

        expresionTraducir = nodoRaiz.hijos[0]
        tablasTraducir = nodoRaiz.hijos[1]

        if expresionTraducir.nombreNodo == "*":

            stringRetornar += "* "

        else :

            cantidadHijos = len(expresionTraducir.hijos)
            contador = 1

            for hijo in expresionTraducir.hijos:

                if contador == 1 :
                    stringRetornar += ""
                else:
                    stringRetornar += ", "
                
                stringRetornar += hijo.getText()
                contador = contador + 1

        
        stringRetornar += "from "
        cantidadHijos = len(tablasTraducir.hijos)
        contador = 1

        for hijo in tablasTraducir.hijos:

            if contador == 1 :
                stringRetornar += ""
            else:
                stringRetornar += ", "

            if hijo.nombreNodo == 'Identificador':
                stringRetornar += hijo.valor
            
            contador =  contador + 1


    elif cantidadHijos == 3:    
        expresionTraducir = nodoRaiz.hijos[0]
        tablasTraducir = nodoRaiz.hijos[1]
        tercerNodo = nodoRaiz.hijos[2]
        expresionTraducir = nodoRaiz.hijos[0]
        tablasTraducir = nodoRaiz.hijos[1]

        if expresionTraducir.nombreNodo == "*":

            stringRetornar += "* "

        else :

            cantidadHijos = len(expresionTraducir.hijos)
            contador = 1

            for hijo in expresionTraducir.hijos:

                if contador == 1 :
                    stringRetornar += ""
                else:
                    stringRetornar += ", "
                
                stringRetornar += hijo.getText()
                contador = contador + 1

        
        stringRetornar += "from "
        cantidadHijos = len(tablasTraducir.hijos)
        contador = 1

        for hijo in tablasTraducir.hijos:

            if contador == 1 :
                stringRetornar += ""
            else:
                stringRetornar += ", "

            if hijo.nombreNodo == 'Identificador':
                stringRetornar += hijo.valor
            
            contador =  contador + 1
        nuevoWhere = Where()
        print(nuevoWhere.compile(tercerNodo))
        stringRetornar+=nuevoWhere.compile(tercerNodo)
    
    stringRetornar += ";"
    return stringRetornar


def traduccion_unique_index(nodoRaiz):
    id1 = nodoRaiz.hijos[0].valor
    id2 = nodoRaiz.hijos[1].valor

    #Resolver sentences
    if nodoRaiz.hijos[2].nombreNodo == "INDEX_NORMAL":
        sentences = resolver_index_normal(nodoRaiz.hijos[2].hijos)
    elif nodoRaiz.hijos[2].nombreNodo == "INDEX_USING":
        sentences = resolver_index_using(nodoRaiz.hijos[2])

    if len(nodoRaiz.hijos)  == 4:
        opc_where = ' WHERE ' + nodoRaiz.hijos[3].getText()
    else:
        opc_where = ''
    return f'CREATE UNIQUE INDEX {id1} ON {id2} {sentences} {opc_where} ;'


def resolver_index_using(nodo):
    metodo = nodo.hijos[0].hijos[0].nombreNodo
    lista = []
    for i in range(1,len(nodo.hijos)):
        lista.append(nodo.hijos[i])
    sentencia = resolver_index_normal(lista)
    return f'USING {metodo} {sentencia}'

def resolver_index_normal(lista):
    string_ = ''
    contador = 0
    for hijo in lista:
        if contador >= len(lista) - 1:
            coma = ''
        else:
            coma = ', '
        contador += 1

        string_ += hijo.hijos[0].valor +' '
        cantidad_ = len(hijo.hijos)
        if cantidad_ < 2:
            string_ += coma
        elif cantidad_ == 2:
            if hijo.hijos[1].nombreNodo == "OPC_ORDER":
                string_ += hijo.hijos[1].hijos[0].valor + coma
            else:
                string_ += f' NULLS {hijo.hijos[1].hijos[0].nombreNodo}' + coma
        elif cantidad_ == 3:
            if hijo.hijos[1].nombreNodo == "OPC_ORDER":
                string_ += hijo.hijos[1].hijos[0].valor
                string_ += f' NULLS {hijo.hijos[2].hijos[0].nombreNodo}' + coma
            else:
                string_ += f' NULLS {hijo.hijos[1].hijos[0].nombreNodo}'
                string_ += hijo.hijos[2].hijos[0].valor + coma
    return '('+string_+')'


def traduccion_index(nodoRaiz):
    if nodoRaiz.hijos[0].valor == nodoRaiz.hijos[1].valor:
        id1 = nodoRaiz.hijos[0].valor
        if nodoRaiz.hijos[2].nombreNodo == "INDEX_NORMAL":
            sentences = resolver_index_normal(nodoRaiz.hijos[2].hijos)
        elif nodoRaiz.hijos[2].nombreNodo == "INDEX_USING":
            sentences = resolver_index_using(nodoRaiz.hijos[2])
        if len(nodoRaiz.hijos)  == 4:
            opc_where = ' WHERE ' + nodoRaiz.hijos[3].getText()            
        return f'CREATE INDEX ON {id1} {sentences} {opc_where};'
    else:
        id1 = nodoRaiz.hijos[0].valor
        id2 = nodoRaiz.hijos[1].valor
        if nodoRaiz.hijos[2].nombreNodo == "INDEX_NORMAL":
            sentences = resolver_index_normal(nodoRaiz.hijos[2].hijos)
        elif nodoRaiz.hijos[2].nombreNodo == "INDEX_USING":
            sentences = resolver_index_using(nodoRaiz.hijos[2])
        if len(nodoRaiz.hijos)  == 4:
            opc_where = ' WHERE ' + nodoRaiz.hijos[3].getText()          
        return f'CREATE INDEX {id1} ON {id2} {sentences} {opc_where};'




def traduccion_create_table(nodoRaiz):
    identificador = nodoRaiz.hijos[0].valor
    cuerpo = ''
    count = 0
    for hijo in nodoRaiz.hijos:
        coma = ','
        if count == len(nodoRaiz.hijos) - 1:
            coma = ''
        count += 1

        if hijo.nombreNodo == "ATRIBUTO_COLUMNA":
            cuerpo += traduccion_atributo_columna(hijo) + coma
        elif hijo.nombreNodo == "OPCIONALES_ATRIBUTO_CHECK":
            cuerpo += traduccion_atributo_check(hijo) + coma
        elif hijo.nombreNodo == "ATRIBUTO_UNIQUE":
            cuerpo += traduccion_atributo_unique(hijo) + coma
        elif hijo.nombreNodo == "ATRIBUTO_PRIMARY_KEY":
            cuerpo += traduccion_atributo_pk(hijo) + coma
        elif hijo.nombreNodo == "ATRIBUTO_REFERENCES":
            cuerpo += traduccion_atributo_references(hijo) + coma
                                                           
    string_ = f'CREATE TABLE {identificador} ( {cuerpo} );\n'
    return string_


def sacar_ids(lista):
    lista_ids = ''
    count = 0
    for item in lista:
        coma = ','
        if count == len(lista) - 1:
            coma = ''
        count += 1    
        lista_ids += f'{item.valor}{coma}'
    return lista_ids

def traduccion_atributo_unique(nodoRaiz):
    lista_ids = sacar_ids(nodoRaiz.hijos)
    string_ = f' UNIQUE({lista_ids})'
    return string_

def traduccion_atributo_pk(nodoRaiz):
    lista_ids = sacar_ids(nodoRaiz.hijos)
    string_ = f' PRIMARY KEY({lista_ids})'
    return string_

def traduccion_atributo_references(nodoRaiz):
    foreign = traduccion_atributo_fk(nodoRaiz.hijos[0].hijos[0])
    return f'{foreign} REFERENCES {nodoRaiz.hijos[1].valor} ({sacar_ids(nodoRaiz.hijos[2].hijos)})'

def traduccion_atributo_fk(nodoRaiz):
    lista_ids = sacar_ids(nodoRaiz.hijos)
    string_ = f' FOREIGN KEY({lista_ids})'
    return string_


def traduccion_atributo_check(nodoRaiz):
    string_ = ''
    lista = None
    if len(nodoRaiz.hijos)  > 1: 
        string_ += f' CONSTRAINT {nodoRaiz.hijos[0].hijos[0].valor} CHECK ('
        lista = nodoRaiz.hijos[1].hijos
    else:
        string_ += ' CHECK ('
        lista = nodoRaiz.hijos[1].hijos
    count = 0
    for item in lista:
        coma = ','
        if count == len(lista) - 1:
            coma = ''
        count += 1
        string_ += f'{item.getText()}{coma}'
    string_ += ')'
    
    return string_
    
def traduccion_atributo_columna(nodoRaiz):
    string_ = ''
    nombre_columna = nodoRaiz.hijos[0].valor
    tipo_declaracion = nodoRaiz.hijos[1].hijos[0].nombreNodo
    for hijo in nodoRaiz.hijos:
        if hijo.nombreNodo == "OPCIONALES_ATRIBUTO_REFERENCES":
            string_ += f' REFERENCES {hijo.hijos[0].nombreNodo}'
        if hijo.nombreNodo == "OPCIONALES_ATRIBUTO_DEFAULT":
            string_ += f' DEFAULT {hijo.hijos[1].hijos[0].valor}'
        if hijo.nombreNodo == "OPCIONALES_ATRIBUTO_CHECK":
            if len(hijo.hijos)  > 1:
                string_ += f' CONSTRAINT {hijo.hijos[0].hijos[0].valor} CHECK ({hijo.hijos[2].getText()})'
            else:
                string_ += f' CHECK ({hijo.hijos[0].hijos[0].getText()})'
        if hijo.nombreNodo == "OPCIONALES_ATRIBUTO_NULL":
            string_ += ' NULL'     
        if hijo.nombreNodo == "OPCIONALES_ATRIBUTO_UNIQUE":
            if len(hijo.hijos) > 1:
                string_ += f' CONSTRAINT {hijo.hijos[0].hijos[0].valor} UNIQUE'
            else:
                string_ += ' UNIQUE'
        if hijo.nombreNodo == "OPCIONALES_ATRIBUTO_NOT_NULL":
            string_ += ' NOT NULL'  
        if hijo.nombreNodo == "OPCIONALES_ATRIBUTO_PRIMARY":
            string_ += ' PRIMARY KEY'  


            

    return f' {nombre_columna} {tipo_declaracion} {string_}'

def traduccionCreate_database(nodoRaiz):
    orreplace=False
    ifnotexists = False
    opcionales_crear_database = False
    hijo_posicion = 0
    string_ = "CREATE "
    opcionales_create = ""
    for child in nodoRaiz.hijos:
        if child.nombreNodo == "ORREPLACE":
            orreplace = True
        if child.nombreNodo == "IF_NOT_EXISTS":
            ifnotexists = True
        if child.nombreNodo == "OPCIONALES_CREAR_DATABASE":
            opcionales_crear_database = True
            for hijillo in child.hijos:
                opcionales_create += ' ' + str(hijillo.nombreNodo)
    
    orr = ''
    ifne = ''
    if orreplace:
        orr = 'OR REPLACE '
        hijo_posicion += 1
    if ifnotexists: 
        ifne = 'IF NOT EXISTS '
        hijo_posicion += 1
    if opcionales_crear_database:
        pass
    identificador = nodoRaiz.hijos[hijo_posicion].valor

    string_ += f'{orr} DATABASE {ifne} {identificador} {opcionales_create};'
    return string_
        
def traduccion_unions(text, nodoRaiz):
    try:
        select1 = nodoRaiz.hijos[0].getText()
        select2 = nodoRaiz.hijos[1].getText()
        return f'{select1} {text} {select2};'
    except:
        return ''