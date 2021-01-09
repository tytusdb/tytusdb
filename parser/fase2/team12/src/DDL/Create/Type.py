import json
import sys, os.path
import os


class Type():
    def __init__(self):
        self.nombre = None
        self.cadenas = []

    def execute(self, parent):
        self.nombre = parent.hijos[0].valor
        for hijo in parent.hijos[1].hijos:
            if not (hijo.valor in self.cadenas):
                self.cadenas.append(hijo.valor)
        
    