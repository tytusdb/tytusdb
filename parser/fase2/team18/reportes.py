
textocss = '''
body{ background-color: #632432; font-family: Arial;} 
#main-container{ margin: 150px auto; width: 600px;}
table{ background-color: white; text-align: left; border-collapse: collapse; width: 100%;}
th, td{padding: 20px;}
thead{background-color: #246355;border-bottom: solid 5px #0F362D; color: white;}
tr:nth-child(even){ background-color: #ddd;}
tr:hover td{background-color: #369681;color: white;}
'''

def Reporte_Errores(lexicos,sintacticos):
    texto = '''
    <!DOCTYPE html>
    <html lang=\"es\">
    <head><meta charset=\"UTF-8\">  <title> Reporte de Errores </title> 
    <style type=\"text/css\"> \n'''
    texto += textocss
    texto += '''</style> </head> </body>
    <div id=\"main-container\">
    <table> <thead> <tr>
    <th>#</th>
    <th>Listado de Errores</th>
    </tr> </thead>
    '''
    contador = 1
    for i in lexicos:
        try: 
            texto += '<tr><td> '+ str(contador)+ '</td>' 
            texto += '<td> '+ i + '</td></tr>'
            contador = contador+1
        except Exception as e:
            print("Error al generar reporte de errores lexicos "+ str(e))
    
    for i in sintacticos:
        try:
            texto += '<tr><td> '+ str(contador)+ '</td>' 
            texto += '<td> '+ i + '</td></tr>'
        except Exception as e:
            print("Error al generar reporte de errores sintacticos " + str(e))
    
    texto += "</table> </div> </body> </html>"
    try:
        with open('Reporte_Errores.html','w') as rep:
            rep.write(texto)
    except Exception as e:
        print("No fue posible generar el reporte: "+ str(e))
    
    return texto


def Reporte_Errores_Sem(semanticos):
    texto = '''
    <!DOCTYPE html>
    <html lang=\"es\">
    <head><meta charset=\"UTF-8\">  <title> Reporte de Errores Semanticos </title> 
    <style type=\"text/css\"> \n'''
    texto += textocss
    texto += '''</style> </head> </body>
    <div id=\"main-container\">
    <table> <thead> <tr>
    <th>#</th>
    <th>Listado de Errores</th>
    </tr> </thead>
    '''
    contador = 1
    for i in semanticos:
        try: 
            texto += '<tr><td> '+ str(contador)+ '</td>' 
            texto += '<td> '+ i + '</td></tr>'
            contador = contador+1
        except Exception as e:
            print("Error al generar reporte de errores semanticos "+ str(e))
      
    texto += "</table> </div> </body> </html>"
    try:
        with open('Reporte_Errores_Sem.html','w') as rep:
            rep.write(texto)
    except Exception as e:
        print("No fue posible generar el reporte: "+ str(e))
    
    return texto


def ReporteTS():
    texto = '''
    <!DOCTYPE html>
    <html lang=\"es\">
    <head><meta charset=\"UTF-8\">  <title> Reporte Tabla de simbolos </title> 
    <style type=\"text/css\"> \n'''
    texto += textocss
    texto += '''</style> </head> </body>
    <div id=\"main-container\">
    <table> <thead> <tr>
    <th>#</th>
    <th>Tabla de simbolos</th>
    </tr> </thead>
    '''

    try:
        with open('Reporte_TS.html','w') as rep:
            rep.write(texto)
    except Exception as e:
        print("No fue posible generar el reporte de TS: "+ str(e))
    return texto