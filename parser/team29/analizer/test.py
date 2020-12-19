from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

from analizer import grammar

s = """ 
    use db1;
    /*create table tblibrosalario( 
    idempleado integer not null,
    aniocalculo integer CONSTRAINT aniosalario CHECK (aniocalculo > 0),
    mescalculo  integer CONSTRAINT mescalculo CHECK (mescalculo > 0 ),
    salariobase  money not null,
    comision decimal,
    primary key(idempleado)
    );
    insert into tblibrosalario values(4,2020,10,2500,6885);
    insert into tblibrosalario values(5,2020,10,2750,5370);
    
    
    */
    
    insert into tblibrosalario (salariobase,idempleado,mescalculo) values(3000,NULL,1);
    
"""


result = grammar.parse(s)
print(result)


