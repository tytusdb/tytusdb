from Instruccion import *
from expresiones import *
import interprete as Inter
from sentencias import *
from Temporales import *

class SqlComandos:

    def __init__(self, sentencia, ts_global = None, t_global = None, ambitoFuncion = None):
        self.sentencia = sentencia
        self.CadenaSQL = None
        self.ts_global = ts_global
        self.t_global = t_global
        self.ambitoFuncion = ambitoFuncion

    def generarCadenaSQL(self):
        i = self.sentencia
        if isinstance(i, DropTable):
            print("Si es un drop table *")
            self.CadenaSQL = self.grafoDropTable(i.id)

        elif isinstance(i, Select):
            print("Es Una Instruccion Select")
            self.CadenaSQL = self.GrafoSelect(i.Lista_Campos, i.Nombres_Tablas, i.unionn)

        elif isinstance(i, Select2):
            print("Es Una Instruccion Select2")
            self.CadenaSQL = self.GrafoSelect2(i.Lista_Campos, i.Nombres_Tablas, i.Cuerpo, i.unionn)

        elif isinstance(i, Select3):
            print("Es Una Instruccion Select 3 ")
            self.CadenaSQL = self.GrafoSelect3(i.distinct, i.Lista_Campos, i.Nombres_Tablas, i.unionn)

        elif isinstance(i, Select4):
            print("Es Una Instruccion Select 4")
            self.CadenaSQL = self.GrafoSelect4(i.distinct, i.Lista_Campos, i.Nombres_Tablas, i.Cuerpo, i.unionn)

        elif isinstance(i, Insert_Datos):
            print("Si es un drop Insert *")
            self.CadenaSQL = self.grafoInsert_Data(i.id_table, i.valores)
            #self.grafoInsert_Data(i.id_table, i.valores)
        # -----------------------------------

        elif isinstance(i, CreateTable):
            print("Si es CreateTable *")
            self.CadenaSQL = self.grafoCreateTable(i.id, i.cuerpo, i.inhe)

        elif isinstance(i, CreateDataBase):
             self.CadenaSQL = self.cadena_create_database(i)

        elif isinstance(i, Delete_Datos):
            print("Es Una Instruccion Delete")
            self.CadenaSQL = self.grafoDelete_Data(i.id_table, i.valore_where)


        elif isinstance(i, Update_Datos):
            print("Es Una Instruccion Update")
            self.CadenaSQL = self.grafoUpdate__Data(i.id_table, i.valores_set, i.valor_where)

        elif isinstance(i, Alter_COLUMN):
            print("Es Una Instruccion Alter  Column")
            # self.CadenaSQL = self.cadena_alter_column(i)
            self.CadenaSQL = self.cadena_alter_column(i)

        elif isinstance(i, ShowDatabases):
            print("Es Una Instruccion Showdatabases")
            self.CadenaSQL = self.grafoShowDatabases(i.cadenaLike)

            #self.grafoShowDatabases(i.cadenaLike)

        elif isinstance(i, AlterDataBase):
            print("Es Una Instruccion AlterDataBase")
            #self.grafoAlterDataBase(i.idDB, i.opcion)

        elif isinstance(i, DropDataBase):
            print("Es Una Instruccion DropDataBase")
            self.CadenaSQL = self.cadena_drop_database(i)

        elif isinstance(i, SelectExtract):
            print("Es Una Instruccion SelectExtract")
            #self.grafoSelectExtract(i.tipoTiempo, i.cadenaFecha)

        elif isinstance(i, SelectDatePart):
            print("Es Una Instruccion SelectDatePart")
            #self.grafoSelectDatePart(i.cadena, i.cadenaIntervalo)

        elif isinstance(i, SelectTipoCurrent):
            print("Es Una Instruccion SelectCurrentType")
            #self.grafoSelectTipoCurrent(i.tipoCurrent)

        elif isinstance(i, SelectStamp):
            print("Es Una Instruccion SelectTIMESTAMP")
            #self.grafoSelectStamp(i.cadena)

        elif isinstance(i, Selectnow):
            print("Es Una Instruccion Select Now")
            #self.grafoSelectnow(i.constru)

        elif isinstance(i, CreacionEnum):
            print("Es Una Instruccion SelectCurrentType")

            #self.grafoCreacionEnum(i.listaCadenas)

        elif isinstance(i, Alter_Table_AddColumn):
            print("Es Una Instruccion SelectCurrentType")
            self.CadenaSQL = self.cadena_alter_add_column(i)

        elif isinstance(i, Alter_Table_Drop_Column):
            print("Es Una Instruccion SelectCurrentType")
            self.CadenaSQL = self.cadena_alter_drop_column(i)

        elif isinstance(i, Alter_Table_Rename_Column):
            print("Es Una Instruccion SelectCurrentType")
            #self.grafoAlter_RenameColumn(i.id_table, i.old_column, i.new_column)
            self.CadenaSQL = self.cadena_alter_rename(i)

        elif isinstance(i, Alter_Table_Drop_Constraint):
            print("Es Una Instruccion SelectCurrentType")
            #self.grafoAlter_DropConstraint(i.id_tabla, i.id_constraint)
            self.CadenaSQL = self.cadena_alter_drop_constraint(i)

        elif isinstance(i, Alter_table_Alter_Column_Set):
            print("Es Una Instruccion SelectCurrentType")
            #self.grafoAlter_AlterColumnSet(i.id_tabla, i.id_column)
            self.CadenaSQL = self.cadena_alter_column_set_not_null(i)

        elif isinstance(i, Alter_table_Add_Foreign_Key):
            print("Es Una Instruccion SelectCurrentType")
            #self.grafoAlter_AddForeignKey(i.id_table, i.id_column, i.id_column_references)
            self.CadenaSQL = self.cadena_alter_add_foreign(i)

        elif isinstance(i, Alter_Table_Add_Constraint):
            print("Es Una Instruccion SelectCurrentType")
            #self.grafoAlter_AddConstraint(i.id_table, i.id_constraint, i.id_column)
            self.CadenaSQL = self.cadena_alter_add_constraint(i)

        elif isinstance(i, SelectExpresion):
            print("Es Una Instruccion SelectCurrentType")
            self.CadenaSQL = self.grafoSelectExpresion(i)

        elif isinstance(i, Funciones_):
            print("Es Una Instruccion SelectCurrentType")
            #self.grafoFuncion(i.Reservada, i.Nombre, i.Retorno,i.Alias, i.Parametros , i.Instrucciones, i.Declaraciones , i.Codigo)

        elif isinstance(i, CrearIndice):
            print("Es Una Instruccion SelectCurrentType")
            #self.GrafoCrearIndice(i)

        elif isinstance(i,Procedimientos_):
            print("Es Una Instruccion SelectCurrentType")
            #self.GrafoProcedure(i.Reservada, i.Nombre, i.Comand,i.Alias, i.Parametros, i.Instrucciones, i.Declaraciones,i.Codigo)


        elif isinstance(i,EjecucionFuncion):
            print("Es Una Instruccion SelectCurrentType")
            #self.GrafoEjecucion(i.Id, i.Parametros)

        elif isinstance(i, useClase):
            self.CadenaSQL = "USE " + str(i.id) + ";"


        elif isinstance(i, AlterIndiceCol):
            self.CadenaSQL =self.Grafo_AlterIndexColumna(i)
            pass

        elif isinstance(i, AlterIndiceName):
            self.CadenaSQL =self.Grafo_AlterIndexName(i)
            pass

        elif isinstance(i, DropIndice):
            self.CadenaSQL = self.Grafo_DropIndex(i)
            pass

        else:
            #self.CadenaSQL = self.cadena_expresion(i)
            print("Es Una Instruccion SelectCurrentType")
            return ""





