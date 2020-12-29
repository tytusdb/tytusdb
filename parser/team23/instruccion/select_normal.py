from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *
from tools.tabla_simbolos import *
from error.errores import *
from abstract.retorno import *
from prettytable import PrettyTable
from abstract.columnaID import*
from storage import jsonMode as funciones
from instruccion.alias_item import *
import operator

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

        #AST
        self.nodo = nodo_AST('SELECT',num_nodo)
        self.nodo.hijos.append(nodo_AST('SELECT',num_nodo+1))

        if distinto!=None:

            self.nodo.hijos.append(nodo_AST('DISTINCT', num_nodo + 2))
            if lista_cols != '*':
                for lista in lista_cols:
                    self.nodo.hijos.append(lista.nodo)
            else:
                self.nodo.hijos.append(nodo_AST('*', num_nodo + 3))

            self.nodo.hijos.append(nodo_AST('FROM', num_nodo + 4))

            self.nodo.hijos.append(nodo_AST(str(list_tables), num_nodo + 5))

            if donde != None:
                self.nodo.hijos.append(donde.nodo)

            if groupby != None:
                self.nodo.hijos.append(groupby.nodo)

            if orderby != None:
                self.nodo.hijos.append(orderby.nodo)

            if having != None:
                self.nodo.hijos.append(having.nodo)

            if limite != None:
                self.nodo.hijos.append(limite.nodo)

        else:

            if lista_cols != '*':
                for lista in lista_cols:
                    self.nodo.hijos.append(lista.nodo)
            else:
                self.nodo.hijos.append(nodo_AST('*', num_nodo + 2))

            self.nodo.hijos.append(nodo_AST('FROM', num_nodo + 3))

            self.nodo.hijos.append(nodo_AST(str(list_tables), num_nodo + 4))

            if donde != None:
                self.nodo.hijos.append(donde.nodo)

            if groupby != None:
                self.nodo.hijos.append(groupby.nodo)

            if orderby != None:
                self.nodo.hijos.append(orderby.nodo)

            if having != None:
                self.nodo.hijos.append(having.nodo)

            if limite != None:
                self.nodo.hijos.append(limite.nodo)

        #Gramatica
        self.grammar_ = '<TR><TD> seleccionar ::= SELECT  distinto select_list FROM list_id donde group_by order_by group_having limite; </TD><TD> seleccionar = new select_normal(); </TD></TR>\n'

        if distinto!=None:
            self.grammar_ += '<TR><TD> distinto ::= DISTINCT </TD><TD> distinto = new distinto(); </TD></TR>\n'
            if lista_cols != '*':
                self.grammar_ += '<TR><TD> select_list ::= expressiones  </TD><TD> select_list = new select_list(); </TD></TR>\n'
                self.grammar_ += lista.grammar_

            else:
               self.grammar_ += '<TR><TD> select_list ::= * </TD><TD> distinto = new distinto(); </TD></TR>\n'

            self.grammar_ += '<TR><TD> list_id ::= list_id , alias  </TD><TD> list_id = lista.append(id); </TD></TR>\n'
            self.grammar_ += '<TR><TD> list_id ::= list_id   </TD><TD> list_id = lista[]; </TD></TR>\n'
            self.grammar_ += '<TR><TD> alias ::= ID  </TD><TD> alias = ID.value; </TD></TR>\n'

            if donde != None:
                self.grammar_ += donde.grammar_

            if groupby != None:
                self.grammar_ += groupby.grammar_

            if orderby != None:
                self.grammar_ += orderby.grammar_

            if having != None:
                self.grammar_ += having.grammar_

            if limite != None:
                self.grammar_ += limite.grammar_

        else:

            if lista_cols != '*':
                self.grammar_ += '<TR><TD> select_list ::= expressiones  </TD><TD> select_list = new select_list(); </TD></TR>\n'
                self.grammar_ += lista.grammar_

            else:
               self.grammar_ += '<TR><TD> select_list ::= * </TD><TD> distinto = new distinto(); </TD></TR>\n'

            self.grammar_ += '<TR><TD> list_id ::= list_id , alias  </TD><TD> list_id = lista.append(id); </TD></TR>\n'
            self.grammar_ += '<TR><TD> list_id ::= list_id   </TD><TD> list_id = lista[]; </TD></TR>\n'
            self.grammar_ += '<TR><TD> alias ::= ID  </TD><TD> alias = ID.value; </TD></TR>\n'

            if donde != None:
                self.grammar_ += donde.grammar_

            if groupby != None:
                self.grammar_ += groupby.grammar_

            if orderby != None:
                self.grammar_ += orderby.grammar_

            if having != None:
                self.grammar_ += having.grammar_

            if limite != None:
                self.grammar_ += limite.grammar_

    def ejecutar(self, imprimir=None):
        try:
            for id_item in self.list_tables:
                if isinstance(id_item, alias_item):
                    id_item.ejecutar([])

            id_db = get_actual_use()
            salidaTabla = PrettyTable()
            encabezados=[]

            registro = []
            registro_aux = []

            if self.donde == None:
                for tabla in self.list_tables:
                    data_table = funciones.extractTable(id_db,tabla)
                    registro=data_table
                    encabezados=ts.field_names(id_db,tabla)
            #si viene where
            else:
                data_were = self.donde.ejecutar(self.list_tables)
                print(data_were)
                if data_were.tipo != tipo_primitivo.ERROR:
                    encabezados = data_were.encabezados
                    registro=data_were.valor
                else:
                    errores.append(nodo_error(self.line, self.column, 'ERROR - No se pudo ejecutar select', 'Semántico'))
                    add_text('ERROR - No se pudo ejecutar select\n')

            #Si viene GroupBy

            if self.groupby != None:
                lista_groupBy = self.groupby.ejecutar()
                print(str(lista_groupBy))
                index_G = self.retornador_index(lista_groupBy[0],encabezados)
                print(str(index_G))

                registro_columnas = []

                for busqueda in registro:

                    contador_aux = 0


                    for aux in busqueda:

                        if index_G == contador_aux:
                            if self.existencia_grupby(busqueda,registro_columnas,index_G):
                                registro_columnas.append(busqueda)

                        contador_aux += 1
                print(registro_columnas)
                registro=registro_columnas

            #Si viene OrderBy
            if self.orderby != None:
                auxOrder_by = self.orderby.ejecutar()
                indexG=self.retornador_index(auxOrder_by.valor[0],encabezados)

                if auxOrder_by.tipo == 'ASC':
                    registro = sorted(registro, key=lambda i: str(i[indexG]).lower())
                elif auxOrder_by.tipo == 'DESC':
                    registro = sorted(registro, key=lambda i: str(i[indexG]).lower(), reverse=True)

            if self.lista_cols != '*':
                listCampos2 = []
                auxEncabezados=[]
                for col in self.lista_cols:
                    contador = -1
                    for campo in encabezados:
                        listCampos2.clear()
                        contador += 1
                        if (col.valor == campo):
                            auxEncabezados.append(col.valor)
                            aux = columnaId([],col.valor)
                            for col2 in registro:
                                listCampos2.append(col2[contador])
                                aux.lista.append(col2[contador])
                            salidaTabla.add_column(campo, listCampos2)
                            registro_aux.append(aux)
                registro=self.metodo_sis(registro_aux)
                encabezados=auxEncabezados
            else:
                salidaTabla.field_names = encabezados
                if len(registro) > 0:
                    salidaTabla.add_rows(registro)

            if self.distinto != None:
                salidaTabla.clear()
                mostrar = []
                aux1 = registro
                for n in registro:
                    if self.metodo_Pegre(n, aux1) == 1:
                        mostrar.append(n)
                        print(n)
                    else:
                        cont = 0
                        for reco in mostrar:

                            if n == reco:
                                cont = 2
                                break
                            else:
                                cont =1

                        if cont == 1:
                            mostrar.append(n)
                registro=mostrar
                salidaTabla.add_rows(mostrar)


            if imprimir==None :
                add_text('\n')
                add_text(salidaTabla)
                add_text('\n')

            return retorno(registro[0][0],encabezados,registro)
        except:
            add_text("E-22005 error in assignment: the query could not be made.\n")

    def OrderByBurbuja(self,lista,index):
        print('Index '+str(index))
        
        

        return sorted_rank
        

    def retornador_index(self, id, lista_campo):

        contador = -1

        for campo in lista_campo:  # RECORRO LOS NOMBRES DE LOS CAMPOS DE LA TS
            contador += 1  # INDICA LA POSICION DE LA COLUMNA DONDE OBTENGO LOS VALORES

            if (id == campo):
                return contador

        return -1
        
    def existencia_grupby(self, valor, lista,index):

        for recorido in lista:
            contadorG = 0
            for columnAA in recorido:
                if contadorG == index:
                    if str(columnAA) == str(valor[index]):
                        return False
                contadorG+=1

        return True

    def metodo_sis(self,lista):
        lista_original = []
        contador = 0

        for recorido in lista[0].lista:
            lista_aux = []
            for columna in lista:
                lista_aux.append(columna.lista[contador])
            contador+=1
            lista_original.append(lista_aux)    

        return lista_original

    def metodo_Pegre(self, dato, lista):
        aux = lista
        contador = 0
        #bandera = True

        for recorrido in aux:
            if (recorrido == dato):
                contador += 1
            else:
                pass

        return contador

