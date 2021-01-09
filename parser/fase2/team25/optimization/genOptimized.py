from optimization.optGrammar import optimize
from optimization.abstract.optimize import OptimizedInstruction

listaOpt = list()

def optimizeCode(entradaOpt:str):
    listaOpt = optimize(entradaOpt)

    generator = OptimizedGenerator()
    #Intentamos optimizar cada instruccion
    for ins in listaOpt:
        if isinstance(ins, OptimizedInstruction):
            ins.optimize(generator)

    #Agregamos al nuevo doc
    for ins in listaOpt:
        if isinstance(ins, OptimizedInstruction):
            ins.addToCode(generator)
        elif isinstance(ins, str):
            generator.addToCode(ins)

    generator.makeCode()
    generator.makeReport()

class OptimizedGenerator:
    """
    Clase encargada de generar codigo optimizado
    """
    def __init__(self) -> None:
        self.report = list()
        self.code = list()

    def addToCode(self, text):
        self.code.append(text+'\n')

    def toReport(self, text):
        self.report.append(text +'\n')

    def genCode(self) -> str:
        string = ''
        string+="from goto import with_goto\n"
        string+="from interpreter import execution\n"
        string+="from c3d.stack import Stack\n"
        for line in self.code:
            string += line

        return string

    def genReport(self) -> str:
        report = '''<html>
<head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/lux/bootstrap.min.css">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <title>Reporte de Optimización</title>
    <meta charset="utf-8">
</head>

<body>
    <div class="container" style="padding: 50px;">
        <h2 class="text-center">Reporte de Optimización</h2>
        <table class="table table-striped">
            <thead class="thead-dark">
                <tr><th scope="col">Instrucción Optimizada</th><th scope="col">Regla</th><th scope="col">Linea</th></td>
            </thead>
            <tbody>'''
        for line in self.report:
            report += line
        report += '''</tbody>
        </table>
    </div>
</body>
</html>'''
        return report

    def makeCode(self):
        code = self.genCode()
        with open('codigoOptimizado.py','w') as file:
            file.write(code)
            file.close()

    def makeReport(self):
        report = self.genReport()
        with open('reporteOptimizado.html','w') as file:
            file.write(report)
            file.close()
