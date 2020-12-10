from Parser.Ascendente.gramatica import parser

if __name__ == '__main__':
	f = open("./entrada.txt", "r")
	input = f.read()
	print('====================ENTRADA====================')
	print(input)
	out:list = parser.parse(input)
	print('====================RESULT====================')
	print(out)