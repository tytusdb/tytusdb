#Gramatica Descendente

\<START\>         ::=    \<STATEMENTS>

\<STATEMENTS>     ::=    \<STATEMENTS> \<STATEMENT>   
      |    \<STATEMENT>

\<STATEMENT>    ::=     \<STM_SELECT> ';'  
            |    \<STM_CREATE> ';'  
            |    \<STM_SHOW>   ';'  
            |    \<STM_ALTER>  ';'  
            |    \<STM_DROP>   ';'  
            |    \<STM_INSERT> ';'  
            |    \<STM_DELETE> ';'  
            |    \<STM_UPDATE> ';'

\<STM_SELECT>    ::=    tSelect [tDistinct]\<COLUMN_LIST>  
tFrom \<TABLE_LIST>  
[\<WHERE_CLAUSE>]  
[\<GROUP_CLAUSE>]  
[\<HAVING_CLAUSE>]

\<COLUMN_LIST>    ::=    tAsterisk   
|     \<LIST_NAMES>

\<TABLE_LIST>    ::=    \<TABLE_LIST> ',' \<TABLE_REF>   
            |    \<TABLE_REF> 

\<TABLE_REF>    ::=    \<TABLE> [tNatural] \<JOIN_TYPE> tJoin \<TABLE>  
|    \<TABLE>

\<JOIN_TYPE>    ::=    INNER  
            |    \<OUTER_JOIN_TYPE> [OUTER]

\<OUTER_JOIN_TYPE>::=    tLeft  
            |    tRight  
            |     tFull  

\<TABLE>        ::=    tIdentifier [tAs tTexto]  
            |    '(' STM_SELECT ')'  

LIST_NAMES ::= LIST_NAMES ',' tIdentificador  
           | tIdentificador  





OPTIONAL_STM_SELECT ::= tLimit tNumero  
                | tOffset tNumero  
\<TYPE> ::=  tSmallint  
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
\<TIME> ::=   tYear  
| tMonth  
| tDay  
| tHour  
| tMinute  
| tSecond   

\<EXP_LOG> ::=   
 \<EXP_REL> tAnd \<EXP_REL>  
|\<EXP_REL> tOR  \<EXP_REL>  
|tNot \<EXP_REL>  
|\<EXP_REL>   

\<EXP_REL> ::=  \<EXP> '\<' \<EXP>   
|\<EXP> '>'  \<EXP>  
        |\<EXP> '='  \<EXP>  
        |\<EXP> '\<=' \<EXP>  
        |\<EXP> '>=' \<EXP>  
        |\<EXP> '\<>' \<EXP>  
        |\<EXP>  

\<EXP> ::=  
| \<EXP> '+' \<EXP>  
| \<EXP> '-' \<EXP>  
| \<EXP> '*' \<EXP>  
| \<EXP> '/' \<EXP>  
| \<EXP> '%' \<EXP>  
| \<EXP> '^' \<EXP>  
| tAbs '(' \<EXP> ')'                 //numero  
| tCbrt '(' \<EXP> ')'                //numero  
| tCeil '(' \<EXP> ')'                //numero  
| tCeiling '(' \<EXP> ')'            //numero  
| tDegrees '(' \<EXP> ')'            //numero  
| tDiv '(' \<EXP> ','\<EXP> ')'        //numeros  
| tExp '(' \<EXP>  ')'                //numero  
| tFactorial '(' \<EXP>  ')'         //[+|-]enteros  
| tFloor '(' \<EXP>  ')'            //numero  
| tGcd '(' \<EXP> ','\<EXP> ')'        //enteros  
| tLcm '(' \<EXP> ','\<EXP> ')'        //enteros  
| tLn '(' \<EXP> ')'                //numero>0  
| tLog '(' \<EXP> ')'                //numero>0  
| tLog10 '(' \<EXP> ')'            //numero>0  
| tMinscale '(' \<EXP> ')'            //numero  
| tMod '(' \<EXP> ','\<EXP> ')'        //numeros  
| tpi '()'  
| tNot \<EXP>   
| [+|-]\<EXP>   
| tTexto  
| tIdentificador  
| tTrue  
| tFalse  
| '('\<EXP_LOG>')'  

\<NUMERO> ::= tEntero  
        | tFloat

\<COMENTARIO> :: = tComentario  
            | tComentarioMultiple