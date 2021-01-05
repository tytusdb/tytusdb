from environment import *

"""
Clase enum DBType:
_____________________________________________________________
Necesaria para tener un fácil acceso a los tipos definidos para una base de datos.
"""
from enum import Enum
class DBType(Enum):
    smallint = 0
    integer = 1
    bigint = 2
    decimal = 3
    numeric = 4
    real = 5
    double_precision = 6
    money = 7
    ch_varying = 8
    varchar=9
    character = 10
    char = 11
    text = 12
    timestamp_wtz = 13
    timestamp_tz = 14
    date = 15
    time_wtz = 16
    time_tz = 17
    interval = 18
    boolean =  19
"""
Diccionario Tipos:
_____________________________________________________________
Este proporciona un acceso rápido a el valor que debe de tener por default una variable no inicializada
ya que Python no permite declarar variables vacías.
"""
tipos = {
      DBType.smallint: 0,
      DBType.integer: 0,
      DBType.bigint: 0,
      DBType.decimal: 0,
      DBType.numeric: 0,
      DBType.real: 0,
      DBType.double_precision: 0,
      DBType.money: 0,
      DBType.ch_varying: "\"\"",
      DBType.varchar: "\"\"",
      DBType.character: "\"\"",
      DBType.char: "\"\"",
      DBType.text: "\"\"",
      DBType.timestamp_tz: "\"1900-01-01 00:00:00\"",
      DBType.timestamp_wtz: "\"1900-01-01 00:00:00\"",
      DBType.date: "\"1900-01-01 00:00:00\"",
      DBType.time_wtz: "\"1900-01-01 00:00:00\"",
      DBType.time_tz: "\"1900-01-01 00:00:00\"",
      DBType.interval: "\"1900-01-01 00:00:00\"",
      DBType.boolean: True
}

"""
Método declare:
_____________________________________________________________
Genera el código 3D de una declaración de variables.
id: Identificador de la variable
tipo: Enum DBType que especifica el tipo de la variable.
Valor: Expresion que se asigna a la variable, si no se cuenta con el se envía None.
"""
def declare(identificador, tipo, valor):
      temporal = getTemp()
      temporales[identificador] = temporal
      id = temporal
      if valor != None:          
            if isinstance(valor, str):
                  return id + '=' + valor + '\n'
            return id + '=' + str(valor) + '\n'
      default = tipos[tipo]
      if isinstance(default, str):
            return id + '=' + default + '\n'
      return id + '=' + str(default) + '\n'

"""
______________________________________________________________
Genera el código 3D para la asignación de un valor a una variable ya existente.
identificador: id de la variable buscada
valor: Valor que se le dará, debe de ser un string       
"""
def assign(identificador, valor):
      id = temporales[identificador]
      if isinstance(valor,str):
            return id + '='  + valor +'\n'

"""
______________________________________________________________
Genera un temporal nuevo en forma de string.
"""
def getTemp():
      global tempCount
      id =  'T' + str(tempCount)
      tempCount += 1
      return id
