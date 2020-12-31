from goto import with_goto
from sintactico import ejecutar_analisis
from Instrucciones.TablaSimbolos.Tabla import Tabla
from Instrucciones.TablaSimbolos.Arbol import Arbol

display = []

tablaGlobal = Tabla()
arbol = Arbol()

display[0] = tablaGlobal
display[1] = arbol

def funcionintermedia():
    t2 = 0
    t3 = heap[t2]
    # Análisis sintactico
    inst = sintactico.ejecutar_analisis(t3)
    t4 = 0
    t5 = display[t4]
    t6 = 1
    t7 = display[t6]
    # Ejecución
    inst.ejecutar(t5,t6)


'''




'''


@with_goto
def main()
    
    # USE ID;

    t0 = "select * from table1"
    t1 = 0
    heap[t1] = t0
    funcionintermedia()

if _name_ == "_main_":
    main()





