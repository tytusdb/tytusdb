# PROYECTO 

## Gramática ascendente

<br>
<br>

---
**\<START>**         ::=    \<STATEMENTS>

-------
**\<STATEMENTS>**        ::=    \<STATEMENTS> \<STATEMENT>   

              |    \<STATEMENT>
---------
**\<STATEMENT>**        ::=     \<STM_SELECT> ‘;’ 

              |    <STM_INSERT> ‘;’
              |    <STM_UPDATE> ‘;’
              |    <STM_DELETE> ‘;’
              |    <STM_CREATE> ‘;’
              |    <STM_ALTER>  ‘;’
              |    <STM_DROP>   ‘;’
              |    <STM_SHOW>   ‘;’
              |    <STM_USE_DB> ‘;’
              |    <STM_SELECT> tUnion [tAll] <STM_SELECT>
              |    <STM_SELECT> tIntersect [tAll] <STM_SELECT>
              |    <STM_SELECT> tExcept [tAll] <STM_SELECT>


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






## Select
<br>


**\<STM_SELECT>**        ::=    tSelect [[tNot] tDistinct]\<LIST_NAMES>  tFrom \<TABLE_LIST>

               [<WHERE_CLAUSE>]
               [<GROUP_CLAUSE>]
               [<HAVING_CLAUSE>]
               [tOrderBy <COL_NAME>]
               [tLimit tEntero]
               [tOffset tEntero]

---
**\<TABLE_LIST>**        ::=    \<TABLE_LIST> ‘,’ \<TABLE_REF>

                |   <TABLE_REF> 

---
**\<TABLE_REF>**        ::=    \<TABLE> [tNatural] \<JOIN_TYPE> tJoin \<TABLE>

                |    <TABLE>

---
**\<JOIN_TYPE>**        ::=    tInner

                |    <OUTER_JOIN_TYPE> [tOuter]

---
**\<OUTER_JOIN_TYPE>**     ::=    tLeft

                |    tRight
                |     tFull

---
**\<TABLE>**        ::=    tIdentifier [tAs tTexto]

                |    ‘(’ <STM_SELECT> ‘)’ [tAs tTexto]

---
**\<LIST_NAMES>**        ::=     \<LIST_NAMES> ‘,’ \<NAMES> [tAs tTexto]

                |    <NAMES> [tAs tTexto]

---
**\<NAMES>**        ::=    tAsterisk

                |    <EXP>
                |    tGreatest ‘(‘ <EXP_LIST> ‘)’
                |    tLeast ‘(‘ <EXP_LIST> ‘)’
                |    <CASE_CLAUSE>
                |    <TIME_OPS>
---
**\<WHERE_CLAUSE>**    ::=    tWhere \<EXP_PREDICATE>

---
**\<GROUP_CLAUSE>**    ::=    tGroup tBy ‘(’ \<GROUP_LIST> ‘)’

---
**\<GROUP_LIST>**        ::=    \<GROUP_LIST> ‘,’ \<COL_NAME>

                |    <COL_NAME>

---
**\<HAVING_CLAUSE>**    ::=    tHaving \<EXP_LOG>

---
**\<CASE_CLAUSE>**        ::=    tCase \<CASE_INNER>[tElse \<EXP>]

---
**\<CASE_INNER>**        ::=    \<CASE_INNER> tWhen \<EXP_LOG> tThen \<EXP>

                |    tWhen <EXP_LOG> tThen <EXP>

---
**\<TIME_OPS>**        ::=    tExtract ‘(‘ \<OPS_FROM_TS> ‘,’ tText ‘)’

                |    tDate_part ‘(‘ tText ‘,’ tINTERVAL tText ‘)’

---
**\<OPS_FROM_TS>**        ::=    tYear tFrom tTimestamp

                |    tHour tFrom tTimestamp
                |    tMinute tFrom tTimestamp
                |    tSecond tFrom tTimestamp
                |    tMonth tFrom tTimestamp
                |    tDay tFrom tTimestamp

 
<br>

## Insert
<br>
               

**\<STM_INSERT>**        ::=    tInsert tInto tIdentifier \<INSERT_OPS>

---
**\<INSERT_OPS>**        ::=    [‘(‘ \<COLUMN_LIST> ‘)’] tValues ‘(‘ \<EXP_LIST> ‘)’

                |    [‘(‘ <COLUMN_LIST> ‘)’] <STM_SELECT>

---
**\<COLUMN_LIST>**        ::=    \<COLUMN_LIST> ‘,’ tIdentifier

                |    tIdentifier


<br>

## Update
<br>


**\<STM_UPDATE>**        ::=    tUpdate tIdentifier tSet \<UPDATE_LIST> 
                [<WHERE_CLAUSE>]

