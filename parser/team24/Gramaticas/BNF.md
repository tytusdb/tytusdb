# Reporte BNF

La sintaxis de SQL es muy compleja, pero para este proyecto se redujo la sintaxis a las funciones mas importantes, a continuación se muestra dos gramáticas diferentes, una descendente y una ascendente.


## Descendente

Esta gramática tiene muchas mas producciones en comparación con la gramática ascendente y no es recomendada utilizarla ya que ply es un analizador ascendente, también en cuanto a pruebas de optimización es un tanto mas lento este método, otro punto en contra es que requiere mucha mas programación para la funcionalidad.

>**'INICIO'** := create **'SENTENCIA_CREATE'**  
| show **'SENTENCIAS_SHOW'**  
| alter **'SENCIAS_ALTER'**  
| drop **'SENTECIAS_DROP'**  
| delete **'SENTENCIA_DELETE'**  
| update **'SENTENCIA_UPDATE'**  
| insert **'SENTENCIAS_INSERT'**  
| **'QUERIES'**  
|

>**'SENTENCIA_CREATE'** := or **'OR_DATABESE'**  
| database **'SENTENCIAS_DATABASE'**  
| table **'SENTENCIA_CREATE_TABLE'**

>**'OR_DATABESE'** := replace database **'SENTENCIAS_DATABASE'**

>**'SENTENCIAS_DATABASE'** := if not exists (identificador) **'OWNER_OR_MODE'**  
| (identificador) **'OWNER_OR_MODE'**

>**'OWNER_OR_MODE'** := ; **'INICIO'**  
| owner = (identificador) **'OWNER_OR_MODE'**  
| mode = (numero) **'OWNER_OR_MODE'**

>**'SENTENCIAS_SHOW'** := database like reguex; **'INICIO'**  
| database; **'INICIO'**

>**'SENTENCIAS_ALTER'** := database (identificador) **'RENAME_OR_OWNER'**  
| table **'ALTER_TABLE'**

>**'ALTER_TABLE'** :=  (identificador) add column type; **'INICIO'**  
|(identificador) add check( (identificador) **'CONDICIONALES'** ; **'INICIO'**  
|(identificador) add constraint (identificador) unique (identificador) ; **'INICIO'**  
|(identificador) add foregn key (identificador) references (identificador); **'INICIO'**  
|(identificador) alter column (identificador) SET NOT NULL; **'INICIO'**  
|(identificador) drop constraint (identicador); **'INICIO'**  
|(identificador) rename column (identificador) to (identificador); **'INICIO'**  
|(identificador) drop column (identificador); **'INICIO'**


>**'RENAME_OR_OWNER'** := rename to 	(identificador) ; **'INICIO'**  
|owner to **'SENTCIAS_OWNER'**

>**'SENTENCIAS_DROP'** := database if exists (identificador); **'INICIO'**  
|database (identificador) ; **'INICIO'**  
|table (identificador) ; **'INICIO'**


>**'SENTENCIA_CREATE_TABLE'** := identificador ( **'TABLA_COLUMNA_INICIAL'**

>**'TABLA_COLUMNA_INICIAL'** := idenficador type **'TABLA_IDENTIFICADOR'**  
| constraint identificador chek **'CONDICIONALES'**  
| unique( **'SENTENCIA_UNIQUE_OR_KEY'**  
| primary key **'SENTENCIA_UNIQUE_OR_KEY'**  
| foreign key **'SENTENCIA_UNIQUE_OR_KEY'**


>**'TABLA_IDENTIFICADOR'** := default (valor) **'TABLA_IDENTIFICADOR'**  
| NOT NULL **'TABLA_IDENTIFICADOR'**  
| NOT      **'TABLA_IDENTIFICADOR'**  
| constraint (identificador) unique **'TABLA_IDENTIFICADOR'**  
| constraint (identificador) check **'CONDICIONALES'**  
| primary key **'TABLA_IDENTIFICADOR'**  
| references **'TABLA_IDENTIFICADOR'**  
| , **'TABLA_COLUMNAS'**
| primary key **'SENTENCIA_UNIQUE_OR_KEY'**  
| foreign key **'SENTENCIA_UNIQUE_OR_KEY'**  
| ); **'INICIO'**

>**'TABLA_COLUMNAS'** := idenficador type **'TABLA_IDENTIFICADOR'**  
|constraint identificador chek **'CONDICIONALES'**  
| unique( **'SENTENCIA_UNIQUE'**  
| ); **'INICIO'**

>**'SENTENCIA_UNIQUE_OR_KEY'** := identificador, **'SENTENCIA_UNIQUE_OR_KEY'**  
| identificador) **'TABLA_IDENTIFICADOR_AUX'**

>**'TABLA_IDENTIFICADOR_AUX := , **'TABLA_COLUMNAS'**  
| ); **'INICIO'**


