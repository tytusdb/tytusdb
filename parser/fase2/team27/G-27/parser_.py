from sys import path
from os.path import dirname as dir
#sys.path.append('../parser/team29')
path.append(dir(path[0]))
#from team29.analizer.interpreter import *
from analizer.interpreter import execution
class Parser(object):
  def __init__(self):
    ''' '''
  def parse(self,input):
    obj = execution(input)
    print(obj)
    return obj['querys']
    