


class OptimizacionR:
    def __init__(self, regla , entrada, salida):
        self.regla = regla
        self.entrada = entrada
        self.salida = salida

class ROptimizacion3D: 
    def __init__(self):
        ''' Reporte Tabla de Simbolos'''

    def crearReporte(self,arrOptimizacion):
        

        f = open("reportes/ReporteOptimizacion.html", "w")
        f.write("<!DOCTYPE html>")
        f.write("<html lang=\"en\" class=\"no-js\">")
        f.write("")
        f.write("<head>")
        f.write("    <meta charset=\"UTF-8\" />")
        f.write("    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge,chrome=1\">")
        f.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
        f.write("    <title>Reporte Optimizacion</title>")
        f.write("    <meta name=\"description\"")
        f.write("        content=\"Sticky Table Headers Revisited: Creating functional and flexible sticky table headers\" />")
        f.write("    <meta name=\"keywords\" content=\"Sticky Table Headers Revisited\" />")
        f.write("    <meta name=\"author\" content=\"Codrops\" />")
        f.write("    <link rel=\"shortcut icon\" href=\"../favicon.ico\">")
        f.write("    <link rel=\"stylesheet\" type=\"text/css\" href=\"css/normalize.css\" />")
        f.write("    <link rel=\"stylesheet\" type=\"text/css\" href=\"css/demo.css\" />")
        f.write("    <link rel=\"stylesheet\" type=\"text/css\" href=\"css/component.css\" />")
        f.write("</head>")

        f.write("<body>")
        f.write("    <div class=\"container\">")
        f.write("        <!-- Top Navigation -->")
        f.write("        <header>")
        f.write("            <h1>Reporte Optimizacion 3D por Mirilla</h1>")
        f.write("        </header>")
        f.write("        <div class=\"component\">")
        f.write("            <table>")
        f.write("                <thead>")
        f.write("                    <tr>")
        f.write("                        <th>No.</th>")
        f.write("                        <th>REGLA</th>")
        f.write("                        <th>ENTRADA</th>")
        f.write("                        <th>SALIDA</th>")
        f.write("                    </tr>")
        f.write("                </thead>")
        f.write("                <tbody>")
        if len(arrOptimizacion) > 0:
                i = 0
                while i < len(arrOptimizacion):
                    f.write("                    <tr>")
                    f.write("                        <td class=\"text-left\">"+ str(i+1) +"</td>")
                    f.write("                        <td class=\"text-left\">"+ str(arrOptimizacion[i].regla) +"</td>")
                    f.write("                        <td class=\"text-left\">"+ str(arrOptimizacion[i].entrada) +"</td>")
                    f.write("                        <td class=\"text-left\">"+ str(arrOptimizacion[i].salida) +"</td>")
                    f.write("                    </tr>")
                    i += 1
        f.write("                </tbody>")
        f.write("            </table>")
        f.write("        </div>")
        f.write("    </div><!-- /container -->")

        f.write("    <script src=\"http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js\"></script>")
        f.write("    <script src=\"http://cdnjs.cloudflare.com/ajax/libs/jquery-throttle-debounce/1.1/jquery.ba-throttle-debounce.min.js\"></script>")
        f.write("    <script src=\"js/jquery.stickyheader.js\"></script>")
        f.write("</body>")
        f.write("")
        f.write("</html>")
        f.close()

