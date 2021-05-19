from ui import PantallaPrincipal

def main():  # Funcion main
    queryTool = PantallaPrincipal.Pantalla2()
    res = queryTool.MetodoParser(str)
    print(res)
    return 0


if __name__ == "__main__":
    main()