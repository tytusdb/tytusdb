from InstruccionesPL.IndicesPL import IndicePL1,  IndicePL7, IndicePL8, IndicePL9, IndicePLUnique, IndicePLUsing, IndicePLUsingNull

import os
from subprocess import check_call
class ArbolPL():
    def __init__(self, instruccionesPL):
        self.instruccionesPL = instruccionesPL
        self.etiquetas = 0 # estas permiten los labels de los diferentes bloques
        self.heap = 0 #permiten las etiquetas de las operaciones en los bloques
        self.listaCuadruplos = {}
        self.defetiqueta = ''
        self.listTripletas = []
        self.listMetodos =[]                            #Creamos una lista para metodos como Procedure y creacion de funcion
        self.listGeneral = []           #Creamos esta lista para poder ingresar la generacion de diferentes etiquetas en orden
                                        #Correspondiente para llevar un orden, segun se vaya formando el codigo, esto para poder tener el codigo en secuencia
                                        #la primer lista nos permitira tener el codigo en bloque segun necesitemos buscar un bloque para la realizacion y ejecucion de codigo 
        self.consola = []   #aca deben almacenar todo lo que quieran imprimir en la consola
        self.lsindices =[]
        self.cod3D = []
        self.tripletaCase = Tripleta(None, None, None, None)
        self.if_index = 0
        self.index_end = 0
    
    def inicializar(self, tabla, arbol):
        codigo = ''
        for elem in self.instruccionesPL:
            codigo += elem.traducir()+'\n'
        return codigo
    def modificarTripleta(self,indice,oper, etiq1,etiq2,modi):
        for x in self.listTripletas:
            if x.verficar(indice,oper,etiq1,etiq2):
                x.setOp2(modi)
    def modificarTripletaCase(self, indice,oper,op1,op2):
        self.tripletaCase.modificacionTotal(indice,oper,op1,op2)

    def getTripletaCase(self):
        return self.tripletaCase


    def generarEtiqueta(self):
        var = 'L' + str(self.etiquetas)
        self.etiquetas += 1
        return var
    def getInstrucciones(self):
        return self.instruccionesPL
        
    def generarHeap(self):
        var = 't'+str(self.heap)
        self.heap += 1
        return var
    
    def agregarTripleta(self, indice, oper, op1, op2):
        tripleta = Tripleta(indice, oper, op1, op2)
        self.listTripletas.append(tripleta)

    def agregarGeneral(self, indice,oper, op1, op2):
        var1 =Tripleta(indice,oper,op1,op2)
        self.listGeneral.append(var1)

    def agregarCuadruplo(self, cuad):
        self.listaCuadruplos[self.defetiqueta].append(cuad)

    def agregarDicEtiqueta(self, cuad, etiqueta):
        self.listaCuadruplos[etiqueta] = []
        self.listaCuadruplos[etiqueta].append(cuad)

    def declararDiccionario(self, etiqueta):
        self.listaCuadruplos[etiqueta] = []
        cuad = Cuadruplo('=', 'array()', '', etiqueta)
        self.listaCuadruplos[etiqueta].insert(0, cuad)

    def getCuadruplos(self):
        return self.listaCuadruplos
    
    def setListaIndice(self, nuevo):
        x  = self.getIndicepl(nuevo.nombreIndice)
        if x != None:
            #si no existe se devuelve NONE porque no existe el indice
            self.consola.append('Ya existe un Indice con ese nombre, porfavor coloque un nuevo nombre')
            return None
        self.lsindices.append(nuevo)
        self.consola.append('Se agrego el indice correctamente')

    def getIndicepl(self, nombre):
        for x in range(0,len(self.lsindices)):
            if(self.lsindices[x].nombreIndice ==nombre):
                return x
        return None
    def setDefEtiqueta(self, etiqueta):
        self.defetiqueta = etiqueta

    def eliminarIndice(self, nombre):
        for x in range(0,len(self.lsindices)):
            if(self.lsindices[x].nombreIndice ==nombre):
                self.lsindices.pop(x)
                return 1
        return 0
    def modificarIndice(self, nombre, columnaActual, columnaNueva):
        #obtenes la posicion del indice
        x  = self.getIndicepl(nombre)
        if x == None:
            #si no existe se devuelve NONE porque no existe el indice
            self.consola.append('No se ha encontrado el indice  con ese nombre, verfique y vuelva a intentarlo Alter Index')
            return None
        #si es un cambio de una columna de un nombre se realiza el cambio
    

        if isinstance(self.lsindices[x], IndicePL1.IndicePL1):
            #puede ser una lista  indices
            #
            if isinstance(self.lsindices[x].columnas, str):
                self.lsindices[x].columnas  = columna
                self.consola.append('se  ha realizado el cambio de la comuna correctamente Alter Index')
                return 1
            else:
                contador = 0
                for id in self.lsindices[x].columnas:
                    if(id.id == columnaActual):
                        self.lsindices[x].columnas[contador].id = columnaNueva
                        self.consola.append('se  ha realizado el cambio de la comuna correctamente Alter Index')
                        return 1
                        
                    contador +=1
            self.consola.append('No se ha encontrado la columna con ese nombre, verfique y vuelva a intentarlo Alter Index')
            return None
        elif isinstance(self.lsindices[x], IndicePL7.IndicePL7):
            if  self.lsindices[x].columnas == columnaActual:
                self.lsindices[x].columnas  = columnaNueva
                self.consola.append('se  ha realizado el cambio de la comuna correctamente Alter Index')
                return 1
            self.consola.append('No se ha encontrado la columna con ese nombre, verfique y vuelva a intentarlo Alter Index')
            return None
        elif isinstance(self.lsindices[x], IndicePL8.IndicePL8):
            if  self.lsindices[x].nombreCampo == columnaActual:
                self.lsindices[x].nombreCampo  = columnaNueva
                self.consola.append('se  ha realizado el cambio de la comuna correctamente Alter Index')
                return 1
            self.consola.append('No se ha encontrado la columna con ese nombre, verfique y vuelva a intentarlo Alter Index')
            return None
        elif isinstance(self.lsindices[x], IndicePL9.IndicePL9):
            if  self.lsindices[x].nombreCampo == columnaActual:
                self.lsindices[x].nombreCampo  = columnaNueva
                self.consola.append('se  ha realizado el cambio de la comuna correctamente Alter Index')
                return 1
            self.consola.append('No se ha encontrado la columna con ese nombre, verfique y vuelva a intentarlo Alter Index')
            return None
        elif isinstance(self.lsindices[x], IndicePLUnique.IndicePLUnique):
            #puede ser una lista de indices
            #
            if isinstance(self.lsindices[x].columnas, str):
                if self.lsindices[x].columnas == columnaActual:
                    self.lsindices[x].columnas  = columnaNueva
                    self.consola.append('se  ha realizado el cambio de la comuna correctamente Alter Index')
                    return 1
                self.consola.append('No se ha encontrado la columna con ese nombre, verfique y vuelva a intentarlo Alter Index')
                return None
            else:
                contador = 0
                for id in self.lsindices[x].columnas:
                    if(id.id == columnaActual):
                        self.lsindices[x].columnas[contador].id = columnaNueva
                        self.consola.append('se  ha realizado el cambio de la comuna correctamente Alter Index')
                        return 1
                        
                    contador +=1
            self.consola.append('No se ha encontrado la columna con ese nombre, verfique y vuelva a intentarlo Alter Index')
            return None
        elif isinstance(self.lsindices[x], IndicePLUsing.IndicePLUsing):
            #puede ser una lista de indices
            #
            if isinstance(self.lsindices[x].nombreCampo, str):
                if self.lsindices[x].nombreCampo == columnaActual:
                    self.lsindices[x].columnas  = columnaNueva
                    self.consola.append('se  ha realizado el cambio de la comuna correctamente Alter Index')
                    return 1
                self.consola.append('No se ha encontrado la columna con ese nombre, verfique y vuelva a intentarlo Alter Index')
                return None
            else:
                contador = 0
                for id in self.lsindices[x].nombreCampo:
                    if(id.id == columnaActual):
                        self.lsindices[x].nombreCampo[contador].id = columnaNueva
                        self.consola.append('se  ha realizado el cambio de la comuna correctamente Alter Index')
                        return 1
                    contador +=1
            self.consola.append('No se ha encontrado la columna con ese nombre, verfique y vuelva a intentarlo Alter Index')
            return None
            
        elif isinstance(self.lsindices[x], IndicePLUsingNull.IndicePLUsingNull): 
            if self.lsindices[x].nombreOperacion == columnaActual:
                self.lsindices[x].nombreOperacion  = columnaNueva
                self.consola.append('se  ha realizado el cambio de la comuna correctamente Alter Index')
                return 1
            self.consola.append('No se ha encontrado la columna con ese nombre, verfique y vuelva a intentarlo Alter Index')
            return None

    def add3D(self, cod):
        self.cod3D.append(cod)

    def imprimir(self):
        for ins in self.cod3D:
            print(ins)

    def imprimirTripletas(self):
        for ins in self.listTripletas:
            valuess= '{0},{1},{2}'.format(ins.getOper(),ins.getOp1(),ins.getOp2())
            print(valuess)

    def imprimirGeneral(self):
        #self.consola.append('')
        for ins in self.listGeneral:
            valuess= '{0},{1},{2}'.format(ins.getOper(),ins.getOp1(),ins.getOp2())
            print(valuess)     

    def getLast(self):
        return len(self.listTripletas)-1

    def getLastTripleta(self):
        return self.listTripletas[self.getLast()]
    
    def modificarLastTripleta(self, indice, oper, op1, op2):
        self.listTripletas[self.getLast()].modifiacionTotal(indice,oper,op1,op2)
    def eliminarTripleta(self):
        self.listTripletas.pop()

    def generarIF(self):
        salida = "if{0}".format(self.if_index)
        self.if_index += 1
        return salida

    def generarEND(self):
        salida = "end{0}".format(self.index_end)
        self.index_end += 1
        return salida


    def generarReporteTripletas(self):
        file = open("Tripletas.txt", "w")        
        file.write('digraph G {'+ os.linesep)
        file.write('node [shape=plaintext]'+ os.linesep)
        file.write(' a [label=<<table border="0" cellborder="1" cellspacing="0">'+ os.linesep)
        file.write('<tr><td><b>\"indice\"</b></td><td>\"operacion\"</td><td>\"operador1\"</td><td>\"operador2\"</td></tr>'+os.linesep)
        cont=0
        for instus in self.listTripletas:
            col1=instus.getOper()
            col2=instus.getOp1()
            col3=instus.getOp2()
            file.write('<tr><td><b>\"'+str(cont)+'\"</b></td><td>\"'+col1+'\"</td><td>\"'+str(col2)+'\"</td><td>\"'+str(col3)+'\"</td></tr>' + os.linesep)
            cont+=1

        file.write("</table>>];"+os.linesep)
        file.write("}")
        file.close()

        check_call(['dot','-Tpng','Tripletas.txt','-o','Tripletas.png'])

    def generarReporteCodigo(self):
        file = open("CodigoGeneral.txt", "w")        
        file.write('digraph G {'+ os.linesep)
        file.write('node [shape=plaintext]'+ os.linesep)
        file.write(' a [label=<<table border="0" cellborder="1" cellspacing="0">'+ os.linesep)
        file.write('<tr><td><b>\"indice\"</b></td><td>\"Codigo\"</td></tr>'+os.linesep)
        cont=0
        for instus in self.cod3D:
            
            for aux in instus:
                col1=aux
            file.write('<tr><td><b>\"'+str(cont)+'\"</b></td><td>\"'+str(col1)+'\"</td></tr>' + os.linesep)
            cont+=1

        file.write("</table>>];"+os.linesep)
        file.write("}")
        file.close()

        check_call(['dot','-Tpng','CodigoGeneral.txt','-o','CodigoGeneral.png'])


    def construirReporteGramatical(self, name):
        ruta = "{0}.dot".format(name)
        destino= "dot -Tpng {0}.dot -o {1}.png".format(name, name)
        try:
            file = open(ruta, "w")
            file.write("digraph ReporteGramatical{\n")
            file.write("graph [ratio=fill];node [label=\"\\N\", fontsize=15, shape=plaintext];\n")
            file.write("graph [bb=\"0,0,352,154\"];\n")
            file.write("arset [label=<")
            file.write("<TABLE ALIGN=\"LEFT\">\n")
            file.write("<TR><TD>Produccion</TD><TD>Reglas Semanticas</TD></TR>\n")
            for nodo in self.listaCuadruplos:
                file.write("<TR>")
                file.write("<TD>")
                file.write(nodo)
                file.write("</TD>")
                file.write("<TD><TABLE BORDER=\"0\">")
                print(self.listaCuadruplos[nodo])
                for regla in self.listaCuadruplos[nodo]:
                    file.write("<TR><TD>")
                    file.write(regla.getCuad())
                    file.write("</TD></TR>")
                file.write("</TABLE></TD>")
                file.write("</TR>\n")
            file.write("</TABLE>")
            file.write("\n>, ];\n")
            file.write("}")
            file.close()
        except:
            print("ERROR AL ESCRIBIR TABLA")
        finally:
            print('fin')

