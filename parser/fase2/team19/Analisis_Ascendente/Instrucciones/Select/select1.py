from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from Analisis_Ascendente.Instrucciones.Time import  Time
from Analisis_Ascendente.storageManager.jsonMode import *
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
import Analisis_Ascendente.Instrucciones.Select as Select

from prettytable import PrettyTable


#from Instrucciones.instruccion import Instruccion
#from Instrucciones.Time import  Time
#from storageManager.jsonMode import *
#import Tabla_simbolos.TablaSimbolos as TS
#import Instrucciones.Select as Select
from C3D import GeneradorTemporales


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

    def getC3D(self,ts, lista_op):
        etiqueta = GeneradorTemporales.nuevo_temporal()
        code = '\n     # ---------SELECT----------- \n'
        code += '    top_stack = top_stack + 1 \n'
        code += '    %s = \"select ' % etiqueta
        code += self.time.getC3D()
        code += ';\" \n'
        code += '    stack[top_stack] = %s \n' % etiqueta
        return code


    def ejecutar(Select,ts, Consola,exceptions,Mostrar):
        # Error semantico - numero error - descripcion - fila - columna
        #si pueden ir a buscar la bd actual
        #simular
        insert('test','tblibrosalario',[1,2020,10,1300,10.30])
        insert('test','tblibrosalario',[2,2020,10,1300,10.30])
        insert('test','tblibrosalario',[3,2020,10,1300,10.30])
        #van usar
        extractTable('test','tblibrosalario')

        x = PrettyTable()

        #print(Select.time.momento)
        datet = Time.resolverTime(Select.time)

        if Select.time.caso == 1:  # EXTRACT

            x.field_names = ["extract"]
            x.add_row([datet])

        elif Select.time.caso == 2:  # NOW
            x.field_names = ["now"]
            x.add_row([str(datet)])

        elif Select.time.caso == 3:  # date_part
            x.field_names = ["date_part"]
            x.add_row([datet])

        elif Select.time.caso == 4:  # current_date
            x.field_names = ["current_date"]
            x.add_row([str(datet)])

        elif Select.time.caso == 5:  # current_time
            x.field_names = ["current_time"]
            x.add_row([str(datet)])

        elif Select.time.caso == 6:  # TIMESTAMP
            x.field_names = ["timestamp"]
            x.add_row([str(datet)])

        if Mostrar:
            Consola.append('\n'+x.get_string()+'\n')
        return str(datet)

