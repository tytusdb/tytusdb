from graphviz import Graph
from Interprete.SELECT.select import select


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
    ins: list
    variable que simulará el funcionamiento de una pila para almacenar los tokens

    Métodos
    -------
    inc()
    Incrementa el índice del nodo usando la variable i
    """

    def __init__(self, ins_):
        self.id = None
        self.i = 0
        self.dot = Graph('AST', format='png')
        self.dot.attr('node', shape='box')
        self.ins = [";", "usuario", "from", "nombre", "select"]


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

    def graficar_select(self, ins_):
        self.inc()
        self.dot.node(str(self.id), 'CONSULTA: SELECT')
        self.inc()

    def graficar_ast(self):
        padre = self.id
        self.dot.node(str(self.id), 'INICIO')
        for i in range(0, len(self.ins)):
            self.inc()
            self.dot.edge(str(padre), str(self.id + 1))
            if isinstance(self.ins[i], select):
                self.graficar_select(self.ins[i])
        self.dot.view()





