from goto import with_goto 
import C3D 

@with_goto  # Decorador necesario
def main():
    t1 = 5 < 9
    if t1 : goto .L1
    goto .L2

    label .L1
    C3D.eje_if = "Verdadero"
    C3D.pila = 0
    C3D.ejecutar() #Crear Base de datos

    goto .L3

    label .L2
    C3D.eje_if = "Else"
    C3D.pila = 0
    C3D.ejecutar() #Crear Base de datos

    label .L3
main()
