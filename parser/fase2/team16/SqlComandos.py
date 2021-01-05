from Instruccion import *
from expresiones import *
import interprete as Inter
from sentencias import *

class SqlComandos:

    def __init__(self, sentencia):
        self.sentencia = sentencia
        self.CadenaSQL = None




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
            #self.grafoSelectExpresion(i.listaCampos)

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

        else:
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


