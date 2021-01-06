from sentencias import *
from goto import with_goto
@with_goto  # Decorador necesario.

def main():
   t0='DBFASE2'
   t1= createDB(t0)
   



   t0='DBFASE2'
   t1='TBPRODUCTO'
   t2=4
   t3= createTbl(t0,t1,t2)
   
   
main()
