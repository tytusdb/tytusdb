from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
#from Instrucciones.instruccion import Instruccion
import  datetime
import pytz


class Time(Instruccion):
    '''#1 EXTRACT
       #2 NOW
       #3 date_part
       #4 current_date
       #5 current_time
       #6 TIMESTAMP'''
    def __init__(self, caso, momento, cadena, cadena2,fila,columna):
        self.caso = caso
        self.momento = momento
        self.cadena = cadena
        self.cadena2 = cadena2
        self.fila = fila
        self.columna = columna

    def resolverTime(Time):
        tz_Guate = pytz.timezone('America/Guatemala')
        if (Time.caso == 1):  # EXTRACT
            momento = Time.momento  # lo que se quiere extraer
            time = Time.cadena  # cadena de fecha
            t = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')

            if str(momento).lower() == 'hour':
                return t.strftime('%H')
            elif str(momento).lower() == 'minute':
                return  t.strftime('%M')
            elif str(momento).lower() == 'second':
                return  t.strftime('%S')
            elif str(momento).lower() == 'day':
                return t.strftime('%d')
            elif str(momento).lower() == 'month':
                return t.strftime('%m')
            elif str(momento).lower() == 'year':
                return t.strftime('%Y')

        elif (Time.caso == 2):  # NOW
            today = datetime.datetime.now(tz_Guate)
            return str(today)

        elif (Time.caso == 3):  # date_part
            moment = Time.cadena
            time = str(Time.cadena2).strip().split(' ')
            valor = 0

            for i in time:
                if (moment == i) or (str(moment + 's') == i):
                    return valor
                if i.isnumeric():
                    valor = i

        elif (Time.caso == 4):  # current_date
            date = datetime.date.today()
            return str(date)

        elif (Time.caso == 5):  # current_time

            time = datetime.datetime.now(tz_Guate)
            return str(time.astimezone().timetz())

        elif (Time.caso == 6):  # TIMESTAMP

            if (str(Time.cadena).lower() == 'now'):
                today = datetime.datetime.now()
                return str(today)
            else:
                return str(Time.cadena)


    def ObtenerCadenaEntrada(Time):

        if (Time.caso == 1):  # EXTRACT PARIZQ momento FROM TIMESTAMP  CADENA PARDR
            momento = Time.momento  # lo que se quiere extraer
            cad = Time.cadena  # cadena de fecha

            return ' EXTRACT ( '+str(momento)+' FROM TIMESTAMP \''+str(cad)+'\' )'


        elif (Time.caso == 2):  # NOW PARIZQ PARDR
            return ' now() '

        elif (Time.caso == 3):  # date_part PARIZQ CADENA COMA INTERVAL CADENA PARDR
            cadena1 = Time.cadena
            cadena2 = Time.cadena2

            return 'date_part ( \''+str(cadena1)+'\', INTERVAL \''+str(cadena2)+'\' )'



        elif (Time.caso == 4):  #  CURRENT_DATE
           return ' CURRENT_DATE '

        elif (Time.caso == 5):  # CURRENT_TIME

            return ' CURRENT_TIME '

        elif (Time.caso == 6):  # TIMESTAMP CADENA
            return ' TIMESTAMP \''+Time.cadena+'\' '


    def traducir(time, ts, consola, exception, tv):
        res = Time.resolverTime(time)
        res = str(res)
        temp = tv.Temp()
        consola.append(f'\t{temp} = \'{res}\'\n')
        return temp