>**'SENTENCIAS_INSERT'** := into (identificador) values ( **'VALORES'**

>**'VALORES'** := numero **'VALORES_AUX'**  
|texto **'VALORES_AUX'**

>**'VALORES_AUX'** := ,numero **'VALORES_AUX'**  
|,texto **'VALORES_AUX'**  
|); **'INICIO'**

>**'SENTENCIAS_UPDATE'** := (identificador) set (identificador) = (primitivo) where **'SUB_QUERY'**

>**'SENTENCIAS_DELETE'** := from identificador where **'SUB_QUERY'**

>**'QUERIES'**	:= **'QUERY'** **'QUERIES''**

>**'QUERIES''**	:= **'QUERY'** **'QUERIES''**
|

>**'QUERY'**	:= **'QUERY''**  **'COM'** ;

>**'COM'**	:= union    **'D'** **'QUERY''**  
| intersect **'D'** **'QUERY''**  
| EXCEPT    **'D'** **'QUERY''**  
|

>**'D'**	:= all  
|

>**'QUERY''**:= select A **'SELECT_LIST'**  from **'TABLE_EXPRESSION'** **'CONDITION'** **'GROUP'** **'ORDER'** **'LIM'** **'OF'**

>**'A'**:= distinct  
|

>**'SELECT_LIST'**	:= ASTERISCO  
| **'LIST'**   
|

>**'LIST'**		:= **'COLUMN'** LIST'  
| **'QUERY''**

>**'LIST''**	:= , **'COLUMN'** **'LIST''**  
|

>**'COLUMN'**	:= id B  
| **'TRIG'**  
| **'MATH'**

>**'B'**	:= . id   
|

>**'CONDITION'** := where **'VALOR'**  
|

