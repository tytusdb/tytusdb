# PROYECTO 

## Gramática descendente

<br>
<br>



**\<S>**            ::=     \<STATEMENTS>

---
**\<STATEMENTS>**       ::=     \<STATEMENT> ’;’ [\<STATEMENTS>]

---
**\<STATEMENT>**    ::=      tCreate [\<REEMPLAZO>] \<OPT_CREATE>

                |    tSelect < PSELECT >
                |    tAlter < PALTER >
                |    tInsert < PINSERT>
                |    tDrop < PDROP >
                |    tShow < PSHOW >        
                |    tUpdate < PUPDATE >
                |    tDelete < PDELETE >
           
<br>           

##   SELECT 
<br>


**\< PSELECT >** ::=      \< PARAMETER >  tfrom  \< FROM_LIST >         

---
**\< PARAMETER >** ::=   '(' \< ID_LIST > ')'

                |  < ID_LIST >
                | [tcount|tdistinct]'(' <ID_NOMBRE> ')' [tas(tnombre|tnumber)]
                | < ASTERISCO_INST >
       
---
**\< ASTERISCO_INST >** ::=  tnombre  tpunto tasterisco [ \< ASTERISCO_INSTPRIM > ]

                | tasterisco

---
**\< ASTERISCO_INSTPRIM >** ::= ','tnombre tpunto tasterisco [\<ASTERISCO_INSTPRIM>]

---
**\< ID_LIST >**  ::=  \< ID_NOMBRE > [ \<LISTA_IDPRIM> ]

**\< LISTA_IDPRIM >** ::=  ',' \< ID_NOMBRE > [\<LISTA_IDPRIM>]

---
**\< ID_NOMBRE >** ::=  [tnombre tpunto]  tnombre
                   

**\< FROM_LIST >**  ::=    \< TABLElIST >

                      [twhere <WHERE_LIST>] 
                      [tgroup tby  < ID_LIST >]
                      [torder tby <ID_LIST> (tdesc|tasc)]
                      [ tlimit tnumber ]  
                      [  toffset  tnumber ]   

---
**\< TABLElIST >** ::=   \< ID_NOMBRE > [tas tnombre]  [\< TABLE_LISTPRIM >]

**\< TABLE_LISTPRIM >** ::=  ',' \< ID_NOMBRE > [tas tnombre] [\<TABLE_LISTPRIM>]

---
**\< WHERE_LIST >** ::= [tnot] \< ID_NOMBRE >  \< OPERATOR_COMPA > [('\'' \< ID_NOMBRE > '\'') 
   
                |  tnumber]  [\<WHERE_INSTPRIM>] 
                | < ID_NOMBRE >  ( texist | tin )  '(' < PSELECT >  ')'
                | < ID_NOMBRE > [not] tlike '\'' '%' tnombre  '%' '\''
 

---
**\< WHERE_INSTPRIM >** \<OPERATOR_LOGICO> [tnot] \<ID_NOMBRE> \<OPERATOR_COMPA> ( ('\'' \<ID_NOMBRE> '\'') | tnumber) [ \< WHERE_INSTPRIM > ]


---                     
**\<OPERATOR_LOGICO>**  ::=  tor

                | tand

---
**\<OPERATOR_COMPA>**  ::=   ‘<’

                |  ‘>’  
                |  ‘<=’  
                |  ‘>=’  
                |  ‘=’  
                |  ‘<>’  
                |  ‘!=’
        
<br>

## Alter 
<br>

**\<PALTER>** ::= talter \<ALTER_LIST>

---
**\<ALTER_LIST>** ::= tdatabase tnombre \<ALTERDBLIST>

                | tTable <ALTERTABLE_LIST> 

---             
**\<ALTERDBLIST>** ::= trename tTo tnombre

                | tOwner tTo <Tipo_OWNEW >
 

 ---
**\<Tipo_OWNEW >** ::= tnombre

                | tCurrent_user
                | tSession_user


---
**\<ALTERTABLE_LIST>** ::=   tnombre tAdd tColumn tnombre
\<TYPE>[‘(‘tEntero’)’]


                |    tnombre tAdd tCheck ‘(‘ <EXP_LOG> ’)’
                |    tnombre tDrop tColumn tnombre
                |    tnombre tAdd tConstraint tnombre tUnique ‘(‘ tnombre ‘)’
                |    tnombre tAdd tForeing tKey ‘(‘tnombre’)’ tReferences tnombre 
                |    tnombre tAlter tColumn tnombre tSet tNot tNull
                |    tDrop tConstraint tnombre
                |    tRename tColumn tnombre tTo tnombre
                |    tnombre tAlter tColumn tType <TYPE> [‘(‘tEntero’)’]


