import re
import webbrowser

class Optimizacion():
    def __init__(self):
        self.Reporte = []
        pass

    def Optimizar(self):
        f = open("Codigo_3D/Codigo3D.py", "r")
        lineas = f.readlines()
        f.close()

        lineas = self.AplicarR8(lineas)
        lineas = self.AplicarR9(lineas)
        lineas = self.AplicarR10(lineas)
        lineas = self.AplicarR11(lineas)
        lineas = self.AplicarR12(lineas)
        lineas = self.AplicarR13(lineas)
        lineas = self.AplicarR14(lineas)
        lineas = self.AplicarR15(lineas)
        lineas = self.AplicarR16(lineas)
        lineas = self.AplicarR17(lineas)
        lineas = self.AplicarR18(lineas)


        f_op = open("Codigo_3D/Codigo3D_Optimizado.py", "w")
        f_op.writelines(lineas)
        f_op.close()
        pass

    def AplicarR1(self, archivo):
        print("Aplicando Regla 1 de optimizacion")
        pass

    def AplicarR2(self, archivo):
        print("Aplicando Regla 2 de optimizacion")
        pass

    def AplicarR3(self, archivo):
        print("Aplicando Regla 3 de optimizacion")
        pass

    def AplicarR4(self, archivo):
        print("Aplicando Regla 4 de optimizacion")
        pass

    def AplicarR5(self, archivo):
        print("Aplicando Regla 5 de optimizacion")
        pass

    def AplicarR6(self, archivo):
        print("Aplicando Regla 6 de optimizacion")
        pass

    def AplicarR7(self, archivo):
        print("Aplicando Regla 7 de optimizacion")
        pass

    def AplicarR8(self, archivo):
        print("Aplicando Regla 8 de optimizacion")
        
        for i in range(4,len(archivo)):
            c = archivo[i].split(' ')
            if len(c) >= 3:
                if c[0].replace("\t","") == c[2]:
                    if "+ 0" in archivo[i]:
                        self.Reporte.append([i, "Regla 8", archivo[i], ""])
                        archivo[i] = "\n"
        return archivo

    def AplicarR9(self, archivo):
        print("Aplicando Regla 9 de optimizacion")
        for i in range(4,len(archivo)):
            c = archivo[i].split(' ')
            if len(c) >= 3:
                if c[0].replace("\t","") == c[2]:
                    if "- 0" in archivo[i]:
                        self.Reporte.append([i, "Regla 9", archivo[i], ""])
                        archivo[i] = "\n"
        return archivo
        pass

    def AplicarR10(self, archivo):
        print("Aplicando Regla 10 de optimizacion")
        for i in range(4,len(archivo)):
            c = archivo[i].split(' ')
            if len(c) >= 3:
                if c[0].replace("\t","") == c[2]:
                    if "* 1" in archivo[i]:
                        self.Reporte.append([i, "Regla 10", archivo[i], ""])
                        archivo[i] = "\n"
        return archivo
        pass

    def AplicarR11(self, archivo):
        print("Aplicando Regla 11 de optimizacion")
        for i in range(4,len(archivo)):
            c = archivo[i].split(' ')
            if len(c) >= 3:
                if c[0].replace("\t","") == c[2]:
                    if "/ 1" in archivo[i]:
                        self.Reporte.append([i, "Regla 11", archivo[i], ""])
                        archivo[i] = "\n"
        return archivo
        pass

    def AplicarR12(self, archivo):
        print("Aplicando Regla 12 de optimizacion")
        for i in range(4,len(archivo)):
            if "+ 0" in archivo[i]:
                self.Reporte.append([i, "Regla 12", archivo[i], archivo[i].replace("+ 0","")])
                archivo[i] = archivo[i].replace("+ 0","")
        return archivo
        pass

    def AplicarR13(self, archivo):
        print("Aplicando Regla 13 de optimizacion")
        for i in range(4,len(archivo)):
            if "- 0" in archivo[i]:
                self.Reporte.append([i, "Regla 13", archivo[i], archivo[i].replace("- 0","")])
                archivo[i] = archivo[i].replace("- 0","")
        return archivo
        pass

    def AplicarR14(self, archivo):
        print("Aplicando Regla 14 de optimizacion")
        for i in range(4,len(archivo)):
            if "* 1" in archivo[i]:
                self.Reporte.append([i, "Regla 14", archivo[i], archivo[i].replace("* 1","")])
                archivo[i] = archivo[i].replace("* 1","")
        return archivo
        pass

    def AplicarR15(self, archivo):
        print("Aplicando Regla 15 de optimizacion")
        for i in range(4,len(archivo)):
            if "/ 1" in archivo[i]:
                self.Reporte.append([i, "Regla 15", archivo[i], archivo[i].replace("/ 1","")])
                archivo[i] = archivo[i].replace("/ 1","")
        return archivo
        pass

    def AplicarR16(self, archivo):
        print("Aplicando Regla 16 de optimizacion")
        for i in range(4,len(archivo)):
            if "* 2" in archivo[i]:
                c = archivo[i].split(' ')
                if len(c) >= 3:
                    self.Reporte.append([i, "Regla 16", archivo[i], archivo[i].replace("* 2", "+ " + c[2])])
                    archivo[i] = archivo[i].replace("* 2", "+ " + c[2])
        return archivo

    def AplicarR17(self, archivo):
        print("Aplicando Regla 17 de optimizacion")
        for i in range(4,len(archivo)):
            if "* 0" in archivo[i]:
                c = archivo[i].split(' ')
                self.Reporte.append([i, "Regla 17", archivo[i], c[0] + " = 0\n"])
                archivo[i] = c[0] + " = 0\n"
        return archivo  
        pass

    def AplicarR18(self, archivo):
        print("Aplicando Regla 18 de optimizacion")
        for i in range(4,len(archivo)):
            if "0 /" in archivo[i]:
                c = archivo[i].split(' ')
                self.Reporte.append([i, "Regla 18", archivo[i], c[0] + " = 0\n"])
                archivo[i] = c[0] + " = 0\n"
        return archivo  
        pass

    def GenerarReporte(self):
        nombre = "Codigo_3D/ReporteOptimizacion.html"
        contenido = ""
        contenido += "<!DOCTYPE HTML5>"
        contenido += "<html lang=\"es\">"
        contenido += "<head>\
                    <meta charset=\"UTF-8\">\
                    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\
                    <title>Bootstrap 4. Tablas</title>\
                    <link rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css\">\
                    </head>\
                    <body>\
                    <div class=\"container\">\
                    <div class=\"row\">\
                    <div class=\"col\">\
                    <table class=\"table table-striped table-bordered table-hover table-dark\">\
                    <thead>\
                    <tr>\
                    <th>Linea</th>\
                    <th>Regla</th>\
                    <th>Codigo original</th>\
                    <th>Codigo optimizado</th>\
                    </tr>\
                    </thead>\
                    <tbody>\n"

        for e in self.Reporte:
            contenido +=    "<tr>\
                                <td>" + str(e[0]) + "</td>\
                                <td>" + str(e[1]) + "</td>\
                                <td>" + str(e[2]) + "</td>\
                                <td>" + str(e[3]) + "</td>\
                    	    </tr>\n"

        contenido += "</tbody>\
                    </table>\
                    </div>\
                    </div>\
                    <script src=\"https://code.jquery.com/jquery-3.4.1.slim.min.js\"></script>\
                    <script src=\"https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js\"></script>\
                    <script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js\"></script>\
                    </body>\
                    </html>"

                

        f = open(nombre, 'w')
        f.write(contenido)
        f.close()
        webbrowser.open_new_tab('Codigo_3D/ReporteOptimizacion.html')
