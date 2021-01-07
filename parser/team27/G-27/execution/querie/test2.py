from execution.abstract.querie import * 
from select_ import *
from execution.symbol.environment import *
from execution.symbol.table import *
from execution.symbol.column import *
from execution.symbol.typ import *
from storageManager import jsonMode as admin
from create import *
from use import *
from create_t import *
from relational import *
from execution.expression.id import *
from execution.expression.literal import *
from insert import *
from main import *
from alter_table import *
from add_column import *
from drop_constraint import *
from alter_column import *
from execution.symbol.typeChecker.Database_Types import *
from avg import  * 
from count import *
from max import * 
from min import * 
from sum import *


'''CREATE OR REPLACE DATABASE tienda;

USE tienda;
CREATE TABLE persona (
    id INTEGER NOT NULL CONSTRAINT uq_persona UNIQUE CONSTRAINT ck_persona_id CHECK(id > -1),
    nombre VARCHAR(2) NOT NULL
);
INSERT INTO persona VALUES(1,'Jose Carlos');
INSERT INTO persona VALUES(1,'Juan Pedro');
INSERT INTO persona VALUES(2,'Cesar Emanuel');
INSERT INTO persona VALUES(3,'Rodolfo Rafael');'''


#select columna1 from tabla1
#where columna2 > 2

database = Create(True,0,'tienda',0,0)
objUse = Use('tienda',1,0)
tipo1={'type':DBType.numeric, 'length': -1, 'default':0 }
tipo2={'type':DBType.varchar, 'length': 20, 'default':0 }
tipo3={'type':DBType.varchar, 'length': 20, 'default':0 }
columna1 = Column('id',DBType.numeric,None,-1)
columna2 = Column('nombre',DBType.varchar,None,20)
columna3 = Column('sexo',DBType.varchar,'masculino',20)

restriccion1 = {'type':'not null','name':'nn_idpersona','value':'id'}
restriccion2 = {'type':'unique','name':'uq_persona','value':'id'}
literal1 = Literal(-1,Type.INT,1,2)
literal2 = Id('id',None,1,2)
cond = Relational(literal2,literal1,'>',1,3)
restriccion3 = {'type':'check','name':'ck_persona_id','value':cond}
restriccion4 = {'type':'not null','name':'nn_nombrepersona','value':'nombre'}
restriccion5 = {'type':'primary','name':'pk_persona','value':'id'}
arrRestriccion=[columna1,columna2,columna3,restriccion1,restriccion2,restriccion3,restriccion4,restriccion5]

objTable = Create_Table('persona',arrRestriccion,2,3)

valor1 = Literal(1,Type.INT,2,3)
valor2 = Literal('Jose Carlos',Type.STRING,2,3)
valor22 = Literal('masculino',Type.STRING,2,3)
valores = [valor1,valor2,valor22]
insert1 = Insert('persona',valores,None,4,3)


valor3 = Literal(2,Type.INT,2,3)
valor4 = Literal('Chepix Pedro',Type.STRING,2,3)
valor23 = Literal('femenino',Type.STRING,2,3)
valores2 = [valor4,valor3, valor23]
columnasval =['nombre','id','sexo']
insert2 = Insert('persona',valores2,columnasval,4,3)


valor5 = Literal(3,Type.INT,2,3)
valor6 = Literal('Juan Pedro',Type.STRING,2,3)
valor24 = Literal('femenino',Type.STRING,2,3)
valores3 = [valor5,valor6,valor24]
insert3 = Insert('persona',valores3,None,4,3)

colList = ['id', 'nombre','sexo']
tabList = ['persona']

idexp = Id('nombre', None, 3,4)
op2 = Id('sexo', Type.INT, 4,4)
where = Relational(idexp, op2, '<>', 5,4)
#count(sexo)
idCount = Id('sexo', None, 5,6)
count = Count(idCount)

expHav= Id('id', None, 3,5)
opxd = Literal(0, Type.INT, 4,12)
hav= Relational(expHav, opxd, '>=', 5,4)

select_ins = Select(False,colList,tabList,where,['sexo'],None,None,['id'],0,0)
#add column
'''tipoColumna={'type':Type.STRING, 'length':-1, 'default':'no tiene'}
add = Add_Column('apellido',tipoColumna,5,8)
alter = Alter_Table('persona',add,9,11)
 
SELECT id, nombre FROM persona WHERE id >= 2;

valor51 = Literal(4,Type.INT,2,3)
valor61 = Literal('cesar Garcia',Type.STRING,2,3)
valor21 = Literal('masculino',Type.STRING,2,3)
valor211 = Literal('juarez',Type.STRING,2,3)
colval2 =['nombre','id',]
valores31 = [valor61,valor51]
insert31 = Insert('persona',valores31,colval2,4,3)


#add column
drop = Drop_Column('nombre',5,8)
alter2 = Alter_Table('persona',drop,9,11)

valor58 = Literal(-2,Type.INT,2,3)
valor28 = Literal('femenino',Type.STRING,2,3)
valor288 = Literal('juarez',Type.STRING,2,3)
valores38 = [valor58,valor28,valor288]
insert38 = Insert('persona',valores38,None,4,3)

dropc = Drop_Constraint('ck_persona_id',5,2)
alter3 = Alter_Table('persona',dropc,5,6)

dropc2 = Alter_Column('nombre','SET NOT NULL',None,2,6)
alter4 = Alter_Table('persona',dropc2,5,6)

tr = {'type':Type.INT, 'length':3, 'default':0}
dropc3 = Alter_Column('apellido','TYPE',tr,2,6)
alter5 = Alter_Table('persona',dropc3,5,6)'''

instrucciones = [database,objUse,objTable,insert1,insert2,insert3,select_ins]


objMain = Main(instrucciones)
env = Environment(None)
objMain.execute(env)