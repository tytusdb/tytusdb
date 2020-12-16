import sys, os.path


nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\AST\\')
sys.path.append(nodo_dir)

create_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\DDL\\Create')
sys.path.append(create_dir)

create_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\DDL\\Use')
sys.path.append(create_dir)

from Nodo import Nodo
from Database import Database
from Use import Use
