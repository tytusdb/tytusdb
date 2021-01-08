from Parser.Reportes.Nodo1 import Nodo


class TourTree:

	def __init__(self):
		self.id:int=1
		self.result:str = ''

		#self.dot = Digraph(

		#	comment='Arbol Ast', engine='dot', format='svg',
		#	graph_attr={'rankdir': 'LR'},  # 'splines': 'ortho',
		#	node_attr={'shape': 'plaintext','fillcolor':'green'},
		#	edge_attr={'color': 'maroon', 'arrowsize': '.5', 'weight': '2.'},
		#)

		#self.directory = "ReporteGrafo"
		#self.basedir = Path(__file__).resolve().parent.parent

	def getDot(self,node:Nodo):
		self.result = ''
		self.result += "digraph G {"
		self.tour(node)
		self.result += "}"
		return self.result


	def tour(self,nodo:Nodo):

		if nodo.valor!=None:
			#para los id
			if nodo.id == 0:
				nodo.id = self.id
				self.id+=1


			print(nodo.valor)
			self.result += str(nodo.id)+'[label= "' +str(nodo.valor)+'" fillcolor="#d62728"];\n'

			#self.dot.node(nodo.id,label=str(nodo.valor))

			for hijo in nodo.hijos:
				self.result+=str(nodo.id)+'->'+str(self.id)+';'
				#self.dot.edge(str(nodo.id),str(self.id))
				self.tour(hijo)


	def render(self):

		#direccion = os.path.join(self.basedir, self.directory) + "/Pert.gv"
		direccion = self.basedir
		print(direccion)
		print(self.basedir)
		self.dot.render(direccion, view=True)

