from analizer.abstract.expression import Expression
from analizer.abstract.expression import TYPE
from analizer.statement.expressions import code
from analizer.abstract.environment import Environment

class Block(Expression):
	def __init__(self, function, declaration, blocks, exception, label, row, column) -> None:
		super().__init__(row, column)
		self.function = function
		self.declaration = declaration
		self. blocks = blocks
		self.exception = exception
		self.label = label

	def execute(self, environment):
		newEnv = Environment()
		decl = ""
		bl = ""
		for d in self.declaration:
			decl += d.execute(newEnv).value
		for b in self.blocks:
			bl += b.execute(newEnv).value
		return code.C3D(decl+bl, "block", self.row, self.column)