import eel


eel.init('client')

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