#===========================================================================   GENERACION CONDIGO SELECT

    #primer tipo de select
    def GrafoSelect(self, ListaCampos, NombresTablas, Uniones):
        Cadenita = "Select  " + str(self.RecorrerListadeCampos(ListaCampos)) + " from " + self.RecorrerListadeNombres(NombresTablas)
        Cadenita += self.RecorrerListaUniones(Uniones)
        return Cadenita



    def GrafoSelect2(self, ListaCampos, NombresTablas, cuerpo, Uniones):
        Cadenita = "Select "  + self.RecorrerListadeCampos(ListaCampos) + " from " + self.RecorrerListadeNombres(NombresTablas)
        Cadenita += self.RecorrerListaCuerpos(cuerpo) + self.RecorrerListaUniones(Uniones)
        return Cadenita


    def GrafoSelect3(self, Distict, ListaCampos, NombresTablas, Uniones):
        Cadenita = "Select "+ Distict +" "+ self.RecorrerListadeCampos(ListaCampos) + " from " + self.RecorrerListadeNombres(NombresTablas)
        Cadenita +=  self.RecorrerListaUniones(Uniones)
        return Cadenita


    def GrafoSelect4(self, Distict, ListaCampos, NombresTablas, cuerpo, Uniones, padre):
        Cadenita = "Select "+ Distict  +"  "+ self.RecorrerListadeCampos(ListaCampos) + " from " + self.RecorrerListadeNombres(NombresTablas)
        Cadenita += self.RecorrerListaCuerpos(cuerpo) + self.RecorrerListaUniones(Uniones)
        return Cadenita


#Recorriendo lista de Campos
    def RecorrerListadeCampos(self, Campos):
        Cadenita=""
        Contador= 0
        for j in Campos:
            if isinstance(j, Campo_AccedidoSinLista):
                if Contador+1 == len(Campos):
                    Cadenita += self.GrafoCampo_AccedidoSinLista(j.NombreT, j.Columna)
                else:
                    Cadenita+= self.GrafoCampo_AccedidoSinLista(j.NombreT, j.Columna)+","
            elif isinstance(j, AccesoSubConsultas):
                if Contador + 1 == len(Campos):
                    Cadenita += self.GrafoAccesoSubConsultas(j.AnteQuery, j.Query, j.Lista_Alias)
                else:
                    Cadenita += self.GrafoAccesoSubConsultas(j.AnteQuery, j.Query, j.Lista_Alias)+","

            elif isinstance(j, CaseCuerpo):
                if Contador + 1 == len(Campos):
                    Cadenita += self.GrafoCampoCasePuro(j.Lista_When, j.Cuerpo)
                else:
                    Cadenita += self.GrafoCampoCasePuro(j.Lista_When, j.Cuerpo)+","

            elif isinstance(j, ExpresionesCase):
                if Contador + 1 == len(Campos):
                    Cadenita += self.GrafoExpresionCase(j.Reservada, j.ListaExpresiones)
                else:
                    Cadenita += self.GrafoExpresionCase(j.Reservada, j.ListaExpresiones)+","
            elif  isinstance(j,ProcesoCount):
                   Cadenita  += self.Grafo_Count(j)
            else:
                print("No Ningun Tipo  vos ")

            Contador +=1
        return  Cadenita

