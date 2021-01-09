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








## PLGSQL LANGUAGE
<br>


**\<ASIG_BASICA>** ::= tIdentifier \<ASIG_ASIGNACION>    \<VALOR_ASIGNACION>

**\<SIG_ASIGNACION>** ::= tDospuntos tIgual

               tIgual
                               
**\<VALOR_ASIGNACION>** ::= \<EXP>

                | '('  <STATEMENTS_SQL> ')' 

**\<STM_PERFORM>** ::=  tPerform tIdentifier PARA tTexto ',' tIdentifier  ')'

**\<STM_IF>** ::=  tIf    \<CONDITION>  THEN  [\<IF_INST>]    [\<ELSIF_OPT>]  [\<ELSE_OPT>]   tEnd  tIf  ';'


**\<CONDITION>** ::=  [\<EXP_PREDICATE>] 


**\<ELSIF_OPT>** ::=  [ \<ELSIF_OPT> tElsIf  \<CONDITION> tThen  [\<IF_INST>]  ]


**\<ELSIF_OPT>** ::=   [ tElse  \<IF_INST>   ]


**\<IF_INST>** ::= \<IF_INST>  \<STATEMENTS_SQL>  ';'   

                |   <IF_INST>  <RAISE_OP> 
                | <IF_INST>  <ASIG_BASICA> ';
                | <IF_INST>  <RETURN_>  ';'
                | <IF_INST>  <STM_IF> ';'



**\<STM_BEGIN>** ::=  [\<DECLARE_OPT>] tBegin [\<STATEMENTS_BEGIN>]  [\<EXCEPTION_OPT>] [\<RETURN_OPT>] tEnd  [\<IF_OPT>] 


**\<STATEMENTS_BEGIN>** ::= \<STATEMENTS_BEGIN>  \<STATEMENTS_SQL>  ';' 

               | <STATEMENTS_BEGIN>  <STM_IF> ';'
               |  <STATEMENTS_BEGIN>  <ASIG_BASICA> ';' 
               | <STATEMENTS_BEGIN>  <STM_CASE>  ';'
               | <STATEMENTS_BEGIN>  <RETURN_>  ';'


**\<RETURN_>** ::=   tReturn  \<EXP_LOG>


**\<EXCEPTION_OPT>** ::=   tException  [\<WHEN_OPT>]  


**\<WHEN_OPT>** ::=   \<WHEN_OPT> tWhen  \<ATR_WHEN> [\<THEN_OP>]

               |  tWhen  <ATR_WHEN> [<THEN_OP>] 
               |  tWhen 


**\<ATR_WHEN>** ::=  tNo_data_found 

               |  tToo_many_rows 
               |  tIdentifier 

**\<then_op>** ::= tTHEN [\<RAISE_OP>]

**\<then_op>** ::= tThen tNull 

**\<RAISE_OP>** ::= tRaise \<ATR_RAISE> tTexto ',' \<COL_NAME> ';' 

               |  tRaise <ATR_RAISE> tTexto  ';'


**\<ATR_RAISE>** ::=  tNotice  

               |  tException  
               |  tIdentifier 

**\<RETURN_OPT>** ::=   tReturn  \<EXP_LOG>  ';' 

**\<STM_EXECUTE>** ::=  tExecute  TEXTO    tInto  tIdentifier  tUsing    \<GROUP_LIST> 

               |   tExecute  tIdentifier  ‘(’  TEXTO     ‘,’   <COLUMN_LIST>   ’)’  tInto tIdentifier  tUsing    <GROUP_LIST>
               |  tExecute  tIdentifier  ‘(’  TEXTO  TEXTO   ‘,’   <COLUMN_LIST>   ’)’  tInto tIdentifier  tUsing    <GROUP_LIST> 
               |   tExecute  tIdentifier  ‘(’  TEXTO     ‘,’   <COLUMN_LIST>   ’)’   tUsing    <GROUP_LIST>
               |  tExecute  tIdentifier  ‘(’  TEXTO  TEXTO   ‘,’   <COLUMN_LIST>   ’)’   tUsing    <GROUP_LIST>
               |   tExecute  tIdentifier  ‘(’  TEXTO     ‘,’   <COLUMN_LIST>   ’)’ 
               |   tExecute  <EXPRESSION>   
               |  tExecute  tIdentifier ‘(’ <EXP_LIST> ‘)’   
               |  tExecute  tIdentifier ‘(’ ‘)’ 


**\<STM_GET>** ::=  tGet  tDiagnostics \<ASIGNACION_BASICA> 