>**'VALOR'**:= **'VALOR'** MAS **'VALOR'**  
| **'VALOR'** MENOS **'VALOR'**  
| **'VALOR'** POR **'VALOR'**  
| **'VALOR'** DIVIDIDO **'VALOR'**  
| **'VALOR'** MOD **'VALOR'**  
| **'VALOR'** AND **'VALOR'**  
| **'VALOR'** OR **'VALOR'**  
| **'VALOR'** XOR **'VALOR'**  
| **'VALOR'** DIFERENTE **'VALOR'**  
| **'VALOR'** IGUALDOBLE **'VALOR'**  
| **'VALOR'** MAYOR **'VALOR'**  
| **'VALOR'** MAYORIGUAL **'VALOR'**  
| **'VALOR'** MENORIGUAL **'VALOR'**  
| **'VALOR'** is distinct  **'VALOR'**  
| **'VALOR'** is not distinct **'VALOR'**  
| not exists ( **'QUERY''** )  
| exists ( **'QUERY''** )  
| **'CE'** **'CE''**  
| **'VALOR'** MENOR **'VALOR'**  
| smallint  
| integer  
| bigint  
| decimal  
| numeric  
| real  
| double precision  
| money

>**'CE'**	:= **'COLUMN'**  
| **'EXPRE'**

>**'CE''**	:= **'OPERA'** **'SAA'** ( **'QUERY''** )  
| in ( **'QUERY''** )  
| not in ( **'QUERY''** )  
| not exists ( **'QUERY''** )  
| exists ( **'QUERY''** )  
|

>**'GROUP'**:= group by **'LIST'** **'HAVE'**  
|

>**'LIM'**	:= limit **'LIM''**  
|

>**'LIM''**	:= number  
| all

>**'OF'**	:= ofset number  
|

>**'ORDER'**	:= COLUMN AD N  
|

>**'AD'**	:= asc  
| des

>**'N'**	:= nulls **'FL'**  
|

>**'FL'**	:= first  
| last

>**'JO'**	:= id **'JO''** join id **'JO'''**

>**'JO''** 	:= natural **'IN'**  
| **'IN'**

>**'IN'**	:= inner  
| **'LRF'** **'OU'**

>**'LRF'**	:= left  
| right  
| full

>**'OU'**	:= outer
|

>**'JO'''**	:= on  **'VALOR'**  
| using ( join LIST )  	
|


>**'TABLE_EXPRESSION'**:  **'TE'** **'TE''**

>**'TE''**	:= , **'TE'** **'TE''**  
|


>**'TE'**	:= **'JO'**  
| id  
| **'QUERY''**  
|

>**'MATH'** := abs ( **'VALOR'** )  
| cbrt ( **'VALOR'** )  
| ceil ( **'VALOR'** )  
| ceiling ( **'VALOR'** )  
| degrees ( **'VALOR'** )  
| div ( **'VALOR'** )  
| exp ( **'VALOR'** )  	
| factorial ( **'VALOR'** )  
| floor ( **'VALOR'** )  
| gcd ( **'VALOR'** )  
| lcm ( **'VALOR'** )  
| ln ( **'VALOR'** )  
| log ( **'VALOR'** , **'VALOR'** )  
| log10 ( **'VALOR'**  )  
| min_scale  
| mod (**'VALOR'**, **'VALOR'**)  
| pi ()  
| power ( **'VALOR'** )  
| radians ( **'VALOR'** )  
| round ( **'VALOR'** )  
| scale  
| sign ( **'VALOR'** )  
| sqrt ( **'VALOR'** )  
| trim_scale  
| truc ( **'VALOR'** , **'VALOR'** )  
| width_bucket ( **'VALOR'** , **'VALOR'** , **'VALOR'** , **'VALOR'** )  
| random ()  
| setseed ( **'VALOR'** )  
| count ( **'VALOR'** )


>**'TRIG'**	:=  acos ( **'VALOR'** )  
| acosd ( **'VALOR'** )  
| asin ( **'VALOR'** )  
| asind ( **'VALOR'** )  
| atan ( **'VALOR'** )  
| atand ( **'VALOR'** )  
| atan2 ( **'VALOR'** )  
| atan2d ( **'VALOR'** )  
| cos ( **'VALOR'** )  
| cosd ( **'VALOR'** )  
| cot ( **'VALOR'** )  
| cotd ( **'VALOR'** )  
| sin ( **'VALOR'** )  
| sind ( **'VALOR'** )  
| tan ( **'VALOR'** )  
| tand ( **'VALOR'** )  
| sinh ( **'VALOR'** )  
| cosh ( **'VALOR'** )  
| tanh ( **'VALOR'** )  
| asinh ( **'VALOR'** )  
| acosh ( **'VALOR'** )  
| atanh ( **'VALOR'** )


>**'TIME'**	:= extract ( **'EX'** )   
| now ( )  
| date_part ( **'DP'** )  
| current_date  
| current_time  
| timestamp **'VALOR'**

>**'EX'**	:= **'TIPO'** from timestamp **'VALOR'**

>**'TIPO'**	:= hour  
| minute  
| second  
| year

>**'PD'**	:= VALOR , interval **'VALOR'**

>**'EXPRE'**:= case when VALOR then **'VALOR'** **'CASES'** **'ELSES'**

>**'CASES'**	:= when VALOR then **'VALOR'** **'CASES'**
|

>**'ELSES'**	:= else **'VALOR'**
|

>**'OPERA'**	:= ||  
| &  
| |  
| #  
| ~  
| MAYORQUE MAYORQUE  
| MENORQUE MENORQUE

>**'SA'**:= some  
| any  
| all


## Ascendente

Esta gramática es mas efectiva para trabajar con ply ya que el analizar por defecto recorre y retorna las producciones de forma ascendente, durante las pruebas de efectividad el tiempo es mas rápido en comparación con la gramática descente

>**'ID'** := Identificador

>**'TIPO'** :=   int  
|  Char  
|  varchar

>**'COND'** := **'ID'** '**TIPO'**

>**'CREREPDB'** := CREATE DATABASE IF NOT EXISTS **'ID'** **'CREREPDB2'**  
|  REPLACE DATABASE IF NOT EXISTS **'ID'** **'CREREPDB2'**

>**'CREREPDB2'** : IGUAL OWNER  IGUAL ID MODE IGUAL **'MODE'**

>**'MODE'** := 1  
|  int

>**'SHOWDB'** := SHOW DATABASES LIKE **'ID'**

>**'ALTERDB'** := ALTER DATABASE **'ID'** **'ALTERDB2'**

>**'ALTERDB2'** := RENAME TO **'ID'**  
|  OWNER TO **'OWNDB'**

>**'OWNDB'** := { 'ID'  'ID'  'ID' }

>**'DROPDB'** := DROP DATABASE  IF EXISTS  **'ID'**

>**'CREATETB'** := CREATE TABLE **'ID'** ( **'CONTTB'** ); **'HERENCIA'**

>**'HERENCIA'** := INHERITS (**'ID'**);

>**'HERENCIA'** := Є

>**'CONTTB'** := **'CONTRB'** , **'COLUMNA'**

>**'CONTTB'** := **'COLUMNA'**

>**'COLUMNA'** := **'ID'** **'TIPO'** **'PROPCOL'**

>**'PROPCOL'** := **'PROPCOL'**  **'PROPIEDADESCOL'**

>**'PROPCOL'** := **'PROPIEDADESCOL'**

>**'PROPIEDADES'** := DEFAULT **'ID'**  
|	NOT NULL  
|	CONSTRAINT **'ID'** UNIQUE  
|	CONSTRAINT **'ID'** CHECK (**'ID'**)  
|	PRIMARY KEY  
|	REFERENCES **'ID'**

>**'DROPTB'** := DROP TABLE **'ID'**;

>**'ALTTB'** := ALTER TABLE **'ID'** **'ALTTB2'**

>**'ALTTB2'** := ADD COLUMN **'ID'** **'TIPO'**;  
|	DROP COLUMN **'ID'**;  
|	ADD CONSTRAINT **'ID'** UNIQUE (**'ID'**);  
|	ADD FOREIGN KEY (**'ID'**) REFERENCES **'ID'**;  
|	ALTER COLUMN **'ID'** **'PROPIEDADES'**;  
|	DROP CONSTRAINT **'ID'**;  
|	RENAME COLUMN **'ID'** TO **'ID'**;

>**'DELETFROM'** := DELETE FROM **'DELETFROM2'**

>**'DELETFROM2'** := [ ONLY ] **'ID'** **'DELETFROM3'**    
|	**'ID'** **'DELETFROM3'**

>**'DELETFROM3'** := * **'DELETFROM4'**  
|	**'DELETFROM4'**

>**'DELETFROM4'** := AS **'ID'** **'DELETFROM5'**  
|	**'DELETFROM5'**

>**'DELETFROM5'** := WHERE **'COND'**

>**'INSERT'** := INSERT INTO **'ID'** VALUES (**'VALORES'**);

>**'VALORES'** := **'VALORES'** , **'TIPO'**

>**'VALORES'** := **'TIPO'**

>**'UPDATE'** := UPDATE **'ID'** SET **'COND'** WHERE **'COND'**;

>**'COND'** := **'ID'** = **'TIPO'**

>**'DELETE'** := DELETE FROM **'ID'** WHERE **'COND'**;

>**'QUERIES'** := **'QUERIES'** **'QUERY'**  
| **'QUERY'**

>**'QUERY'** := **'QUERY'**' **'COM'** ;

>**'COM'** : = UNION **'QUERY'**  
| INTERSERCT **'QUERY'**  
| EXCEPT **'QUERY'**  
|

>**'QUERY'**' : = select **'DISTINCT'** **'SELECT_LIST'**  from **'TABLE_**'EXP'**RESSION'** CONDITION GROUP ORDER LIM OF

>**'DISTINCT'** : = **'DISTINCT'**  
|

>**'SELECT_LIST'** := ASTERISCO  
| **'LIST'**

>**'LIST'** := **'COLUMN'** **'ALIASCOL'**, **'LIST'**
| **'COLUMN'** **'ALIASCOL'**

>**'COLUMN'** := id **'COLUMNP'**  
| **'TRIG'**  
| **'MATH'**

>**'COLUMNP'** := . id  
|

>**'ALIAS'** := id  
|

>**'ALIASCOL'** := as id  
|

>**'TRIG'** := acos ( valor )  
| acosd ( valor )  
| asin ( valor )  
| asind ( valor )  
| atan ( valor )  
| atand ( valor )  
| atan2 ( valor )  
| atan2d ( valor )  
| cos ( valor )  
| cosd ( valor )  
| cot ( valor )  
| cotd ( valor )  
| sin ( valor )  
| sind ( valor )  
| tan ( valor )  
| tand ( valor )  
| sinh ( valor )  
| cosh ( valor )  
| tanh ( valor )  
| asinh ( valor )  
| acosh ( valor )  
| atanh ( valor )

>**'MATH'** : = abs ( valor )  
| cbrt ( valor )  
| ceil ( valor )  
| ceiling ( valor )  
| degrees ( valor )  
| div ( valor )  
| **'EXP'** ( valor )  
| factorial ( valor )  
| floor ( valor )  
| gcd ( valor )  
| lcm ( valor )  
| ln ( valor )  
| log ( valor , valor )  
| log10 ( valor  )  
| min_scale  
| mod (valor, valor)  
| pi ()  
| power ( valor,valor )	 	
| radians ( valor )  
| round ( valor )  
| scale ( valor )  
| sign ( valor )  
| sqrt ( valor )  
| trim_scale  
| trunc ( valor , valor )  
| width_bucket ( valor , valor , valor , valor )  
| random ()  
| setseed ( valor )

>**'TABLE_EXPRESSION'** := id **'ALIAS'** **'TE''**  
| **'QUERY'**  
| **'CASEWHEN'**

>**'TE''** := , **'TABLE_**'EXP'**RESSION'**  
| **'JOIN'** **'TE''**  
|

>**'JOIN'** := **'JOINTYPE'** **'JOIN'** on **'BOOL_EXP'**

>**'JOINTYPE'** := inner  
| **'LRF'** **'OUTER'**

>**'LRF'** := left  
| right  
| full

>**'OUTER'** := **'OUTER'**  
|

>**'BOOL_EXP'** := **'EXP'** MAYORQ **'EXP'**  
| **'EXP'** MENORQ **'EXP'**  
| **'EXP'** MAYORQ= **'EXP'**  
| **'EXP'** MENORQ= **'EXP'**  
| **'EXP'** == **'EXP'**  
| **'EXP'** != **'EXP'**  
| **'BOOL_EXP'** AND **'BOOL_EXP'**  
| **'BOOL_EXP'** OR **'BOOL_EXP'**  
| ( **'BOOL_EXP'**'** )  
| not exists (**'QUERY'**)  
| exists ( **'QUERY'** )  
| **'EXP'** between **'EXP'** and **'EXP'**

>**'EXP'** : = smallint  
| integer  
| bigint  
| decimal  
| numeric  
| real  
| double precision  
| money  
| varchar  
| char  
| text  
| datetime

>**'CASEWHEN'** : = case when **'BOOL_EXP'** then **'EXP'** **'CASES'** **'ELSE'** end **'ALIAS'**

>**'CASES'** := when **'BOOL_EXP'** then **'EXP'** **'CASES'**  
|

>**'ELSE'** := **'ELSE'** **'EXP'**
