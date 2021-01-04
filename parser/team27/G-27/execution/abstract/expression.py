class Expression(object):
    def __init__(self, row, column):
        """Constructor de la clase abstracta expression"""
        self.row = row
        self.column = column 

    def execute(self, environment):
        """Ejecutar

        Método abstracto el cual necesita implementarse según cada tipo de expression
        
        Args:
            environment(Environment): Entorno con la tabla de simbolos
        
        Returns:
            | Literal Number, String or Boolean
            | Tabla
            | Null
        """
        raise NotImplementedError