class Tripleta():
    def __init__(self, indice, oper, op1, op2):
        self.indice = indice
        self.oper = oper
        self.op1 = op1
        self.op2 = op2
    
    def verficar(self, indice, oper, op1, op2):
        if  (self.oper == oper)and (self.op1 == op1) and (self.op2 == op2):
            return True
        return False
    def modificacionTotal(self, indice,oper,op1, op2):
        self.indice = indice
        self.oper = oper
        self.op1 = op1
        self.op2 = op2

    def setOp2(self, op2):
        self.op2 =str(op2) # Error de tipos convertir string a var como se hace alex?

    def getOper(self):
        return self.oper

    def getOp1(self):
        return self.op1

    def getOp2(self):
        return self.op2

    def getIndice(self):
        return self.indice
    
    def setIndice(self,indice):
        self.indice = indice

    def setOper(self, oper):
        self.oper = oper

    def setOp1(self, op1):
        self.op1 = op1

    def setOp2(self, op2):
        self.op2 = op2 

class Cuadruplo:
    def __init__(self, operador, arg1, arg2, result):
        self.op = operador
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

    def getCuad(self):
        return str(self.op) + str(self.arg1) + str(self.arg2) + str(self.result)

class Cuadruplos: 
    def __init__(self):
        self.cuadruplos = []
        self.index_temporal = 0

    def add(self, cuadruplo):
        self.cuadruplos.append(cuadruplo)



'''
1,2,3,4,5,6
list.len =6 

'''

'''
Manejar algun tipo de estructura para poder guardar un bloque de instrucciones 3D
sabiendo que cada bloque sera definido como def bloque1
y teniendo en cuenta que dentro del bloque se encuentra un listado de instruciones 3 D
considerando que se pueden hacer llamadas desde afuera del bloque para ser ejecutadas
Se debe considerar que Execute y perfome realizan una accion para la ejecucion de un bloque
Al momento de generar el codigo 3D debemos al inicio formular un main el cual hara las diferentes llamadas y ejecuciones
de los bloques que se desean ejecutar 
Si se cuenta con un bloque se podrian usar las diferentes etiquetas que sean diferentes e instancias en otros bloques para la optimizacion 
se debe tomar en cuenta si esta no se ven modificadas por otras etiquetas brindando un resultado diferente 
Considerar que se puede manejar diferentes ambitos dentro del pl

'''
class Bloque():
    def __init__(self, nombre,listC3D):
        self.nombre = nombre
        self.listC3D  = listC3D

    def getNombre(self):
        return self.nombre

    def getListC3D(self):
        return self.listC3D

    def setListC3D(self, listC3D):
        self.listC3D = listC3D

    