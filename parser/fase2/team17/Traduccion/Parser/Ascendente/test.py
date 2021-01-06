import  traceback
from Parser.Ascendente.gramatica import parse
from Interprete.Arbol import Arbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos

if __name__ == '__main__':
	f = open("entrada.sql", "r")

	try:
		input = f.read()
		print('====================ENTRADAInicio====================')
		print(input)
		print('====================ENTRADAFIN====================')
		result:Arbol = parse(input)
		print('====================RESULT====================')
		print('Analisis Sintactico realizado con exito')

		entornoCero:Tabla_de_simbolos = Tabla_de_simbolos()
		entornoCero.NuevoAmbito()

		try:
			for item in result.instrucciones:
				item.execute(entornoCero, result)
		except:
			traceback.print_exc()
			print('Error En el analisis Semantico')


	except:
		print('Ocurrion un error en el analisis Sintactico')


