import sys
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
from environment import *

class Main(object):
    def __init__(self,queryArray):
        self.queryArray = queryArray

    
    def execute(self, environment):
        
        for item in self.queryArray:
            env = Environment(environment)
            print(item.execute(env))
        
            



