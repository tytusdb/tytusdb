from analizer_pl.abstract import instruction


class AlterDataBase(instruction.Instruction):
    def __init__(self, option, name, newname, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.option = option  # define si se renombra o se cambia de dueño
        self.name = name  # define el nombre nuevo de la base de datos o el nuevo dueño
        self.newname = newname

    def execute(self, environment):
        pass
