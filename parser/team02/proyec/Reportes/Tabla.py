import webbrowser
class Tabla():

    def write(self,entorno,tree):
        input = "<html>" + '\n' + "<head>" + '\n' + "<title>Reporte Gramatical</title>" + '\n' + "</head>" + '\n'
        input = input + "<body bgcolor=\"white\">" + '\n' + "<center><Font size=12 >" + "Tabla de simbolos" + "</Font></center>" + '\n'
        input = input + "<hr >" + '\n' + "<font color=black>" + '\n' + "<center>" + '\n'
        input = input + "<table " + '\n'
        input = input + "<TR bgcolor=silver>" + "\n"
        input = input + "<TH  style=\"font-size: 14px; width:15%; \"\" align=center>Tipo de Dato</TH>" + '\n'
        input = input + "<TH  style=\"font-size: 14px; width:20%; \" align=center>ID</TH>" + '\n'
        input = input + "<TH  style=\"font-size: 14px; width:15%; \" align=center>Ambito</TH>" + '\n'
        input = input + "<TH  style=\"font-size: 14px; width:15%; \" align=center>Valor</TH>" + '\n'
        input = input + "<TH  style=\"font-size: 14px; width:10%; \" align=center>Linea</TH>" + '\n'
        input = input + "<TH  style=\"font-size: 14px; width:10%; \" align=center>Columna</TH>" + '\n'







        for sent in tree.sentencias:
            input = input + "<TR>"
        #    input = input + "<TD style=\"font-size: 15px; color:white;\" color:white align=center>"+sent.getTipo()+"</TD>" + '\n'
            input = input + "<TD style=\"font-size: 15px; color:black;\"  align=center>" + str(sent.id )+ "</TD>" + '\n'
            input = input + "<TD style=\"font-size: 15px; ;\"  align=center>-</TD>" + '\n'
            input = input + "<TD style=\"font-size: 15px; ;\"  align=center>-</TD>" + '\n'
            input = input + "<TD style=\"font-size: 15px; ;\"  align=center>-</TD>" + '\n'
            input = input + "<TD style=\"font-size: 15px; ;\"  align=center>" + str(sent.line)+ "</TD>" + '\n'
            input = input + "<TD style=\"font-size: 15px; ;\"  align=center>" + str(sent.column) + "</TD>" + '\n'
            input = input + "</TR>" + '\n'

        input = input + '\n' + "</center>" + '\n' + "</table>" + "</body>" + '\n' + "</html>"

        f = open ('Tabla.html','w')
        f.write(input)
        f.close()
        webbrowser.open_new_tab('Tabla.html')
