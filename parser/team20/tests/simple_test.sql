CREATE DATABASE db1;
/*{"DB1": {}}*/
CREATE DATABASE IF NOT EXISTS db1;
/*{"DB1": {}}*/
CREATE DATABASE IF NOT EXISTS db2;
/*{"DB1": {}, "DB2": {}}*/
CREATE OR REPLACE DATABASE db1;
/*{"DB1": {}, "DB2": {}}*/
CREATE OR REPLACE DATABASE db1 MODE = 1;
/*{"DB1": {}, "DB2": {}}*/
CREATE OR REPLACE DATABASE db1 OWNER = user1;
/*{"DB1": {}, "DB2": {}}*/
--CREATE OR REPLACE DATABASE db3 MODE = 3 OWNER = user3; --Syntactic Error in OWNER
/*{"DB1": {}, "DB2": {}, "DB3": {}}*/
CREATE OR REPLACE DATABASE db3 OWNER = user3 MODE = 3;
/*{"DB1": {}, "DB2": {}, "DB3": {}}*/
CREATE OR REPLACE DATABASE db4 OWNER = user4 MODE = 4;
/*{"DB1": {}, "DB2": {}, "DB3": {}, "DB4": {}}*/

DROP DATABASE db2;
/*{"DB1": {}, "DB3": {}, "DB4": {}}*/
DROP DATABASE db2; --Semantic Error
/*{"DB1": {}, "DB3": {}, "DB4": {}}*/
DROP DATABASE IF EXISTS db2;
/*{"DB1": {}, "DB3": {}, "DB4": {}}*/
DROP DATABASE IF EXISTS db1;
/*{"DB3": {}, "DB4": {}}*/

CREATE DATABASE IF NOT EXISTS CUSTOMERS MODE 2;
USE CUSTOMERS;
CREATE TABLE USER (
    id INTEGER,
    id_ADDRESS INTEGER,
    first_name TEXT NULL DEFAULT "Default First Name",
    second_name TEXT,
    first_last_name TEXT,
    second_last_name TEXT,
    age INTEGER,
    CHECK ( age>=18 ),
    PRIMARY KEY (id)
);
CREATE TABLE ADDRESS (
    id INTEGER,
    country TEXT,
    department TEXT,
    PRIMARY KEY (id)
);
--{"DB3": {}, "DB4": {}, "CUSTOMERS": {"USER": {"NCOL": 7}, "ADDRESS": {"NCOL": 3}}}

INSERT INTO ADDRESS VALUES (0, 'Guatemala', "Guatemala");
INSERT INTO ADDRESS VALUES (0, 'Guatemala', "Guatemala"); --Semantic Error
INSERT INTO ADDRESS VALUES (1, 'Guatemala'); --Semantic Error
INSERT INTO ADDRESS VALUES (2, 'Guatemala', "Guatemala", "Extra"); --Semantic Error
INSERT INTO ADDRESS VALUES ("Primary Key", "Guatemala", "Extra"); --Semantic Error

INSERT INTO LOCATION VALUES (0, 'Guatemala', "Petén"); --Semantic Error

INSERT INTO USER VALUES (0, 0, "First Name", "Second Name", "First Last Name", "Second Last Name", 25);
INSERT INTO USER VALUES (0, 0, "First Name", "Second Name", "First Last Name", "Second Last Name", 15); --Semantic Error