## Insert
<br>

**\<PINSERT>**        ::=    tInto tnombre \<INSERT_LIST>

---
**\<INSERT_LIST>**        ::=    [‘(‘ \<ID_LIST> ‘)’] tValues ‘(‘ \<EXP_LIST> ‘)’

                |    [‘(‘ <ID_LIST> ‘)’] <PSELECT>
<br>

## Drop
<br>

**\<PDROP>**        ::= tdatabase [tif texists] tnombre

                |    tdrop tTable tnombre
<br>

## Show
<br>

**\<PSHOW>**        ::= tdatabases [tlike [‘%’] tTexto [‘%’]]





## Create


**\<OPT_CREATE>**    ::=    TYPE \<TYPE_BODY>

                |    TABLE <ID_NOMBRE> ‘(‘ <TABLE_BODY> ’)’    
                |    DATABASE [tIf tNot tExists] tnombre [ tOwner [=] user_name ][ tMode [=] <MODE> ]
    
---
**\<TYPE_BODY>**       ::=     tnombre tAa tEnum ‘(‘ \<EXP_LIST> ’)’

---
**\<TABLE_BODY>**    ::=     \<TBODY_PART> [',' \<TABLE_BODY>]

---
**\<TBODY_PART>**    ::=     tnombre \<TYPE> [\<DEFAULT_OPT>]   [\<NULLABLE>] \<C_CONSTRAINT> tConstraint \<CONSTRAINT_DEF>                        

---
**\<C_CONSTRAINT>**    ::=    tPrimary tKey

                |    rReferences tnombre
                |    [[tConstraint tnombre] tUnique] [[tConstraint tnombre] tCheck ‘(’ <BOOL_EXPR> ‘)’]

---
**\<DEFAULT_OPT>**   ::=     tDefault \<VALUE>

---
**\<NULLABLE>**      ::=    ‘NOT NULL’

                |  ’NULL’

---
**\<CONSTRAINT_DEF>**  ::=     tPrimary tKey ‘(‘ \<ID_LIST> ’)’

                |tForeign tKey ‘(‘ <ID_LIST> ’)’ tReferences tnombre ‘(‘ <ID_LIST> ’)’

---
**\<ID_LIST>**        ::=    tnombre [, \<ID_LIST> ]

---
**\<STR_LIST>**        ::=    tString [, \<STR_LIST>]

---
**\<MODE>**        ::=    ‘1’ 

                | ‘2’ 
                | ‘3’ 
                | ‘4’

---           
**\<SIZE_DEF1>**    ::=    ‘(’ tEntero ‘)’

---
**\<SIZE_DEF2>**    ::=    ‘(’ tEntero ‘,’ tEntero ‘)’

<br>

## Update
<br>

**\<PUPDATE>**        ::=  tnombre tset \<UPDATE_LIST> [<WHERE_CLAUSE>]

---
**\<UPDATE_LIST>**        ::=    tnombre ‘=’ \<EXP_LOG>  [<UPDATE_LISTPRIM>]
            
**\<UPDATE_LISTPRIM>**        ::=    ‘,’ tnombre ‘=’  \<EXP_LOG> [<UPDATE_LISTPRIM>]

<br>

## Delete
<br>

**\<PDELETE>**        ::= tFrom tnombre [<WHERE_CLAUSE>]

---
**\<WHERE_CLAUSE>**    ::=    twhere \<EXP_PREDICATE>

<br>
<br>

**\<EXP_LIST>**        ::=    \<EXP> [<EXP_LISTPRIM>] 

**\<EXP_LISTPRIM>**        ::=    ‘,’ \<EXP> [<EXP_LISTPRIM>]
    

---
**\<EXP_PREDICATE>**    ::=    tBetween \<EXP> tAnd \<EXP>

                |<EXP> tIs tNull
                |<EXP> tIs tNot tNull
                |<EXP> tIs [tNot] tDisctint tFrom <EXP>
                |<EXP> tIs [tNot] tTrue <EXP>
                |<EXP> tIs [tNot] tFalse <EXP>
                |<EXP> tIs [tNot] tUnknown <EXP>
                |<EXP_LOG>

---
**\<EXP_LOG>** ::= \<EXP_REL> tAnd \<EXP_REL>

                |<EXP_REL> tOR  <EXP_REL>
                |tNot <EXP_REL>
                |<EXP_REL>

