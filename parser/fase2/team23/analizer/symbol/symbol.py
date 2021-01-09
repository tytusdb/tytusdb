class Symbol:
    """
    Esta clase representa los simbolos que producen los resultados
    de las diferentes ejecuciones (execute()) de las instrucciones y
    expresiones.
    """

    def __init__(self, value, type_, row, column, col_creada, cons, return_func = None, params_func = None, bloque_func = None, val_var = None, tabla_index = None) -> None:
        self.value = value
        self.type = type_
        self.row = row
        self.column = column
        self.col_creada = col_creada
        self.cons = cons
        self.tabla_index = tabla_index
        #VARIABLES PARA FUNCIONES
        self.return_func = return_func
        self.params_func = params_func
        self.bloque_func = bloque_func
        self.val_var = val_var
        

