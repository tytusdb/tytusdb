
from Fase1.Sql import Sql
from goto import with_goto

heap = None

def inter():
    global  heap
    sql:Sql = Sql()
    sql.run(heap)

if __name__ == '__main__':
	principal()
