import threading
import time
import re

from InstruccionesPL.TablaSimbolosPL.ArbolPL import Cuadruplo


class Optimizacion():
    def __init__(self, etiquetas):

        self.etiquetas = etiquetas
        self.optimizadas = []
        self.C3D = []
        self.eliminadas = {}
    
    def optimizar(self):
        #self.printCuadruplos()
        self.optimizadas = []
        'regla 1'
        self.etiquetas = self.regla1()
        'regla 2'
        self.etiquetas = self.regla2()
        'regla 3'
        self.etiquetas = self.regla3()
        'regla 3'
        self.etiquetas = self.regla3(pasada =1)
        'regla 4'
        self.etiquetas = self.regla4()
        'regla 2'
        self.etiquetas = self.regla2()
        'regla 5'
        self.etiquetas = self.regla5()
        'regla 2'
        self.etiquetas = self.regla2()
        'regla 6'
        self.etiquetas = self.regla6()
        'regla 7'
        self.etiquetas = self.regla7()
        'regla 8'
        self.etiquetas = self.regla8()
        'regla 9'
        self.etiquetas = self.regla9()
        'regla 10'
        self.etiquetas = self.regla10()
        'regla 11'
        self.etiquetas = self.regla11()
        'regla 12'
        self.etiquetas = self.regla12()
        'regla 13'
        self.etiquetas = self.regla13()
        'regla 14'
        self.etiquetas = self.regla14()
        'regla 15'
        self.etiquetas = self.regla15()
        'regla 16'
        self.etiquetas = self.regla16()
        'regla 17'
        self.etiquetas = self.regla17()
        'regla 18'
        self.etiquetas = self.regla18()
        #-----------------------#

        print('------------------Traduccion------------------------')
        self.trad3D()

        return self.optimizadas

    def trad3D(self):
        self.imprimir3D()
        for cod in self.C3D:
            print(cod)

    def testOpt(self):
        print('----------------------Start Optimizacion----------------')
        for etiqueta in self.etiquetas:  
            print(etiqueta)  
            for eti in self.etiquetas[etiqueta]:
                print(str(eti.getCuad()))
        
        print('----------------------End Optimizacion----------------')

    def printCuadruplos(self):
        print('----------------------Start Cuadruplos----------------')
        for etiqueta in self.etiquetas:  
            print(etiqueta)  
            for eti in self.etiquetas[etiqueta]:
                print(str(eti.getCuad()))
        
        print('----------------------End Cuadruplos----------------')

    def imprimir3D(self):
        self.codigo = ""
        for etiqueta in self.etiquetas:
            self.C3D.append(etiqueta+":")
            self.codigo += etiqueta+":\n" 
            for cuadruplo in self.etiquetas[etiqueta]:
                if cuadruplo.op == "if":
                    self.C3D.append("  if({0}) goto {1};".format(cuadruplo.arg1, cuadruplo.result))
                    self.codigo+="  if({0}) goto {1};".format(cuadruplo.arg1, cuadruplo.result)
                elif cuadruplo.op == "goto":
                    self.C3D.append("  goto {0};".format(cuadruplo.arg1))
                    self.codigo+="  goto {0};".format(cuadruplo.arg1)
                elif cuadruplo.op == "print":
                    self.C3D.append("  print({0});".format(cuadruplo.arg1))
                    self.codigo+="  print({0});".format(cuadruplo.arg1)
                elif cuadruplo.op == "exit":
                    self.C3D.append("  exit;")
                    self.codigo+=" exit;"
                elif cuadruplo.op != "=":
                    self.C3D.append("  {0}={1} {2} {3};".format(cuadruplo.result,cuadruplo.arg1, cuadruplo.op, cuadruplo.arg2))
                    self.codigo+="  {0}={1} {2} {3};".format(cuadruplo.result,cuadruplo.arg1, cuadruplo.op, cuadruplo.arg2)
                else:
                    self.C3D.append("  {0}={1}{2};".format(cuadruplo.result,cuadruplo.arg1,cuadruplo.arg2))
                    self.codigo+="  {0}={1}{2};".format(cuadruplo.result,cuadruplo.arg1,cuadruplo.arg2)
                self.codigo+="\n"
            self.C3D.append("")
            self.codigo+="\n"
    
    def regla1(self):
        etiquetas = {}
        cambios = {}
        for etiqueta in self.etiquetas:
            etiquetas[etiqueta] = []
            for cuadruplo in self.etiquetas[etiqueta]:
                ''#debemos ir buscando op con =
                pattern = r'(\$t[0-9]+)'
                match1 = re.match(pattern,str(cuadruplo.arg1))
                if cuadruplo.op == "=" and match1:
                    if len(etiquetas[etiqueta])!=0:
                        ant = etiquetas[etiqueta].pop()
                        if ant.result == cuadruplo.arg1 and (not '[' in cuadruplo.result) and (cuadruplo.arg2 !=" "):
                            self.add(ant,1)
                            cambios[ant.result] = cuadruplo.result
                            new = Cuadruplo(ant.op,ant.arg1,ant.arg2,cuadruplo.result)
                            etiquetas[etiqueta].append(new)
                            continue
                        else:
                            etiquetas[etiqueta].append(ant)
                        

                etiquetas[etiqueta].append(cuadruplo)

        return etiquetas
    
    def regla2(self):
        #objeto para almacenar etiquetas 
        etiquetas = {}
        eliminar = False
        for etiqueta in self.etiquetas:
            etiquetas[etiqueta] = []
            eliminar = False

            for cuadruplo in self.etiquetas[etiqueta]:
                if eliminar:
                    self.add(cuadruplo, 2)
                    continue
                if cuadruplo.op == "goto":
                    etiquetas[etiqueta].append(cuadruplo)
                    eliminar = True
                else:
                    etiquetas[etiqueta].append(cuadruplo)

        return etiquetas

    #Region para regla 3
    def regla3(self, pasada = 0):
        etiquetas = {}
        eliminadas = {}
        flag = False
        for etiqueta in self.etiquetas:
            if  not etiqueta in eliminadas:
                etiquetas[etiqueta] = []

                for i in range(len(self.etiquetas[etiqueta])):
                    if flag:
                        flag = False
                    else:
                        if self.etiquetas[etiqueta][i].op == "if":
                            if 0 != len(etiquetas[etiqueta]):
                                if i+1 < len(self.etiquetas[etiqueta]):
                                    if self.etiquetas[etiqueta][i+1].op == "goto":
                                        cuadruplo = etiquetas[etiqueta].pop()
                                        _if = self.etiquetas[etiqueta][i].result
                                        _if = _if.replace('L', 'if')
                                        goto_end = self.etiquetas[etiqueta][i+1]
                                        #generamos el nuevo if (negacion ) goto end
                                        new = self.generarIf(cuadruplo, goto_end.arg1)
                                        if not self.canChange(cuadruplo):
                                            etiquetas[etiqueta].append(cuadruplo)
                                        else:
                                            self.add(cuadruplo,3)
                                        if new:
                                            etiquetas[etiqueta].append(new)
                                            eliminadas[_if]=goto_end.arg1
                                            #obtendria todas las instrucciones del if
                                            for item in self.etiquetas[_if]:
                                                etiquetas[etiqueta].append(item)
                                            flag = True
                                            continue
                                    elif pasada == 0:
                                        cuadruplo = etiquetas[etiqueta].pop()
                                        self.add(cuadruplo,3)
                                        new = Cuadruplo("if", "{0}{1}{2}".format( cuadruplo.arg1, cuadruplo.op, cuadruplo.arg2),"goto" ,self.etiquetas[etiqueta][i].result)
                                        etiquetas[etiqueta].append(new)
                                        continue

                        etiquetas[etiqueta].append(self.etiquetas[etiqueta][i])


            else:
                etiquetas[etiqueta] = []
                #for cuadruplo in self.etiquetas[etiqueta]:
                    #self.add(cuadruplo,3)
        #una vez terminado el proceso seguimos a eliminar las etiquetas que cambiaron
        for etiqueta in eliminadas:
            self.add(etiqueta + ":",3)
            try:
                etiqueta = etiqueta.replace('L', 'if')
                del etiquetas[etiqueta]
            except KeyError:
                pass
        #recorremos la lista de nuevo en busca de if y goto que puedan tener las etiquetas
        for salto in eliminadas:
            for etiqueta in etiquetas:
                for cuadruplo in etiquetas[etiqueta]:
                    if cuadruplo.op == "if":
                        if cuadruplo.result == salto:
                            cuadruplo.result = eliminadas[salto]
                    elif cuadruplo.op == "goto":
                        if cuadruplo.arg1 == salto:
                            cuadruplo.arg1 = eliminadas[salto]

        return etiquetas

    def canChange(self,cuadruplo):
        op = cuadruplo.op
        change = False
        if op == ">":
            op = "<="
            change = True
        elif op == "<":
            op= ">="
            change = True
        elif op == ">=":
            op = "<"
            change = True
        elif op == "<=":
            op = ">"
            change = True
        elif op == "==":
            op = "!="
            change = True
        elif op =="!=":
            op  = "=="
            change = True
        return change
    def generarIf(self,cuadruplo, goto_end):
        op = cuadruplo.op
        change = False
        if op == '>':
            op = '<='
            change = True
        elif op == '<':
            op= '>='
            change = True
        elif op == '>=':
            op = '<'
            change = True
        elif op == '<=':
            op = '>'
            change = True
        elif op == '==':
            op = '!='
            change = True
        elif op =='!=':
            op  = '=='
            change = True
        
        if change:
            return Cuadruplo("if", "{0}{1}{2}".format( cuadruplo.arg1, op, cuadruplo.arg2),"goto" ,goto_end)
        elif cuadruplo.op == '=':
            return Cuadruplo("if","!"+cuadruplo.result,"goto",goto_end)
        else:
            return None
    #End Region para regla 3
    def regla4(self):
        etiquetas = {}
        for etiqueta in self.etiquetas:
            etiquetas[etiqueta] = []
            for cuadruplo in self.etiquetas[etiqueta]:
                ''
                if cuadruplo.op == "if":
                    ''
                    if cuadruplo.arg1 == "1==1":
                        ''
                        new_cuadruplo = Cuadruplo("goto", cuadruplo.result,"","")
                        etiquetas[etiqueta].append(new_cuadruplo)
                        self.add(cuadruplo, 4)
                        continue
                etiquetas[etiqueta].append(cuadruplo)

        return etiquetas

    def regla5(self):
        etiquetas = {}
        for etiqueta in self.etiquetas:
            etiquetas[etiqueta] = []
            for i in range(len(self.etiquetas[etiqueta])):
                ''
                if self.etiquetas[etiqueta][i].op == "if":
                    ''
                    if self.etiquetas[etiqueta][i].arg1 == "1==0":
                        ''
                        if i + 1 < len(self.etiquetas[etiqueta]):
                            ''
                            if self.etiquetas[etiqueta][i+1].op == "goto":
                                ''
                                new_cuadruplo = Cuadruplo("goto", self.etiquetas[etiqueta][i+1].arg1,"","")
                                etiquetas[etiqueta].append(new_cuadruplo)
                                self.add(self.etiquetas[etiqueta][i], 4)
                                continue
                            else:
                                ''
                        else:
                            ''
                    else:
                        ''
                etiquetas[etiqueta].append(self.etiquetas[etiqueta][i])
        return etiquetas
    
    def regla6(self):
        ''
        etiquetas = {}
        eliminadas = {}
        for etiqueta in self.etiquetas:
            etiquetas[etiqueta] = []
            for cuadruplo in self.etiquetas[etiqueta]:
                if cuadruplo.op == "goto":
                    ''
                    etiqueta_goto = cuadruplo.arg1
                    etiqueta_goto = etiqueta_goto.replace('L', 'if')
                    try:
                        if 1 == len(self.etiquetas[etiqueta_goto]):
                            ''
                            goto_temp = self.etiquetas[etiqueta_goto][0]
                            if goto_temp.op == "goto":
                                ''
                                self.add(cuadruplo,6)
                                new_salto = Cuadruplo("goto",goto_temp.arg1, "","")
                                etiquetas[etiqueta].append(new_salto)
                                eliminadas[etiqueta_goto] = goto_temp.arg1
                                continue
                    except KeyError:
                        pass
                etiquetas[etiqueta].append(cuadruplo)
        self.eliminadas = eliminadas
        indice = 0
        for salto in eliminadas:
            for etiqueta in etiquetas:
                indice = 0
                for cuadruplo in etiquetas[etiqueta]:
                    if cuadruplo.op == "if":
                        if cuadruplo.result == salto:
                             etiquetas[etiqueta][indice].result = eliminadas[salto]
                    elif cuadruplo.op == "goto":
                        if cuadruplo.arg1 == salto:
                            etiquetas[etiqueta][indice].arg1 = eliminadas[salto]
                    indice +=1

        return etiquetas

    def regla7(self):
        ''
        etiquetas = {}
        eliminadas = {}
        for etiqueta in self.etiquetas:
            etiquetas[etiqueta] = []
            for cuadruplo in self.etiquetas[etiqueta]:
                if cuadruplo.op == "if":
                    ''
                    etiqueta_goto = cuadruplo.result
                    etiqueta_got = etiqueta_goto.replace('L', 'if')
                    try:
                        if 1 == len(self.etiquetas[etiqueta_goto]):
                            ''
                            goto_temp = self.etiquetas[etiqueta_goto][0]
                            if goto_temp.op == "goto":
                                ''
                                self.add(cuadruplo,7)
                                new_salto = Cuadruplo("if",cuadruplo.arg1,cuadruplo.arg2,goto_temp.arg1)
                                etiquetas[etiqueta].append(new_salto)
                                eliminadas[etiqueta_goto] = goto_temp.arg1
                                continue
                    except KeyError:
                        pass
                etiquetas[etiqueta].append(cuadruplo)
        #una vez terminado el proceso seguimos a eliminar las etiquetas que cambiaron
        for etiqueta in self.eliminadas:
            self.add(etiqueta + ":",6)
            del etiquetas[etiqueta]

        for etiqueta in eliminadas:
            if etiqueta in etiquetas:
                self.add(etiqueta + ":",7)
                del etiquetas[etiqueta]
        #recorremos la lista de nuevo en busca de if y goto que puedan tener las etiquetas
        indice = 0
        for salto in eliminadas:
            for etiqueta in etiquetas:
                indice = 0
                for cuadruplo in etiquetas[etiqueta]:
                    if cuadruplo.op == "if":
                        if cuadruplo.result == salto:
                             etiquetas[etiqueta][indice].result = eliminadas[salto]
                    elif cuadruplo.op == "goto":
                        if cuadruplo.arg1 == salto:
                            etiquetas[etiqueta][indice].arg1 = eliminadas[salto]
                    indice +=1
        
        return etiquetas

    def regla8(self):
        etiquetas = {}
        for etiqueta in self.etiquetas:
            etiquetas[etiqueta] = []
            for cuadruplo in self.etiquetas[etiqueta]:
                ''
                if cuadruplo.op =="+":
                    if cuadruplo.arg1 == cuadruplo.result:
                        if str(cuadruplo.arg2) == "0":
                            self.add(cuadruplo,8)
                            continue
                    elif cuadruplo.arg2 == cuadruplo.result:
                        if str(cuadruplo.arg1) == "0":
                            self.add(cuadruplo,8)
                            continue
                etiquetas[etiqueta].append(cuadruplo)
                
        return etiquetas

    def regla9(self):
        etiquetas = {}
        for etiqueta in self.etiquetas:
            etiquetas[etiqueta] = []
            for cuadruplo in self.etiquetas[etiqueta]:
                ''
                if cuadruplo.op =="-":
                    if cuadruplo.arg1 == cuadruplo.result:
                        if str(cuadruplo.arg2) == "0":
                            self.add(cuadruplo,9)
                            continue
                etiquetas[etiqueta].append(cuadruplo)
                
        return etiquetas
    
    def regla10(self):
        etiquetas = {}
        for etiqueta in self.etiquetas:
            etiquetas[etiqueta] = []
            for cuadruplo in self.etiquetas[etiqueta]:
                ''
                if cuadruplo.op =="*":
                    if cuadruplo.arg1 == cuadruplo.result:
                        if str(cuadruplo.arg2) == "1":
                            self.add(cuadruplo,10)
                            continue
                    elif cuadruplo.arg2 == cuadruplo.result:
                        if str(cuadruplo.arg1) == "1":
                            self.add(cuadruplo,10)
                            continue
                etiquetas[etiqueta].append(cuadruplo)
                
        return etiquetas

    def regla11(self):
        etiquetas = {}
        for etiqueta in self.etiquetas:
            etiquetas[etiqueta] = []
            for cuadruplo in self.etiquetas[etiqueta]:
                ''
                if cuadruplo.op =="/":
                    if cuadruplo.arg1 == cuadruplo.result:
                        if str(cuadruplo.arg2) == "1":
                            self.add(cuadruplo,11)
                            continue
                etiquetas[etiqueta].append(cuadruplo)
                
        return etiquetas

    def regla12(self):
        ''
        etiquetas = {}
        for etiqueta in self.etiquetas:
            etiquetas[etiqueta] = []
            for cuadruplo in self.etiquetas[etiqueta]:
                ''
                if cuadruplo.op =="+":
                    if str(cuadruplo.arg1) == "0":
                        self.add(cuadruplo,12)
                        etiquetas[etiqueta].append(Cuadruplo("=",cuadruplo.arg2,"", cuadruplo.result))
                        continue
                    if str(cuadruplo.arg2) == "0":
                        self.add(cuadruplo,12)
                        etiquetas[etiqueta].append(Cuadruplo("=",cuadruplo.arg1,"", cuadruplo.result))
                        continue
                etiquetas[etiqueta].append(cuadruplo)
                
        return etiquetas

    def regla13(self):
        ''
        etiquetas = {}
        for etiqueta in self.etiquetas:
            etiquetas[etiqueta] = []
            for cuadruplo in self.etiquetas[etiqueta]:
                ''
                if cuadruplo.op =="-":
                    if str(cuadruplo.arg2) == "0":
                        self.add(cuadruplo,13)
                        etiquetas[etiqueta].append(Cuadruplo("=",cuadruplo.arg1,"", cuadruplo.result))
                        continue
                etiquetas[etiqueta].append(cuadruplo)
                
        return etiquetas

    def regla14(self):
        ''
        etiquetas = {}
        for etiqueta in self.etiquetas:
            etiquetas[etiqueta] = []
            for cuadruplo in self.etiquetas[etiqueta]:
                ''
                if cuadruplo.op =="*":
                    if str(cuadruplo.arg1) == "1":
                        self.add(cuadruplo,14)
                        etiquetas[etiqueta].append(Cuadruplo("=",cuadruplo.arg2,"", cuadruplo.result))
                        continue
                    if str(cuadruplo.arg2) == "1":
                        self.add(cuadruplo,14)
                        etiquetas[etiqueta].append(Cuadruplo("=",cuadruplo.arg1,"", cuadruplo.result))
                        continue
                etiquetas[etiqueta].append(cuadruplo)
                
        return etiquetas

    def regla15(self):
        ''
        etiquetas = {}
        for etiqueta in self.etiquetas:
            etiquetas[etiqueta] = []
            for cuadruplo in self.etiquetas[etiqueta]:
                ''
                if cuadruplo.op =="/":
                    if str(cuadruplo.arg2) == "1":
                        self.add(cuadruplo,15)
                        etiquetas[etiqueta].append(Cuadruplo("=",cuadruplo.arg1,"", cuadruplo.result))
                        continue
                etiquetas[etiqueta].append(cuadruplo)
                
        return etiquetas

    def regla16(self):
        ''
        etiquetas = {}
        for etiqueta in self.etiquetas:
            etiquetas[etiqueta] = []
            for cuadruplo in self.etiquetas[etiqueta]:
                ''
                if cuadruplo.op =="*":
                    if str(cuadruplo.arg1) == "2":
                        self.add(cuadruplo,16)
                        etiquetas[etiqueta].append(Cuadruplo("+",cuadruplo.arg2,cuadruplo.arg2, cuadruplo.result))
                        continue
                    if str(cuadruplo.arg2) == "2":
                        self.add(cuadruplo,16)
                        etiquetas[etiqueta].append(Cuadruplo("+",cuadruplo.arg1,cuadruplo.arg1, cuadruplo.result))
                        continue
                etiquetas[etiqueta].append(cuadruplo)
                
        return etiquetas

    def regla17(self):
        ''
        etiquetas = {}
        for etiqueta in self.etiquetas:
            etiquetas[etiqueta] = []
            for cuadruplo in self.etiquetas[etiqueta]:
                ''
                if cuadruplo.op =="*":
                    if str(cuadruplo.arg1) == "0":
                        self.add(cuadruplo,17)
                        etiquetas[etiqueta].append(Cuadruplo("=","0","", cuadruplo.result))
                        continue
                    if str(cuadruplo.arg2) == "0":
                        self.add(cuadruplo,17)
                        etiquetas[etiqueta].append(Cuadruplo("=","0", "", cuadruplo.result))
                        continue
                etiquetas[etiqueta].append(cuadruplo)
                
        return etiquetas

    def regla18(self):
        ''
        etiquetas = {}
        for etiqueta in self.etiquetas:
            etiquetas[etiqueta] = []
            for cuadruplo in self.etiquetas[etiqueta]:
                ''
                if cuadruplo.op =="/":
                    if str(cuadruplo.arg1) == "0":
                        self.add(cuadruplo,18)
                        etiquetas[etiqueta].append(Cuadruplo("=","0","", cuadruplo.result))
                        continue
        
                etiquetas[etiqueta].append(cuadruplo)
                
        return etiquetas

    def add(self, cuadruplo, regla):
        self.optimizadas.append({"linea":cuadruplo, "regla": regla})