---
\<EXP_REL> ::=  \<EXP> ‘\<’ \<EXP>


                |<EXP> ‘>’  <EXP>
                |<EXP> ‘=’  <EXP>
                |<EXP> ‘<=’ <EXP>
                |<EXP> ‘>=’ <EXP>
                |<EXP> ‘<>’ <EXP>
                |<EXP> [tNot] tLike [‘%’] <EXP> [‘%’]
                |<EXP>

---
**\<EXP>** ::= \<EXP> ‘+’ \<EXP>

                | <EXP> ‘-’ <EXP>
                | <EXP> ‘*’ <EXP>
                | <EXP> ‘/’ <EXP>
                | <EXP> ‘%’ <EXP>
                | <EXP> ‘^’ <EXP>
                | tAbs ‘(’ <EXP> ’)’                
                | tCbrt ‘(’ <EXP> ’)’               
                | tCeil ‘(’ <EXP> ’)’              
                | tCeiling ‘(’ <EXP> ’)’          
                | tDegrees ‘(’ <EXP> ’)’           
                | tDiv ‘(’ <EXP> ‘,’<EXP> ’)’        
                | tExp ‘(’ <EXP>  ’)’               
                | tFactorial ‘(’ <EXP>  ’)’        
                | tFloor ‘(’ <EXP>  ’)’           
                | tGcd ‘(’ <EXP> ‘,’<EXP> ’)’
                | tLcm ‘(’ <EXP> ‘,’<EXP> ’)’
                | tLn ‘(’ <EXP> ’)’               
                | tLog ‘(’ <EXP> ’)’               
                | tLog10 ‘(’ <EXP> ’)’            
                | tMinscale ‘(’ <EXP> ’)’          
                | tMod ‘(’ <EXP> ‘,’<EXP> ’)’       
                | tPi ‘()’
                | tPower ‘(’ <EXP> ‘,’<EXP> ’)’
                | tRadians ‘(’ <EXP> ’)’
                | tRound ‘(’ <EXP> ’)’
                | tScale ‘(’ <EXP> ’)’
                | tSign ‘(’ <EXP> ’)’
                | tSqrt ‘(’ <EXP> ’)’
                | tTrimScale ‘(’ <EXP> ’)’
                | tTruc ‘(’ <EXP> ’)
                | tWidthBucket ‘(’ <EXP> ‘,’<EXP> ’)’
                | tRandom ‘()’
                | tSetseed ‘(‘ <EXP> ’)’
                | tAcos ‘(’ <EXP> ’)’
                | tAcosd ‘(’ <EXP> ’)’
                | tAsin ‘(’ <EXP> ’)’
                | tAsind ‘(’ <EXP> ’)’
                | tAtan ‘(’ <EXP> ’)’
                | tAtand ‘(’ <EXP> ’)’
                | tAtan2 ‘(’ <EXP> ‘,’ <EXP> ’)’
                | tAtand2 ‘(’ <EXP> ‘,’ <EXP> ’)’
                | tCos ‘(’ <EXP> ’)’
                | tCosd ‘(’ <EXP> ’)’
                | tCot ‘(’ <EXP> ’)’
                | tCotd ‘(’ <EXP> ’)’
                | tSin ‘(’ <EXP> ’)’
                | tSind ‘(’ <EXP> ’)’
                | tTan ‘(’ <EXP> ’)’
                | tTand ‘(’ <EXP> ’)’
                | tSinh ‘(’ <EXP> ’)’
                | tCosh ‘(’ <EXP> ’)’
                | tTanh ‘(’ <EXP> ’)’
                | tAsinh ‘(’ <EXP> ’)’
                | tAcosh ‘(’ <EXP> ’)’
                | tAtanh ‘(’ <EXP> ’)’
                | tNot <EXP>
                | [+ | -] <EXP>
                | tTexto
                | <COL_NAME>
                | tTrue
                | tFalse
                | tNow ’()’
                | ‘(‘<EXP_LOG>’)’

---
**\<NUMERO>** ::= tEntero

                | tFloat


<br>

## Tipos
<br>

---
**\<TYPE>** ::=  tSmallint

                |  tInteger
                |  tBigint
                |  tDecimal
                |  tNumeric
                |  tReal
                |  tDoublePrecision
                |  tMoney
                |  tCharacter tVarying
                |  tVarchar
                |  tCharacter
                |  tChar
                |  tText
                |  tTimestamp
                |  tDate
                |  tTime
                |  tInterval
                |  tBoolean

---
**\<TIME>** ::=   tYear

                |  tMonth
                |  tDay
                |  tHour
                |  tMinute
                |  tSecond 

---
**\<REEMPLAZO>**     ::=    tOr tReplace

---
**\<EXISTS>**        ::=     tIf tNot tExists
