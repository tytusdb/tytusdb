from tytus.parser.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from tytus.parser.team21.Analisis_Ascendente.Instrucciones.Time import  Time
from tytus.parser.team21.Analisis_Ascendente.storageManager.jsonMode import *
import tytus.parser.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
import tytus.parser.team21.Analisis_Ascendente.Instrucciones.Select as Select

from prettytable import PrettyTable


#from Instrucciones.instruccion import Instruccion
#from Instrucciones.Time import  Time
#from storageManager.jsonMode import *
#import Tabla_simbolos.TablaSimbolos as TS
#import Instrucciones.Select as Select

class selectTime(Instruccion):
    '''#1 EXTRACT
           #2 NOW
           #3 date_part
           #4 current_date
           #5 current_time
           #6 TIMESTAMP

           self.caso = caso
           self.momento = momento
           self.cadena = cadena
           self.cadena2 = cadena2'''
    def ejecutar(Select,ts, Consola,exceptions,Mostrar):

        # Error semantico - numero error - descripcion - fila - columna
        #si pueden ir a buscar la bd actual






        x = PrettyTable()

        print(Select.time.momento)
        datet= Time.resolverTime(Select.time)

        if (Select.time.caso == 1):  # EXTRACT

            x.field_names = ["date_part"]
            x.add_row([datet])

        elif (Select.time.caso == 2):  # NOW
            x.field_names = ["now"]
            x.add_row([str(datet)])

        elif (Select.time.caso == 3):  # date_part
            x.field_names = ["date_part"]
            x.add_row([datet])

        elif (Select.time.caso == 4):  # current_date
            x.field_names = ["current_date"]
            x.add_row([str(datet)])

        elif (Select.time.caso == 5):  # current_time
            x.field_names = ["current_time"]
            x.add_row([str(datet)])

        elif (Select.time.caso == 6):  # TIMESTAMP
            x.field_names = ["current_time"]
            x.add_row([str(datet)])

        if(Mostrar):
            Consola.append('\n'+x.get_string()+'\n')
        return str(datet)