#Tipos de acceso a los campos
    def GrafoCampo_AccedidoSinLista(self, NombreT, Columna):
        Cadenita = ""
        if not isinstance(Columna, string_types):
            Cadenita += " " +self.cadena_expresion(Columna)+" "  # self.graficar_expresion(Columna)

        elif ((NombreT != "") and (Columna != "")):
            Cadenita +=  NombreT + '.' + Columna

        # Campo
        elif ((NombreT == "") and (Columna != "")):
            Cadenita += Columna
        else:
            print("Error Sintactico")

        return Cadenita

    def GrafoAccesoSubConsultas(self, AnteQuery, Query, Lista_Alias):
        Cadenita =""
        # AnteQuery ( query )
        if (AnteQuery != False) and (Query != False) and (Lista_Alias == False):
            #Recorre Condiciones
            Cadenita += " " +self.cadena_expresion(AnteQuery)+" "  # self.graficar_expresion(AnteQuery)
            #Se sustituyo ya que recorre solo expresiones
            #self.Recorrer_Condiciones(AnteQuery)

            #Recorre la lista Querys
            Cadenita += self.RecorrerListaSubconsultas(Query)

        # AnteQuery ( query ) Alias
        elif (AnteQuery != False) and (Query != False) and (Lista_Alias != False):
            #Recorre Condiciones
            Cadenita += " " +self.cadena_expresion(AnteQuery)+" "  # self.graficar_expresion(AnteQuery)
            #Se sustituyo ya que recorre solo expresiones
            #self.Recorrer_Condiciones(AnteQuery)

            #Recorre la lista Querys
            Cadenita += self.RecorrerListaSubconsultas(Query)

            #Recorre los tipos de alias
            Cadenita += self.RecorrerTiposAlias(Lista_Alias)

        # ( query )
        elif (AnteQuery == False) and (Query != False) and (Lista_Alias == False):
            #Recorre la lista Querys
            Cadenita += self.RecorrerListaSubconsultas(Query)

        # ( query ) Alias
        elif (AnteQuery == False) and (Query != False) and (Lista_Alias != False):
            #Recorre la lista Querys
            Cadenita += self.RecorrerListaSubconsultas(Query)
            #Recorre los tipos de alias
            Cadenita += self.RecorrerTiposAlias(Lista_Alias)

        return Cadenita

    def GrafoCampoCasePuro(self, Lista_When, Cuerpo):
        Cadenita = ""
        Cadenita += " Case " + str(self.RecorrerListaWhens(Lista_When)) + str(Cuerpo)
        return Cadenita

    def GrafoExpresionCase(self, Reservada, ListaExpresiones):
        Cadenita =str(Reservada) +  self.Recorrer_CondicioneSLista(ListaExpresiones)
        return  Cadenita

    def RecorrerListaSubconsultas(self, i):
        Cadenita = ""
        if isinstance(i, SubSelect):
            print("Es un Campo Accedido Por una Subconsulta ")
            Cadenita += self.GrafoSubSelect(i.Lista_Campos, i.Nombres_Tablas)
        elif isinstance(i, SubSelect2):
            print("Es un Campo Accedido Por una Subconsulta 2 ")
            Cadenita += self.GrafoSubSelect2(i.Lista_Campos, i.Nombres_Tablas, i.Cuerpo)
        elif isinstance(i, SubSelect3):
            print("Es un Campo Accedido Por una Subconsulta 3 ")
            Cadenita += self.GrafoSubSelect3(i.Distict, i.Lista_Campos, i.Nombres_Tablas)
        elif isinstance(i, SubSelect4):
            print("Es un Campo Accedido Por una Subconsulta 4 ")
            Cadenita += self.GrafoSubSelect4(i.Distict, i.Lista_Campos, i.Nombres_Tablas, i.Cuerpo)
        else:
            print("No hay Ningun Tipo")

        return Cadenita

    def RecorrerTiposAlias(self, i):
        Cadenita = ""
        # Alias de los Campos Sin Lista
        if isinstance(i, Alias_Campos_ListaCamposSinLista):
            print("Es un Campo Accedido Por la Tabla" + i.Alias)
            Cadenita += self.GrafoAlias_Campos_ListaCamposSinLista(i.Alias)
        # Alias de las Nombres de las Tablas Sin Lista
        elif isinstance(i, Alias_Table_ListaTablasSinLista):
            # print("Es un Campo Accedido Por la Tabla" + i.Alias)
            Cadenita += self.GrafoAlias_Table_ListaTablasSinLista(i.Alias)
        # Alias de los Group By Sin Lista
        elif isinstance(i, Alias_Tablas_GroupSinLista):
            #  print("Es un Campo Accedido Por la Tabla" + i.Alias)
            Cadenita += self.GrafoAlias_Tablas_GroupSinLista(i.Alias)
        # Alias de las Subconsulta sin lista
        elif isinstance(i, Alias_SubQuerysSinLista):
            print("Es un Campo Accedido Por subconsulta sin lista " + i.Alias)
            Cadenita += self.GrafoAlias_SubQuerysSinLista(i.Alias)
        else:
            print("No Ningun Tipo")

        return Cadenita

    def RecorrerListaWhens(self, Lista):
        Cadenita = ""
        for i in Lista:
            if isinstance(i, TiposWhen):
                print("Es un Acceso A Tipo determinado de When")
                Cadenita +=  self.GrafoTiposWhen(i.Reservada, i.ListaExpresiones1, i.Reservada2, i.ListaExpresiones2, i.Reservada3,i.ListaExpresiones3)
            else:
                print("No Ningun Tipo")
        return Cadenita


    def GrafoTiposWhen(self, Reservada, ListaExpresiones1, Reservada2, ListaExpresiones2, Reservada3, ListaExpresiones3):
        Cadenita = ""

        # When ListaExpresiones1 then listaExpresiones3
        if ((Reservada != "") and (ListaExpresiones1 != False) and (Reservada2 == "") and
           (ListaExpresiones2 == False) and (Reservada3 != "") and (ListaExpresiones3 != False)):

            Cadenita += Reservada
            Cadenita +=" " +self.cadena_expresion(ListaExpresiones1)+" "   # self.graficar_expresion(AnteQuery)
            # Se sustituyo ya que recorre solo expresiones
            #self.Recorrer_Condiciones(ListaExpresiones1, 'Node' + str(self.i))



            Cadenita += Reservada3
            Cadenita += " " +self.cadena_expresion(ListaExpresiones3)+" "  # self.graficar_expresion(AnteQuery)
            # Se sustituyo ya que recorre solo expresiones
            #self.Recorrer_Condiciones(ListaExpresiones3, 'Node' + str(self.i))


        # When ListaExpresiones1 Else listaExpresiones2 then ListaExpresiones3
        if ((Reservada != "") and (ListaExpresiones1 != False) and (Reservada2 != "") and
            (ListaExpresiones2 != False) and (Reservada3 != "") and (ListaExpresiones3 != False)):
            Cadenita += Reservada
            Cadenita += " " +self.cadena_expresion(ListaExpresiones1)+" "   # self.graficar_expresion(AnteQuery)
            # Se sustituyo ya que recorre solo expresiones
            #self.Recorrer_Condiciones(ListaExpresiones1, 'Node' + str(self.i))


            Cadenita += Reservada2
            Cadenita += " " +self.cadena_expresion(ListaExpresiones2)+" "   # self.graficar_expresion(AnteQuery)
            # Se sustituyo ya que recorre solo expresiones
            #self.Recorrer_Condiciones(ListaExpresiones2, 'Node' + str(self.i))

            Cadenita += Reservada3
            Cadenita += " " +self.cadena_expresion(ListaExpresiones3)+" "  # self.graficar_expresion(AnteQuery)
            # Se sustituyo ya que recorre solo expresiones
            #self.Recorrer_Condiciones(ListaExpresiones3, 'Node' + str(self.i))

        # When ListaExpresiones1
        if ((Reservada != "") and (ListaExpresiones1 != False) and (Reservada2 == "") and
           (ListaExpresiones2 == False) and (Reservada3 == "") and (ListaExpresiones3 == False)):

            Cadenita += Reservada
            Cadenita += " " + self.cadena_expresion(ListaExpresiones1) +" "   # self.graficar_expresion(AnteQuery)
            # Se sustituyo ya que recorre solo expresiones
            # self.Recorrer_Condiciones(ListaExpresiones1, 'Node' + str(self.i))


        # When ListaExpresiones1 Else listaExpresiones2
        if ((Reservada != "") and (ListaExpresiones1 != False) and (Reservada2 != "") and
           (ListaExpresiones2 != False) and (Reservada3 == "") and (ListaExpresiones3 == False)):

            Cadenita += Reservada
            Cadenita += " " +self.cadena_expresion(ListaExpresiones1)+" "   # self.graficar_expresion(AnteQuery)
            # Se sustituyo ya que recorre solo expresiones
            # self.Recorrer_Condiciones(ListaExpresiones1, 'Node' + str(self.i))

            Cadenita += Reservada2
            Cadenita += " " +self.cadena_expresion(ListaExpresiones2)+" "   # self.graficar_expresion(AnteQuery)
            # Se sustituyo ya que recorre solo expresiones
            # self.Recorrer_Condiciones(ListaExpresiones2, 'Node' + str(self.i))

        return Cadenita

    def Recorrer_CondicioneSLista(self, Lista):
        Cadenita = ""
        for i in Lista:
            # LLAMAMOS A GRAFICAR EXPRESION
            if(str(i)!=","):
                Cadenita +=" " +self.cadena_expresion(Lista)+" "   # self.graficar_expresion(i)
            else:
                print("Es una Coma")
        return Cadenita


#tipos de alias
    def GrafoAlias_Campos_ListaCamposSinLista(self, Alias):
        Cadenita = ""
        # as Alias
        if ((Alias != "")):
            Cadenita += "  As  " + str(Alias) + "  "
        else:
            print("Verificar Errores Sintacticos")

        return  Cadenita


    def GrafoAlias_Table_ListaTablasSinLista(self, Alias):
        Cadenita = ""
        # as Alias
        if ((Alias != "")):
            Cadenita += "  As  " + str(Alias) + "  "
        else:
            print("Verificar Errores Sintacticos")

        return Cadenita

    def GrafoAlias_Tablas_GroupSinLista(self, Alias):
        Cadenita = ""
        # as Alias
        if ((Alias != "")):
            Cadenita += " As " + str(Alias)  + "  "
        else:
            print("Verificar Errores Sintacticos")

        return Cadenita

    def GrafoAlias_SubQuerysSinLista(self, Alias):
        Cadenita = ""
        # as Alias
        if ((Alias != "")):
            Cadenita += " As " + str(Alias) + "  "
        else:
            print("Verificar Errores Sintacticos")

        return Cadenita



#todo Referente los nombres de las tablas
    def RecorrerListadeNombres(self, Nombres ):
        Cadenita = ""
        Contador = 0
        for i in Nombres:
            if isinstance(i, AccesoTabla):

                if Contador+1==len(Nombres):
                    # print("Es un Campo Accedido Por la Tabla" + i.NombreT)
                    Cadenita += self.GrafoAccesoTabla(i.NombreT, i.Lista_Alias)
                else:
                    Cadenita += self.GrafoAccesoTabla(i.NombreT, i.Lista_Alias)+","

            elif isinstance(i, AccesoTablaSinLista):
                if Contador+1==len(Nombres):
                    # print("Es un Campo Accedido Por la Tabla" + i.NombreT)
                    Cadenita += self.GrafoAccesoTablaSinLista(i.NombreT)
                else:
                    # print("Es un Campo Accedido Por la Tabla" + i.NombreT)
                    Cadenita += self.GrafoAccesoTablaSinLista(i.NombreT)+","

            elif isinstance(i, AccesoSubConsultas):
                if Contador+1==len(Nombres):
                    print("Es un Acceso a  una subconsulta")
                    Cadenita += self.GrafoAccesoSubConsultas(i.AnteQuery, i.Query, i.Lista_Alias)
                else:
                    print("Es un Acceso a  una subconsulta")
                    Cadenita += self.GrafoAccesoSubConsultas(i.AnteQuery, i.Query, i.Lista_Alias)+","
            else:
                print("No Ningun Tipo")

        return  Cadenita

    def GrafoAccesoTabla(self, NombreT, Lista_Alias):
        Cadenita = ""
        if ((NombreT != "") and (Lista_Alias != False)):
            Cadenita += NombreT
            # Verificar el Tipo que viene
            Cadenita += self.RecorrerTiposAlias(Lista_Alias)

        else:
            print("Error sintactico")

        return  Cadenita

    def GrafoAccesoTablaSinLista(self, NombreT):
        Cadenita = ""
        # Nombre
        if ((NombreT != "")):
            Cadenita += NombreT
        else:
            print("Error sintactico")

        return Cadenita



