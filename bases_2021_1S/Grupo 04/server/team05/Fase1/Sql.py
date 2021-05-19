from Fase1.analizer import interpreter
from prettytable import PrettyTable


class Sql:

	def __init__(self):
		self.lexicalErrors = list()
		self.syntacticErrors = list()
		self.semanticErrors = list()
		self.postgreSQL = list()
		self.ts = list()
		self.console = ''
		self.table:PrettyTable = PrettyTable()

	def fill_table(self, columns, rows):
		self.table.field_names = columns
		self.table.add_rows(rows)
		self.console+=self.table.get_string()
		self.console+='\n'

	def show_result(self, consults):
		if consults != None:
			for consult in consults:
				if consult != None:
					self.fill_table(consult[0], consult[1] )
				else:
					self.console+="Error: Consulta sin resultado\n"

	def refresh(self):
		self.table =PrettyTable()
		self.console=''
		self.semanticErrors.clear()
		self.syntacticErrors.clear()
		self.lexicalErrors.clear()
		self.postgreSQL.clear()
		self.ts.clear()

	def analize(self,entrada):
		self.refresh()

		result = interpreter.execution(entrada)
		self.lexicalErrors = result["lexical"]
		self.syntacticErrors = result["syntax"]
		self.semanticErrors = result["semantic"]
		self.postgreSQL = result["postgres"]
		self.ts = result["symbols"]
		if (
				len(self.lexicalErrors)
				+ len(self.syntacticErrors)
				+ len(self.semanticErrors)
				+ len(self.postgreSQL)
				> 0
		):
			#print('La consulta contiene errores')

			if len(self.postgreSQL) > 0:
				i = 0
				self.console+= '-----------ERRORS----------\n'
				while i < len(self.postgreSQL):
					self.console+=self.postgreSQL[i] + "\n"
					i += 1

		messages = result["messages"]
		if len(messages) > 0:
			i = 0
			self.console+='-----------MESSAGES----------\n'
			while i < len(messages):
				if messages[i] != None:
					self.console+=str(messages[i]) + "\n"
				i += 1

		self.console += '--------------QUERYS----------------\n'
		querys = result["querys"]
		self.show_result(querys)

	def parse(self, input):
		self.refresh()
		# variable de almacenamiento de la entrada
		result = interpreter.parser(input)
		if len(result["lexical"]) + len(result["syntax"]) != 0:
			self.lexicalErrors = result["lexical"]
			self.syntacticErrors = result["syntax"]
			print('La consulta contiene errores')


	def run(self, input):
		self.parse(input)
		self.analize(input)
		print(self.console)



if __name__ == '__main__':
	f = open("entrada.txt", "r")
	input = f.read()
	sql:Sql = Sql()
	sql.run(input)









