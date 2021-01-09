from optimizacion.Instrucciones.C3D.AsignacionC3D import AsignacionC3D
from optimizacion.Instrucciones.C3D.MetodoC3D import MetodoC3D
from optimizacion.Instrucciones.C3D.AsignacionHSC3D import AsignacionHSC3D
from optimizacion.Instrucciones.C3D.ErrorOpt import ErrorOpt
from optimizacion.Instrucciones.C3D.GotoC3D import GotoC3D
from optimizacion.Instrucciones.C3D.LabelC3D import LabelC3D
from optimizacion.Instrucciones.C3D.SentenciaIf import SentenciaIf

class Mirillas():

    def __init__(self,instrucciones):
        self.instrucciones = instrucciones
        self.reporteOptimizacion = []
        print("ENTRO A Mirillas")
    
    def addItemReporte(self, reporte):
        self.reporteOptimizacion.append(reporte)
    
    def getItemReporte(self):
        return self.reporteOptimizacion

    def optimizarCodigo(self):
        self.regla1()
        self.regla7()
        self.regla3()
        self.regla4()
        self.regla5()
        self.regla6()
        self.regla2()
        self.regla8()
        self.regla9()
        self.regla10()
        self.regla11()
        self.regla12()
        self.regla13()
        self.regla14()
        self.regla15()
        self.regla16()
        self.regla17()
        self.regla18()
    
    
    def regla1(self):
        self.regla1_aplicar(self.instrucciones)
        pass

    def regla1_aplicar(self, instrucciones):
        i = 0
        tam = len(instrucciones)
        tam = tam-1
        while i < tam:
            ins = instrucciones[i]
            ins2 = instrucciones[i+1]
            if isinstance(ins , AsignacionC3D) and isinstance(ins2 , AsignacionC3D):
                if(ins.id[0] == ins2.op1):
                    if(ins.op1 == ins2.id[0]):
                        y = i+1
                        print("aqui se optimizo Regla 1")
                        self.addItemReporte(ErrorOpt("1", "t2 = b;  b = t2; -> t2 = b;", ins.linea, ins.getC3D(), "eliminación duplicada"))
                        instrucciones.pop(y)
                        tam -= 1
                        i += 1
            i += 1

    def regla2(self):
        self.regla2_aplicar(self.instrucciones)
        pass

    '''
    goto L1;
        <instrucciones>
    L1:
    '''
    def regla2_aplicar(self, instrucciones):
        i = 1
        tam = len(instrucciones)
        regla2 = ""
        activada = False
        listaTemporal = []
        listaActual = ""
        while i < tam:
            ins = instrucciones[i-1]
            ins2 = instrucciones[i]
            if isinstance(ins , GotoC3D):
                regla2 = ins.valor
                activada = True

            if(activada == True):                
                if isinstance(ins2 , LabelC3D):
                    if(regla2 == ins2.valor):
                        print("aqui se optimizo regla 2")
                        s = i-1
                        listaTemporal.append(s)
                        ca = "se elimino la linea del Goto y la de instrucciones"
                        for k in reversed(range(0,len(listaTemporal))):
                            z = listaTemporal[k]
                            instrucciones.pop(z)
                            tam = tam - 1
                        self.addItemReporte(ErrorOpt("2", "goto .L1 <instrucciones> label .L1  --> label .L1", ins.linea, ca, "eliminación de goto e instrucciones"))
                        activada = False
                else:
                    s = i-1
                    listaTemporal.append(s)
                    print("aqui agregamos a lista")
            i += 1
        
    def regla3(self):
        self.regla3_aplicar(self.instrucciones)
        pass

    '''
        if a == 10 goto L1;
        goto L2;
        L1:
        <instrucciones>
        L2:
    '''
    def regla3_aplicar(self, instrucciones):
        i = 0
        tam = len(instrucciones)
        band = False
        gotoFinal = ""
        listaDeInstrucciones = []
        ca = ""
        posV = ""
        posF = ""
        posLV = ""
        while i < tam:
            print(i)
            ins = instrucciones[i]
            
            if(band == True):
                listaDeInstrucciones.append(ins)
                print("agregar regla")
            
            if(isinstance(ins ,SentenciaIf) and tam > i+3 ):
                gotoV = instrucciones[i+1]
                posV = i+1
                gotoF = instrucciones[i+2]
                posF = i+2
                LV = instrucciones[i+3]
                posLV = i+3
                if(isinstance(gotoV,GotoC3D) and isinstance(gotoF,GotoC3D) and isinstance(LV,LabelC3D)):
                    if(gotoV.valor == LV.valor):
                        i += 3
                        band = True
                        gotoFinal = gotoF
    
            if(isinstance(ins,LabelC3D) and band == True):
                LF = instrucciones[i]
                if(LF.valor == gotoFinal.valor):
                    #aqui tenemos que cambiar el simbolo
                    #"aqui vamos a cambiar el goto"
                    #"aqui vamos a eliminar"
                    instrucciones.pop(posLV)
                    instrucciones.pop(posV)
                    self.addItemReporte(ErrorOpt("3", " if <cond> goto Lv; goto Lf; Lv: <instrucciones> Lf", ins.linea, ca, "if (!<cond>) goto Lf; <instrucciones> Lf: "))    
                    band = False
                    tam = tam - 2
            i += 1

    def regla4(self):
        self.regla4_aplicar(self.instrucciones)
        pass

    '''
    if 1 == 1 goto L1;
    goto L2;
    '''
    def regla4_aplicar(self, instrucciones):
        i = 0
        tam = len(instrucciones)
        band = False
        gotoFinal = ""
        ca = ""
        while i < tam:
            print(i)
            ins = instrucciones[i]
            posIns = i
            if(isinstance(ins ,SentenciaIf) and tam > i+2):
                gotoV = instrucciones[i+1]
                posV = i+1
                gotoF = instrucciones[i+2]
                posF = i-1
                if(isinstance(gotoV,GotoC3D) and isinstance(gotoF,GotoC3D)):
                    if(ins.opIzq == ins.opDer and ins.relacional == "="):
                        instrucciones.pop(posF)
                        instrucciones.pop(posIns)
                        tam = tam - 2
                        self.addItemReporte(ErrorOpt("4", " if <cond> goto Lv; goto Lf; --> goto Lv", ins.linea, ca, "se elimina el if y goto lf"))
                    #i+=2
            i += 1

    def regla5(self):
        self.regla5_aplicar(self.instrucciones)
        pass

    '''
    if 1 == 0 goto L1;
    goto L2;
    '''
    def regla5_aplicar(self, instrucciones):
        i = 0
        tam = len(instrucciones)
        band = False
        gotoFinal = ""
        ca = ""
        while i < tam:
            print(i)
            ins = instrucciones[i]
            posIns = i
            if(isinstance(ins ,SentenciaIf)):
                gotoV = instrucciones[i+1]
                posV = i+1
                gotoF = instrucciones[i+2]
                posF = i-1
                if(isinstance(gotoV,GotoC3D) and isinstance(gotoF,GotoC3D)):
                    if(ins.opIzq != ins.opDer and ins.relacional == "<>"):
                        instrucciones.pop(posF)
                        instrucciones.pop(posIns)
                        tam = tam - 2
                        self.addItemReporte(ErrorOpt("5", " if <cond> goto Lv; goto Lf; --> goto Lf", ins.linea, ca, "se elimina el if y goto lv"))
                    #i+=2
            i += 1

    def regla6(self):
        self.regla6_aplicar(self.instrucciones)
        pass

    '''
    goto L1
        <instrucciones>
    L1:
    goto L2
    '''

    def regla6_aplicar(self, instrucciones):
        i = 0
        tam = len(instrucciones)
        bandG = False
        labelG = False
        gotoFinal = ""
        ApuntadorLabelG = ""
        ApuntadorBandera = ""
        ca = ""
        while i < tam:
            print(i)
            ins = instrucciones[i]
            
            if(bandG == True):
                print("agregar instruccion")

            if(isinstance(ins ,LabelC3D)):
                labelG = True
                ApuntadorLabelG = ins.valor
            
            if(isinstance(ins ,GotoC3D)):
                if(bandG == False):
                    bandG = True
                    ApuntadorBandera = ins
                    posiBandera = i
                    print("agregar instruccion")
                else:
                    if(bandG == True and labelG == True):
                        print("aqui se va a cambiar")
                        if(ApuntadorBandera):
                            ApuntadorBandera.valor = ins.valor
                            instrucciones[posiBandera] = ApuntadorBandera
                            self.addItemReporte(ErrorOpt("6", "goto Lv <instrucciones> Lv: goto Lf", ins.linea, ca, "se remplaza goto Lv por goto LF;"))
            i += 1
    
    def regla7(self):
        self.regla7_aplicar(self.instrucciones)
        pass

    '''
    if t9 >= t10 goto L1;
        <instrucciones>
    L1:
    goto L2;
    '''
    def regla7_aplicar(self, instrucciones):
        i = 0
        tam = len(instrucciones)
        band = False
        gotoFinal = ""
        gotoF = None
        ca = ""
        posIns = ""
        while i < tam:
            print(i)
            ins = instrucciones[i]
            if(isinstance(ins ,SentenciaIf)):
                gotoV = instrucciones[i+1]
                posIns = i+1
                labelV = instrucciones[i+2]
                if(isinstance(labelV,GotoC3D)):
                    return ""
                
                if(isinstance(labelV,LabelC3D)):
                    if(isinstance(gotoV,GotoC3D)):
                        band = True
                        i += 2

            if(band == True):
                if(isinstance(ins,LabelC3D)):
                    gotoV.valor = ins.valor
                    instrucciones[posIns] = gotoV
                    self.addItemReporte(ErrorOpt("7", "goto Lv <instrucciones> Lv: goto Lf", ins.linea, ca, "se remplaza el goto;"))
                    band = False
            
            i += 1
    
    def regla8(self):
        self.regla8_aplicar(self.instrucciones)
        pass

    def regla8_aplicar(self, instrucciones):
        y = 0
        for x in range(0, len(instrucciones)):
            ins = instrucciones[y]
            if isinstance(ins , AsignacionC3D):
                id = ins.id[0]
                res = ins.getOp1()
                if(isinstance(res, (float, int, str))):
                    pass
                else:
                    op1 = res.id
                    op2 = res.op2
                    operador = res.op1
                    if(id == op1 and operador == "+" and op2 == 0) or (id == op2 and operador == "+" and op1 == 0):
                        self.addItemReporte(ErrorOpt("8", "Simplificacion algebraica: X = X + 0", ins.linea, ins.getC3D(), "Instruccion eliminada"))
                        self.instrucciones.pop(y)
                        y -= 1
            y += 1

    def regla9(self):
        self.regla9_aplicar(self.instrucciones)
        pass


    def regla9_aplicar(self, instrucciones):
        y = 0
        for x in range(0, len(instrucciones)):
            ins = instrucciones[y]
            if isinstance(ins, AsignacionC3D):
                id = ins.id[0]
                res = ins.getOp1()
                if(isinstance(res, (float, int, str))):
                    pass
                else:
                    op1 = res.id
                    op2 = res.op2
                    operador = res.op1
                    if id == op1 and str(op2) == "0" and operador == "-":
                        self.addItemReporte(ErrorOpt("9", "Simplificacion algebraica: X = X - 0", str(ins.linea), ins.getC3D(), "Instruccion eliminada"))
                        instrucciones.pop(y)
                        y -= 1
            y += 1


    def regla10(self):
        self.regla10_aplicar(self.instrucciones)
        pass
    
    def regla10_aplicar(self, instrucciones):
        y = 0
        for x in range(0, len(instrucciones)):
            ins = instrucciones[y]
            if isinstance(ins, AsignacionC3D):
                id = ins.id[0]
                res = ins.getOp1()
                if(isinstance(res, (float, int, str))):
                    pass
                else:
                    op1 = res.id
                    op2 = res.op2
                    operador = res.op1
                    if (id == op1 and str(op2) == "1" and operador == "*") or (id == op2 and str(op1) == "1" and operador == "*"):
                        self.addItemReporte(ErrorOpt("10", "Simplificacion algebraica: X = X * 1", str(ins.linea), ins.getC3D(), "Instruccion eliminada"))
                        instrucciones.pop(y)
                        y -= 1
            y += 1


    def regla11(self):
        self.regla11_aplicar(self.instrucciones)
        pass

    
    def regla11_aplicar(self, instrucciones):
        y = 0
        for x in range(0, len(instrucciones)):
            ins = instrucciones[y]
            if isinstance(ins, AsignacionC3D):
                id = ins.id[0]
                res = ins.getOp1()
                if(isinstance(res, (float, int, str))):
                    pass
                else:
                    op1 = res.id
                    op2 = res.op2
                    operador = res.op1
                    if (id == op1 and str(op2) == "1" and operador == "/"):
                        self.addItemReporte(ErrorOpt("11", "Simplificacion algebraica: X = X / 1", str(ins.linea), ins.getC3D(), "Instruccion eliminada"))
                        instrucciones.pop(x)
                        y -= 1
            y += 1
    


    def regla12(self):
        self.regla12_aplicar(self.instrucciones)
        pass

    
    def regla12_aplicar(self, instrucciones):
        for x in range(0, len(instrucciones)):
            ins = instrucciones[x]
            if isinstance(ins , AsignacionC3D):
                id = ins.id
                res = ins.getOp1()
                if(isinstance(res, (float, int, str))):
                    pass
                else:
                    op1 = res.id
                    op2 = res.op2
                    operador = res.op1
                    if(id != op1 and operador == "+" and str(op2) == "0"):
                        antes = ins.getC3D()
                        cade = str(ins.id[0]) + " = " + op1
                        self.addItemReporte( ErrorOpt("12", "Simplificacion algebraica: X = Y + 0 ->  X = Y", str(ins.linea), antes,cade))
                        
                    elif id != op2 and operador == "+" and str(op1) == "0":
                        antes = ins.getC3D()
                        cade = str(ins.id[0]) + " = " + op2
                        self.addItemReporte( ErrorOpt("12", "Simplificacion algebraica: X = 0 + Y ->  X = Y", str(ins.linea), antes,cade))
                        
    def regla13(self):
        self.regla13_aplicar(self.instrucciones)
        pass
    
    def regla13_aplicar(self, instrucciones):
        for x in range(0, len(instrucciones)):
            ins = instrucciones[x]
            if isinstance(ins , AsignacionC3D):
                id = ins.id
                res = ins.getOp1()
                if(isinstance(res, (float, int, str))):
                    pass
                else:
                    op1 = res.id
                    op2 = res.op2
                    operador = res.op1
                    if( id != op1 and operador == "-" and str(op2) == "0" ):
                        antes = ins.getC3D()
                        cade  = str(ins.id) + " = " + str(op1)
                        self.addItemReporte( ErrorOpt("13", "Simplificacion algebraica: X = Y - 0 ->  X = Y", str(ins.linea), antes, cade))
                    
    def regla14(self):
        self.regla14_aplicar(self.instrucciones)
        pass

    def regla14_aplicar(self, instrucciones):
        for x in range(0, len(instrucciones)):
            ins = instrucciones[x]
            if isinstance(ins , AsignacionC3D):
                id = ins.id
                res = ins.getOp1()
                if(isinstance(res, (float, int, str))):
                    pass
                else:
                    op1 = res.id
                    op2 = res.op2
                    operador = res.op1
                    if(id != op1 and operador == "*" and str(op2) == "1"):
                        antes = ins.getC3D()
                        cade  = str(ins.id) + " = " + str(op1)
                        self.addItemReporte( ErrorOpt("14", "Simplificacion algebraica: X = Y * 1 ->  X = Y", str(ins.linea), antes, cade))
                        
                    elif id != op2 and operador == "*" and op1 == "1":
                        antes = ins.getC3D()
                        
                        self.addItemReporte( ErrorOpt("14", "Simplificacion algebraica: X = 1 * Y ->  X = Y", str(ins.linea), antes, cade))
                    

    def regla15(self):
        self.regla15_aplicar(self.instrucciones)
        pass

    def regla15_aplicar(self, instrucciones):
        for x in range(0, len(instrucciones)):
            ins = instrucciones[x]
            if isinstance(ins , AsignacionC3D):
                id = ins.id
                res = ins.getOp1()
                if(isinstance(res, (float, int, str))):
                    pass
                else:
                    op1 = res.id
                    op2 = res.op2
                    operador = res.op1
                    if( id != op1 and operador == "/" and str(op2) == "1" ):
                        antes = ins.getC3D()
                        cade  = str(ins.id) + " = " + str(op1)
                        self.addItemReporte( ErrorOpt("15", "Simplificacion algebraica: X = Y / 1 ->  X = Y", str(ins.linea), antes, ins.getC3D()) )
                    
    def regla16(self):
        self.regla16_aplicar(self.instrucciones)
        pass

    def regla16_aplicar(self, instrucciones):
        for x in range(0, len(instrucciones)):
            ins = instrucciones[x]
            if isinstance(ins , AsignacionC3D):
                id = ins.id
                res = ins.getOp1()
                if(isinstance(res, (float, int, str))):
                    pass
                else:
                    op1 = res.id
                    op2 = res.op2
                    operador = res.op1
                    if(id != op1 and operador == "*" and str(op2) == "2"):
                        antes = ins.getC3D()
                        cade  = str(ins.id) + " = " + str(op1) + " " +  operador + " " + str(op1)
                        self.addItemReporte( ErrorOpt("16", "Simplificacion algebraica: X = Y * 2 ->  X = Y + Y", str(ins.linea), antes, cade))
                    elif id != op2 and operador == "*" and str(op1) == "2":
                        antes = ins.getC3D()
                        cade  = str(ins.id) + " = " + str(op2) + " " +  operador + " " + str(op2)
                        self.addItemReporte( ErrorOpt("16", "Simplificacion algebraica: X = 2 * Y ->  X = Y + Y", str(ins.linea), antes, cade))
                    
    def regla17(self):
        self.regla17_aplicar(self.instrucciones)
        pass

    def regla17_aplicar(self, instrucciones):
        for x in range(0, len(instrucciones)):
            ins = instrucciones[x]
            if isinstance(ins , AsignacionC3D):
                id = ins.id
                res = ins.getOp1()
                if(isinstance(res, (float, int, str))):
                    pass
                else:
                    op1 = res.id
                    op2 = res.op2
                    operador = res.op1
                    if(id != op1 and operador == "*" and str(op2) == "0"):
                        antes = ins.getC3D()
                        cade  = str(ins.id) + " = 0" 
                        self.addItemReporte( ErrorOpt("17", "Simplificacion algebraica: X = Y * 0 ->  X = 0", str(ins.linea), antes, cade))
                    elif id != op2 and operador == "*" and str(op1) == "0":
                        antes = ins.getC3D()
                        cade  = str(ins.id) + " = 0"
                        self.addItemReporte( ErrorOpt("17", "Simplificacion algebraica: X = 0 * Y ->  X = 0", str(ins.linea), antes, cade))
                    

    def regla18(self):
        self.regla18_aplicar(self.instrucciones)
        pass
    
    def regla18_aplicar(self, instrucciones):
        for x in range(0, len(instrucciones)):
            ins = instrucciones[x]
            if isinstance(ins , AsignacionC3D):
                id = ins.id
                res = ins.getOp1()
                if(isinstance(res, (float, int, str))):
                    pass
                else:
                    op1 = res.id
                    op2 = res.op2
                    operador = res.op1
                    if( id != op2 and operador == "/" and str(op1) == "0" ):
                        antes = ins.getC3D()
                        cade  = str(ins.id) + " = 0"
                        self.addItemReporte( ErrorOpt("18", "Simplificacion algebraica: X = 0 / Y ->  X = 0", str(ins.linea), antes, cade))
                    