# todo Referente a las uniones
    def RecorrerListaUniones(self, Uniones):
        Cadenita = ""
        for i in Uniones:
            if isinstance(i, CamposUnions):
                print("Es un Campo Accedido Por una Subconsulta ")
                Cadenita += self.GrafoAccesoUniones(i.Reservada, i.Comportamiento, i.Consulta)
            else:
                print("No hay Ningun Tipo")

        return  Cadenita

    def GrafoAccesoUniones(self, Reservada, Comportamiento, Consulta):
        Cadenita = ""
        # Comportamiento Reservada Consulta
        if ((Comportamiento != "") and (Reservada != "") and (Consulta != False)):

            Cadenita += "\n " + Reservada +"  " +  Comportamiento +" \n"
            Cadenita += self.RecorrerTipoSelect(Consulta)


        # Comportamiento Consulta
        elif ((Comportamiento != "") and (Reservada == "") and (Consulta != False)):

            Cadenita += "\n " + Comportamiento + " \n"
            Cadenita += self.RecorrerTipoSelect(Consulta)

        # puntocoma
        elif ((Comportamiento == "") and (Reservada != "") and (Consulta == False)):

            Cadenita += "; \n"

        else:
            print("Verificar Errores Sinstacticos")

        return  Cadenita




#tipos de select
    def RecorrerTipoSelect(self, i):
        Cadenita = ""
        if isinstance(i, Select):
            print("Es Una Instruccion Select ")
            Cadenita += self.GrafoSelect(i.Lista_Campos, i.Nombres_Tablas, i.unionn)

        elif isinstance(i, Select2):
            print("Es Una Instruccion Select 2")
            Cadenita += self.GrafoSelect2(i.Lista_Campos, i.Nombres_Tablas, i.Cuerpo, i.unionn)

        elif isinstance(i, Select3):
            print("Es Una Instruccion Select 3 ")
            Cadenita += self.GrafoSelect3(i.distinct, i.Lista_Campos, i.Nombres_Tablas, i.unionn)

        elif isinstance(i, Select4):
            print("Es Una Instruccion Select 4")
            Cadenita += self.GrafoSelect4(i.distinct, i.Lista_Campos, i.Nombres_Tablas, i.Cuerpo, i.unionn)
        else:
            print("No hay tipo aun")

        return Cadenita



#todo Referente al cuerpo de las tablas
    def RecorrerListaCuerpos(self, Groups):
        Cadenita = ""
        for i in Groups:
            if isinstance(i, Cuerpo_TipoWhere):
                print("Es un Acceso a Where")
                Cadenita += self.GrafoCuerpo_Condiciones(i.Cuerpo)

            elif isinstance(i, GroupBy):
                print("Es un Campo Accedido Por la Cuerpo ")
                Cadenita += self.GrafoGroupBy(i.Lista_Campos, i.Condiciones)


            elif isinstance(i, OrderBy):
                print("Es un Campo Accedido  Order by ")
                Cadenita += self.GrafoOrderBy(i.Lista_Campos, i.Condiciones)

            elif isinstance(i, AccesoLimit):
                print("Es un Campo Accedido Limit ")
                Cadenita += self.GrafoLimit(i.Reservada, i.Expresion_Numerica)


            elif isinstance(i, AccesoSubConsultas):
                print("Es un Acceso a  una subconsulta")
                Cadenita += self.GrafoAccesoSubConsultas(i.AnteQuery, i.Query, i.Lista_Alias)

            elif isinstance(i, Cuerpo_Condiciones):
                print("Es un acceso a where con condicion de subconsulta")
                Cadenita += self.GrafoCuerpo_Condiciones(i.Cuerpo)

            else:
                print("No Ningun Tipo")

        return  Cadenita


    def GrafoCuerpo_Condiciones(self, Lista):
        Cadenita = " Where "  + " " + self.cadena_expresion(Lista) + " " #self.Recorrer_Condiciones(Lista)
        return  Cadenita


    def GrafoGroupBy(self, Lista_Campos, Condiciones):
        Cadenita = ""
        # Group by ListaCampos Having Condiciones
        if ((Lista_Campos != False) and (Condiciones != False)):

            Cadenita += " GROUP BY " +  self.RecorrerListaCamposGroupBy(Lista_Campos)
            Cadenita += " HAVING  " + " " +self.cadena_expresion(Condiciones)+" " # self.Recorrer_Condiciones(Condiciones)

        # Group by ListaCampos
        elif ((Lista_Campos != False) and (Condiciones == False)):
            Cadenita += " GROUP BY " + self.RecorrerListaCamposGroupBy(Lista_Campos)

        return  Cadenita



    # grafo Order by
    def GrafoOrderBy(self, Lista_Campos, Condiciones):
        Cadenita = ""
        # Group by ListaCampos Having Condiciones
        if ((Lista_Campos != False) and (Condiciones != False)):
            Cadenita += " ORDER BY " +  self.RecorrerListaCamposGroupBy(Lista_Campos)
            Cadenita += " HAVING  " + " " +self.cadena_expresion(Condiciones)+" "

        # Group by ListaCampos
        elif ((Lista_Campos != False) and (Condiciones == False)):
            Cadenita += " ORDER BY " + self.RecorrerListaCamposGroupBy(Lista_Campos)


    # Grafo de los Limit
    def GrafoLimit(self, Reservada, Expresion_Numerica):
        Cadenita = Reservada + str(Expresion_Numerica)
        return  Cadenita



    def RecorrerListaCamposGroupBy(self, Lista_Campos):
        Cadenita = ""
        Contador = 0

        for i in Lista_Campos:
            if(Contador+1 != len(Lista_Campos)):
                if isinstance(i, AccesoGroupBy):
                    # print("Es un Campo Accedido Por la Cuerpo ")
                    Cadenita +=  " "+ self.GrafoAccesoGroupBy(i.NombreT, i.Columna, i.Lista_Alias, i.Estado)+ ",  "

                else:
                    print("No hay Ningun Tipo")
            else:
                if isinstance(i, AccesoGroupBy):
                    # print("Es un Campo Accedido Por la Cuerpo ")
                    Cadenita += " "+ self.GrafoAccesoGroupBy(i.NombreT, i.Columna, i.Lista_Alias, i.Estado)+ "  "
                else:
                    print("No hay Ningun Tipo")
            Contador+=1
        return Cadenita


    def GrafoAccesoGroupBy(self, NombreT, Columna, Lista_Alias, Estado):
        Cadenita =""
        # Tabla.Columna Alias
        if ((NombreT != "") and (Columna != "") and (Lista_Alias != False) and (Estado == "")):

            Cadenita += NombreT + '.' + Columna + " AS "+ self.RecorrerTiposAlias(Lista_Alias)

        # Tabla.Columna
        elif ((NombreT != "") and (Columna != "") and (Lista_Alias == False) and (Estado == "")):
            Cadenita += NombreT + '.' + Columna

        # columna Alias
        elif ((NombreT == "") and (Columna != "") and (Lista_Alias != False) and (Estado == "")):

            Cadenita += Columna + "AS "+ self.RecorrerTiposAlias(Lista_Alias)

        # Columna
        elif ((NombreT == "") and (Columna != "") and (Lista_Alias == False) and (Estado == "")):

            Cadenita += Columna

        # Tabla.Columna Alias Estado
        elif ((NombreT != "") and (Columna != "") and (Lista_Alias != False) and (Estado != "")):
            Cadenita += NombreT + '.' + Columna + " AS " + self.RecorrerTiposAlias(Lista_Alias) + str(Estado)


        # Tabla.Columna  Estado
        elif ((NombreT != "") and (Columna != "") and (Lista_Alias == False) and (Estado != "")):

            Cadenita += NombreT + '.' + Columna +  str(Estado)

        # Columna Alias Estado
        elif ((NombreT == "") and (Columna != "") and (Lista_Alias != False) and (Estado != "")):

            Cadenita += Columna + "AS " + self.RecorrerTiposAlias(Lista_Alias) + str(Estado)

        # Columna  Estado
        elif ((NombreT == "") and (Columna != "") and (Lista_Alias == False) and (Estado != "")):

            Cadenita += Columna  + str(Estado)
        else:
            print("Verificar Errores Sintacticos")


        return  Cadenita

