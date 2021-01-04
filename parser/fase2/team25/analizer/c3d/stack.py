"""
es una pila
"""
class Stack:
    def __init__(self):
        self.pila = list()

    def push(self , objeto):
        self.pila.append(objeto)

    def pop(self):
        return self.pila.pop()
