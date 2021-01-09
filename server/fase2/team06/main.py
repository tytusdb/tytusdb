import eel


import sys
sys.path.append('../G26/Instrucciones')
sys.path.append('../G26/Librerias')
sys.path.append('../G26/Utils')
sys.path.append('../G26')

import gramatica as g
import Instrucciones.DML.select as select
import Instrucciones.DDL.show as show
from storageManager import jsonMode as storage
import Lista as l
from Error import *

eel.init('client')
storage.dropAll()
datos = l.Lista({}, '')

@eel.expose
def analize(texto):
  global datos
  instrucciones = g.parse(texto)


  for instr in instrucciones['ast']:
    if instr != None:
      result = instr.execute(datos)
      if isinstance(result, Error):
        eel.printText(str(result))
        
      elif isinstance(instr, select.Select) or isinstance(instr, select.QuerysSelect):
        eel.addTable(str(instr.ImprimirTabla(result).get_html_string(format=True)))
        
      elif isinstance(instr, show.Show):
        eel.addTable(str(result.get_html_string(format=True)))
         
      else:
        eel.printText(str(result))
        
        #return str(result)
 
  errores = g.getMistakes()
  errores.clear()
  del instrucciones

@eel.expose
def PYejecutarScript():
  #el contenido del script se recibe y se guarda en la variable x par aluego ejecutarla
  texto="ejecutar query"
  print('Ejecutando query ')
  return texto



@eel.expose
def PYAbrirArchivo(x):
  #guardar la ruta del archivo en la variable x
  f = open (x,'r')
  mensaje = f.read()
  contenidoQuery=mensaje
  f.close()
  print('Query abierto')
  return contenidoQuery


@eel.expose
def PYguardarArchivo(x,y):
  #guardar la ruta del archivo en la variable x
  # guardar el contenido de un query en y
  # y luego se sobre escribe el archivo
  file = open(x, "w")
  file.write(y)
  file.close()
  print('Guardado')
  return y


@eel.expose
def PYcrearBD():
  contenidoBD="DB"
  print('Se ha creado la base de datos')
  return contenidoBD

@eel.expose
def PYcrearTabla():
  #se guarda el nombre de la tabla en la variable x
  contenidoTabla="tabla"
  print('Se ha creado la tabla')
  return contenidoTabla

eel.start('main.html', size=(1024, 768))

  #let input = document.querySelector("input[name='abrir']");
  #
#    let textarea = document.querySelector("textarea[name='query1']");
