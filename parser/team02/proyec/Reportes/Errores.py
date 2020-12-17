import webbrowser

def agregar(error,param=False):

    if not hasattr(agregar,"datavar"):
        agregar.datavar = []

    if(param):
        agregar.datavar = []
    else:
        if(error!=None):
            agregar.datavar.append(error)
        else:
            return agregar.datavar




def write(self):
        datavar = agregar(None)

        input = "<html>" + '\n' + "<head>" + '\n' + "<title>Reporte Gramatical</title>" + '\n' + "</head>" + '\n'
        input = input + "<body bgcolor=\"white\">" + '\n' + "<center><Font size=12 >" + "Tabla de simbolos" + "</Font></center>" + '\n'
        input = input + "<hr >" + '\n' + "<font color=black>" + '\n' + "<center>" + '\n'
        input = input + "<table " + '\n'
        input = input + "<TR bgcolor=silver>" + "\n"
        input = input + "<TH  style=\"font-size: 14px; width:15%; \"\" align=center>Tipo de Error</TH>" + '\n'
        input = input + "<TH  style=\"font-size: 14px; width:20%; \" align=center>Descripción del Error</TH>" + '\n'
        input = input + "<TH  style=\"font-size: 14px; width:15%; \" align=center>Linea</TH>" + '\n'
        input = input + "<TH  style=\"font-size: 14px; width:15%; \" align=center>Columna</TH>" + '\n'


        for error in datavar:
            input = input + "<TR>"
            input = input + "<TD style=\"font-size: 15px; color:black;\"  align=center>" + error.tipo  + "</TD>" + '\n'
            input = input + "<TD style=\"font-size: 15px; color:black;\"  align=center>" + error.error  + "</TD>" + '\n'
            input = input + "<TD style=\"font-size: 15px; color:black;\"  align=center>" + error.line  + "</TD>" + '\n'
            input = input + "<TD style=\"font-size: 15px; color:black;\"  align=center>" + error.column + "</TD>" + '\n'

            input = input + "</TR>" + '\n'

        input = input + '\n' + "</center>" + '\n' + "</table>" + "</body>" + '\n' + "</html>"

        f = open ('TablaErr.html','w')
        f.write(input)
        f.close()
        webbrowser.open_new_tab('TablaErr.html')
