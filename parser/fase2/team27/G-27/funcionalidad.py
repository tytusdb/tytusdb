from environment import *

fp = {
      'FUNCTION':'LA FUNCION',
      'PROCEDURE': 'EL PROCEDIMIENTO'
}

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
      default = tipos.get(tipo,'None')
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
Genera una etiqueta nuevo en forma de string.
"""
def getLabel():
      global labelCount
      id =  'L' + str(labelCount)
      labelCount += 1
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
                        elif isinstance(data,dict):
                              value = data
                        else:
                              value['temp'] = str(data)
                  return value

"""
______________________________________________________________

"""
def funcion(diccionarioFuncion, codigo3D):
      arregloFunciones.append(diccionarioFuncion) #Agrego a la metadata general de las funciones.      
      id = diccionarioFuncion['id']
      codigoGenerado = '@with_goto\n'
      codigoGenerado += "def " + id + '('
      for v in diccionarioFuncion['parametros']:
            codigoGenerado += v + ','
      if codigoGenerado[len(codigoGenerado)-1] == ',':
            codigoGenerado = codigoGenerado[:-1]
      codigoGenerado += '):\n'
      codigo3D = '\n' +  codigo3D
      codigo3D = codigo3D.replace('\n', '\n\t')
      codigo3D = codigo3D[:-1]
      temporales.clear()
      return codigoGenerado +"\t#INICIA DECLARE"+ codigo3D
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
      if c3d[len(c3d)-1] == ',':
            c3d = c3d[:-1]
      c3d += ')\n'
      retorno = {'c3d':c3d,'temp':temporal}
      return retorno

"""
______________________________________________________________

"""
def callNative(id, listaParámetros):

      c3d = ""
      paramsTemp = []
      for v in listaParámetros:
            aux = traduct(v)
            paramsTemp.append(aux['temp'])
            c3d += aux['c3d']
      temporal = getTemp()
      c3d += temporal + '=' + str(get_lower(id)) + '('
      for temp in paramsTemp:
            c3d += temp + ','
      c3d = c3d[:-1]
      c3d += ')\n'
      return {'c3d':c3d,'temp':temporal}


"""
______________________________________________________________

"""
def returnF (exp):
      ret = traduct(exp)
      res = ret['c3d'] + '\nreturn ' + ret['temp'] + '\n'
      return res

"""
______________________________________________________________

"""
def assignQ(identificador,valor):
      id = temporales[identificador]
      if isinstance(valor,str):
            return '\n' +id + '= parser.parse( \''  + valor +'\')\n'
"""
______________________________________________________________

"""


def resFinal(funciones, codigo):
      resultado = 'from goto import with_goto\nfrom parser_ import Parser\nfrom libraries.bstring_functions import *\n'
      resultado += 'from libraries.datetime_functions import *\nfrom libraries.math_functions import *\nfrom libraries.trigonometric_functions import *\n\n' 
      resultado += 'parser = Parser()\n'
      for f in funciones:
            resultado += f +'\n'
      resultado += codigo 
      funciones = []
      return resultado  


"""
DICCIONARIO PARA LOS METODOS
______________________________________________________________

"""
dict_Func = {
      'LENGTH':'length',
      'SUBSTRING':'substring',
      'TRIM':'trim',
      'MD5':'md5',
      'SHA256':'sha256',
      'SUBSTR':'substr',
      'GET_BYTE':'get_byte',
      'SET_BYTE':'set_byte',
      'CONVERT':'convert',
      'DECODE':'decode',
      'ENCODE':'encode',
      'NOW':'now',
      'EXTRACT':'extract',
      'DATE_PART':'date_part',
      'CURRENT_DATE':'current_date',
      'CURRENT_TIME':'current_time',
      'ABSOLUTE':'absolute',
      'CBRT':'cbrt',
      'CEIL':'ceil',
      'CEILING':'ceiling',
      'DEGREES':'degrees',
      'DIV':'div',
      'EXP':'exp',
      'FACTORIAL':'factorial',
      'FLOOR':'floor',
      'GCD':'gcd',
      'LN':'ln',
      'LOG':'log',
      'PI':'pi',
      'POWER':'power',
      'RADIANS':'radians',
      'SIGN':'sign',
      'SQRT':'sqrt',
      'TRUNC':'trunc',
      'RANDOM':'random',
      'ACOS':'acos',
      'ACOSD':'acosd',
      'ASIN':'asin',
      'ASIND':'asind',
      'ATAN':'atan',
      'ATAND':'atand',
      'ATAN2':'atan2',
      'ATAN2D':'atan2d',
      'COS':'cos',
      'COSD':'cosd',
      'COT':'cot',
      'COTD':'cotd',
      'SIN':'sin',
      'SIND':'sind',
      'TAN':'tan',
      'TAND':'tand',
      'SINH':'sinh',
      'COSH':'cosh',
      'TANH':'tanh',
      'ASINH':'asinh',
      'ACOSH':'acosh',
      'ATANH':'atanh',
      'ABS':'abs'
}


"""
DICCIONARIO PARA LOS METODOS
______________________________________________________________
funcion para castear un strig de mayusculas a minusculas
"""

def get_lower(name_func):
     return dict_Func.get(name_func, name_func)

"""
______________________________________________________________

"""
def deleteProcFunc(tipo, id, ListaFunciones):
      for v in arregloFunciones:
            if v['tipo'] == tipo and v['id'] == id:                          
                  v['estado'] = 'ELIMINADO'
                  return 'del '+ id
      return ''



"""______________________________________________________________

"""
def AddTs(id, tipo, operacion):
      #else variable .-      if id in temporales:
      if id in temporales:
            variable = {'id':id, 'tipo':tipo, 'temporal': temporales[id],'operacion':operacion}
      else:
            variable = {'id':id, 'tipo':tipo, 'temporal': 'None','operacion':operacion}
      funcionAux.append(variable)


"""
_______________________________________________________________
"""
def modifyTs(id,valor, operacion):
      encontrada = {}
      for i in range(len(funcionAux)):
            if id == funcionAux[i]['id']:
                  encontrada['id'] = funcionAux[i]['id']
                  encontrada['tipo'] = funcionAux[i]['tipo']
                  encontrada['temporal'] = valor
                  encontrada['operacion'] = operacion
                  funcionAux.append(encontrada)
                  break

"""
_______________________________________________________________
"""
def genTable(functionId):
      aux = []
      for v in funcionAux:
            aux.append(v)
      arregloF.append({'id':functionId,'valor':aux})
      funcionAux.clear()
