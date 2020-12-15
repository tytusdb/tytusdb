SENTENCIA_CREAR             ::= 'CREATE' 'TYPE' identificador 'AS' 'ENUM' '(' LISTA_CADENAS ')' ';'
                                | 'CREATE' SENTENCIA_ORREPLACE 'DATABASE' SENTENCIA_IFNOTEXISTS id OPCIONALES_CREAR_DATABASE ';'
                                | 'CREATE' 'TABLE' id '(' CUERPO_CREAR_TABLA ')' ';'

CUERPO_CREAR_TABLA          ::= CUERPO_CREAR_TABLA ',' CUERPO_CREAR_TABLA_CONST
                                | CUERPO_CREAR_TABLA_CONST

CUERPO_CREAR_TABLA_CONST    ::=  id TIPO OPC_CREARTABLA_COLUMNA
                                | OPCIONAL_CONSTRAINT 'UNIQUE' LISTA_ID
                                | OPCIONAL_CONSTRAINT 'CHECK' '(' COMPARACIONES  ')'
                                | 'PRIMARY' 'KEY' '(' LISTA_ID ')' 
                                | 'FOREIGN' 'KEY' '(' LISTA     _ID ')' 'REFERENCES' '(' LISTA_ID ')'

LISTA_ID              ::= LISTA_ID ',' id
                                | id

OPC_CREARTABLA_COLUMNA      ::= OPC_CREARTABLA_COLUMNA 'DEFAULT' EXPRESION
                                | OPC_CREARTABLA_COLUMNA 'NOT' 'NULL' 
                                | OPC_CREARTABLA_COLUMNA 'NULL'
                                | OPC_CREARTABLA_COLUMNA OPCIONAL_CONSTRAINT 'UNIQUE'
                                | OPC_CREARTABLA_COLUMNA OPCIONAL_CONSTRAINT 'CHECK' '(' COMPARACIONES  ')'
                                | OPC_CREARTABLA_COLUMNA 'PRIMARY' 'KEY'
                                | OPC_CREARTABLA_COLUMNA 'REFERENCES' id
                                | 'DEFAULT' EXPRESION
                                | 'NOT' 'NULL' 
                                | 'NULL'
                                | OPCIONAL_CONSTRAINT 'UNIQUE'
                                | OPCIONAL_CONSTRAINT 'CHECK' '(' COMPARACIONES ')'
                                |

OPCIONAL_CONSTRAINT         ::= 'CONSTRAINT' id
                                |

SENTENCIA_ORREPLACE         ::= 'OR' 'REPLACE'
                                |

SENTENCIA_IFNOTEXISTS       ::= 'IF' 'NOT' 'EXISTS'
                                |

OPCIONALES_CREAR_DATABASE   ::= 'OWNER' OPCIONAL_COMPARAR id
                                | 'MODE' OPCIONAL_COMPARAR entero
                                |

OPCIONAL_COMPARAR           ::= '='
                                |

LISTA_CADENAS               ::= LISTA_CADENAS ',' cadena 
                                | cadena