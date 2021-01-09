from goto import with_goto

@with_goto
def f():

    label .etiquete
    age = input("Edad: ")

    try:
        age = int(age)
        print('edad',age)
    except ValueError:
        goto .etiquete

if __name__ == '__main__':
    f()