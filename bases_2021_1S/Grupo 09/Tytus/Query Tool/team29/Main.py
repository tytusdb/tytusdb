from team29.ui.PantallaPrincipal import Pantalla

CO = Pantalla()

# region Metodos

# Crear Base De Datos
def Parsear(entrada: str) -> list:
    return CO.parse(entrada)
	
# Mostrar Bases De Datos
def Analizar(entrada: str) -> list:
    return CO.analize(entrada)
	
# endregion