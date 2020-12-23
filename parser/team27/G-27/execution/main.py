import sys
from execution.symbol.environment import Environment

class Main(object):
    def __init__(self,queryArray):
        self.queryArray = queryArray

    
    def execute(self, environment):
        
        for item in self.queryArray:
            env = Environment(environment)
            print(item.execute(env))
        
            



