from tabla_Simbolos import simbolo
from tabla_Simbolos import tipoSimbolo
from tabla_Simbolos import simboloColumna

class NodoPosicion():

    def __init__(self,fila,columna):
        self.fila = fila
        self.columna = columna
        self.tipoDatoResultado = None
        self.tipoOperacion = None
        
    
    def operar(self,tipoOperacion):        

        if (self.fila == 0 and self.columna == 0):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores smallInt")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.smallInt)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.smallInt)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.smallInt)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.smallInt)
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.smallInt)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.smallInt)
                return simb
            
        elif (self.fila == 0 and self.columna == 1):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores smallInt - Integer")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.integer)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.integer)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo Integer no puede ser contenido dentro de una columna tipo smallInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.integer)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.integer)
                return simb
        elif (self.fila == 0 and self.columna == 2):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores smallInt - bigInt")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.bigInit)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.bigInit)
                return simb                
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo bigInt no puede ser contenido dentro de una columna tipo smallInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.bigInit)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.bigInit)
                return simb
            
        elif (self.fila == 0 and self.columna == 3):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores smallInt - decimal")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo decimal no puede ser contenido dentro de una columna tipo smallInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)
                return simb
            
        elif (self.fila == 0 and self.columna == 4):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores smallInt - numeric")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo numeric no puede ser contenido dentro de una columna tipo smallInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.numeric)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simb
        elif (self.fila == 0 and self.columna == 5):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores smallInt - real")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo real no puede ser contenido dentro de una columna tipo smallInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.real)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb
        elif (self.fila == 0 and self.columna == 6):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores smallInt - double")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo double no puede ser contenido dentro de una columna tipo smallInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb
        elif (self.fila == 0 and self.columna == 7):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores smallInt - money")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo money no puede ser contenido dentro de una columna tipo smallInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb
        elif (self.fila == 0 and self.columna == 8):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores smallInt - varchar")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.varchar)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo varchar no puede ser contenido dentro de una columna tipo smallInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores smallInt - varchar")
                return simb
        elif (self.fila == 0 and self.columna == 9):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores smallInt - char")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.character)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo char no puede ser contenido dentro de una columna tipo smallInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores smallInt - char")
                return simb
        elif (self.fila == 0 and self.columna == 10):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores smallInt - text")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo text no puede ser contenido dentro de una columna tipo smallInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores smallInt - text")
                return simb
        elif (self.fila == 0 and self.columna == 11):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores smallInt - date")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion == tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.date)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.date)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores smallInt - date")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo date no puede ser contenido dentro de una columna tipo smallInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores smallInt - date")
                return simb
        elif (self.fila == 0 and self.columna == 12):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores smallInt - Time withOut time zone")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion == tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_No_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_No_zone)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores smallInt - withOut time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time withOut time zone no puede ser contenido dentro de una columna tipo smallInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores smallInt - withOut time zone")
                return simb
        elif (self.fila == 0 and self.columna == 13):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores smallInt - time with time zone")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion == tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_si_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_si_zone)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores smallInt - time with time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time with time zone no puede ser contenido dentro de una columna tipo smallInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores smallInt - time with time zone")
                return simb
        elif (self.fila == 0 and self.columna == 14):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()                
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores smallInt - boolean")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores smallInt - boolean")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo boolean no puede ser contenido dentro de una columna tipo smallInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones:suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores smallInt - boolean")
                return simb

        # ********************************************************************************************
        # ************************************* FILA 1 ***********************************************
        # #*******************************************************************************************
        if (self.fila == 1 and self.columna == 0):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores Integer - smallInt")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.integer)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.integer)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.integer)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.integer)
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.integer)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.integer)
                return simb
            
        elif (self.fila == 1 and self.columna == 1):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores Integer")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.integer)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.integer)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.integer)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.integer)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.integer)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.integer)
                return simb
        elif (self.fila == 1 and self.columna == 2):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores integer - bigInt")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.bigInit)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.bigInit)
                return simb                
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo bigInt no puede ser contenido dentro de una columna tipo Integer")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.bigInit)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.bigInit)
                return simb
            
        elif (self.fila == 1 and self.columna == 3):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores Integer - decimal")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo decimal no puede ser contenido dentro de una columna tipo Integer")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)
                return simb
            
        elif (self.fila == 1 and self.columna == 4):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores Integer - numeric")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo numeric no puede ser contenido dentro de una columna tipo Integer")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.numeric)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simb
        elif (self.fila == 1 and self.columna == 5):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores Integer - real")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo real no puede ser contenido dentro de una columna tipo Integer")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.real)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb
        elif (self.fila == 1 and self.columna == 6):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores Integer - double")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo double no puede ser contenido dentro de una columna tipo Integer")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb
        elif (self.fila == 1 and self.columna == 7):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores Integer - money")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo money no puede ser contenido dentro de una columna tipo Integer")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb
        elif (self.fila == 1 and self.columna == 8):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores integer - varchar")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.varchar)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo varchar no puede ser contenido dentro de una columna tipo integer")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores integer - varchar")
                return simb
        elif (self.fila == 1 and self.columna == 9):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores integer - char")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.character)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo char no puede ser contenido dentro de una columna tipo Integer")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores integer - char")
                return simb
        elif (self.fila == 1 and self.columna == 10):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores integer - text")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo text no puede ser contenido dentro de una columna tipo integer")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores integer - text")
                return simb
        elif (self.fila == 1 and self.columna == 11):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores integer - date")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion == tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.date)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.date)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores integer - date")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo date no puede ser contenido dentro de una columna tipo integer")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores integer - date")
                return simb
        elif (self.fila == 1 and self.columna == 12):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores integer - Time withOut time zone")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion == tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_No_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_No_zone)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores integer - withOut time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time withOut time zone no puede ser contenido dentro de una columna tipo integer")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores integer - withOut time zone")
                return simb
        elif (self.fila == 1 and self.columna == 13):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores integer - time with time zone")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion == tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_si_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_si_zone)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores integer - time with time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time with time zone no puede ser contenido dentro de una columna tipo integer")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores integer - time with time zone")
                return simb
        elif (self.fila == 1 and self.columna == 14):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()                
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores integer - boolean")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores integer - boolean")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo boolean no puede ser contenido dentro de una columna tipo integer")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones:suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores integer - boolean")
                return simb
        
        # ********************************************************************************************
        # ************************************* FILA 2 ***********************************************
        # #*******************************************************************************************
        if (self.fila == 2 and self.columna == 0):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores bigInt - smallInt")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.bigInit)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.bigInit)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.bigInit)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.bigInit)
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.bigInit)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.bigInit)
                return simb
            
        elif (self.fila == 2 and self.columna == 1):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores bigInt - Integer")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.bigInit)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.bigInit)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.bigInit)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.bigInit)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.bigInit)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.bigInit)
                return simb
        elif (self.fila == 2 and self.columna == 2):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores bigInt - bigInt")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.bigInit)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.bigInit)
                return simb                
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.bigInit)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.bigInit)                                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.bigInit)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.bigInit)
                return simb
            
        elif (self.fila == 2 and self.columna == 3):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores bigInt - decimal")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo decimal no puede ser contenido dentro de una columna tipo bigInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)
                return simb
            
        elif (self.fila == 2 and self.columna == 4):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores bigInt - numeric")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo numeric no puede ser contenido dentro de una columna tipo bigInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.numeric)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simb
        elif (self.fila == 2 and self.columna == 5):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores bigInt - real")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo real no puede ser contenido dentro de una columna tipo bigInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.real)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb
        elif (self.fila == 2 and self.columna == 6):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores bigInit - double")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo double no puede ser contenido dentro de una columna tipo bigInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb
        elif (self.fila == 2 and self.columna == 7):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores bigInit - money")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo money no puede ser contenido dentro de una columna tipo bigInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb
        elif (self.fila == 2 and self.columna == 8):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores bigInt - varchar")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.varchar)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo varchar no puede ser contenido dentro de una columna tipo bigInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores bigInt - varchar")
                return simb
        elif (self.fila == 2 and self.columna == 9):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores bigInt - char")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.character)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo char no puede ser contenido dentro de una columna tipo bigInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores bigInt - char")
                return simb
        elif (self.fila == 2 and self.columna == 10):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores bigInt - text")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo text no puede ser contenido dentro de una columna tipo bigInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores bigInt - text")
                return simb
        elif (self.fila == 2 and self.columna == 11):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores bigInt - date")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion == tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.date)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.date)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores bigInt - date")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo date no puede ser contenido dentro de una columna tipo bigInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores bigInt - date")
                return simb
        elif (self.fila == 2 and self.columna == 12):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores bigInt - Time withOut time zone")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion == tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_No_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_No_zone)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores bigInt - withOut time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time withOut time zone no puede ser contenido dentro de una columna tipo bigInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores bigInt - withOut time zone")
                return simb
        elif (self.fila == 2 and self.columna == 13):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores bigInt - time with time zone")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion == tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_si_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_si_zone)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores bigInt - time with time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time with time zone no puede ser contenido dentro de una columna tipo bigInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores bigInt - time with time zone")
                return simb
        elif (self.fila == 2 and self.columna == 14):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()                
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores bigInt - boolean")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores bigInt - boolean")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo boolean no puede ser contenido dentro de una columna tipo bigInt")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones:suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores bigInt - boolean")
                return simb
        # ********************************************************************************************
        # ************************************* FILA 3 ***********************************************
        # #*******************************************************************************************
        if (self.fila == 3 and self.columna == 0):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores decimal - smallInt")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)
                return simb
            
        elif (self.fila == 3 and self.columna == 1):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores decimal - Integer")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)
                return simb
        elif (self.fila == 3 and self.columna == 2):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores decimal - bigInt")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)
                return simb                
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)                                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)
                return simb
            
        elif (self.fila == 3 and self.columna == 3):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores decimal - decimal")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)
                return simb
            
        elif (self.fila == 3 and self.columna == 4):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores decimal - numeric")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.numeric)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simb
        elif (self.fila == 3 and self.columna == 5):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores decimal - real")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.decimal)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)
                return simb
        elif (self.fila == 3 and self.columna == 6):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores decimal - double")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo double no puede ser contenido dentro de una columna tipo decimal")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb
        elif (self.fila == 3 and self.columna == 7):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores decimal - money")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo money no puede ser contenido dentro de una columna tipo decimal")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb
        elif (self.fila == 3 and self.columna == 8):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores decimal - varchar")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.varchar)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo varchar no puede ser contenido dentro de una columna tipo decimal")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores decimal - varchar")
                return simb
        elif (self.fila == 3 and self.columna == 9):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores decimal - char")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.character)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo char no puede ser contenido dentro de una columna tipo decimal")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores decimal - char")
                return simb
        elif (self.fila == 3 and self.columna == 10):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores decimal - text")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo text no puede ser contenido dentro de una columna tipo decimal")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores decimal - text")
                return simb
        elif (self.fila == 3 and self.columna == 11):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores decimal - date")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion == tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.date)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.date)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores decimal - date")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo date no puede ser contenido dentro de una columna tipo decimal")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores decimal - date")
                return simb
        elif (self.fila == 3 and self.columna == 12):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores decimal - Time withOut time zone")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion == tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_No_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_No_zone)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores decimal - withOut time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time withOut time zone no puede ser contenido dentro de una columna tipo decimal")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores decimal - withOut time zone")
                return simb
        elif (self.fila == 3 and self.columna == 13):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores decimal - time with time zone")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion == tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_si_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_si_zone)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores decimal - time with time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time with time zone no puede ser contenido dentro de una columna tipo decimal")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores decimal - time with time zone")
                return simb
        elif (self.fila == 3 and self.columna == 14):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()                
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores decimal - boolean")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores decimal - boolean")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo boolean no puede ser contenido dentro de una columna tipo decimal")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones:suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores decimal - boolean")
                return simb
        # ********************************************************************************************
        # ************************************* FILA 4 ***********************************************
        # #*******************************************************************************************
        if (self.fila == 4 and self.columna == 0):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores numeric - smallInt")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.numeric)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.numeric)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.numeric)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simb
            
        elif (self.fila == 4 and self.columna == 1):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores numeric - Integer")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.numeric)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.numeric)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.numeric)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simb
        elif (self.fila == 4 and self.columna == 2):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores numeric - bigInt")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.numeric)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simb                
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.numeric)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)                                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.numeric)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simb
            
        elif (self.fila == 4 and self.columna == 3):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores numeric - decimal")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.numeric)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.numeric)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simb
            
        elif (self.fila == 4 and self.columna == 4):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores numeric - numeric")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.numeric)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.numeric)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simb
        elif (self.fila == 4 and self.columna == 5):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores numeric - real")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo real no puede ser contenido dentro de una columna tipo numeric")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.real)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb
        elif (self.fila == 4 and self.columna == 6):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores numeric - double")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo double no puede ser contenido dentro de una columna tipo numeric")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb
        elif (self.fila == 4 and self.columna == 7):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores numeric - money")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo money no puede ser contenido dentro de una columna tipo numeric")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb
        elif (self.fila == 4 and self.columna == 8):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores numeric - varchar")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.varchar)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo varchar no puede ser contenido dentro de una columna tipo numeric")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores numeric - varchar")
                return simb
        elif (self.fila == 4 and self.columna == 9):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores numeric - char")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.character)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo char no puede ser contenido dentro de una columna tipo numeric")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores numeric - char")
                return simb
        elif (self.fila == 4 and self.columna == 10):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores numeric - text")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo text no puede ser contenido dentro de una columna tipo numeric")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores numeric - text")
                return simb
        elif (self.fila == 4 and self.columna == 11):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores numeric - date")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion == tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.date)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.date)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores numeric - date")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo date no puede ser contenido dentro de una columna tipo numeric")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores numeric - date")
                return simb
        elif (self.fila == 4 and self.columna == 12):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores numeric - Time withOut time zone")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion == tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_No_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_No_zone)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores numeric - withOut time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time withOut time zone no puede ser contenido dentro de una columna tipo numeric")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores numeric - withOut time zone")
                return simb
        elif (self.fila == 4 and self.columna == 13):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores numeric - time with time zone")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion == tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_si_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_si_zone)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores bigInt - numeric with time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time with time zone no puede ser contenido dentro de una columna tipo numeric")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores numeric - time with time zone")
                return simb
        elif (self.fila == 4 and self.columna == 14):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()                
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores numeric - boolean")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores numeric - boolean")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo boolean no puede ser contenido dentro de una columna tipo numeric")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones:suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores numeric - boolean")
                return simb
        # ********************************************************************************************
        # ************************************* FILA 5 ***********************************************
        # #*******************************************************************************************
        if (self.fila == 5 and self.columna == 0):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores real - smallInt")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.real)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.real)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.real)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb
            
        elif (self.fila == 5 and self.columna == 1):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores real - Integer")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.real)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.real)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.real)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb
        elif (self.fila == 5 and self.columna == 2):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores real - bigInt")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.real)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb                
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.real)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)                                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.real)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb
            
        elif (self.fila == 5 and self.columna == 3):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores real - decimal")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.real)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.real)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb
            
        elif (self.fila == 5 and self.columna == 4):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores real - numeric")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.real)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.real)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb
        elif (self.fila == 5 and self.columna == 5):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores real - real")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.real)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.real)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simb
        elif (self.fila == 5 and self.columna == 6):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores real - double")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo double no puede ser contenido dentro de una columna tipo real")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb
        elif (self.fila == 5 and self.columna == 7):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores real - money")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo money no puede ser contenido dentro de una columna tipo real")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb
        elif (self.fila == 5 and self.columna == 8):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores real - varchar")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.varchar)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo varchar no puede ser contenido dentro de una columna tipo real")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores real - varchar")
                return simb
        elif (self.fila == 5 and self.columna == 9):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores real - char")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.character)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo char no puede ser contenido dentro de una columna tipo real")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores real - char")
                return simb
        elif (self.fila == 5 and self.columna == 10):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores real - text")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo text no puede ser contenido dentro de una columna tipo real")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores real - text")
                return simb
        elif (self.fila == 5 and self.columna == 11):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores real - date")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion == tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.date)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.date)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores real - date")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo date no puede ser contenido dentro de una columna tipo real")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores real - date")
                return simb
        elif (self.fila == 5 and self.columna == 12):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores real - Time withOut time zone")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion == tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_No_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_No_zone)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores real - withOut time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time withOut time zone no puede ser contenido dentro de una columna tipo real")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores real - withOut time zone")
                return simb
        elif (self.fila == 5 and self.columna == 13):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores real - time with time zone")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion == tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_si_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_si_zone)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores real - numeric with time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time with time zone no puede ser contenido dentro de una columna tipo real")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores real - time with time zone")
                return simb
        elif (self.fila == 5 and self.columna == 14):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()                
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores real - boolean")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores real - boolean")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo boolean no puede ser contenido dentro de una columna real numeric")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones:suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores real - boolean")
                return simb
        
        # ********************************************************************************************
        # ************************************* FILA 6 ***********************************************
        # #*******************************************************************************************
        if (self.fila == 6 and self.columna == 0):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores double - smallInt")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb
            
        elif (self.fila == 6 and self.columna == 1):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores double - Integer")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb
        elif (self.fila == 6 and self.columna == 2):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores dobule - bigInt")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb                
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)                                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb
            
        elif (self.fila == 6 and self.columna == 3):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores double - decimal")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb
            
        elif (self.fila == 6 and self.columna == 4):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores double - numeric")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb
        elif (self.fila == 6 and self.columna == 5):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores double - real")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb
        elif (self.fila == 6 and self.columna == 6):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores double - double")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.double_precision)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simb
        elif (self.fila == 6 and self.columna == 7):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores double - money")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo money no puede ser contenido dentro de una columna tipo double")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb
        elif (self.fila == 6 and self.columna == 8):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores double - varchar")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.varchar)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo varchar no puede ser contenido dentro de una columna tipo double")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores double - varchar")
                return simb
        elif (self.fila == 6 and self.columna == 9):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores double - char")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.character)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo char no puede ser contenido dentro de una columna tipo double")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores double - char")
                return simb
        elif (self.fila == 6 and self.columna == 10):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores double - text")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo text no puede ser contenido dentro de una columna tipo double")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores double - text")
                return simb
        elif (self.fila == 6 and self.columna == 11):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores double - date")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion == tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.date)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.date)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores double - date")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo date no puede ser contenido dentro de una columna tipo double")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores double - date")
                return simb
        elif (self.fila == 6 and self.columna == 12):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores double - Time withOut time zone")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion == tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_No_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_No_zone)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores double - withOut time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time withOut time zone no puede ser contenido dentro de una columna tipo double")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores double - withOut time zone")
                return simb
        elif (self.fila == 6 and self.columna == 13):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores double - time with time zone")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion == tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_si_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_si_zone)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores double - numeric with time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time with time zone no puede ser contenido dentro de una columna tipo double")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores double - time with time zone")
                return simb
        elif (self.fila == 6 and self.columna == 14):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()                
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores double - boolean")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores double - boolean")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo boolean no puede ser contenido dentro de una columna tipo double")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones:suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores double - boolean")
                return simb
        # ********************************************************************************************
        # ************************************* FILA 7 ***********************************************
        # #*******************************************************************************************
        if (self.fila == 7 and self.columna == 0):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores money - smallInt")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb
            
        elif (self.fila == 7 and self.columna == 1):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores money - Integer")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb
        elif (self.fila == 7 and self.columna == 2):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores money - bigInt")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.DIVISION:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb                
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)                                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb
            
        elif (self.fila == 7 and self.columna == 3):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores money - decimal")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb
            
        elif (self.fila == 7 and self.columna == 4):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores money - numeric")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb
        elif (self.fila == 7 and self.columna == 5):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores money - real")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb
        elif (self.fila == 7 and self.columna == 6):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores money - double")
                return simb
            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb
        elif (self.fila == 7 and self.columna == 7):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores money - money")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.money)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simb
        elif (self.fila == 7 and self.columna == 8):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores money - varchar")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.varchar)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo varchar no puede ser contenido dentro de una columna tipo money")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores money - varchar")
                return simb
        elif (self.fila == 7 and self.columna == 9):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores money - char")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.character)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo char no puede ser contenido dentro de una columna tipo money")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores money - char")
                return simb
        elif (self.fila == 7 and self.columna == 10):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores money - text")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo text no puede ser contenido dentro de una columna tipo money")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores money - text")
                return simb
        elif (self.fila == 7 and self.columna == 11):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores money - date")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores money - date")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo date no puede ser contenido dentro de una columna tipo money")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores money - date")
                return simb
        elif (self.fila == 7 and self.columna == 12):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores money - Time withOut time zone")
                return simb                      
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores money - withOut time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time withOut time zone no puede ser contenido dentro de una columna tipo money")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma,resta, multiplicacion, division, potencia, modulo no pueden operar valores money - withOut time zone")
                return simb
        elif (self.fila == 7 and self.columna == 13):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores money - time with time zone")
                return simb                   
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores money - numeric with time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time with time zone no puede ser contenido dentro de una columna tipo money")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma,resta, multiplicacion, division, potencia, modulo no pueden operar valores money - time with time zone")
                return simb
        elif (self.fila == 7 and self.columna == 14):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()                
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores money - boolean")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: >, >=, <, <=, == y <> no pueden operar valores money - boolean")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo boolean no puede ser contenido dentro de una columna tipo money")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones:suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores money - boolean")
                return simb
        # ********************************************************************************************
        # ************************************* FILA 8 ***********************************************
        # #*******************************************************************************************
        if (self.fila == 8 and self.columna == 0):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores varchar - smallInt")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.varchar)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo smallInt no puede ser contenido dentro de una columna tipo varchar")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores varchar - smallInt")
                return simb
            
        elif (self.fila == 8 and self.columna == 1):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores varchar - integer")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.varchar)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo integer no puede ser contenido dentro de una columna tipo varchar")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores varchar - integer")
                return simb
        elif (self.fila == 8 and self.columna == 2):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores varchar - bigInt")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.varchar)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo bitInt no puede ser contenido dentro de una columna tipo varchar")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores bigInt - smallInt")
                return simb
            
        elif (self.fila == 8 and self.columna == 3):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores varchar - decimal")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.varchar)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo decimal no puede ser contenido dentro de una columna tipo varchar")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores varchar - decimal")
                return simb
            
        elif (self.fila == 8 and self.columna == 4):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores varchar - numeric")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.varchar)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo numeric no puede ser contenido dentro de una columna tipo varchar")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores varchar - numeric")
                return simb

        elif (self.fila == 8 and self.columna == 5):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores varchar - real")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.varchar)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo real no puede ser contenido dentro de una columna tipo varchar")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores varchar - real")
                return simb

        elif (self.fila == 8 and self.columna == 6):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores varchar - double")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.varchar)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo double no puede ser contenido dentro de una columna tipo varchar")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores varchar - double")
                return simb

        elif (self.fila == 8 and self.columna == 7):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores varchar - money")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: >, >=, <, <=, ==, <> no puede operar varlos varchar - money")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.varchar)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo money no puede ser contenido dentro de una columna tipo varchar")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores varchar - money")
                return simb

        elif (self.fila == 8 and self.columna == 8):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores varchar - varchar")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.varchar)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.varchar)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores varchar - varchar")
                return simb

        elif (self.fila == 8 and self.columna == 9):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores varchar - char")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.varchar)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.varchar)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores varchar - char")
                return simb

        elif (self.fila == 8 and self.columna == 10):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores varchar - text")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.varchar)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)    
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores varchar - text")
                return simb
        elif (self.fila == 8 and self.columna == 11):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores varchar - date")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valures varchar - date")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo date no puede ser contenido dentro de una columna tipo varchar") 
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores varchar - date")
                return simb

        elif (self.fila == 8 and self.columna == 12):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores varchar - time withOut time zone")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valures varchar - time withOut time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time withOut time no puede ser contenido dentro de una columna tipo varchar") 
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores varchar - time withOut time zone")
                return simb

        elif (self.fila == 8 and self.columna == 13):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores varchar - time with time zone")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valures varchar - time with time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time with time zone no puede ser contenido dentro de una columna tipo varchar") 
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores time with time zone - varchar")
                return simb

        elif (self.fila == 8 and self.columna == 14):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores varchar - boolean")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valures varchar - boolean")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo boolean no puede ser contenido dentro de una columna tipo varchar") 
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores varchar - boolean")
                return simb
        # ********************************************************************************************
        # ************************************* FILA 9 ***********************************************
        # #*******************************************************************************************
        if (self.fila == 9 and self.columna == 0):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores char - smallInt")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.character)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo smallInt no puede ser contenido dentro de una columna tipo char")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores char - smallInt")
                return simb
            
        elif (self.fila == 9 and self.columna == 1):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores char - integer")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.character)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo integer no puede ser contenido dentro de una columna tipo char")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores char - integer")
                return simb
        elif (self.fila == 9 and self.columna == 2):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores char - bigInt")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.character)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo bitInt no puede ser contenido dentro de una columna tipo char")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores char - smallInt")
                return simb
            
        elif (self.fila == 9 and self.columna == 3):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores char - decimal")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.character)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo decimal no puede ser contenido dentro de una columna tipo char")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores char - decimal")
                return simb
            
        elif (self.fila == 9 and self.columna == 4):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores char - numeric")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.character)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo numeric no puede ser contenido dentro de una columna tipo char")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores char - numeric")
                return simb

        elif (self.fila == 9 and self.columna == 5):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores char - real")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.character)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo real no puede ser contenido dentro de una columna tipo char")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores char - real")
                return simb

        elif (self.fila == 9 and self.columna == 6):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores char - double")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.character)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo double no puede ser contenido dentro de una columna tipo char")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores char - double")
                return simb

        elif (self.fila == 9 and self.columna == 7):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores char - money")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: >, >=, <, <=, ==, <> no puede operar varlos char - money")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.character)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo money no puede ser contenido dentro de una columna tipo char")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores char - money")
                return simb

        elif (self.fila == 9 and self.columna == 8):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores char - varchar")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.character)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.character)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores char - varchar")
                return simb

        elif (self.fila == 9 and self.columna == 9):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores char - char")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.character)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.character)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores char - char")
                return simb

        elif (self.fila == 9 and self.columna == 10):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores char - text")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.character)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.character)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.character)    
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores char - text")
                return simb
        elif (self.fila == 9 and self.columna == 11):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores char - date")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valures char - date")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo date no puede ser contenido dentro de una columna tipo char") 
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores char - date")
                return simb

        elif (self.fila == 9 and self.columna == 12):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores char - time withOut time zone")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valures char - time withOut time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time withOut time no puede ser contenido dentro de una columna tipo char") 
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores char - time withOut time zone")
                return simb

        elif (self.fila == 9 and self.columna == 13):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores char - time with time zone")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valures char - time with time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time with time zone no puede ser contenido dentro de una columna tipo char") 
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores time with time zone - char")
                return simb

        elif (self.fila == 9 and self.columna == 14):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores char - boolean")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valures char - boolean")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo boolean no puede ser contenido dentro de una columna tipo char") 
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores char - boolean")
                return simb

        # ********************************************************************************************
        # ************************************* FILA 10 ***********************************************
        # #*******************************************************************************************
        if (self.fila == 10 and self.columna == 0):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores text - smallInt")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo smallInt no puede ser contenido dentro de una columna tipo text")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores text - smallInt")
                return simb
            
        elif (self.fila == 10 and self.columna == 1):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores text - integer")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo integer no puede ser contenido dentro de una columna tipo text")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores text - integer")
                return simb
        elif (self.fila == 10 and self.columna == 2):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores text - bigInt")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo bitInt no puede ser contenido dentro de una columna tipo text")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores text - smallInt")
                return simb
            
        elif (self.fila == 10 and self.columna == 3):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores text - decimal")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo decimal no puede ser contenido dentro de una columna tipo text")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores text - decimal")
                return simb
            
        elif (self.fila == 10 and self.columna == 4):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores text - numeric")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo numeric no puede ser contenido dentro de una columna tipo text")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores text - numeric")
                return simb

        elif (self.fila == 10 and self.columna == 5):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores text - real")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo real no puede ser contenido dentro de una columna tipo text")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores text - real")
                return simb

        elif (self.fila == 10 and self.columna == 6):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores text - double")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo double no puede ser contenido dentro de una columna tipo text")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores text - double")
                return simb

        elif (self.fila == 10 and self.columna == 7):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores text - money")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: >, >=, <, <=, ==, <> no puede operar varlos text - money")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo money no puede ser contenido dentro de una columna tipo text")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores text - money")
                return simb

        elif (self.fila == 10 and self.columna == 8):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores text - varchar")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores text - varchar")
                return simb

        elif (self.fila == 10 and self.columna == 9):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores text - char")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores text - char")
                return simb

        elif (self.fila == 10 and self.columna == 10):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores text - text")
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                simb = simbolo.Simbolo()                
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.text)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.text)    
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: resta, multiplicacion, division, potencia, modulo no pueden operar valores text - text")
                return simb
        elif (self.fila == 10 and self.columna == 11):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores text - date")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valures text - date")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo date no puede ser contenido dentro de una columna tipo text") 
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores text - date")
                return simb

        elif (self.fila == 10 and self.columna == 12):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores text - time withOut time zone")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valures text - time withOut time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time withOut time no puede ser contenido dentro de una columna tipo text") 
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores text - time withOut time zone")
                return simb

        elif (self.fila == 10 and self.columna == 13):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores text - time with time zone")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valures text - time with time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time with time zone no puede ser contenido dentro de una columna tipo text") 
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores time text - with time zone ")
                return simb

        elif (self.fila == 10 and self.columna == 14):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores text - boolean")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valures text - boolean")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo boolean no puede ser contenido dentro de una columna tipo text") 
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores text - boolean")
                return simb
        # ********************************************************************************************
        # ************************************* FILA 11 ***********************************************
        # #*******************************************************************************************
        if (self.fila == 11 and self.columna == 0):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores date - smallInt")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores date - smallInt")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion==tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.date)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.date)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo smallInt no puede ser contenido dentro de una columna tipo date")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores date - smallInt")
                return simb
            
        elif (self.fila == 11 and self.columna == 1):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores date - integer")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores date - integer")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion==tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.date)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.date)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo integer no puede ser contenido dentro de una columna tipo date")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores date - integer")
                return simb
        elif (self.fila == 11 and self.columna == 2):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores date - bigInit")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores date - bigInit")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion==tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.date)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.date)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo bigInit no puede ser contenido dentro de una columna tipo date")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores date - bigInit")
                return simb
            
        elif (self.fila == 11 and self.columna == 3):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores date - decimal")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores date - decimal")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion==tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.date)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.date)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo decimal no puede ser contenido dentro de una columna tipo date")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores date - decimal")
                return simb
            
        elif (self.fila == 11 and self.columna == 4):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores date - numeric")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores date - numeric")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion==tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.date)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.date)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo numeric no puede ser contenido dentro de una columna tipo date")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores date - numeric")
                return simb

        elif (self.fila == 11 and self.columna == 5):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores date - real")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores date - real")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion==tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.date)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.date)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo real no puede ser contenido dentro de una columna tipo date")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores date - real")
                return simb

        elif (self.fila == 11 and self.columna == 6):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores date - double")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores date - double")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion==tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.date)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.date)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo double no puede ser contenido dentro de una columna tipo date")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores date - double")
                return simb

        elif (self.fila == 11 and self.columna == 7):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores date - money")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores date - money")
                return simb           
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo money no puede ser contenido dentro de una columna tipo date")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores date - money")
                return simb

        elif (self.fila == 11 and self.columna == 8):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores date - varchar")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valores date - varchar")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo varchar no puede ser contenido dentro de una columna tipo date")              
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores date - varchar")
                return simb

        elif (self.fila == 11 and self.columna == 9):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores date - char")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valores date - char")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo char no puede ser contenido dentro de una columna tipo date")              
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores date - char")
                return simb

        elif (self.fila == 11 and self.columna == 10):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores date - text")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valores date - text")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo text no puede ser contenido dentro de una columna tipo date")              
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores date - text")
                return simb

        elif (self.fila == 11 and self.columna == 11):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores date - date")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.date)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.date)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.date)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.date)
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores date - date")
                return simb

        elif (self.fila == 11 and self.columna == 12):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores date - time withOut time zone")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valures date - time withOut time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time withOut time no puede ser contenido dentro de una columna tipo date") 
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores date - time withOut time zone")
                return simb

        elif (self.fila == 11 and self.columna == 13):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores date - time with time zone")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valores date - time with time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time with time zone no puede ser contenido dentro de una columna tipo date") 
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores time date - with time zone ")
                return simb

        elif (self.fila == 11 and self.columna == 14):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores date - boolean")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valores date - boolean")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo boolean no puede ser contenido dentro de una columna tipo date") 
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores date - boolean")
                return simb
        # ********************************************************************************************
        # ************************************* FILA 12 ***********************************************
        # #*******************************************************************************************
        if (self.fila == 12 and self.columna == 0):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time withOut time zone - smallInt")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time withOut time zone - smallInt")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion==tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_No_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_No_zone)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo smallInt no puede ser contenido dentro de una columna tipo time withOut time zone")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores time withOut time zone - smallInt")
                return simb
            
        elif (self.fila == 12 and self.columna == 1):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time withOut time zone - integer")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time withOut time zone - integer")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion==tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_No_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_No_zone)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo integer no puede ser contenido dentro de una columna tipo time withOut time zone")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores time withOut time zone - integer")
                return simb
        elif (self.fila == 12 and self.columna == 2):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time withOut time zone - bigInit")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time withOut time zone - bigInit")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion==tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_No_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_No_zone)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo bigInit no puede ser contenido dentro de una columna tipo time withOut time zone")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores time withOut time zone - bigInit")
                return simb
            
        elif (self.fila == 12 and self.columna == 3):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time withOut time zone - decimal")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time withOut time zone - decimal")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion==tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_No_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_No_zone)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo decimal no puede ser contenido dentro de una columna tipo time withOut time zone")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores time withOut time zone - decimal")
                return simb
            
        elif (self.fila == 12 and self.columna == 4):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time withOut time zone - numeric")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time withOut time zone - numeric")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion==tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_No_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_No_zone)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo numeric no puede ser contenido dentro de una columna tipo time withOut time zone")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores time withOut time zone - numeric")
                return simb

        elif (self.fila == 12 and self.columna == 5):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time withOut time zone - real")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time withOut time zone - real")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion==tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_No_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_No_zone)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo real no puede ser contenido dentro de una columna tipo time withOut time zone")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores time withOut time zone - real")
                return simb

        elif (self.fila == 12 and self.columna == 6):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time withOut time zone - double")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time withOut time zone - double")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion==tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_No_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_No_zone)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo double no puede ser contenido dentro de una columna tipo time withOut time zone")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores time withOut time zone - double")
                return simb

        elif (self.fila == 12 and self.columna == 7):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time withOut time zone - money")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time withOut time zone - money")
                return simb           
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo money no puede ser contenido dentro de una columna tipo time withOut time zone")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores time withOut time zone - money")
                return simb

        elif (self.fila == 12 and self.columna == 8):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time withOut time zone - varchar")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valores time withOut time out - varchar")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo varchar no puede ser contenido dentro de una columna tipo time withOut time zone")              
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores time withOut time zone - varchar")
                return simb

        elif (self.fila == 12 and self.columna == 9):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time withOut time zone - char")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valores time withOut time zone - char")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo char no puede ser contenido dentro de una columna tipo time withOut time zone")              
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores time withOut time zone - char")
                return simb

        elif (self.fila == 12 and self.columna == 10):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time withOut - text")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valores time withOut time zone - text")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo text no puede ser contenido dentro de una columna tipo time withOut time zone")              
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores time withOut time zone - text")
                return simb

        elif (self.fila == 12 and self.columna == 11):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time withOut time zone - date")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valures time withOut time zone - date")                
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo date no puede ser contenido dentro de una columna tipo time withOut time zone") 
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores time withOut time zone - date")
                return simb

        elif (self.fila == 12 and self.columna == 12):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time withOut time zone - time withOut time zone")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_No_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_No_zone)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_No_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_No_zone)                
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores time withOut time zone - time withOut time zone")
                return simb

        elif (self.fila == 12 and self.columna == 13):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time withOut time zone - time with time zone")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_No_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_No_zone)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time with time zone no puede ser contenido dentro de una columna tipo time withOut time zone")             
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores time withOut time zone - time with time zone")
                return simb

        elif (self.fila == 12 and self.columna == 14):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time wtihOut time zone - boolean")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valores time withOut time zone - boolean")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo boolean no puede ser contenido dentro de una columna tipo time withOut time zone") 
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores time withOut time zone - boolean")
                return simb
        # ********************************************************************************************
        # ************************************* FILA 13 ***********************************************
        # #*******************************************************************************************
        if (self.fila == 13 and self.columna == 0):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time zone - smallInt")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time with time zone - smallInt")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion==tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_si_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_si_zone)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo smallInt no puede ser contenido dentro de una columna tipo time with time zone")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores time with time zone - smallInt")
                return simb
            
        elif (self.fila == 13 and self.columna == 1):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time zone - integer")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time with time zone - integer")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion==tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_si_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_si_zone)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo integer no puede ser contenido dentro de una columna tipo time with time zone")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores time with time zone - integer")
                return simb
        elif (self.fila == 13 and self.columna == 2):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time zone - bigInit")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time with time zone - bigInit")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion==tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_si_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_si_zone)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo bigInit no puede ser contenido dentro de una columna tipo time with time zone")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores time with time zone - bigInit")
                return simb
            
        elif (self.fila == 13 and self.columna == 3):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time zone - decimal")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time with time zone - decimal")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion==tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_si_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_si_zone)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo decimal no puede ser contenido dentro de una columna tipo time with time zone")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores time with time zone - decimal")
                return simb
            
        elif (self.fila == 13 and self.columna == 4):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time zone - numeric")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time with time zone - numeric")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion==tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_si_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_si_zone)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo numeric no puede ser contenido dentro de una columna tipo time with time zone")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores time with time zone - numeric")
                return simb

        elif (self.fila == 13 and self.columna == 5):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time zone - real")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time with time zone - real")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion==tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_si_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_si_zone)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo real no puede ser contenido dentro de una columna tipo time with time zone")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores time with time zone - real")
                return simb

        elif (self.fila == 13 and self.columna == 6):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time zone - double")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time with time zone - double")
                return simb
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.SUMA or tipoOperacion==tipoSimbolo.TipoSimbolo.RESTA:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_si_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_si_zone)
                return simb
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo double no puede ser contenido dentro de una columna tipo time with time zone")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: multiplicacion, division, potencia, modulo no pueden operar valores time with time zone - double")
                return simb

        elif (self.fila == 13 and self.columna == 7):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time zone - money")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time with time zone - money")
                return simb           
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo money no puede ser contenido dentro de una columna tipo time with time zone")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores time with time zone - money")
                return simb

        elif (self.fila == 13 and self.columna == 8):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time zone - varchar")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valores time with time out - varchar")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo varchar no puede ser contenido dentro de una columna tipo time with time zone")              
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores time with time zone - varchar")
                return simb

        elif (self.fila == 13 and self.columna == 9):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time zone - char")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valores time with time zone - char")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo char no puede ser contenido dentro de una columna tipo time with time zone")              
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores time with time zone - char")
                return simb

        elif (self.fila == 13 and self.columna == 10):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with - text")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valores time with time zone - text")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo text no puede ser contenido dentro de una columna tipo time with time zone")              
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores time with time zone - text")
                return simb

        elif (self.fila == 13 and self.columna == 11):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time zone - date")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valures time with time zone - date")                
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo date no puede ser contenido dentro de una columna tipo time with time zone") 
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores time with time zone - date")
                return simb

        elif (self.fila == 13 and self.columna == 12):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time zone - time with time zone")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones <, <=, >, >=, == , <> no pueden operar valores time with time zone - time withOut time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time withOut time zone no puede ser contenido dentro de una columna time with time zone")              
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores time with time zone - time withOut time zone")
                return simb

        elif (self.fila == 13 and self.columna == 13):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time zone - time with time zone")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_si_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_si_zone)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.time_si_zone)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.time_si_zone)
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores time with time zone - time with time zone")
                return simb

        elif (self.fila == 13 and self.columna == 14):
            if(tipoSimbolo==tipoSimbolo.TipoSimbolo.AND or tipoSimbolo==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time zone - boolean")
                return simb                    
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones: <, <=, >, >=, ==, <> no pueden operar valores time with time zone - boolean")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb  = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo boolean no puede ser contenido dentro de una columna tipo time with time zone") 
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores time with time zone - boolean")
                return simb
        # ********************************************************************************************
        # ************************************* FILA 14 ***********************************************
        # #*******************************************************************************************
        if (self.fila == 14 and self.columna == 0):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time boolean - smallInt")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time with time boolean - smallInt")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo smallInt no puede ser contenido dentro de una columna tipo time with time boolean")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores boolean - smallInt")
                return simb
            
        elif (self.fila == 14 and self.columna == 1):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time boolean - integer")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time with time boolean - integer")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo integer no puede ser contenido dentro de una columna tipo time with time boolean")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores boolean - integer")
                return simb

        elif (self.fila == 14 and self.columna == 2):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time boolean - bigInt")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time with time boolean - bigInt")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo bigInit no puede ser contenido dentro de una columna tipo time with time boolean")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores boolean - bigInt")
                return simb

        elif (self.fila == 14 and self.columna == 3):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time boolean - decimal")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time with time boolean - decimal")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo decimal no puede ser contenido dentro de una columna tipo time with time boolean")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores boolean - decimal")
                return simb

        elif (self.fila == 14 and self.columna == 4):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time boolean - numeric")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time with time boolean - numericc")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo numeric no puede ser contenido dentro de una columna tipo time with time boolean")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores boolean - numeric")
                return simb

        elif (self.fila == 14 and self.columna == 5):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time boolean - real")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time with time boolean - real")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo real no puede ser contenido dentro de una columna tipo time with time boolean")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores boolean - real")
                return simb

        elif (self.fila == 14 and self.columna == 6):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time boolean - double")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time with time boolean - double")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo double no puede ser contenido dentro de una columna tipo time with time boolean")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores boolean - double")
                return simb

        elif (self.fila == 14 and self.columna == 7):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time boolean - money")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time with time boolean - money")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo money no puede ser contenido dentro de una columna tipo time with time boolean")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores boolean - money")
                return simb

        elif (self.fila == 14 and self.columna == 8):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time boolean - varchar")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time with time boolean - varchar")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo varchar no puede ser contenido dentro de una columna tipo time with time boolean")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores boolean- varchar")
                return simb

        elif (self.fila == 14 and self.columna == 9):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time boolean - char")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time with time boolean - char")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo char no puede ser contenido dentro de una columna tipo time with time boolean")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores boolean - char")
                return simb

        elif (self.fila == 14 and self.columna == 10):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time boolean - text")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time with time boolean - text")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo text no puede ser contenido dentro de una columna tipo time with time boolean")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores boolean - text")
                return simb

        elif (self.fila == 14 and self.columna == 11):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time boolean - date")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time with time boolean - date")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo date no puede ser contenido dentro de una columna tipo time with time boolean")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores boolean - date")
                return simb

        elif (self.fila == 14 and self.columna == 12):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time boolean - time withOut time zone")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time with time boolean - time withOut time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time withOut time zone no puede ser contenido dentro de una columna tipo time with time boolean")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores boolean - time withOut time zone")
                return simb

        elif (self.fila == 14 and self.columna == 13):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Las operaciones And, Or no pueden operar valores time with time boolean - time with time zone")
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operacion: <, <=, >, >=, ==, <> no puede operar valores time with time boolean - time with time zone")
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("Valor tipo time with time zone no puede ser contenido dentro de una columna tipo time with time boolean")
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores boolean - time with time zone")
                return simb

        elif (self.fila == 14 and self.columna == 14):
            if(tipoOperacion==tipoSimbolo.TipoSimbolo.AND or tipoOperacion==tipoSimbolo.TipoSimbolo.OR):
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.boolean)
                return simb            
            elif tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.MAYOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_QUE or tipoOperacion==tipoSimbolo.TipoSimbolo.MENOR_IGUAL or tipoOperacion==tipoSimbolo.TipoSimbolo.IGUALACION or tipoOperacion==tipoSimbolo.TipoSimbolo.DISTINTO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.boolean)
                return simb            
            elif tipoOperacion == tipoSimbolo.TipoSimbolo.COLUMNA_DATO:
                simb = simbolo.Simbolo()
                simb.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                simb.setTipoDatosCasteo(simboloColumna.TiposDatos.boolean)
                return simb
            else:
                simb = simbolo.Simbolo()
                simb.setDescripcionError("La operaciones: suma, resta, multiplicacion, division, potencia, modulo no pueden operar valores boolean - boolean")
                return simb        
        else:
            return None
    
        

        