#Grafos Acerca de los Subquerys


    # GRAFO DEL SUB SELECT
    def GrafoSubSelect(self, ListaCampos, NombresTablas):
        Cadenita = "( Select " + self.RecorrerListadeCampos(ListaCampos) +  "From  "+ self.RecorrerListadeNombres(NombresTablas) + ") "

        return  Cadenita


    # Grafo Sub Select Con Cuerpo
    def GrafoSubSelect2(self, ListaCampos, NombresTablas, cuerpo):
        Cadenita = "( Select " + self.RecorrerListadeCampos(ListaCampos) + " From  " + self.RecorrerListadeNombres(NombresTablas)
        Cadenita += self.RecorrerListaCuerpos(cuerpo)+ ") "

        return Cadenita



    def GrafoSubSelect3(self, Distinct, ListaCampos, NombresTablas):
        Cadenita = "( Select " + Distinct +"  "+  self.RecorrerListadeCampos(ListaCampos) + "From  " + self.RecorrerListadeNombres(NombresTablas)+ ") "

        return Cadenita

    # Grafo Sub Select Con Cuerpo
    def GrafoSubSelect4(self, Distinct, ListaCampos, NombresTablas, cuerpo):

        Cadenita = "( Select "  + Distinct+"  " + self.RecorrerListadeCampos(ListaCampos) + "From  " + self.RecorrerListadeNombres(NombresTablas)
        Cadenita += self.RecorrerListaCuerpos(cuerpo)+ ") "

        return Cadenita




# ===========================================================================   GENERACION CONDIGO CREATE TABLE

    def grafoCreateTable(self, id, cuerpo, inher):
        Cadenita = "\n CREATE TABLE " + id + " (\n"
        contador = 0

        for k in cuerpo:
            if(contador+1 != len(cuerpo)):
                if isinstance(k, CampoTabla):
                    Cadenita +=  " "+self.grafoCampoTabla(k)+ ", "

                elif isinstance(k, constraintTabla):
                    Cadenita +=  " "+self.grafoConstraintTabla(k)+ ", "
            else:
                if isinstance(k, CampoTabla):
                    Cadenita += " "+self.grafoCampoTabla(k) + " "
                elif isinstance(k, constraintTabla):
                    Cadenita +=  " "+self.grafoConstraintTabla(k)+ " "

            contador +=1

        # Graficar INHERITS DE CREATE TABLE
        if inher is not None:
            # print("Si tiene un inher")
            Cadenita += self.grafoInhertis(inher.id) + " \n "
        else:
            print("No tiene inherits")


        Cadenita +=  " );"+ "\n"

        return Cadenita


    def grafoCampoTabla(self, campo):
        Cadenita = ""
        contador = 0
        Cadenita +=" \n " + str(campo.id) +" "

        if isinstance(campo.tipo, valorTipo):

            if(str(campo.tipo.valor).upper() == "VARCHAR"):
                Cadenita += " " + str(campo.tipo.valor)+ "("
                Cadenita +=  " " + str(self.cadena_expresion(campo.tipo.expresion)) +") "    # self.graficar_expresion(campo.tipo.expresion)
            else:
                Cadenita += " " + str(campo.tipo.valor)+ " "
                Cadenita +=  " " + str(self.cadena_expresion(campo.tipo.expresion)) +" "

        else:
            Cadenita += " " + str(campo.tipo)+" "

        if isinstance(campo.validaciones, list):
            for k in campo.validaciones:

                if isinstance(k, CampoValidacion):
                    if k.id != None and k.valor != None:
                        Cadenita += " " + self.grafoCampoValidaciones(k) + "  "

                    elif k.id != None and k.valor == None:
                        Cadenita += " " + self.grafoCampoValidaciones(k) + "  "
                contador+=1
        else :
            if isinstance(campo.validaciones, CampoValidacion):
                if campo.validaciones.id != None and campo.validaciones.valor != None:
                    Cadenita += " " + self.grafoCampoValidaciones(campo.validaciones) + "  "

                elif campo.validaciones.id != None and campo.validaciones.valor == None:
                    Cadenita += " " + self.grafoCampoValidaciones(campo.validaciones) + "  "
        Cadenita += " \n"
        return  Cadenita


    def grafoConstraintTabla(self, contraint):
        Cadenita = ""
        '''CONSTRAINTS OPTIONS: '''
        if contraint.valor != None:
            Cadenita += " " + str(contraint.valor)+" "
        if contraint.id != None:
            Cadenita += " " + str(contraint.id)+" "
        if contraint.condiciones != None:
            for i in contraint.condiciones:
                Cadenita +=  " " +self.cadena_expresion(i)+" "  # self.graficar_expresion(i)
        if contraint.listas_id != None:
            Cadenita += " " +self.grafoListaIDs(contraint.listas_id)+" "
        if contraint.idRef != None:
            Cadenita += " " + str(contraint.idRef)+" "
        if contraint.referencia != None:
            Cadenita += " " + self.grafoListaIDs(contraint.referencia)+" "

        return Cadenita


    def grafoInhertis(self, id):
        Cadenita = ""
        Cadenita += "INHERITS" + id

        return Cadenita



    def grafoCampoValidaciones(self, validacion):
        Cadenita = ""

        if (validacion.valor == None):
            Cadenita +=' ' + str(validacion.id)+ ' '
        else:
            Cadenita += ' ' + str(validacion.id) + ' ' + str(validacion.valor)+ ' '


        return Cadenita



    def grafoListaIDs(self, lista: ExpresionValor):
        Cadenita = ""
        Contador = 0

        for v in lista:
            if(Contador+1 != len(lista)):
                Cadenita += "  "+str(v.val)+", "
            else:
                Cadenita += "  "+str(v.val)+"  "
            Contador+=1


        return Cadenita



