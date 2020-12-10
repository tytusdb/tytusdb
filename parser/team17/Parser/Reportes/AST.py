from graphviz import Graph


class Ast:
    """
    Esta clase permitirá la creación de un árbol AST mediante graphviz

    ...

    Atributos
    ----------
    i : int
    variable que servirá como índice para el ordenamiento de los nodos
    dot : any
    variable que generará la imagen png del dot creado

    Métodos
    -------
    inc()
    Incrementa el índice del nodo usando la variable i
    """

    def __init__(self):
        self.id = None
        self.i = 0
        self.dot = Graph('AST', format='png')
        self.dot.attr('node', shape='box')

    def inc(self):
        self.i += 1

    def graficar_drop(self, expresion):
        """Prints what the animals name is and what sound it makes.

                If the argument `sound` isn't passed in, the default Animal
                sound is used.

                Parameters
                ----------
                sound : str, optional
                    The sound the animal makes (default is None)

                Raises
                ------
                NotImplementedError
                    If no sound is set for the animal or passed in as a
                    parameter.
                """
        self.inc()
        self.dot.node(str(self.id), 'DROP')
        self.inc()
        self.dot.node(str(self.id), 'id')
        self.dot.edge(str(self.id - 1), str(self.id))
        self.inc()
        self.dot.node(str(self.id), str(expresion.id))
        self.dot.edge(str(self.id - 1), str(self.id))



