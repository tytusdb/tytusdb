from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

from analizer import grammar

s = """ 
    /*
    USE DATABASE db1;
    CREATE TYPE if not exists mood AS ENUM ('sad', 'ok', 'happy');
    CREATE TABLE IF NOT EXISTS Persona2( 
        Dpi bigint not null primary key,
        Nombre varchar(20),
        fecha Date,
        estado mood not null primary key,
        Dpi2 bigint,
        Foreign key (Dpi2) references Persona (Dpi)
    );
    
    INSERT INTO Persona VALUES (22, "Estela Pérez", "2000-03-29 10:28:30", "xd",0);
    */
    SELECT 3+3;
"""


result = grammar.parse(s)
print(result)