---
**\<UPDATE_LIST>**        ::=    \<UPDATE_LIST> ‘,’ tIdentifier ‘=’ \<EXP_LOG>

                |    tIdentifier ‘=’ <EXP_LOG>


<br>

## Delete
<br>

**\<STM_DELETE>**        ::=    tDelete tFrom tIdentifier                 [<WHERE_CLAUSE>]

 
<br>

## Create
<br>

**\<STM_CREATE>**        ::=    tCreate tType tIdentifier tAs tEnum ‘(‘ \<EXP_LIST> ‘)’

                |    tCreate [tOr tReplace] tDatabase tIdentifier  [tOwner ‘=’ tTexto] [tMode ‘=’ tEntero]
                |    tCreate tTable tIdentifier ‘(‘<TAB_CREATE_LST>’)’[tInherits ‘(‘ tIdentifier ‘)’]

---
**\<TAB_CREATE_LST>**    ::=    \<TAB_CREATE_LST>‘,’tIdentifier \<TYPE>[[tNot]tNull][tPK] 

                |    tIdentifier <TYPE> [[tNot]tNull][tPK]


<br>

## Alter
<br>

**\<STM_ALTER>**        ::=    tAlter tDatabase tIdentifier tRename tTo tIdentifier

                |    tAlter tDatabase tIdentifier tOwner tTo <DB_OWNER>
                |    tAlter tTable tIdentifier tAdd tColumn tIdentifier <TYPE>[‘(‘tEntero’)’]
                |    tAlter tTable tIdentifer tAdd tCheck ‘(‘<EXP_LOG>’)’
                |    tAlter tTable tIdentifier tDrop tColumn tIdentifier
                |    tAlter tTable tIdentifier tAdd tConstraint tIdentifier 
                     tUnique ‘(‘ tIdentifier ‘)’
                |    tAlter tTable tIdentifier tAdd tForeing tKey ‘(‘iIdentifier’)’
                     tReferences tIdentifier ‘(‘iIdentifier’)’
                |    tAlter tTable tIdentifier tAlter tColumn tIdentifier tSet tNot tNull
                |    tAlter tTable tIdentifier tDrop tConstraint tIdentifier
                |    tAlter tTable tIdentifier tRename tColumn tIdentifier tTo tIdentifier
                |    tAlter tTable tIdentifer tAlter tColumn tType <TYPE>[‘(‘tEntero’)’]


---
**\<EXP_LIST>**        ::=    \<EXP_LIST> ‘,’ \<EXP>

                |    <EXP>

---
**\<DB_OWNER>**        ::=    tText

                |    tCurrentUser
                |    tSessionUser


<br>

## Drop
<br>


**\<STM_DROP>**        ::=    tDrop tDatabase [tIf tExists] tIdentifier

                |    tDrop tTable tIdentifier 


<br>

## Show
<br>


**\<STM_SHOW>**        ::=    tShow tDatabases [tLike [‘%’] tTexto [‘%’]]

<br>

**\<STM_USE_DB>**        ::=    tUse tDatabases tIdentificador

<br>

## Tipos
<br>

**\<TYPE>** ::=  tSmallint

                |tInteger
                |tBigint
                |tDecimal
                |tNumeric
                |tReal
                |tDoublePrecision
                |tMoney
                |tCharacter tVarying
                |tVarchar
                |tCharacter
                |tChar
                |tText
                |tTimestamp
                |tDate
                |tTime
                |tInterval
                |tBoolean

---
**\<TIME>** ::=   tYear

                | tMonth
                | tDay
                | tHour
                | tMinute
                | tSecond 

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
**\<EXP_LOG>** ::= \<EXP_LOG> tAnd \<EXP_LOG>

                |<EXP_LOG> tOR  <EXP_LOG>
                |tNot <EXP_LOG>
                |<EXP_LOG> 

---
**\<EXP_REL>** ::=  \<EXP> ‘\<’ \<EXP> 

                |<EXP> ‘>’  <EXP>
                |<EXP> ‘=’  <EXP>
                |<EXP> ‘<=’ <EXP>
                |<EXP> ‘>=’ <EXP>
                |<EXP> ‘<>’ <EXP>
                |<EXP> [tNot] tLike [‘%’] tTexto [‘%’]
                |<EXP>

---
**\<EXP>** ::=  \<EXP> ‘+’ \<EXP>

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
                | [+|-]<EXP> 
                | tTexto
                | <COL_NAME>
                | tTrue
                | tFalse
                | <NUMERO>
                | tNow ’()’
                | ‘(‘<EXP_LOG>’)’

---
**\<NUMERO>** ::= tEntero

                | tFloat

---
**\<COL_NAME>** ::= tIdentificador [‘.’ tIdentificador]



