# Reporte Gramatical G19

# [Descendente](https://github.com/markdown-it/markdown-it-container)

    S ::= INSTRUCCIONES

    INSTRUCCIONES  ::= INSTRUCCION INSTRUCCIONES_PRIMA 

    INSTRUCCIONES_PRIMA ::= p_coma INSTRUCCIONES_PRIMA2 | epsilon     

    INSTRUCCIONES_PRIMA2 ::= INSTRUCCION p_coma INSTRUCCIONES_PRIMA2
                    | epsilon

    INSTRUCCION ::= create C
                    | show database LK  

                    | alter DT  

                    | drop DO  

                    | delete from OL  

                    | insert into id VALUES parent_i L_VAL parent_d  
                    
                    | update id set ACT

    C ::= type id as enum parent_i L_VAL parent_d 
         | RE database IFEX id OW MO
         | table id parent_i CT parent_d INH

    L_VAL ::= VAL L_VALP

    L_VALP ::= coma VAL L_VALP
              | epsilon 

    VAL ::= decimal 
            | entero
            | caracter
            | cadena
            | true
            | false

    RE ::= or replace
          | epsilon

    IFEX ::= if not exists
             | epsilon

    OW ::= owner HI id
           | epsilon

    HI ::= igual
           | epsilon

    MO ::= mode HI entero 
          | epsilon

    INH ::= inherits parent_I id parent_d
           | epsilon

    CT ::= COL CTP

    CTP ::= coma COL CTP
           | epsilon

    COL ::= id id AT
            | CK
            | unique parent_i L_ID parent_d
            | primary key parent_i L_ID parent_d 
            | foreign key parent_i L_ID parent_d references id parent_i L_ID parent_d

    L_IDP ::= coma id L_IDP
             | epsilon

    AT ::= primary key 
          | references id
          | DEFU

    DEFU ::= default VAL NN
            | NN

    NN ::= not null CC
          | null CC
          | CC

    CC ::= constraint id UC
          | UC

    UC ::= unique CK
          | check parent_i LOG parent_d
          | epsilon

    CK ::= constraint id ckeck parent_i LOG parent_d 
          | epsilon

    LOG ::= W LOGP

    LOGP ::= W LOGP
            | epsilon

    W ::= Y WP

    WP ::= mas Y WP
          | menos Y WP 
          | epsilon 

    Y ::= Z YP

    YP ::= por Z YP
          | division Z YP
          | modulo Z YP
          | epsilon 

    Z ::= X ZP

    ZP ::= potencia X ZP
          | epsilon

    X ::= U XP 

    XP ::= mayorque U 
          | menorque U 
          | mayorigual U 
          | menorigual U 
          | igual U
          | distinto U 
          | epsilon

    U ::= V UP 

    UP ::= or V UP 
          | epsilon

    V ::= R VP 

    VP ::= and R VP
          | epsilon

    R ::= parent_i W parent_d
         | id PU
         | VAL

    LK ::= like VAL
          | epsilon

    DT ::= database id AL
          | table id FM

    AL ::= rename to id
      | owner to llave_abre id ORSIGNO current_user ORSIGNO session_user llave_cierre

    FM ::= add CL 
          | drop DP
          | alter column id set AR
          | rename column id to id 

    CL ::= column id id
          | check parent_i LOG parent_d
          | constraint id unique parent_i id parent_d
          | foreign key parent_i id parent_d references id

    DP ::= column id
          | constraint id

    AR ::= not null
           | null 

    DO ::= database IFE id
          | table id

    IFE ::= if exists
           | epsilon 
    
    OL ::= only id ICO ALI US WH RET
           | id ICO ALI US WH RET

    ICO ::= POR
           | epsilon 

    ALI ::= as id 
           | epsilon
    
    US ::= using L_ID
          | epsilon

    WH ::= where CD
          | epsilon

    CD ::= LOG
          | current of id 

    RET ::= RETURNING RS
           | epsilon

    RS ::= POR
          | LOG ALI

    ACT ::= L_ASIG where LOG

    L_ASIG ::= ASIG L_ASIGP

    L_ASIGP ::= coma ASIG L_ASIGP
               | epsilon

    ASIG ::= id igual VAL 
    
    PU ::= parent_i SE parent_d
          | epsilon 

    SE ::= L_ARG
          | epsilon

    L_ARG ::= ARG L_ARGP

    L_ARGP ::= coma ARG L_ARGP  
                | epsilon

