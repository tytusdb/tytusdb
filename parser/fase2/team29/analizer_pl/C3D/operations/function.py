from analizer_pl.abstract.expression import Expression
from analizer_pl.statement.expressions import code

class FunctionDeclaration(Expression):

	def __init__(self, id, params, returns, row, column) -> None:
		super().__init__(row, column)
		self.id = id
		self.params = params
		self.returns = returns

	def execute(self, environment):
		if self.params:
			for p in self.params:
				p.execute(environment)
		#TODO: Codigo 3d
		return code.C3D(self.id+"\n", self.id, self.row, self.column)