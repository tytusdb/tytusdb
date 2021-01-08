import sys, os.path


nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\AST\\')
sys.path.append(nodo_dir)

create_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\DDL\\Create')
sys.path.append(create_dir)

create_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\DDL\\Use')
sys.path.append(create_dir)

select_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\DML\\Select')
sys.path.append(select_path)

insert_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\DML\\INSERT')
sys.path.append(insert_path)

group_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\DML\\Groups')
sys.path.append(group_path)

update_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\DML\\UPDATE\\UPDATE')
sys.path.append(update_path)

alter_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\DML\\ALTER')
sys.path.append(alter_path)

procedure_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\PLSQL\\')
sys.path.append(procedure_path)



from Nodo import Nodo
from Database import Database
from Table import Table
from Use import Use
from Type import Type
from Select import Select
from InsertTable import InsertTable
from UnionAll import UnionAll
from Union import Union
from Intersect import Intersect
from Except import Except
from UpdateTable import UpdateTable
from AlterTable import AlterTable
from Procedure import Procedure
from Procedure import Procedure
from Index import Index
from Execute import Execute
