import PLSQL.tfPLSQL as TF
from PLSQL.expresionesPLSQL import *
from PLSQL.instruccionesPLSQL import *


class FuncionesTipo:
    def __init__(self, id,instruccion,tipo,valor,ambito):
        self.id = id
        self.instruccion = instruccion
        self.tipo = tipo
        self.valor = valor
        self.ambito = ambito

FuncionesTipoArr = []

class RTablaDeSimbolosF: 
    def __init__(self):
        ''' Reporte Tabla de Simbolos'''

    def getOperador(self,operador):
        if operador == OPERADOR.MAS:
            return "+"
        elif operador == OPERADOR.MENOS:
            return "-"
        elif operador == OPERADOR.POR:
            return "*"
        elif operador == OPERADOR.DIVIDIDO:
            return "/"
        elif operador == OPERADOR.NOT:
            return "!"
        elif operador == OPERADOR.AND:
            return "&&"
        elif operador == OPERADOR.OR:
            return "||"
        elif operador == OPERADOR.XOR:
            return "xor"
        elif operador == OPERADOR.NOTB:
            return "~"
        elif operador == OPERADOR.ANDB:
            return "&"
        elif operador == OPERADOR.ORB:
            return "|"
        elif operador == OPERADOR.XORB:
            return "^"
        elif operador == OPERADOR.SHIFTD:
            return ">>"
        elif operador == OPERADOR.SHIFTI:
            return "<<"
        elif operador == OPERADOR.IGUAL:
            return "=="
        elif operador == OPERADOR.DIFERENTE:
            return "!="
        elif operador == OPERADOR.MAYORIGUAL:
            return ">="
        elif operador == OPERADOR.MENORIGUAL:
            return "<="
        elif operador == OPERADOR.MAYOR:
            return ">"
        elif operador == OPERADOR.MENOR:
            return "<"
        elif operador == OPERADOR.MOD:
            return "%"

    def getExpresion(self,ins):
        if (isinstance(ins,ExpresionNumero)):
            return ins.val
        elif (isinstance(ins,ExpresionBooleana)):
            return ins.val
        elif (isinstance(ins,ExpresionCadena)):
            return ins.val
        elif (isinstance(ins,ExpresionIdentificador)):
            return ins.id
        elif (isinstance(ins,ExpresionBinaria)):
            expp1 = self.getExpresion(ins.exp1)
            expp2 = self.getExpresion(ins.exp2)
            op = self.getOperador(ins.operador)
            strr = str(expp1) +" " + str(op)+" "+str(expp2)
            return strr
        else:
            return ins

    def getFunciones(self,instrucciones,ambito,tipo):
        for instr in instrucciones:
            #print(instr)
            if(isinstance(instr,ListaDeclaraciones)):
                self.getFunciones(instr.declaraciones,ambito,instr.tipo)
            elif(isinstance(instr,Declaracion)):
                #print('DECLARACION',instr.id,self.getExpresion(instr.exp),ambito)

                funcionTemp = FuncionesTipo(instr.id,'DECLARACION','DECLARACION',self.getExpresion(instr.exp),ambito)
                FuncionesTipoArr.append(funcionTemp)
            elif(isinstance(instr,Asignacion)):
                #print('ASIGNACION',instr.id,self.getExpresion(instr.exp),ambito)
                funcionTemp = FuncionesTipo(instr.id,'ASIGNACION','ASIGNACION',self.getExpresion(instr.exp),ambito)
                FuncionesTipoArr.append(funcionTemp)
            elif(isinstance(instr,Impresion)):
                #print('IMPRESION',self.getExpresion(instr.impresiones[0]),ambito)
                funcionTemp = FuncionesTipo(' ','RAISE','RAISE',self.getExpresion(instr.impresiones[0]),ambito)
                FuncionesTipoArr.append(funcionTemp)
            elif(isinstance(instr,Etiqueta)):
                print('Etiqueta')
            elif(isinstance(instr,Salto)):
                print('Salto')
            elif(isinstance(instr,SentenciaIf)):
                if instr.si != None:
                    self.getFunciones([instr.si],ambito,tipo)
                if instr.sino != None:
                    self.getFunciones([instr.sino],ambito,tipo)
                funcionTemp = FuncionesTipo(' ','IF','CONTROL STRUCTURES',0,ambito)
                FuncionesTipoArr.append(funcionTemp)
            elif(isinstance(instr,SentenciaCase)):
                funcionTemp = FuncionesTipo(' ','CASE','CONTROL STRUCTURES',0,ambito)
                FuncionesTipoArr.append(funcionTemp)
                self.getFunciones(instr.casos,ambito,tipo)
            elif(isinstance(instr,Caso)):
                if instr.sentencias != None:
                    self.getFunciones([instr.sentencias],ambito,tipo)
            elif(isinstance(instr,Funcion)):
                print('Funcion')
                
            elif(isinstance(instr,LlamadaFuncion)):
                #print('LlamadaFuncion',instr.id,ambito)
                funcionTemp = FuncionesTipo(instr.id,'LLAMADA FUNCION','LLAMADA FUNCION',0,ambito)
                FuncionesTipoArr.append(funcionTemp)
            elif(isinstance(instr,Parametro)):
                #print('Parametro',instr.tipo,instr.id,ambito) 
                funcionTemp = FuncionesTipo(instr.id,'PARAMETRO','PARAMETRO',0,ambito)
                FuncionesTipoArr.append(funcionTemp)           
            elif(isinstance(instr,Principal)):
                self.getFunciones(instr.instrucciones,ambito,tipo)

    def crearReporte(self,ts_globalFunciones):
        '''if len(ts_globalFunciones.funciones) > 0:
            for simb in ts_globalFunciones.funciones.values():
                funcionTemp = FuncionesTipo(simb.id,'FUNCION','FUNCION',0,'GLOBAL')
                FuncionesTipoArr.append(funcionTemp)'''

        if len(ts_globalFunciones.funciones) > 0:
            for simb in ts_globalFunciones.funciones.values():
                CadenaFuncion = ""
                if simb.tipo_funcion == TIPO_DECLARACION_FUNCION.FUNCTION:
                    CadenaFuncion = 'FUNCTION'
                else:
                    CadenaFuncion = 'PROCEDURE'
                funcionTemp = FuncionesTipo(simb.id,'DECLARACION FUNCION',CadenaFuncion,0,'GLOBAL')
                FuncionesTipoArr.append(funcionTemp)
                if simb.parametros != None:
                    self.getFunciones(simb.parametros,simb.id,'INTEGER')
                if simb.instrucciones.instrucciones != None:
                    self.getFunciones(simb.instrucciones.instrucciones,simb.id,'INTEGER')

        cadenaTS = ""
        try:
            ff = open("./reportes/dot.dot", "r")
            cadenaTS = ff.read()
        except :
            pass

        f = open("reportes/TablaDeSimbolos.html", "w")
        f.write("<!DOCTYPE html>")
        f.write("<html lang=\"en\" class=\"no-js\">")
        f.write("")
        f.write("<head>")
        f.write("    <meta charset=\"UTF-8\" />")
        f.write("    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge,chrome=1\">")
        f.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
        f.write("    <title>Tabla de Simbolos</title>")
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
        f.write("            <h1>Tabla de Simbolos Funciones</h1>")
        f.write("        </header>")
        f.write("        <div class=\"component\">")
        f.write("            <table>")
        f.write("                <thead>")
        f.write("                    <tr>")
        f.write("                        <th>No.</th>")
        f.write("                        <th>ID</th>")
        f.write("                        <th>INSTRUCCION</th>")
        f.write("                        <th>TIPO</th>")
        f.write("                        <th>VALOR</th>")
        f.write("                        <th>AMBITO</th>")
        f.write("                    </tr>")
        f.write("                </thead>")
        f.write("                <tbody>")
        if len(FuncionesTipoArr) > 0:
                i = 0
                while i < len(FuncionesTipoArr):
                    f.write("                    <tr>")
                    f.write("                        <td class=\"text-left\">"+ str(i+1) +"</td>")
                    f.write("                        <td class=\"text-left\">"+ str(FuncionesTipoArr[i].id) +"</td>")
                    f.write("                        <td class=\"text-left\">"+ str(FuncionesTipoArr[i].instruccion) +"</td>")
                    f.write("                        <td class=\"text-left\">"+ str(FuncionesTipoArr[i].tipo) +"</td>")
                    f.write("                        <td class=\"text-left\">"+ str(FuncionesTipoArr[i].valor) +"</td>")
                    f.write("                        <td class=\"text-left\">"+ str(FuncionesTipoArr[i].ambito) +"</td>")
                    f.write("                    </tr>")
                    i += 1
        f.write("                </tbody>")
        f.write("            </table>")
        f.write("        </div>")
        f.write("    </div><!-- /container -->")

        f.write(cadenaTS)

        f.write("    <script src=\"http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js\"></script>")
        f.write("    <script src=\"http://cdnjs.cloudflare.com/ajax/libs/jquery-throttle-debounce/1.1/jquery.ba-throttle-debounce.min.js\"></script>")
        f.write("    <script src=\"js/jquery.stickyheader.js\"></script>")
        f.write("</body>")
        f.write("")
        f.write("</html>")
        f.close()

        ff = open("./reportes/dot.dot", "w")
        ff.close()

        