# ===========================================================================   GENERACION CONDIGO INSERT TABLE

    def grafoInsert_Data(self, id, valores):
        Cadenita = " INSERT INTO  "
        Contador  = 0

        Contador1 = 0

        for i in id:
            if(Contador+1 != len(id)):
                Cadenita += " " + i.val + ", "
            else:
                Cadenita += " " + i.val + " "
            Contador+=1

        Cadenita += " values( "

        # GRAFICANDO EXPRESION===========================

        for i in valores:

            if(Contador1+1 != len(valores)):
                Cadenita += " " +str(self.cadena_expresion(i))+", "
            else:
                Cadenita += " " + str(self.cadena_expresion(i)) + " "

            Contador1+=1

        Cadenita += "  );"

        return  Cadenita



# ===========================================================================   GENERACION CONDIGO DROP TABLE

    def grafoDropTable(self, id):

        Cadenita = "Drop table "
        Contador = 0

        for i in id:
            if(Contador+1!=len(id)):
                Cadenita += " " + i.val +", "
            else:
                Cadenita += " " + i.val + "  "

            Contador+=1


        Cadenita+=";"
        return Cadenita


# ===========================================================================   GENERACION CONDIGO SHOW DATABASE
    def grafoShowDatabases(self, cadenaLike):
        bandera = False
        Cadenita = "SHOW DATABASES "
        if cadenaLike != 0:
            Cadenita += " " +str(cadenaLike) + "; "
            bandera = True

        if(bandera != True):
            Cadenita+= "; "

        return Cadenita


# ===========================================================================   GENERACION CONDIGO DELETE
    def grafoDelete_Data(self, id, valores):
        Cadenita=" DELETE  From"
        Contador=0

        for i in id:
            if(Contador+1!=len(id)):
                Cadenita+= " "+i.val+", "
            else:
                Cadenita+= " "+i.val+" "

            Contador+=1

        Cadenita +=  "WHERE " + self.cadena_expresion(valores) +";  "

        return  Cadenita

# ===========================================================================   GENERACION CONDIGO UPDATE

    def grafoUpdate__Data(self, id, valores_set, valores):
        Cadenita = " UPDATE "
        Contador1= 0
        Contador2= 0


        for i in id:
            if(Contador1+1!=len(id)):
                Cadenita += " " + i.val + ", "
            else:
                Cadenita += " " + i.val + " "
            Contador1+=1




        # GRAFICAR============VALORES DEL SET======================

        Cadenita+= " SET  "

        # GRAFICANDO EXPRESION===========================
        for i in valores_set:
            if(Contador2+1!=len(valores_set)):
                Cadenita +=  " " + self.cadena_expresion(i)+", "
            else:
                Cadenita += " "  + self.cadena_expresion(i) + " "
            Contador2+=1

        # GRAFICAR============VALORES DEL WHERE======================
        Cadenita+= " WHERE  "+ self.cadena_expresion(valores) + "; "

        return  Cadenita










    def cadena_create_database(self, createDataBase):
        codigo3d = "CREATE "

        if createDataBase.replace == 1:
            codigo3d += "OR REPLACE "
        codigo3d += "DATABASE "
        if createDataBase.exists == 1:
            codigo3d += "IF NOT EXISTS "
        codigo3d += str(createDataBase.idBase)
        if createDataBase.idOwner != 0:
            codigo3d += " OWNER = " + str(createDataBase.idOwner)
        if createDataBase.Modo != 0:
            codigo3d += " MODE = " + str(createDataBase.Modo)
        codigo3d += ";"

        return codigo3d

    def cadena_drop_database(self, dropDataBase):
        codigo3d = "DROP DATABASE "

        if dropDataBase.existe == 1:
            codigo3d += "IF EXISTS "
        codigo3d += str(dropDataBase.id) + ";"

        return codigo3d


    def cadena_expresion(self, expresiones):
        cadena = ""
        if isinstance(expresiones, ExpresionAritmetica):
            return self.cadena_aritmetica(expresiones)

        elif isinstance(expresiones, ExpresionRelacional):
            return self.cadena_relacional(expresiones)

        elif isinstance(expresiones, ExpresionLogica):
            return self.cadena_logica(expresiones)
        elif isinstance(expresiones, UnitariaNegAritmetica):
            return "- " + str(self.cadena_expresion(expresiones))
        elif isinstance(expresiones, UnitariaLogicaNOT):
            return "NOT " + str(self.cadena_expresion(expresiones))
        elif isinstance(expresiones, UnitariaNotBB):
            return "~ " + str(self.cadena_expresion(expresiones))
        elif isinstance(expresiones, ExpresionValor):
            if isinstance(expresiones.val, string_types):
                return '"' + str(expresiones.val) + '"'
            return str(expresiones.val)
        elif isinstance(expresiones, Variable):
            # Buscar variable en la tabla de simbolos
            r = None
            for item in self.t_global.tablaSimbolos:
                v: tipoSimbolo = self.t_global.obtenerSimbolo(item)

                if v.nombre == expresiones.id and v.ambito == self.ambitoFuncion:
                    # print(str(v.temporal))
                    r = str(v.temporal)

            if r is not None:
                return '""" + str(' + str(r) + ') + """'
            return expresiones.id
        elif isinstance(expresiones, UnitariaAritmetica):
            return self.getVar(expresiones.operador) + " " + str(self.cadena_expresion(expresiones.exp1))
        elif isinstance(expresiones, ExpresionFuncion):
            return self.cadena_expresion_funcion(expresiones)
        elif isinstance(expresiones, ExpresionTiempo):
            return expresiones.nombre
        elif isinstance(expresiones, ExpresionConstante):
            return expresiones.nombre

        #vienen los tipos de subquerys
        elif isinstance(expresiones,AccesoSubConsultas):
            return  self.ProcesoSub(expresiones)


        elif isinstance(expresiones, Absoluto):
            try:
                cadena = "(" + self.cadena_expresion(expresiones.variable) + ")"
                return cadena

            except:
                print('Error no se puede aplicar abs() por el tipo de dato')
                # consola.insert('end','>>Error: No se puede aplicar abs() al tipo de dato\n>>')
                # newErr=ErrorRep('Semantico','No se puede aplicar abs() al tipo de dato ',indice)
                # LisErr.agregar(newErr)
                return None

        elif isinstance(expresiones, CAMPO_TABLA_ID_PUNTO_ID):
            return expresiones.tablaid + "." + expresiones.campoid


        else:
            print(expresiones)
            print('Error:Expresion no reconocida')
        return None


