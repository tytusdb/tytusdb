import webbrowser
class ReporteGramatical():

    def generarReporte(self, nodo):

        contenido = "<html>" + '\n' + "<head>" + '\n' + "<title>Reporte Gramatical</title>" + '\n' + "</head>" + '\n'
        contenido = contenido + "<body bgcolor=\"black\">" + '\n' + "<center><Font size=22 color=darkred>" + "Reporte Gramatical" + "</Font></center>" + '\n'
        contenido = contenido + "<hr >" + '\n' + "<font color=white>" + '\n' + "<center>" + '\n'
        contenido = contenido + "<table border=1 align=center style=\"width:80%;\" >" + '\n'
        contenido = contenido + "<TR bgcolor=darkred>" + "\n"
        contenido = contenido + "<TH  style=\"font-size: 18px; width:40%; color:white\" align=center>Producción</TH>" + '\n'
        contenido = contenido + "<TH  style=\"font-size: 18px; width:40%; color:white\" align=center>Reglas Semánticas</TH>" + '\n'
        contenido = contenido + "</TR>" + '\n'

        contenido = contenido + "<TR>" + '\n'
        contenido = contenido + "<TD style=\"font-size: 15px; color:white;\" color:white align=rigth>S->etiquetas</TD>" + '\n'
        contenido = contenido + "<TD style=\"font-size: 15px; color:white;\" color:white align=left>&nbsp;</TD>" + '\n'
        contenido = contenido + "</TR>" + '\n'

        contenido = contenido + "<TR>" + '\n'
        contenido = contenido + "<TD style=\"font-size: 15px; color:white;\" color:white align=rigth><p>" + nodo.produccion + "</p></TD>" + '\n'
        contenido = contenido + "<TD style=\"font-size: 15px; color:white;\" color:white align=left><p>" + nodo.reglas + "</p></TD>" + '\n'
        contenido = contenido + "</TR>" + '\n'

        if (nodo.hijos != None):
            for hijo in reversed(nodo.hijos):
                contenido = contenido + "<TR>" + '\n'
                contenido = contenido + "<TD style=\"font-size: 15px; color:white;\" color:white align=rigth><p>" + hijo.produccion + "</p></TD>" + '\n'
                contenido = contenido + "<TD style=\"font-size: 15px; color:white;\" color:white align=left><p>" + hijo.reglas + "</p></TD>" + '\n'
                contenido = contenido + "</TR>" + '\n'

            for hijo in reversed(nodo.hijos):
                contenido = contenido + self.obtenerHijos(hijo)

        contenido = contenido + '\n' + "</center>" + '\n' + "</table>" + "</body>" + '\n' + "</html>"

        f = open('reporteGramatical.html', 'w')
        f.write(contenido)
        f.close()

        webbrowser.open_new_tab('reporteGramatical.html')

    def obtenerHijos(self, nodo):
        contenido = ""
        if (nodo.hijos != None):
            for hijo in reversed(nodo.hijos):
                contenido = "<TR>" + '\n'
                contenido = contenido + "<TD style=\"font-size: 15px; color:white;\" color:white align=rigth><p>" + hijo.produccion + "</p></TD>" + '\n'
                contenido = contenido + "<TD style=\"font-size: 15px; color:white;\" color:white align=left><p>" + hijo.reglas + "</p></TD>" + '\n'
                contenido = contenido + "</TR>" + '\n'

            for hijo in reversed(nodo.hijos):
                contenido = contenido + self.obtenerHijos(hijo)

        return contenido