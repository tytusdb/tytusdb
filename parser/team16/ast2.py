from Instruccion import *
from graphviz import Digraph
from graphviz import escape
from expresiones import *
import interprete as Inter
class Ast2:

    def __init__(self, sentencias):
        self.i = 0
        self.sentencias = sentencias

    def inc(self):
        global i
        self.i += 1

    def crearReporte(self):
        global dot

        dot = Digraph('AST', format='png', filename='c:/source/ast.gv')
        dot.attr('node', shape='box', color='#31CEF0')
        dot.node('Node' + str(self.i), '"AST"')
        dot.edge_attr.update(arrowhead='none')
        self.recorrerInstrucciones(self.sentencias, 'Node' + str(self.i))
        dot.render('AST', format='png', view=True)
        print('Hecho')





    def recorrerInstrucciones(self, sente, padre):
        for i in sente:
            #VIENE UN DROP TABLE
            if isinstance(i, DropTable):
                print("Si es un drop table *")
                self.grafoDropTable(i.id, padre)

            elif isinstance(i, Select):
                print("Es Una Instruccion Select")
                self.GrafoSelect(i.Lista_Campos,i.Nombres_Tablas,i.unionn,padre)

            elif isinstance(i, Select2):
                print("Es Una Instruccion Select2")
                self.GrafoSelect2(i.Lista_Campos,i.Nombres_Tablas,i.Cuerpo,i.unionn,padre)

            elif isinstance(i, Select3):
                print("Es Una Instruccion Select 3 ")
                self.GrafoSelect3(i.distinct, i.Lista_Campos, i.Nombres_Tablas, i.unionn, padre)

            elif isinstance(i, Select4):
                print("Es Una Instruccion Select 4")
                self.GrafoSelect4(i.distinct, i.Lista_Campos, i.Nombres_Tablas, i.Cuerpo, i.unionn, padre)

            elif isinstance(i, Insert_Datos):
                print("Si es un drop Insert *")
                self.grafoInsert_Data(i.id_table,i.valores, padre)
            #-----------------------------------
            elif isinstance(i, CreateTable):
                self.grafoCreateTable(i.id, i.cuerpo, i.inhe, padre)

            elif isinstance(i, CreateDataBase):
                self.grafoCreateDataBase(i.replace, i.exists, i.idBase, i.idOwner ,i.Modo, padre)

            elif isinstance(i, Delete_Datos):
                print("Es Una Instruccion Delete")
                self.grafoDelete_Data(i.id_table,i.valore_where,padre)

            elif isinstance(i, Update_Datos):
                print("Es Una Instruccion Update")
                self.grafoUpdate__Data(i.id_table,i.valores_set,i.valor_where,padre)

            elif isinstance(i, Alter_COLUMN):
                print("Es Una Instruccion Alter  Column")
                self.grafoAlter_Column(i.idtabla,i.columnas,padre)

            elif isinstance(i, Alter_Table_AddColumn):
                print("Es Una Instruccion Alter Add Column")
                self.grafoAlter_AddColumn(i.id_table, i.id_columnas, padre)

            elif isinstance(i, ShowDatabases):
                print("Es Una Instruccion Showdatabases")
                self.grafoShowDatabases(i.cadenaLike, padre)

            elif isinstance(i, AlterDataBase):
                print("Es Una Instruccion AlterDataBase")
                self.grafoAlterDataBase(i.idDB, i.opcion, padre)

            elif isinstance(i, DropDataBase):
                print("Es Una Instruccion DropDataBase")
                self.grafoDropDataBase(i.id, i.existe, padre)

            elif isinstance(i, SelectExtract):
                print("Es Una Instruccion SelectExtract")
                self.grafoSelectExtract(i.tipoTiempo, i.cadenaFecha, padre)

            elif isinstance(i, SelectDatePart):
                print("Es Una Instruccion SelectDatePart")
                self.grafoSelectDatePart(i.cadena, i.cadenaIntervalo, padre)

            elif isinstance(i, SelectTipoCurrent):
                print("Es Una Instruccion SelectCurrentType")
                self.grafoSelectTipoCurrent(i.tipoCurrent, padre)

            elif isinstance(i, SelectStamp):
                print("Es Una Instruccion SelectTIMESTAMP")
                self.grafoSelectStamp(i.cadena, padre)

            elif isinstance(i, Selectnow):
                print("Es Una Instruccion Select Now")
                self.grafoSelectnow(i.constru, padre)

            elif isinstance(i, CreacionEnum):
                print("Es Una Instruccion CReate Type ENUM")
                self.grafoCreacionEnum(i.listaCadenas, padre)

            elif isinstance(i, Alter_Table_AddColumn):
                self.grafoAlter_AddColumn(i.id_table,i.id_columnas,padre)
            elif isinstance(i, Alter_Table_Drop_Column):
                print("es una instruccion alter drop column")
                self.grafoAlter_DropColumn(i.id_table, i.columnas, padre)
            elif isinstance(i, Alter_Table_Rename_Column):
                self.grafoAlter_RenameColumn(i.id_table, i.old_column, i.new_column, padre)
            elif isinstance(i, Alter_Table_Drop_Constraint):
                self.grafoAlter_DropConstraint(i.id_tabla, i.id_constraint, padre)
            elif isinstance(i, Alter_table_Alter_Column_Set):
                self.grafoAlter_AlterColumnSet(i.id_tabla, i.id_column, padre )
            elif isinstance(i, Alter_table_Add_Foreign_Key):
                self.grafoAlter_AddForeignKey(i.id_table, i.id_column, i.id_column_references, padre)
            elif isinstance(i, Alter_Table_Add_Constraint):
                self.grafoAlter_AddConstraint(i.id_table, i.id_constraint, i.id_column, padre)
            
            else:
                print("No es droptable")





    def RecorrerTipoSelect(self, sente, padre):
        i=sente
        if isinstance(i, Select):
            print("Es Una Instruccion Select ")
            self.GrafoSelect(i.Lista_Campos, i.Nombres_Tablas, i.unionn, padre)
        elif isinstance(i, Select2):
            print("Es Una Instruccion Select 2")
            self.GrafoSelect2(i.Lista_Campos, i.Nombres_Tablas, i.Cuerpo, i.unionn, padre)

        elif isinstance(i, Select3):
            print("Es Una Instruccion Select 3 ")
            self.GrafoSelect3(i.distinct,i.Lista_Campos, i.Nombres_Tablas, i.unionn, padre)

        elif isinstance(i, Select4):
            print("Es Una Instruccion Select 4")
            self.GrafoSelect4(i.distinct, i.Lista_Campos, i.Nombres_Tablas, i.Cuerpo, i.unionn, padre)
        else:
            print("No hay tipo aun");





    # ----------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------
    # INSTRUCCIONES NECESARIAS PARA LOS SELECT
    # ----------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------


    # CAMPOS ACCEDIDOS
    # ----------------------------------------------------------------------------------------------------------

    # Objeto Que Accede A este Tipo "Campo_Accedido"
    # Campos Accedidos Con Lista
    def GrafoCampo_Accedido(self, NombreT, Columna, Lista_Alias, padre):
        global dot
        # NombreT.Campo Lista
        if ((NombreT != "") and (Columna != "") and (Lista_Alias != False )):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), NombreT + '.' + Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la Lista de Alias
            self.inc();
            dot.node('Node' + str(self.i), "Lista_Alias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerTiposAlias(Lista_Alias, 'Node' + str(self.i))

        # Campo Lista
        elif ((NombreT == "") and (Columna != "") and (Lista_Alias != False)):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))
            self.inc();
            dot.node('Node' + str(self.i), Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la Lista de Alias
            self.inc();
            dot.node('Node' + str(self.i), "Lista_Alias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            # Recorrer la lista de alias
            self.RecorrerTiposAlias(Lista_Alias, 'Node' + str(self.i))
        else:
            print("Error Sintactico")


        #Objeto Que Accede A este Tipo "Campo_AccedidoSinLista"
        # Campos Accedidos Sin Lista
    def GrafoCampo_AccedidoSinLista(self, NombreT, Columna, padre):
        global dot
         # NombreT.Campo
        if ((NombreT != "") and (Columna != "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), NombreT + '.' + Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        # Campo
        elif ((NombreT == "") and (Columna != "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))
            self.inc();
            dot.node('Node' + str(self.i), Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        else:
            print("Error Sintactico")





    # NOMBRE TABLAS ACCEDIDOS
    # ----------------------------------------------------------------------------------------------------------

    #Objeto Que accede "AccesoTabla"
    #Nombres Lista Accedidos  Con lista
    def GrafoAccesoTabla(self, NombreT, Lista_Alias, padre):
        global dot
        if ((NombreT != "") and (Lista_Alias != False)):

            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Nombre_Tabla")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), NombreT)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la Lista de Alias
            self.inc();
            dot.node('Node' + str(self.i), "Lista_Alias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            # Verificar el Tipo que viene
            self.RecorrerTiposAlias(Lista_Alias, 'Node' + str(self.i))

        else:
            print("Error sintactico")


    #Objeto Que accede "AccesoTablaSinLista"
    #Nombres Lista Accedidos  Sin lista
    def GrafoAccesoTablaSinLista(self, NombreT, padre):
        global dot
        # Nombre
        if ((NombreT != "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Nombre_Tabla")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), NombreT)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        else:
            print("Error sintactico")




    # Campos Accedidos desde el group By
    # ----------------------------------------------------------------------------------------------------------

    #Objeto Que accede "AccesoGroupBy"  NombreT,Columna,Estado,Lista_Alias=[]

    #Nombres Lista Accedidos  Con lista
    def GrafoAccesoGroupBy(self, NombreT,Columna, Lista_Alias,Estado, padre):
        global dot

        # Tabla.Columna Alias
        if ((NombreT != "") and (Columna != "") and (Lista_Alias != False ) and (Estado == "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), NombreT + '.' + Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la Lista de Alias
            self.inc();
            dot.node('Node' + str(self.i), "Lista_Alias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            self.RecorrerTiposAlias(Lista_Alias, 'Node' + str(self.i))
            #Ver tipos de Alias Agregar el de Group By




        # Tabla.Columna
        elif((NombreT != "") and (Columna != "") and (Lista_Alias == False) and (Estado == "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), NombreT + '.' + Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))



        #columna Alias
        elif ((NombreT == "") and (Columna != "") and (Lista_Alias != False) and (Estado == "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i),Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la Lista de Alias
            self.inc();
            dot.node('Node' + str(self.i), "Lista_Alias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            self.RecorrerTiposAlias(Lista_Alias, 'Node' + str(self.i))
            #Agregar Tipo de Alias de Group by




        #Columna
        elif ((NombreT == "") and (Columna != "") and (Lista_Alias == False) and (Estado == "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))
            self.inc();
            dot.node('Node' + str(self.i), Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))


        #Tabla.Columna Alias Estado
        elif ((NombreT != "") and (Columna != "") and (Lista_Alias != False) and (Estado != "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))
            self.inc();
            dot.node('Node' + str(self.i), NombreT + '.' + Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la Lista de Alias
            self.inc();
            dot.node('Node' + str(self.i), "Lista_Alias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerTiposAlias(Lista_Alias, 'Node' + str(self.i))


            #Recorrer Listado de Estados

        #Tabla.Columna  Estado
        elif ((NombreT != "") and (Columna != "") and (Lista_Alias == False) and (Estado != "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))
            self.inc();
            dot.node('Node' + str(self.i), NombreT + '.' + Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))


            self.inc();
            dot.node('Node' + str(self.i), Estado)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        #Columna Alias Estado
        elif ((NombreT == "") and (Columna != "") and (Lista_Alias != False) and (Estado != "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))
            self.inc();
            dot.node('Node' + str(self.i),  Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la Lista de Alias
            self.inc();
            dot.node('Node' + str(self.i), "Lista_Alias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerTiposAlias(Lista_Alias, 'Node' + str(self.i))
            #Agregar el tipo de alias del group by

            # Estado
            self.inc();
            dot.node('Node' + str(self.i), Estado)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))


        #Columna  Estado
        elif ((NombreT == "") and (Columna != "") and (Lista_Alias == False) and (Estado != "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Estado
            self.inc();
            dot.node('Node' + str(self.i), Estado)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        else:
            print("Verificar Errores Sintacticos")



    # Campos Accedidos desde Las Subconsultas
    # ----------------------------------------------------------------------------------------------------------

    #Objeto Que accede "AccesoSubConsultas"  AnteQuery=[], Query=[], Lista_Alias=[]
    #Nombres Lista Accedidos  Con Las Subconsultas

    def GrafoAccesoSubConsultas(self, AnteQuery,Query, Lista_Alias, padre):
        print(AnteQuery, Query, Lista_Alias)
        #AnteQuery ( query )
        if  (AnteQuery != False) and  (Query !=False) and  (Lista_Alias ==False):

            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Acceso_Subconsulta")
            dot.edge(padre, 'Node' + str(self.i))


            #Recorrido de las Expresiones Ante Query
            self.inc();
            dot.node('Node' + str(self.i), "AnteQuery")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.Recorrer_Condiciones(AnteQuery, 'Node' + str(self.i))



            #Recorrido de las subconsultas
            self.inc();
            dot.node('Node' + str(self.i), "(  SubQuery  )")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerListaSubconsultas(Query,'Node' + str(self.i) )


        # AnteQuery ( query ) Alias
        elif (AnteQuery != False) and (Query != False) and (Lista_Alias != False):

            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Acceso_Subconsulta")
            dot.edge(padre, 'Node' + str(self.i))

            # Recorrido de las Expresiones Ante Query
            self.inc();
            dot.node('Node' + str(self.i), "AnteQuery ")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.Recorrer_Condiciones(AnteQuery, 'Node' + str(self.i))

            # Recorrido de las subconsultas
            self.inc();
            dot.node('Node' + str(self.i), "(  SubQuery  )")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerListaSubconsultas(Query, 'Node' + str(self.i))

            # Recorrido De la Lista de Alias
            self.inc();
            dot.node('Node' + str(self.i), "Lista_Alias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerTiposAlias(Lista_Alias, 'Node' + str(self.i))


        # ( query )
        elif (AnteQuery == False) and (Query != False) and (Lista_Alias == False):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Acceso_Subconsulta ")
            dot.edge(padre, 'Node' + str(self.i))

            # Recorrido de las subconsultas
            self.inc();
            dot.node('Node' + str(self.i), "(  SubQuery  )")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerListaSubconsultas(Query, 'Node' + str(self.i))


        # ( query ) Alias
        elif (AnteQuery == False) and (Query != False) and (Lista_Alias != False):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Acceso_Subconsulta")
            dot.edge(padre, 'Node' + str(self.i))

            # Recorrido de las subconsultas
            self.inc();
            dot.node('Node' + str(self.i), "(  SubQuery  )")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerListaSubconsultas(Query, 'Node' + str(self.i))

            # Recorrido De la Lista de Alias
            self.inc();
            dot.node('Node' + str(self.i), "Lista_Alias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerTiposAlias(Lista_Alias, 'Node' + str(self.i))