# [Ascendente](https://github.com/markdown-it/markdown-it-container)

    SQL :: = SENTENCIAS_SQL
            |  EMPTY 

    SENTENCIAS_SQL :: = SENTENCIAS_SQL SENTENCIA_SQL
                        | SENTENCIA_SQL

    SENTENCIA_SQL :: = SENTENCIAS_DML
                    | SENTENCIAS_DDL

    SENTENCIAS_DML ::= SELECT_SQL pyc
                    | t_insert t_into id INSERT_SQL pyc
                    | t_update id t_set LISTA_EXP t_where EXP pyc
                    | t_delete t_from id CONDICIONES pyc
                    | t_use t_database id

    SELECT_SQL ::= t_select LISTA_EXP t_from TABLE_EXPRESSION CONDICIONES

    TABLE_EXPRESSION ::= ALIAS_TABLA
                        | SUBQUERIES

    ALIAS_TABLA ::=  LISTA_ID
                    |  LISTA_ALIAS 

    SUBQUERIES ::= par1 t_select  par2

    INSERT_SQL ::= par1 LISTA_ID par2 t_values par1 EXP par2
                    |  t_values par1 EXP par2

    CONDICIONES ::= t_where EXP
                    | empty

    SENTENCIAS_DML ::= SELECT_SQL pyc
                    | t_insert t_into id INSERT_SQL pyc
                    | t_update id t_set LISTA_EXP t_where EXP pyc
                    | t_delete t_from id DELETE_COND pyc
                    | t_use t_database id

    SELECT_SQL ::= t_select LISTA_ID t_from LISTA_ID CONDICIONES_SEL

    CONDICIONES_SEL ::= t_where
                        | t_having

    INSERT_SQL ::= par1 LISTA_ID par2 t_values par1 EXP par2
                    | t_values par1 EXP par2

    DELETE_Cond ::= t_where EXP
                    | empty

    SENTENCIAS_DDL ::= t_show t_databases SHOW_DB_LIKE_CHAR pyc
                        | ENUM_TYPE
                        | t_drop DROP pyc
                        | t_alter ALTER pyc 
                        | t_create CREATE pyc

    SHOW_DB_LIKE_CHAR ::= t_like char 
                        | empty

    ENUM_TYPE ::= t_create t_type id t_as t_enum par1 LISTA_ENUM par2 pyc

    DROP ::= t_database DROPDB id
                | t_table  id 

    DROPDB ::= t_if t_exists
                | empty

    ALTER ::= t_database id ALTERDB
                | t_table id ALTERTB 

    ALTERDB ::= t_rename t_to id
                    | t_owner t_to SESIONDB

    SESIONDB ::= id
                    | t_current_user
                    | t_session_user 

    ALTERTB ::= t_add ADD_OPC
                    | t_drop DROP_Opc
                    | t_alter t_column ALTER_COLUMN
                    | t_rename t_column id t_to id 

    ADD_OPC ::= t_column id TIPO
                | CONSTRAINT_ALTERTB t_foreign t_key par1 id par2 t_references id par1 Lista_ID par2
                | CONSTRAINT_ALTERTB t_unique par1 id par2
                | CONSTRAINT_ALTERTB t_check EXP 

    CONSTRAINT_ALTERTB ::=      t_constraint id
                                | EMPTY'''

    DROP_OPC ::=  t_column id
                    |  t_constraint id 

    ALTER_COLUMN ::=   id t_set t_not t_null
                        |   ALTER_COLUMNS

    ALTER_COLUMNS ::= ALTER_COLUMNS coma ALTER_COLUMN1
                        | ALTER_COLUMN1

    ALTER_COLUMN1 ::=  id t_type t_varchar par1 entero par2
                        | t_alter t_column id t_type t_varchar par1 entero par2

    CREATE ::= CREATEDB   
                | CREATETB

    CREATEDB ::= ORREPLACECREATEDB t_database IFNOTEXISTCREATEDB id SESION

    ORREPLACECREATEDB ::= t_or t_replace
                        | empty

    IFNOTEXISTCREATEDB ::=      t_if t_not t_exists
                                | empty

    SESION ::= t_owner OP_SESION SESION_MODE
                    | t_mode OP_MODE
                    | empty 

    OP_SESION ::= igual char
                | char 

    SESION_MODE ::= t_mode OP_MODE
                    | empty 

    OP_MODE ::= igual entero
                | entero

    CREATETB ::= t_table id par1 COLUMNAS par2 INHERITS 

    INHERITS  ::= INHERITS  par1 id par2
                | empty 

    COLUMNAS ::= COLUMNAS coma COLUMNA
                    | COLUMNA

    COLUMNA ::= id TIPO COND_CREATETB 
                    | CONSTRAINT

    COND_CREATETB ::= CONSTRAINT_CREATETB t_default id COND_CREATETB 
                        | CONSTRAINT_CREATETB t_not t_null COND_CREATETB 
                        | CONSTRAINT_CREATETB t_null COND_CREATETB 
                        | CONSTRAINT_CREATETB t_unique COND_CREATETB 
                        | CONSTRAINT_CREATETB t_check par1 EXP par2 COND_CREATETB 
                        | CONSTRAINT_CREATETB t_primary t_key COND_CREATETB 
                        | CONSTRAINT_CREATETB t_references id COND_CREATETB 
                        | empty

    CONSTRAINT_CREATETB ::= t_constraint id
                     | EMPTY

    CONSTRAINT ::= CONSTRAINT_CREATETB t_unique par1 LISTA_ID par2
                    | CONSTRAINT_CREATETB t_check par1 EXP par2
                    | CONSTRAINT_CREATETB t_primary t_key par1 LISTA_ID par2
                    | CONSTRAINT_CREATETB t_foreign t_key par1 LISTA_ID par2 t_references id par1 LISTA_ID par2
                    | empty 

    TIPO ::= t_smallint
                | t_integer 
                | t_bigint
                | t_decimal 
                | t_numeric 
                | t_real
                | t_double t_precision
                | t_money
                | t_character t_varying par1 Valor par2 
                | t_varchar par1 Valor par2
                | t_character par1 Valor par2
                | t_charn par1 Valor par2
                | t_text 
                | t_boolean 

    VALOR ::= decimal
                | entero
                | string
                | char 
                | t_true
                | t_false
                | id

    EMPTY ::= vacia

    EXP ::= EXP mas EXP
            | EXP menos EXP
            | EXP asterisco EXP
            | EXP div EXP
            | EXP pot EXP
            | EXP porcentaje EXP
            | par1 EXP par2

    EXP ::= EXP mayor EXP
            | EXP mayori EXP
            | EXP menor EXP
            | EXP menori EXP
            | EXP igual EXP
            | EXP diferente EXP
            | EXP diferentede EXP

    EXP ::= EXP t_and EXP
        | EXP t_or EXP

    EXP ::= mas EXP  %prec umas
            | menos EXP  %prec umenos
            | t_not EXP

    EXP ::= VALOR

    EXP ::=  t_avg par1 EXP par2
                | t_sum par1 EXP par2
                | t_count par1 EXP par2
                | t_max par1 EXP par2
                | t_min par1 EXP par2

    EXP ::= t_abs par1 EXP par2
                | t_cbrt par1 EXP par2
                | t_ceil par1 EXP par2
                | t_ceiling par1 EXP par2
                | t_degrees par1 EXP par2
                | t_div par1 EXP coma EXP par2
                | t_exp par1 EXP par2
                | t_factorial par1 EXP par2
                | t_floor par1 EXP par2
                | t_gcd par1 EXP coma EXP par2
                | t_ln par1 EXP par2
                | t_log par1 EXP par2
                | t_mod par1 EXP coma EXP par2
                | t_pi par1  par2
                | t_power par1 EXP coma EXP par2
                | t_radians par1 EXP par2 
                | t_round par1 EXP par2 
                | t_min_scale par1 EXP par2
                | t_scale par1 EXP par2
                | t_sign par1 EXP par2
                | t_sqrt par1 EXP par2 
                | t_trim_scale par1 EXP par2
                | t_trunc par1 EXP par2
                | t_width_bucket par1 Lista_EXP par2
                | t_random par1 par2
                | t_setseed par1 EXP par2

    EXP ::= t_acos par1 EXP par2
                | t_acosd par1 EXP par2
                | t_asin par1 EXP par2
                | t_asind par1 EXP par2
                | t_atan par1 EXP par2
                | t_atand par1 EXP par2
                | t_atan2 par1 EXP coma EXP par2
                | t_atan2d par1 EXP coma EXP par2
                | t_cos par1 EXP par2
                | t_cosd par1 EXP par2
                | t_cot par1 EXP par2
                | t_cotd par1 EXP par2
                | t_sin par1 EXP par2
                | t_sind par1 EXP par2
                | t_tan par1 EXP par2
                | t_tand par1 EXP par2 
                
    EXP ::= t_length par1 id par2 
                | t_substring par1 char coma integer coma integer par2
                | t_trim par1 char par2
                | t_md5 par1 char par2
                | t_sha256 par1 par2
                | t_substr par1 par2
                | t_get_byte par1 par2
                | t_set_byte par1 par2
                | t_convert par1 EXP t_as Tipo par2
                | t_encode par1 par2
                | t_decode par1 par2 

    LISTA_ID ::= LISTA_ID coma id
                | id 

    LISTA_ENUM ::= LISTA_ENUM coma char
                | char
            
    LISTA_EXP ::= LISTA_EXP coma EXP
                | EXP 

    LISTA_ALIAS ::= LISTA_AlIAS coma NOMBRE_ALIAS
                | NOMBRE_ALIAS

    NOMBRE_ALIAS ::= id id
