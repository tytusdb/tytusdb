# Gramatica Generada Automaticamente
La gramatica que se genero en el analisis realizado es la siguiente:
******************************************************************
<init> ::= <instrucciones>
<instrucciones> ::= <instruccion>
<instruccion> ::= <select> PTCOMA
<select> ::= SELECT <parametrosselect> <fromopcional>
<parametrosselect> ::= <listadeseleccion>
<listadeseleccion> ::= <listadeseleccionados> <asopcional>
<listadeseleccionados> ::= ASTERISCTO
<asopcional> ::= EPSILON
<fromopcional> ::= FROM <parametrosfrom> <whereopcional>
<parametrosfrom> ::= <parametrosfromr> <asopcional>
<parametrosfromr> ::= TBROL
<asopcional> ::= EPSILON
<whereopcional> ::= EPSILON

******************************************************************