from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *
from tools.tabla_simbolos import *
from abstract.retorno import *
from prettytable import PrettyTable
from abstract.columnaID import*
from storage import jsonMode as funciones

class select_normal(instruccion):
    def __init__(self,distinto, lista_cols, list_tables, donde, groupby, orderby, having, limite, line, column, num_nodo):
        super().__init__(line,column)
        self.distinto=distinto
        self.lista_cols = lista_cols
        self.list_tables = list_tables
        self.donde = donde
        self.groupby = groupby
        self.orderby = orderby
        self.having = having
        self.limite = limite
        self.nodo = nodo_AST('SELECT',num_nodo)

        self.grammar_ = ' '

    def ejecutar(self):
        id_db = get_actual_use()
        salidaTabla = PrettyTable()
        encabezados=[]

        registro = []

        if self.donde == None:

            for tabla in self.list_tables:
                data_table = funciones.extractTable(id_db,tabla)
                registro=data_table
                encabezados=ts.field_names(id_db,tabla)

        #si viene where
        elif self.donde != None:
            data_were = self.donde.ejecutar(self.list_tables)
            print(data_were)
            encabezados = data_were.encabezados
            registro=data_were.valor
        
        #Si viene GroupBy

        if self.groupby == None:
            pass
        
        if self.lista_cols != '*':
            listCampos2 = []
            for col in self.lista_cols:
                contador = -1
                for campo in encabezados:  # RECORRO LOS NOMBRES DE LOS CAMPOS DE LA TS
                    listCampos2.clear()  # LIMPIO LA LISTA DONDE ALMACENARE LOS DATOS DE CADA COLUMNA
                    contador += 1  # INDICA LA POSICION DE LA COLUMNA DONDE OBTENGO LOS VALORES
                    if (col.valor == campo):
                        for col2 in registro:  # RECORRO LOS DATOS DE LA TABLA DE SIMBOLOS
                            listCampos2.append(col2[contador])
                        salidaTabla.add_column(campo, listCampos2)
                      
        else:
            salidaTabla.field_names = encabezados
            if len(registro) > 0:
                salidaTabla.add_rows(registro)

        add_text('\n')
        add_text(salidaTabla)
        add_text('\n')

        return retorno(registro,tipo_primitivo.TABLA,True,encabezados=encabezados)