#llamada alas subconsultas
    def ProcesoSub(self,ii):
        if (isinstance(ii, AccesoSubConsultas)):
            if (ii.Lista_Alias != False):
                sub = ii.Query
                if isinstance(sub, SubSelect):
                    return self.GrafoSubSelect(sub.Lista_Campos, sub.Nombres_Tablas)

                elif isinstance(sub, SubSelect2):
                    return self.GrafoSubSelect2(sub.Lista_Campos, sub.Nombres_Tablas, sub.Cuerpo)

                elif isinstance(sub, SubSelect3):
                    return self.GrafoSubSelect3(sub.Lista_Campos, sub.Nombres_Tablas)

                elif isinstance(sub, SubSelect4):
                    return self.GrafoSubSelect4(sub.Lista_Campos, sub.Nombres_Tablas, sub.Cuerpo)
                else:
                    return ""

            else:
                sub = ii.Query
                if isinstance(sub, SubSelect):
                    return self.GrafoSubSelect(sub.Lista_Campos, sub.Nombres_Tablas)

                elif isinstance(sub, SubSelect2):
                    return self.GrafoSubSelect2(sub.Lista_Campos, sub.Nombres_Tablas, sub.Cuerpo)

                elif isinstance(sub, SubSelect3):
                    return self.GrafoSubSelect3(sub.Lista_Campos, sub.Nombres_Tablas)

                elif isinstance(sub, SubSelect4):
                    return self.GrafoSubSelect4(sub.Lista_Campos, sub.Nombres_Tablas, sub.Cuerpo)
                else:
                    print("F")
                    return ""
        else:
            print("No Genero")
            return ""

    def cadena_logica(self, expresion: ExpresionLogica):
        cadena = ""
        exp1 = self.cadena_expresion(expresion.exp1)
        exp2 = self.cadena_expresion(expresion.exp2)

        if exp1 is not None and exp2 is not None:
            cadena = str(exp1) + " " + self.getVar(expresion.operador) + " " + str(exp2)
            return cadena

        if exp1 is not None and exp2 is None:
            cadena = self.getVar(expresion.operador) + " " + str(exp1)
            return cadena

        return None


    def cadena_relacional(self, expresion: ExpresionRelacional):
        cadena = ""

        exp1 = self.cadena_expresion(expresion.exp1)
        exp2 = self.cadena_expresion(expresion.exp2)

        cadena += str(exp1) + " " + self.getVar(expresion.operador) + " " + str(exp2)

        return cadena



    def cadena_aritmetica(self, expresion:ExpresionAritmetica):
        cadena = ""

        exp1 = self.cadena_expresion(expresion.exp1)
        exp2 = self.cadena_expresion(expresion.exp2)

        cadena += str(exp1) + " " + self.getVar(expresion.operador) + " " + str(exp2)

        return cadena



    def cadena_expresion_funcion(self, expresion: ExpresionFuncion, tipo_exp=""):
        cadena = ""

        cadena = self.getVar(expresion.id_funcion) + "("

        parametro1 = ""
        parametro2 = ""
        parametro3 = ""
        parametro4 = ""

        if expresion.exp1 is not None:
            parametro1 = ""
        if expresion.exp2 is not None:
            parametro2 = ""
        if expresion.exp3 is not None:
            parametro3 = ""
        if expresion.exp4 is not None:
            parametro4 = ""

        if expresion.id_funcion == FUNCION_NATIVA.EXTRACT:
            cadena += parametro1 + " FROM TIMESTAMP " + parametro2
        elif expresion.id_funcion == FUNCION_NATIVA.DATE_PART:
            cadena += parametro1 + ", INTERVAL " + parametro2
        else:
            cadena += parametro1

            if parametro2 != "":
                cadena += ", " + parametro2
            if parametro3 != "":
                cadena += ", " + parametro3
            if parametro4 != "":
                cadena += ", " + parametro4

        cadena += ")"
        return cadena


    def getVar(self, padreID):
        if padreID == OPERACION_ARITMETICA.MAS:
            return '+'
        elif padreID == OPERACION_ARITMETICA.MENOS:
            return '-'
        elif padreID == OPERACION_ARITMETICA.MULTI:
            return '*'
        elif padreID == OPERACION_ARITMETICA.DIVIDIDO:
            return '/'
        elif padreID == OPERACION_ARITMETICA.RESIDUO:
            return '%'
        elif padreID == OPERACION_LOGICA.AND:
            return 'AND'
        elif padreID == OPERACION_LOGICA.OR:
            return 'OR'
        elif padreID == OPERACION_RELACIONAL.IGUALQUE:
            return '='
        elif padreID == OPERACION_RELACIONAL.DISTINTO:
            return '!='
        elif padreID == OPERACION_RELACIONAL.MAYORIGUAL:
            return '>='
        elif padreID == OPERACION_RELACIONAL.MENORIGUAL:
            return '!='
        elif padreID == OPERACION_RELACIONAL.MAYORQUE:
            return '>'
        elif padreID == OPERACION_RELACIONAL.MENORQUE:
            return '<'
        # NUEVAS COSAS
        elif padreID == OPERACION_LOGICA.IS_NOT_NULL:
            return 'IS_NOT_NULL'
        elif padreID == OPERACION_LOGICA.IS_NOT_TRUE:
            return 'IS_NOT_TRUE'
        elif padreID == OPERACION_LOGICA.IS_NOT_FALSE:
            return 'IS_NOT_FALSE'
        elif padreID == OPERACION_LOGICA.IS_NOT_UNKNOWN:
            return 'IS_NOT_UNKNOWN'
        elif padreID == OPERACION_LOGICA.IS_NULL:
            return 'IS_NULL'
        elif padreID == OPERACION_LOGICA.IS_TRUE:
            return 'IS_TRUE'
        elif padreID == OPERACION_LOGICA.IS_FALSE:
            return 'IS_FALSE'
        elif padreID == OPERACION_LOGICA.IS_UNKNOWN:
            return 'IS_NOT_UNKNOWN'
        elif padreID == OPERACION_LOGICA.IS_NOT_DISTINCT:
            return 'IS_NOT_DISTINCT'
        elif padreID == OPERACION_LOGICA.IS_DISTINCT:
            return 'IS_DISTINCT'
        elif padreID == OPERACION_LOGICA.EXISTS:
            return 'EXISTS'
        elif padreID == OPERACION_LOGICA.NOT_EXISTS:
            return 'NOTEXISTS'
        elif padreID == OPERACION_LOGICA.IN:
            return 'IN'
        elif padreID == OPERACION_LOGICA.NOT_IN:
            return 'NOTIN'
        elif padreID == FUNCION_NATIVA.ABS:
            return 'ABS'
        elif padreID == FUNCION_NATIVA.CBRT:
            return 'CBRT'
        elif padreID == FUNCION_NATIVA.CEIL:
            return 'CEIL'
        elif padreID == FUNCION_NATIVA.CEILING:
            return 'CEILING'
        elif padreID == FUNCION_NATIVA.DEGREES:
            return 'DEGREES'
        elif padreID == FUNCION_NATIVA.EXP:
            return 'EXP'
        elif padreID == FUNCION_NATIVA.FACTORIAL:
            return 'FACTORIAL'
        elif padreID == FUNCION_NATIVA.FLOOR:
            return 'FLOOR'
        elif padreID == FUNCION_NATIVA.LN:
            return 'LN'
        elif padreID == FUNCION_NATIVA.LOG:
            return 'LOG'
        elif padreID == FUNCION_NATIVA.MOD:
            return 'MOD'
        elif padreID == FUNCION_NATIVA.RADIANS:
            return 'RADIANS'
        elif padreID == FUNCION_NATIVA.ROUND:
            return 'ROUND'
        elif padreID == FUNCION_NATIVA.SIGN:
            return 'SIGN'
        elif padreID == FUNCION_NATIVA.SQRT:
            return 'SQRT'
        elif padreID == FUNCION_NATIVA.TRUNC:
            return 'TRUNC'
        elif padreID == FUNCION_NATIVA.ACOS:
            return 'ACOS'
        elif padreID == FUNCION_NATIVA.ACOSD:
            return 'ACOSD'
        elif padreID == FUNCION_NATIVA.ASIN:
            return 'ASIN'
        elif padreID == FUNCION_NATIVA.ASIND:
            return 'ASIND'
        elif padreID == FUNCION_NATIVA.ATAN:
            return 'ATAN'
        elif padreID == FUNCION_NATIVA.ATAND:
            return 'ATAND'
        elif padreID == FUNCION_NATIVA.COS:
            return 'COS'
        elif padreID == FUNCION_NATIVA.COSD:
            return 'COSD'
        elif padreID == FUNCION_NATIVA.COT:
            return 'COT'
        elif padreID == FUNCION_NATIVA.COTD:
            return 'COTD'
        elif padreID == FUNCION_NATIVA.COSD:
            return 'COSD'
        elif padreID == FUNCION_NATIVA.SIN:
            return 'SIN'
        elif padreID == FUNCION_NATIVA.SIND:
            return 'SIND'
        elif padreID == FUNCION_NATIVA.TAN:
            return 'TAN'
        elif padreID == FUNCION_NATIVA.TAND:
            return 'TAND'
        elif padreID == FUNCION_NATIVA.SINH:
            return 'SINH'
        elif padreID == FUNCION_NATIVA.COSH:
            return 'COSH'
        elif padreID == FUNCION_NATIVA.TANH:
            return 'TANH'
        elif padreID == FUNCION_NATIVA.ASINH:
            return 'ASINH'
        elif padreID == FUNCION_NATIVA.ACOSH:
            return 'ACOSH'
        elif padreID == FUNCION_NATIVA.ATANH:
            return 'ATANH'
        elif padreID == FUNCION_NATIVA.LENGTH:
            return 'LENGTH'
        elif padreID == FUNCION_NATIVA.TRIM:
            return 'TRIM'
        elif padreID == FUNCION_NATIVA.MD5:
            return 'MD5'
        elif padreID == FUNCION_NATIVA.SHA256:
            return 'SHA256'
        elif padreID == FUNCION_NATIVA.DIV:
            return 'DIV'
        elif padreID == FUNCION_NATIVA.GCD:
            return 'GCD'
        elif padreID == FUNCION_NATIVA.MOD:
            return 'MOD'
        elif padreID == FUNCION_NATIVA.POWER:
            return 'POWER'
        elif padreID == FUNCION_NATIVA.ATAN2:
            return 'ATAN2'
        elif padreID == FUNCION_NATIVA.ATAN2D:
            return 'ATAN2D'
        elif padreID == FUNCION_NATIVA.GET_BYTE:
            return 'GET_BYTE'
        elif padreID == FUNCION_NATIVA.ENCODE:
            return 'ENCODE'
        elif padreID == FUNCION_NATIVA.DECODE:
            return 'DECODE'
        elif padreID == CONDICIONAL_SUBQUERY.ANY:
            return 'ANY'
        elif padreID == CONDICIONAL_SUBQUERY.ALL:
            return 'ALL'
        elif padreID == CONDICIONAL_SUBQUERY.SOME:
            return 'SOME'
        elif padreID == FUNCION_NATIVA.SUBSTRING:
            return 'SUBSTRING'
        elif padreID == FUNCION_NATIVA.SUBSTR:
            return 'SUBSTR'
        elif padreID == FUNCION_NATIVA.SET_BYTE:
            return 'SET_BYTE'
        elif padreID == FUNCION_NATIVA.WIDTH_BUCKET:
            return 'WIDTH_BUCKET'
        elif padreID == OPERACION_ARITMETICA.CUBICA:
            return '||'
        elif padreID == OPERACION_ARITMETICA.CUADRATICA:
            return '|'
        elif padreID == OPERACION_ARITMETICA.POTENCIA:
            return '^'
        elif padreID == FUNCION_NATIVA.EXTRACT:
            return 'EXTRACT'
        elif padreID == FUNCION_NATIVA.DATE_PART:
            return 'DATE_PART'
        elif padreID == FUNCION_NATIVA.NOW:
            return 'NOW'
        elif padreID == FUNCION_NATIVA.PI:
            return 'PI'
        elif padreID == FUNCION_NATIVA.RANDOM:
            return 'RANDOM'
        else:
            return 'op'





