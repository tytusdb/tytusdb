class numerico:
    '''clase abstracta'''

class smallint(numerico):
    def __init__(self,val):
        self.val = val
        self.min = -32769
        self.max = 32769

class integer(numerico):
    def __init__(self,val):
        self.val = val
        self.min = -2147483648
        self.max = 2147483648

class bigint(numerico):
    def __init__(self,val):
        self.val = val
        self.min = -9223372036854775808
        self.max = 9223372036854775808

class numeric(numerico):
    def __init__(self,val):
        self.val = val

class real(numerico):
    def __init__(self,val):
        self.val = val
        self.precision = 6
    
class double_precision(numerico):
    def __init__(self,val):
        self.val = val
        self.precision = 15

class money(numerico):
    def __init__(self,val):
        self.val = val
        self.min = -92233720368547758.08
        self.max = 92233720368547758.08

class caracteres:
    '''clase abstracta'''

class character_varing(caracteres):
    def __init__(self,val, limit):
        self.val = val
        self.min = limit

class varchar(caracteres):
    def __init__(self,val, limit):
        self.val = val
        self.min = limit

class character(caracteres):
    def __init__(self,val, limit):
        self.val = val
        self.min = limit

class char(caracteres):
    def __init__(self,val, limit):
        self.val = val
        self.min = limit

class text(caracteres):
    def __init__(self,val):
        self.val = val
        

class tiempo:
    '''clase abstracta'''
    

class timestamp(tiempo):
    def __init__(self,val):
        self.val = val
        self.low = "4713 BC"
        self.high ="294276 AD"

class date(tiempo):
    def __init__(self,val):
        self.val = val
        self.low = "4713 BC"
        self.high ="5874897 AD"

class time(tiempo):
    def __init__(self,val):
        self.val = val
        self.low = "00:00:00"
        self.high ="24:00:00"


class time_without(tiempo):
    def __init__(self,val):
        self.val = val
        self.low = "00:00:00"
        self.high ="24:00:00"

class time_with(tiempo):
    def __init__(self,val):
        self.val = val
        self.low = "00:00:00+1559"
        self.high ="24:00:00-1559"

class interval(tiempo):
     def __init__(self,val):
        self.val = val
        self.low = -178000000
        self.high =178000000

class logico:
    '''clase abstracta'''

class boolean(logico):
    def __init__(self,valor):
        self.val= valor