class ErroresSintacticos():
    '''
        Parametros:
            - Descripcion:str
                Descripcion
            - linea y columna:numeric
                linea y columna
            - clase origen:str
                Sirve para decir en que clase del patron interprete trono
    '''

    def __init__(self, descripcion, linea, columna, origen):
        self.descripcion = descripcion
        self.linea = linea
        self.columna = columna
        self.origen = origen

    '''
      ______ _____  _____   ____  _____  
     |  ____|  __ \|  __ \ / __ \|  __ \ 
     | |__  | |__) | |__) | |  | | |__) |
     |  __| |  _  /|  _  /| |  | |  _  / 
     | |____| | \ \| | \ \| |__| | | \ \ 
     |______|_|  \_\_|  \_\\____/|_|  \_\

    Descripcion: 
    '''