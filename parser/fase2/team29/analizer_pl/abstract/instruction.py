from abc import abstractmethod


class Instruction:
    """
    Esta clase representa una instrucción
    """

    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column

    @abstractmethod
    def execute(self, environment):
        """
        Metodo que servira para ejecutar las instrucciones
        """
