from abc import ABC, abstractmethod
from Interpreter.node import Node


class Instruction(Node):
    def execute(self, env):
        pass