"""
______________________________________________________________
Traduce una expresión en forma de diccionario con las llaves:
-left, right y data
En donde left y right son diccionarios y data es el operador.
"""
def traduct(raiz):
      if(raiz != None):
            l = None
            r = None
            if  isinstance( raiz, dict):
                  valoriz = raiz['left']
                  valorder = raiz['right']
                  if valoriz != None:
                        if 'c3d' in valoriz:
                              l = raiz['left']
                        elif(raiz['left']):
                              l = traduct(raiz['left'])
                  if valorder != None:
                        if 'c3d' in valorder:
                              r = raiz['right']
                        elif(raiz['right']):
                              r = traduct(raiz['right'])
                  data = raiz['data']
                  value = {}

                  if(data == '+'):#suma
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + r['c3d'] + temp + '=' + l['temp'] + '+' + r['temp'] + '\n'
                        value['temp'] = temp
                  elif(data == '-'):#resta
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + r['c3d'] + temp + '=' + l['temp'] + '-' + r['temp'] + '\n'
                        value['temp'] = temp
                  elif(data == '*'):#multiplicacion
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + r['c3d'] + temp + '=' + l['temp'] + '*' + r['temp'] + '\n'
                        value['temp'] = temp
                  elif(data == '/'):#division
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + r['c3d'] + temp + '=' + l['temp'] + '/' + r['temp'] + '\n'
                        value['temp'] = temp
                  elif(data == '%'):#modulo
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + r['c3d'] + temp + '=' + l['temp'] + '%' + r['temp'] + '\n'
                        value['temp'] = temp
                  elif(data == '^'):#potencia
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + r['c3d'] + temp + '=' + l['temp'] + '**' + r['temp'] + '\n'
                        value['temp'] = temp
                  elif(data == '<'):#menor
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + r['c3d'] + temp + '=' + l['temp'] + '<' + r['temp'] + '\n'
                        value['temp'] = temp
                  elif(data == '>'):#mayor
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + r['c3d'] + temp + '=' + l['temp'] + '>' + r['temp'] + '\n'
                        value['temp'] = temp
                  elif(data == '<='):#menor o igual
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + r['c3d'] + temp + '=' + l['temp'] + '<=' + r['temp'] + '\n'
                        value['temp'] = temp
                  elif(data == '>='):#mayor o igual
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + r['c3d'] + temp + '=' + l['temp'] + '>=' + r['temp'] + '\n'
                        value['temp'] = temp
                  elif(data == '='):#igual
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + r['c3d'] + temp + '=' + l['temp'] + '==' + r['temp'] + '\n'
                        value['temp'] = temp
                  elif(data == '!='):#No igual
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + r['c3d'] + temp + '=' + l['temp'] + '!=' + r['temp'] + '\n'
                        value['temp'] = temp
                  elif(data == '<>'):#Diferente
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + r['c3d'] + temp + '=' + l['temp'] + '!=' + r['temp'] + '\n'
                        value['temp'] = temp
                  elif(data == 'OR'):#or
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + r['c3d'] + temp + '=' + l['temp'] + ' or ' + r['temp'] + '\n'
                        value['temp'] = temp
                  elif(data == 'AND'):#and
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + r['c3d'] + temp + '=' + l['temp'] + ' and ' + r['temp'] + '\n'
                        value['temp'] = temp
                  elif(data == 'NOT'):#not
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + temp + '= not ' + l['temp'] + '\n'
                        value['temp'] = temp
                  elif(data == '||'):#concatenation
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + r['c3d'] + temp + '=' + l['temp'] + ' + ' + r['temp'] + '\n'
                        value['temp'] = temp
                  elif(data == '&'):#bitwise and
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + r['c3d'] + temp + '=' + l['temp'] + ' & ' + r['temp'] + '\n'
                        value['temp'] = temp
                  elif(data == '|'):#bitwise or
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + r['c3d'] + temp + '=' + l['temp'] + ' | ' + r['temp'] + '\n'
                        value['temp'] = temp
                  elif(data == '#'):#bitwise xor
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + r['c3d'] + temp + '=' + l['temp'] + ' # ' + r['temp'] + '\n'
                        value['temp'] = temp
                  elif(data == '~'):#bitwise not
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + temp + '= ~' + l['temp'] + '\n'
                        value['temp'] = temp
                  elif(data == '<<'):#bitwise shift left
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + r['c3d'] + temp + '=' + l['temp'] + ' << ' + r['temp'] + '\n'
                        value['temp'] = temp
                  elif(data == '>>'):#bitwise shift right
                        temp = getTemp()
                        value['c3d'] = l['c3d'] + r['c3d'] + temp + '=' + l['temp'] + ' >> ' + r['temp'] + '\n'
                        value['temp'] = temp
                  else:
                        value['c3d'] = ""
                        if isinstance(data, str):
                              temporal = data
                              if data in temporales:
                                    temporal = temporales[data]
                              value['temp'] = temporal
                        else:
                              value['temp'] = str(data)
                  return value

"""
______________________________________________________________

"""
def funcion(diccionarioFuncion, codigo3D):
      arregloFunciones.append(diccionarioFuncion) #Agrego a la metadata general de las funciones.      
      id = diccionarioFuncion['id']
      codigoGenerado = "def " + id + '('
      for v in diccionarioFuncion['parametros']:
            codigoGenerado += v + ','
      codigoGenerado = codigoGenerado[:-1]
      codigoGenerado += '):\n'
      codigo3D = '\n' +  codigo3D
      codigo3D = codigo3D.replace('\n', '\n\t')
      codigo3D = codigo3D[:-1]
      return codigoGenerado +"\t#ZONA DE DECLARE"+ codigo3D
"""
______________________________________________________________

"""
def call(id, listaParámetros):
      c3d = ""
      paramsTemp = []
      for v in listaParámetros:
            aux = traduct(v)
            paramsTemp.append(aux['temp'])
            c3d += aux['c3d']
      temporal = getTemp()
      c3d += temporal + '=' + id + '('
      for temp in paramsTemp:
            c3d += temp + ','
      c3d = c3d[:-1]
      c3d += ')\n'
      return {'c3d':c3d,'temp':temporal}
