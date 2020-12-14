from abc import abstractmethod
from enum import Enum

class TYPE(Enum):
  NUMBER = 1
  STRING = 2
  BOOLEAN = 3
  

class Expresion:
  '''
    Esta clase representa una expresión
  '''
  @abstractmethod
  def execute(self):
    pass


class ExpresionUnaria(Expresion):
  '''
    Esta clase recibe un parametro de expresion 
    para realizar operaciones unarias
  '''
  def __init__(self, exp, operador):
      self.exp = exp
      self.operador = operador
      self.lineno = 0
  
  def execute(self):
    try: 
      if self.operador == '-': 
        value = self.exp.execute().value * -1
      else:
        value = self.exp.execute().value
      return Primitivos("Null", value)
    except TypeError:
      print("Error de tipos")
    except:
      print("Error desconocido")
      return Primitivos(None, None)

class ExpresionBinaria(Expresion):
  '''
    Esta clase recibe dos parametro de expresion 
    para realizar operaciones entre ellas
  '''
  def __init__(self, exp1, exp2, operador):
      self.exp1 = exp1
      self.exp2 = exp2
      self.operador = operador
      self.temp = exp1.temp + str(operador) + exp2.temp
      self.lineno = 0

  def execute(self):
    try:
      if self.operador == '+': 
        value = self.exp1.execute().value + self.exp2.execute().value
      elif self.operador == '-':
        value = self.exp1.execute().value - self.exp2.execute().value
      elif self.operador == '*':
        value = self.exp1.execute().value * self.exp2.execute().value
      elif self.operador == '/':
        value = self.exp1.execute().value / self.exp2.execute().value
      elif self.operador == '^':
        value = self.exp1.execute().value ** self.exp2.execute().value
      elif self.operador == '%':
        value = self.exp1.execute().value % self.exp2.execute().value
      else:
        value = self.exp1.execute().value + self.exp2.execute().value
      return Primitivos("None", value)
    except TypeError:
      print("Error de tipos")
    except:
      print("Error desconocido")
    return Primitivos(None, None)
    
class Primitivos(Expresion):
  '''
    Esta clase contiene los tipos primitivos de datos como STRING, INTEGER, DECIMAL
  '''
  def __init__(self, tipo, value):
      self.tipo = tipo
      self.value = value
      self.temp = str(value)
      self.lineno = 0
  
  def execute(self):
      return self

class NombreColumna(Expresion):
  '''
    Esta clase 
  '''
  def __init__(self, tabla, columna):
      self.tabla = tabla
      self.columna = columna
      self.lineno = 0