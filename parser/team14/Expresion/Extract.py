from Expresion.Expresion import Expresion

class Extract(Expresion):
    'This is an abstract class'

    def __init__(self,field=None,timestamp=None):
        self.field=field
        self.timestamp=timestamp


    def getval(self):
        'spliteo el timestamp'
        splited=self.timestamp.split(' ')
        fecha= splited[0]
        hora = splited[1]
        splitedfecha= fecha.split('-')
        splitedhora = hora.split(':')
        if self.field=='year':
            return splitedfecha[0]
        elif self.field=='month':
            return splitedfecha[1]
        elif self.field == 'day':
            return splitedfecha[2]
        elif self.field=='hour':
            return splitedhora[0]
        elif self.field=='minute':
            return splitedhora[1]
        elif self.field == 'second':
            return splitedhora[2]
