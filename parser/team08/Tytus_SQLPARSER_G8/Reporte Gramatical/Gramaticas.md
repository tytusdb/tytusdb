# Gramaticas de proyecto Fase 1

Univers'ID'ad de San Carlos de Guatemala  
Facultad de Ingeniería  
Curso: 781 Organización de Lenguajes y Compiladores 2  
Diciembre 2020
Ing. Luis Espino, Aux. Juan Carlos Maeda
Grupo 8

## Índice
- [Gramatica Descendente](#gramatica-descendente) 
- [Gramatica Ascendente](#gramatica-ascendente)

## Gramatica Descendente 

~~~
instrucciones := instrucion { instrucion }
                 
			
instrucion : 'CREATE' 'TABLE' 'ID' '(' campos ')' ';'
			| 'TRUNCATE' 'TABLE' 'ID' ';'
			| 'DROP' 'TABLE' 'ID' ';'
			| 'DROP' 'ID'
			| 'UPDATE' 'ID' 'SET' l_columnas 'WHERE' logicos ';'
			| 'DELETE' 'FROM' 'ID' 'WHERE' logicos ';'
			| 'CREATE' 'FUNCTI'ON'' 'ID' 'BEGIN' instrucciones 'END' ';'
			| 'CREATE' 'FUNCTI'ON'' 'ID' '(' lcol ')' 'BEGIN' instrucciones 'END' ';'
			| 'CREATE' 'FUNCTI'ON'' 'ID' '(' lcol ')' 'AS' expresion 'BEGIN' instrucciones 'END' ';'
			| 'DECLARE' expresion 'AS' expresion ';'
			| 'DECLARE' expresion tipo ';'
			| 'SET' expresion '=' logicos ';'
			| 'ALTER' 'TABLE' 'ID' 'ADD' 'ID' tipo ';'
			| 'ALTER' 'TABLE' 'ID' 'DROP' lcol 'ID' ';'
			| 'INSERT' 'INTO' 'ID' '(' lcol ')' 'VALUES' '(' l_expresiones ')' ';'
			| 'INSERT' 'INTO' 'ID' 'VALUES' '(' l_expresiones ')' ';'
			| 'SELECT' lcol 'FROM' lcol inners ';'
			| 'SELECT' '*' 'FROM' lcol inners ';'
			| 'SELECT' lcol 'FROM' lcol inners 'WHERE' logicos ';'
			| 'SELECT' '*' 'FROM' lcol inners 'WHERE' logicos ';'


l_columnas : logicos ',' { logicos }
			
inners : 'INNER' 'JOIN' logicos 'ON' logicos
        | 'LEFT' 'JOIN' logicos 'ON' logicos
        | 'FULL' 'OUTER' 'JOIN' logicos 'ON' logicos
        | 'JOIN' logicos 'ON' logicos
        | 'RIGTH' 'JOIN' logicos 'ON' logicos
        | 

logicos : lt 'OR' { lt }

lt : lf 'AND' { lf }
	
lf : lfp 'LIKE' {lfp }
	| lfp 'BETWEEN' { lfp }
	| lfp 'IN' { lfp }
	| lfp 'NOT' 'LIKE' { lfp }
	| lfp 'NOT' 'BETWEEN' { lfp }

lfp : relacional
	| 'NOT' logicos 
	| '(' logicos ')'

relacional : rf '=' { rf }
			| rf '>' { rf }
			| rf '<' { rf }
			| rf '>=' { rf }
			| rf '<=' { rf }
			| rf '<>' { rf }

rf : expre
	| '(' logicos ')'
	
expre : t '+' { t }
		| t '-' { t }

t : tp '*' { tp }
	| tp '/' { tp }
	
tp : tpp '%' { tpp }

tpp : expresion 'AS' 'ID'
	| expresion

expresion : 'CADENA'
            | 'CARACTER'
            | 'ENTERO'
            | 'FDECIMAL'
            | 'DOUBLE'
            | 'ID'
            | 'ID' '.' 'ID'
            | '@' 'ID'
            | 'ID' '(' lcol ')'	
			
campos : 'ID' l_campo ',' { 'ID' l_campo }
			
l_campo : tipo {tipo}
			 
l_expresiones : expresion ',' { expresion }
						

lcol : expre ',' { expre }
        

tipo : 'INT'
		| 'DATE'
        | 'NOT'
        | 'NULL'
        | 'PRIMARY' 'KEY'
        | 'FOREIGN' 'KEY' 'REFERENCES'
        | 'ID' '(' 'ID' ')'
		| 'VARCHAR' '(' 'ENTERO' ')'
        | 'CHAR' '(' 'ENTERO' ')'
		| 'DECIMAL' '(' 'ENTERO' ',' 'ENTERO' ')'
        | 'DOUBLE'
        | 'DECIMAL'
        | 'ENTERO'
		| 'SMALLINT'
		| 'BIGINT'
		| 'NUMERIC'
		| 'REAL'
        | 'FLOAT' '(' 'ENTERO' ',' 'ENTERO' ')' 
~~~


## Gramatica Ascendente
