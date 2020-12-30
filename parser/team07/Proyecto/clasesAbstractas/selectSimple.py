import jsonMode
from Errores import errorReportar
from prettytable import PrettyTable
from .instruccionAbstracta import InstruccionAbstracta

class selectSimple(InstruccionAbstracta):

    '''Clase que representa un select simple el cual lleva como atributos'''

    def __init__(self, selectColumnas, selectTablas, selectCondiciones, Distinct):
        self.selectColumnas = selectColumnas
        self.selectTablas = selectTablas
        self.selectCondiciones = selectCondiciones
        self.Distinct = Distinct


    def ejecutar(self, tabalSimbolos, listaErrores):  

        #Se verifica si hay una base de datos en uso
        if tabalSimbolos.useDataBase == None:
            nodoError = errorReportar.ErrorReportar(self.fila, self.columna,"Ejecucion","Ninguna base de datos en uso")
            listaErrores.append(nodoError)
        else:

            #Select sin tablas en el FROM y se asume que viene una funcion matematica
            if self.selectTablas is None: 
                for elemento in self.selectColumnas.hijos:
                    Res = elemento.hijos[0].ejecutar(tabalSimbolos, listaErrores)
                    if Res != None:
                        print(Res.valorRetorno) 

            #Select con tablas en el FROM  
            else:
                ListaTablasFrom = {"Nombre": [], "ID": []}
                ListaSubquerysFrom = {"Subquery": [], "ID": []}

                #Se obtienen todos los nombres de las tablas del from y los subquerys
                for Tabla in self.selectTablas.hijos:
                    #Es una declaracion simple de una tabla
                    if str.lower(Tabla.hijos[0].nombreNodo) == "dec_id_from": 
                        if len(Tabla.hijos[0].hijos) == 1:
                            ListaTablasFrom["Nombre"].append(Tabla.hijos[0].hijos[0].valor)
                            ListaTablasFrom["ID"].append(Tabla.hijos[0].hijos[0].valor)
                        elif len(Tabla.hijos[0].hijos) == 2:
                            ListaTablasFrom["Tabla"].append(Tabla.hijos[0].hijos[0].valor)
                            ListaTablasFrom["ID"].append(Tabla.hijos[0].hijos[1].valor)
                    
                    #Es un subquery
                    else: 
                        if len(Tabla.hijos) == 1:
                            ListaSubquerysFrom["Subquery"].append(Tabla.hijos[0])
                            ListaSubquerysFrom["ID"].append(None)
                        if len(Tabla.hijos) == 2:
                            ListaSubquerysFrom["Subquery"].append(Tabla.hijos[0])
                            ListaSubquerysFrom["ID"].append(Tabla.hijos[0].valor)

                #Se extraen de la base de datos las tablas del from

                TablasDatosCompletos = {"Nombre": [], "Campos": [], "TipoCampos": [], "Datos": []}

                for tabla in ListaTablasFrom["Nombre"]:
                    TablasDatosCompletos["Nombre"].append(tabla)
                    
                    tiposcolumnas = []
                    columnas = []
                    for col in tabalSimbolos.useDataBase.obtenerTabla(tabla).columnas:
                        tiposcolumnas.append(col.tipoDato)
                        columnas.append(col.nombre)

                    TablasDatosCompletos["Campos"].append(columnas)
                    TablasDatosCompletos["TipoCampos"].append(tiposcolumnas)

                    TablasDatosCompletos["Datos"].append(jsonMode.extractTable(tabalSimbolos.useDataBase.nombre, tabla))

                #Se verifica si se mando a llamar un Selec *
                if self.selectColumnas.valor == "*": 
                    Tablas = []
                    for i in range(0, len(TablasDatosCompletos["Nombre"])):
                        TablaPrint = PrettyTable()
                        TablaPrint.field_names = TablasDatosCompletos["Campos"][i]
                        TablaPrint.add_rows(TablasDatosCompletos["Datos"][i])
                        Tablas.append(TablaPrint)
                    for T in Tablas:
                        print(T)

                else:
                    #No vienen ninguna condicion where
                    if self.selectCondiciones == None:
                        TablaPrint = PrettyTable()
                        rownum = 1

                        for elemento in self.selectColumnas.hijos:
                            #La columna es solo un campo simple
                            if elemento.nombreNodo == "TABLA_CAMPO_ALIAS":
                                nombrecampo = ""
                                datoscolumnatmp = []
                                if len(elemento.hijos) == 1:
                                    nombrecampo = elemento.hijos[0].valor
                                else:
                                    nombrecampo = elemento.hijos[1].valor

                                for i in range(0, len(TablasDatosCompletos["Nombre"])):
                                    for j in range(0, len(TablasDatosCompletos["Campos"][i])):
                                        if TablasDatosCompletos["Campos"][i][j] == nombrecampo:
                                            for k in range(0, len(TablasDatosCompletos["Datos"][i])):
                                                datoscolumnatmp.append(TablasDatosCompletos["Datos"][i][k][j])
                                                if k > rownum:
                                                    rownum = k

                                TablaPrint.add_column(nombrecampo, datoscolumnatmp)

                            #la columna es una funcion
                            else:
                                resfuncion = elemento.hijos[0].ejecutar(tabalSimbolos, listaErrores)

                                if resfuncion != None:
                                    res = []
                                    for i in range(0,rownum+1):
                                        res.append(resfuncion.valorRetorno)

                                    TablaPrint.add_column(elemento.hijos[0].hijos[0].valor,res)

                        print(TablaPrint)
                    
                    #Se aplican las condiciones en el where
                    else:
                        for clausula in self.selectCondiciones.hijos:
                            if str.lower(clausula.hijos[0].valor) == "where":

                                
                                print("vino un where")
                            elif str.lower(clausula.hijos[0].valor) == "group":
                                print("vino un group")
                            elif str.lower(clausula.hijos[0].valor) == "having":
                                print("vino un having")
                            elif str.lower(clausula.hijos[0].valor) == "order":
                                print("vino un order")
                            elif str.lower(clausula.hijos[0].valor) == "limit":
                                print("vino un limit")
                            else:
                                print("vino desconocido")
