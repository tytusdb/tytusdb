class prueba():
    def suma(n1,n2):
        return n1+n2
    
    print(suma(1,1))

    del suma

    print(suma(1,1))

    def suma(n1,n2):
        return n1 + n2 + 1

    print(suma(1,1))