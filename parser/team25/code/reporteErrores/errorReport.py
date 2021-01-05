
class ErrorReport:
    """
    ATTRIBUTES:
    - line : number
    - description : string
    - type : string
    """
    def __init__(self, type , description , line):
        self.type = type
        self.description = description
        self.line = int(line)
        
    


class ListError:
    """
    ATTRIBUTES:
    - listaErrores : List
    """
    def __init__(self):
        self.listErrors = []
    
    def clear(self):
        self.listErrors = []
    
    def addError(self,error):
        self.listErrors.append(error)
    
    def generateReport(self):
        archivo = open('data/Reportes/reporteErrores.html' ,'w')# w es escritura, si no existe lo crea
        # HEAD
        archivo.write('<!DOCTYPE html> '+"\n")
        archivo.write('<html lang=\"en\">'+"\n")
        archivo.write("<head> " + "\n")
        archivo.write("<meta charset=\"UTF - 8\">" + "\n")
        archivo.write("<title>LISTA DE TOKENS</title>" + "\n")
        archivo.write("</head>" + "\n")
        # STYLE 
        archivo.write("\n"+"""
        <style>
        table{
        color : white;
        border-width: 5px;
        align-content: center;
        }
        th{
        text-align: center;
        font-size: 40px;
        background-color: black;
        }
        td{
        text-align: center;
        font-size: 20px;
        border: black 2px solid;
        background-color: #F5B041;
        color : black;
        }
        </style>
        """+"\n")
        # BODY
        archivo.write("<body>" + "\n")
        archivo.write("<table border=\"3\" width=\"100%\">" + "\n")
        archivo.write("<center>" + "\n")
        archivo.write("<th colspan=\"4\">REPORTE DE ERRORES </th>" + "\n")
        archivo.write("<tr><td>#</td><td>TYPE</td><td>DESCRIPTION</td><td>LINE</td></tr>" + "\n")
        # TABLE BODY 
        for i in range(len(self.listErrors)):
            archivo.write('<tr>')
            archivo.write('<td>'+str(i+1)+'</td>')
            archivo.write('<td>'+self.listErrors[i].type+'</td>')
            archivo.write('<td>'+self.listErrors[i].description+'</td>')
            archivo.write('<td>'+str(self.listErrors[i].line)+'</td>')
            archivo.write('</tr>')
         
        archivo.write("</center>" + "\n")
        archivo.write("</table>" + "\n")
        archivo.write("</body>" + "\n")
        archivo.write("</html>" + "\n")
        archivo.close()
 
"""
EJEMPLO:
 
Para declarar un error:
error1 = ErrorReport('lexico' , 'caracter desconocido' , '3')

Para adjuntarlo a la lista:

listaErrores = ListError()
listaErrores.addError(error1)
"""       
        
    