**\<STM_CASE>** ::=   tCase  [\<ID_CASE>]     [\<WHEN_INST>]  \<CONDITION> tThen  [\<CASE_INST]  [\<WHEN_INST>] [\<CASE_ELSE>]   tEnd  tCase 


**\<ID_CASE>** ::=  \<COLUMN_LIST> 

**\<WHEN_INST>** ::=  \<WHEN_INST >    tWhen  \<CONDITION> tThen   \<CASE_INST> 

               |    tWhen  \<CONDITION> tThen   \<CASE_INST>  


**\<CASE_ELSE>** ::= tElse    \<CASE_INST>  

**\<CASE_INST>** ::= [\<CASE_INST>]  \<STATEMENTS_SQL>  ';' 

               |   [<CASE_INST>]   <RAISE_OP>  
               |  [<CASE_INST>]    <ASIG_BASICA> ';'
               |  <CASE_INST>  <RETURN_>  ';' 
               |  <CASE_INST>  <STM_IF> ';' 



**\<STATEMENTS_SQL>** ::= [\<STATEMENTS_SQL>]  \<STM_SELECT>  ';' 

               |    <STM_INSERT>  
               |    <STM_UPDATE> ';'



**\<STM_CREATE FUNCTION>** ::= tCreate tFunction tIdentifier '(' [\<LIST_PARAM_FUNCTION_OPT>] ')' tReturns \<TYPE> [\<AS_OPT>] \<STM_BEGIN> ';' '$$' tLanguage tPlpgsql

<br>

**\<LIST_PARAM_FUNCTION_OPT>** ::= [\<PARAMS_FUNCTION>]


**\<PARAMS_FUNCTION>** ::= \<PARAMS_FUNCTION> ','   \<PARAM_FUNCTION>

               |  <PARAM_FUNCTION>
               | tIdentifier
               | <type>
               | tIdentifier <TYPE>
               | [<PARAM_MODE_OPT>] tIdentifier <TYPE>


**\<PARAM_MODE>** ::=   [IN  |  OUT  |  INOUT]

**\<AS_OPT>** ::= tAs '$$' ';'

**\<DECLARES_OPT>** ::= [\<DECLARES_OPT>] tDeclare \<DECLARATIONS>

**\<DECLARATIONS>** ::= [\<DECLARATIONS>] \<DECLARATION>

               |  <DECLARATION>

**\<DECLARATION>** ::= tIdentifier \<CONSTANT_OPT> \<TYPE>  \<COLLATE_OPT>  \<NOT_NULL_OPT> \<EXPRESSION_OPT> ';' 

               |  tId tAlias tFor $ tEntero ';'
               | tIdentifier tIdentifier '%' tRowtype ';'  
               | tIdentifier tIdentifier tPunto '%' tType
               |  tIdentifier tRecord ','


 **\<CONSTANT>** ::= tConstant     

               |  tCollate tIdentifier

**\<NOT_NULL_OPT>** ::= tNot tNull

**\<EXPRESSION_OPT>** ::= tDefault \<EXPRESSION>

               |  ':=' <EXPRESSION> 
               |  '=' <EXPRESSION>


**\<STM_DROP_FUNCTION>** ::= tDrop tFunction [\<IF_EXISTS_OPT>] tIdentifier [\<MODE_DROP_FUNCTION_OPT>]

**\<STM_DROP_PROCEDURE>** ::= tDrop tProcedure [\<IF_EXISTS_OPT>] tIdentifier [\<MODE_DROP_FUNCTION_OPT>]

**\<MODE_DROP_FUNCTION>** ::= tCascade

               |  tRestrict

**\<STM_CREATE_PROCEDURE>** ::= tCreate tProcedure tIdentifier '(' [\<LIST_PARAM_FUNCTION_OPT>] ')' tLanguage tPlpgsql tAs \<STM_BEGIN> ';' '$$'

**\<STM_INDEX>** ::= tCreate [\<UNIQUE_OPT>] tIndex  tIdentifier tOn tIdentifier \<USING_HASH_OPT> '(' \<PARAMS_INDEX> ')' \<WHERE_CLAUSE_OPT> 

**\<PARAMS_INDEX>** ::= [\<PARAMS_INDEX>] ',' <PARAM_INDEX>

               |  <PARAM_INDEX>
               |  tIdendtifier <ORDER_OPT>
               |  tIdentifier <ORDER_OPT>   tNUlls tFirst 
               | tIdentifier <ORDER_OPT> tNulls tLast
               | <EXP>







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