#============================= ALTER TABLE ============================================
    def cadena_alter_column_set_not_null(self, alterColumn):
        cadena = "ALTER TABLE " + alterColumn.id_tabla + " ALTER COLUMN " + alterColumn.id_column.val
        cadena += " SET NOT NULL;"

        return cadena

    def cadena_alter_add_column(self, alterTable):
        cadena = 'ALTER TABLE ' + alterTable.id_table + " ADD COLUMN "

        for index, columna in enumerate(alterTable.id_columnas):
            exp: ExpresionValor2 = columna
            if index == 0:
                cadena += exp.val + " " + exp.tipo
            else:
                cadena += ", " + exp.val + " " + exp.tipo

        cadena += ";"

        return cadena

    def cadena_alter_drop_column(self, alterTable):
        cadena = "ALTER TABLE " + alterTable.id_table + " DROP COLUMN "

        for index, id in enumerate(alterTable.columnas):
            if index == 0:
                cadena += id.val
            else:
                cadena += ", " + id.val

        return cadena

    def cadena_alter_rename(self, alterTable):
        cadena = 'ALTER TABLE ' + alterTable.id_table + ' RENAME COLUMN ' + alterTable.old_column.val
        cadena += ' TO ' + alterTable.new_column.val + ';'

        return cadena

    def cadena_alter_drop_constraint(self, alterTable):
        cadena = 'ALTER TABLE ' + alterTable.id_tabla + ' DROP CONSTRAINT ' + alterTable.id_constraint.val + ";"
        return cadena

    def cadena_alter_add_foreign(self, alterTable):
        cadena = 'ALTER TABLE ' + alterTable.id_table

        if alterTable.idforeign is not None:
            cadena += ' ADD CONSTRAINT ' + alterTable.idforeign

        cadena += ' FOREIGN KEY (' + alterTable.id_column.val + ')'

        cadena += ' REFERENCES ' + alterTable.id_column_references.val

        if alterTable.id_table_references is not None:
            cadena += ' (' + alterTable.id_table_references.val + ')'

        cadena += ';'

        return cadena

    def cadena_alter_add_constraint(self, alterTable):
        cadena = "ALTER TABLE " + alterTable.id_table + " ADD CONSTRAINT " + alterTable.id_constraint.val
        cadena += ' UNIQUE (' + alterTable.id_column.val + ');'


    def cadena_alter_column(self, alterTable):
        cadena = "ALTER TABLE " + alterTable.idtabla

        for index, columna in enumerate(alterTable.columnas):
            col: ExpresionValor2 = columna

            if index == 0:
                cadena += " ALTER COLUMN " + col.val + " TYPE " + col.tipo.valor
                if col.tipo.valor == "varchar":
                    cadena += "(" + self.cadena_expresion(col.tipo.expresion) + ")"

            else:
                cadena += ", ALTER COLUMN " + col.val + " TYPE " + col.tipo.valor
                if col.tipo.valor == "varchar":
                    cadena += "(" + self.cadena_expresion(col.tipo.expresion) + ")"


        cadena += ";"

        return cadena

    def Grafo_AlterIndexColumna(self, objeto):
        ob: AlterIndiceCol = objeto
        Cadenita = " ALTER INDEX " + ob.id_indice + " ALTER COLUMN " + str(
            ob.no_col) + " SET STATISTICS " + ob.tipo_set + " ; "

        return Cadenita

    def Grafo_AlterIndexName(self, objeto):
        ob: AlterIndiceName = objeto
        Cadenita = " ALTER INDEX " + ob.id_indice + " RENAME TO " + ob.new_Indice + " ;  "
        return Cadenita

    def Grafo_DropIndex(self, objeto):
        ob: DropIndice = objeto
        Cadenita = " DROP INDEX " + ob.id_indice + " ;  "
        return Cadenita

    def grafoSelectExpresion(self, objeto):
        cadena = "SELECT "


        for campo in objeto.listaCampos:
            if isinstance(campo, Campo_AccedidoSinLista):
                cadena += self.cadena_expresion(campo.Columna)

            elif isinstance(campo, Campo_Accedido):
                cadena += self.cadena_expresion(campo.Columna)

            if campo != objeto.listaCampos[-1]:
                cadena += ", "

        cadena += ";"

        return cadena
    def Grafo_Count(self, objeto):
        ob: ProcesoCount = objeto
        Cadenita = "COUNT ("+ob.Columna+")"

        return Cadenita
