from Instrucciones.Sql_create.Tipo_Constraint import Tipo_Constraint, Tipo_Dato_Constraint
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Expresiones.Primitivo import Primitivo
from Instrucciones.TablaSimbolos.Simbolo import Simbolo
from Instrucciones.TablaSimbolos.Tabla import Tabla
from Instrucciones.Excepcion import Excepcion
import numpy as np
from storageManager.jsonMode import *

# valor -----> nombre de la tabla
# lcol ------> lista con el nombre de las columnas
# lexpre ----> lista de expresiones a insertar

class insertTable(Instruccion):
    def __init__(self, valor, tipo, lcol, lexpre, strGram ,linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor
        self.lcol = lcol
        self.lexpre = lexpre

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if arbol.bdUsar != None:
            objetoTabla = arbol.devolviendoTablaDeBase(self.valor)
            if objetoTabla != 0:
                #print('Ok!')
                lista = []
                # Si el insert tiene la lista de columnas
                if(self.lcol != None):
                    tablaLocal = Tabla(tabla)
                    # Se valia que la lista de columnas este bien.
                    listaNombreColumnas = []
                    listaColumnas = []
                    indices = []
                    for c in self.lcol:
                        for col in objetoTabla.lista_de_campos:
                            if col.nombre == c:
                                listaNombreColumnas.append(col.nombre)
                                listaColumnas.append(col)
                                indices.append(col.orden)

                    listaNoEncontrados = list(set(self.lcol) - set(listaNombreColumnas))
                    if len(listaNoEncontrados)>0:
                        for c in listaNoEncontrados:
                            error = Excepcion('42703',"Semántico","No existe la columna «"+c+"» en la relación «"+self.valor+"»",self.linea,self.columna)
                            arbol.excepciones.append(error)
                            arbol.consola.append(error.toString())
                        return

                    # Se valida que la lista de expresiones sea igual a la lista de columnas
                    if len(self.lexpre) != len(self.lcol):
                        error = Excepcion('23505',"Semántico","INSERT tiene más o menos expresiones que columnas de destino",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error 

                    # Recorrido para insertar
                    for c in range(0,len(listaColumnas)):
                        res = self.lexpre[c].ejecutar(tabla, arbol)
                        if isinstance(res, Excepcion):
                            return res
                        if listaColumnas[c].constraint != None:
                            for constraint in listaColumnas[c].constraint:
                                if constraint.tipo == Tipo_Dato_Constraint.PRIMARY_KEY:
                                    valida = self.validacionesPrimary(listaColumnas[c].nombre,res,arbol)
                                    if not valida:
                                        error = Excepcion('23505',"Semántico","Llave duplicada viola restricción de unicidad «"+constraint.id+"»",self.linea,self.columna)
                                        arbol.excepciones.append(error)
                                        arbol.consola.append(error.toString())
                                        return error
                                if constraint.tipo == Tipo_Dato_Constraint.UNIQUE:
                                    valida = self.validacionesPrimary(listaColumnas[c].nombre,res,arbol)
                                    if not valida:
                                        error = Excepcion('23505',"Semántico","Llave duplicada viola restricción de unicidad «"+constraint.id+"»",self.linea,self.columna)
                                        arbol.excepciones.append(error)
                                        arbol.consola.append(error.toString())
                                        return error
                                elif constraint.tipo == Tipo_Dato_Constraint.NOT_NULL:
                                    pass
                                elif constraint.tipo == Tipo_Dato_Constraint.FOREIGN_KEY:
                                    valida = self.validacionesForeign(constraint.referencia,constraint.expresion.nombre,res,arbol)
                                    if not valida:
                                        error = Excepcion('23505',"Semántico","Inserción o actualización en la tabla «"+self.valor+"» viola la llave foránea "+constraint.id,self.linea,self.columna)
                                        arbol.excepciones.append(error)
                                        arbol.consola.append(error.toString())
                                        return error
                            
                        # Comprobación de que el tipo sea el mismo
                        comprobar = self.comprobarTipo(listaColumnas[c].tipo,self.lexpre[c].tipo, res, arbol)
                        if isinstance(comprobar, Excepcion):
                            return comprobar
                        if comprobar:
                            if listaColumnas[c].constraint != None:
                                for constraint in listaColumnas[c].constraint:
                                    if constraint.tipo == Tipo_Dato_Constraint.CHECK:
                                        arbol.comprobacionCreate = True
                                        resultado = self.validacionesCheck(listaColumnas[c].nombre,listaColumnas[c].tipo, res,constraint.expresion,tablaLocal,arbol)
                                        if isinstance(resultado, Excepcion):
                                            return resultado
                                        if not resultado:
                                            error = Excepcion('23505',"Semántico","El nuevo registro para la relación «"+self.valor+"» viola la restricción «check» «"+constraint.id+"»",self.linea,self.columna)
                                            arbol.excepciones.append(error)
                                            arbol.consola.append(error.toString())
                                            return error
                                        arbol.comprobacionCreate = False
                            lista.append(res) 
                        else:
                            error = Excepcion('42804',"Semántico","La columna «"+listaColumnas[c].nombre+"» es de tipo "+listaColumnas[c].tipo.toString()+" pero la expresión es de tipo "+self.lexpre[c].tipo.toString(),self.linea,self.columna)
                            arbol.excepciones.append(error)
                            arbol.consola.append(error.toString())
                    
                    columnasNulas = list(set(objetoTabla.lista_de_campos) - set(listaColumnas))

                    for c in range(0,len(columnasNulas)):
                        if columnasNulas[c].constraint != None:
                            for constraint in columnasNulas[c].constraint:
                                if constraint.tipo == Tipo_Dato_Constraint.PRIMARY_KEY:
                                    error = Excepcion('23505',"Semántico","El valor nulo en la columna «"+columnasNulas[c].nombre+"» de la relación «"+self.valor+"» viola la restricción de no nulo",self.linea,self.columna)
                                    arbol.excepciones.append(error)
                                    arbol.consola.append(error.toString())
                                    return error
                                if constraint.tipo == Tipo_Dato_Constraint.UNIQUE:
                                    error = Excepcion('23505',"Semántico","El valor nulo en la columna «"+columnasNulas[c].nombre+"» de la relación «"+self.valor+"» viola la restricción de no nulo",self.linea,self.columna)
                                    arbol.excepciones.append(error)
                                    arbol.consola.append(error.toString())
                                    return error
                                elif constraint.tipo == Tipo_Dato_Constraint.NOT_NULL:
                                    error = Excepcion('23505',"Semántico","El valor nulo en la columna «"+columnasNulas[c].nombre+"» de la relación «"+self.valor+"» viola la restricción de no nulo",self.linea,self.columna)
                                    arbol.excepciones.append(error)
                                    arbol.consola.append(error.toString())
                                    return error
                                elif constraint.tipo == Tipo_Dato_Constraint.FOREIGN_KEY:
                                    error = Excepcion('23505',"Semántico","El valor nulo en la columna «"+columnasNulas[c].nombre+"» de la relación «"+self.valor+"» viola la restricción de no nulo",self.linea,self.columna)
                                    arbol.excepciones.append(error)
                                    arbol.consola.append(error.toString())
                                    return error
                        lista.append("Null") 
                        indices.append(columnasNulas[c].orden)
                    
                    listaOrden = []
                    for i in range(0,len(indices)):
                        objeto = [indices[i],lista[i]]
                        listaOrden.append(objeto)
                    
                    ordenados = sorted(listaOrden)
                    listaFinal = [item[1] for item in ordenados]
                    
                    if len(lista) != len(objetoTabla.lista_de_campos):
                        return

                    resultado = insert(arbol.getBaseDatos(),self.valor,listaFinal)
                    if resultado == 1:
                        error = Excepcion('XX000',"Semántico","Error interno",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    elif resultado == 2:
                        error = Excepcion('42P00',"Semántico","La base de datos "+str(arbol.getBaseDatos())+" no existe",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    elif resultado == 3:
                        error = Excepcion('42P01',"Semántico","No existe la relación "+self.valor,self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    elif resultado == 4:
                        error = Excepcion('2BP01',"Semántico","Llave duplicada viola restricción de unicidad «"+self.valor+"_pkey»",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    elif resultado == 5:
                        error = Excepcion('XX002',"Semántico","Columna fuera de limites."+self.valor,self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    arbol.consola.append(f"el registro se inserto correctamente.")
                    print("EL REGISTRO SE INSERTO CORRECTAMENTE [InsertTable ejecutado correctamente]")
                    
                # El insert no tiene una lista de columnas
                else:
                    if len(self.lexpre) != len(objetoTabla.lista_de_campos):
                        error = Excepcion('23505',"Semántico","INSERT tiene más o menos expresiones que columnas de destino",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    tablaLocal = Tabla(tabla)
                    for c in range(0,len(objetoTabla.lista_de_campos)):
                        res = self.lexpre[c].ejecutar(tabla, arbol)
                        if isinstance(res, Excepcion):
                            return res
                        if objetoTabla.lista_de_campos[c].constraint != None:
                            for constraint in objetoTabla.lista_de_campos[c].constraint:
                                if constraint.tipo == Tipo_Dato_Constraint.PRIMARY_KEY:
                                    valida = self.validacionesPrimary(objetoTabla.lista_de_campos[c].nombre,res,arbol)
                                    if not valida:
                                        error = Excepcion('23505',"Semántico","Llave duplicada viola restricción de unicidad «"+constraint.id+"»",self.linea,self.columna)
                                        arbol.excepciones.append(error)
                                        arbol.consola.append(error.toString())
                                        return error
                                if constraint.tipo == Tipo_Dato_Constraint.UNIQUE:
                                    valida = self.validacionesPrimary(objetoTabla.lista_de_campos[c].nombre,res,arbol)
                                    if not valida:
                                        error = Excepcion('23505',"Semántico","Llave duplicada viola restricción de unicidad «"+constraint.id+"»",self.linea,self.columna)
                                        arbol.excepciones.append(error)
                                        arbol.consola.append(error.toString())
                                        return error
                                elif constraint.tipo == Tipo_Dato_Constraint.NOT_NULL:
                                    pass
                                elif constraint.tipo == Tipo_Dato_Constraint.FOREIGN_KEY:
                                    valida = self.validacionesForeign(constraint.referencia,constraint.expresion.nombre,res,arbol)
                                    if not valida:
                                        error = Excepcion('23505',"Semántico","Inserción o actualización en la tabla «"+self.valor+"» viola la llave foránea "+constraint.id,self.linea,self.columna)
                                        arbol.excepciones.append(error)
                                        arbol.consola.append(error.toString())
                                        return error
                        # Comprobación de que el tipo sea el mismo
                        comprobar = self.comprobarTipo(objetoTabla.lista_de_campos[c].tipo,self.lexpre[c].tipo, res, arbol)
                        if isinstance(comprobar, Excepcion):
                            return comprobar
                        if comprobar:
                            if objetoTabla.lista_de_campos[c].constraint != None:
                                for constraint in objetoTabla.lista_de_campos[c].constraint:
                                    if constraint.tipo == Tipo_Dato_Constraint.CHECK:
                                        arbol.comprobacionCreate = True
                                        resultado = self.validacionesCheck(objetoTabla.lista_de_campos[c].nombre,objetoTabla.lista_de_campos[c].tipo, res,constraint.expresion,tablaLocal,arbol)
                                        if isinstance(resultado, Excepcion):
                                            return resultado
                                        if not resultado:
                                            error = Excepcion('23505',"Semántico","El nuevo registro para la relación «"+self.valor+"» viola la restricción «check» «"+constraint.id+"»",self.linea,self.columna)
                                            arbol.excepciones.append(error)
                                            arbol.consola.append(error.toString())
                                            return error
                                        arbol.comprobacionCreate = False
                            lista.append(res) 
                        else:
                            error = Excepcion('42804',"Semántico","La columna «"+objetoTabla.lista_de_campos[c].nombre+"» es de tipo "+objetoTabla.lista_de_campos[c].tipo.toString()+" pero la expresión es de tipo "+self.lexpre[c].tipo.toString(),self.linea,self.columna)
                            arbol.excepciones.append(error)
                            arbol.consola.append(error.toString())
                            
                    if len(lista) != len(self.lexpre):
                        return

                    #print("esta es la insercion de lista, ya inserto estaticamente")
                    resultado = insert(arbol.getBaseDatos(),self.valor,lista)
                    if resultado == 1:
                        error = Excepcion('XX000',"Semántico","Error interno",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    elif resultado == 2:
                        error = Excepcion('42P00',"Semántico","La base de datos "+str(arbol.getBaseDatos())+" no existe",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    elif resultado == 3:
                        error = Excepcion('42P01',"Semántico","No existe la relación "+self.valor,self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    elif resultado == 4:
                        error = Excepcion('2BP01',"Semántico","Llave duplicada viola restricción de unicidad «"+self.valor+"_pkey»",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    elif resultado == 5:
                        error = Excepcion('XX002',"Semántico","Columna fuera de limites."+self.valor,self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    arbol.consola.append(f"el registro se inserto correctamente.")
                    print("EL REGISTRO SE INSERTO CORRECTAMENTE [InserTable ejecutado correctamente]")
            else:
                error = Excepcion('42P01',"Semántico","No existe la relación "+self.valor,self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        else:
            error = Excepcion("100","Semantico","No ha seleccionado ninguna Base de Datos.",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())

    def validacionesPrimary(self, nombreColumna, val, arbol):
        indice = arbol.devolverOrdenDeColumna(self.valor, nombreColumna)
        tablaSelect = extractTable(arbol.getBaseDatos(),self.valor)
        columna = [item[0] for item in tablaSelect]
        if len(columna) == 0:
            return True
        for c in columna:
            if c == val:
                return False
        return True
    
    def validacionesForeign(self, nombreTabla, nombreColumna, val, arbol):
        
        indice = arbol.devolverOrdenDeColumna(nombreTabla, nombreColumna)
        tablaSelect = extractTable(arbol.getBaseDatos(),nombreTabla)
        columna = [item[0] for item in tablaSelect]
        if len(columna) == 0:
            return False
        for c in columna:
            if c == val:
                return True
        return False
    
    def validacionesCheck(self, nombreColumna, tipo, val, expresion, tabla, arbol):
        #print("Validaciones CHECK-----------------",nombreColumna,tipo.toString(),val)
        variable = Simbolo(nombreColumna,tipo,val,self.linea,self.columna)
        tabla.setVariable(variable)
        resultado = expresion.ejecutar(tabla, arbol)
        #print("RESULTADO---------------------------------",resultado)
        if isinstance(resultado, Excepcion):
            return resultado
        return resultado

    def comprobarTipo(self, tipoColumna, tipoValor, val, arbol):
        if (tipoColumna.tipo == Tipo_Dato.MONEY) and (tipoValor.tipo == Tipo_Dato.CHAR):
            if ',' in val:
                val = val.replace(',','')
            try:
                val = float(val)
            except:
                error = Excepcion('22P02',"Semántico","La sintaxis de entrada no es válida para tipo money",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
            return True
        if tipoColumna.tipo == Tipo_Dato.TIPOENUM:
            existe = arbol.getEnum(tipoColumna.nombre)
            existeValor = existe.buscarTipo(val)
            if existeValor == None:
                error = Excepcion('2BP01',"Semántico","El valor "+val+" no existe dentro del TYPE ENUM "+tipoColumna.nombre,self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
            return True
        if (tipoColumna.tipo == Tipo_Dato.CHAR or tipoColumna.tipo == Tipo_Dato.VARCHAR or tipoColumna.tipo == Tipo_Dato.VARYING or tipoColumna.tipo == Tipo_Dato.CHARACTER or tipoColumna.tipo == Tipo_Dato.TEXT) and (tipoValor.tipo == Tipo_Dato.CHAR or tipoValor.tipo == Tipo_Dato.VARCHAR or tipoValor.tipo == Tipo_Dato.VARYING or tipoValor.tipo == Tipo_Dato.CHARACTER or tipoValor.tipo == Tipo_Dato.TEXT):
            if tipoColumna.dimension != None:
                if len(val) >= tipoColumna.dimension:
                    error = Excepcion('2BP01',"Semántico","el valor es demasiado largo para el tipo "+tipoColumna.toString()+"("+str(tipoColumna.dimension)+")",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            return True
        elif (tipoColumna.tipo == Tipo_Dato.SMALLINT or tipoColumna.tipo == Tipo_Dato.INTEGER or tipoColumna.tipo == Tipo_Dato.BIGINT or tipoColumna.tipo == Tipo_Dato.DECIMAL or tipoColumna.tipo == Tipo_Dato.NUMERIC or tipoColumna.tipo == Tipo_Dato.REAL or tipoColumna.tipo == Tipo_Dato.DOUBLE_PRECISION or tipoColumna.tipo == Tipo_Dato.MONEY) and (tipoValor.tipo == Tipo_Dato.SMALLINT or tipoValor.tipo == Tipo_Dato.INTEGER or tipoValor.tipo == Tipo_Dato.BIGINT or tipoValor.tipo == Tipo_Dato.DECIMAL or tipoValor.tipo == Tipo_Dato.NUMERIC or tipoValor.tipo == Tipo_Dato.REAL or tipoValor.tipo == Tipo_Dato.DOUBLE_PRECISION or tipoValor.tipo == Tipo_Dato.MONEY):
            if tipoColumna.tipo == Tipo_Dato.SMALLINT:
                if(val < -32768 or val > 32767):
                    error = Excepcion('2BP01',"Semántico",tipoColumna.toString()+" fuera de rango",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            elif tipoColumna.tipo == Tipo_Dato.INTEGER:
                if(val < -2147483648 or val > 2147483647):
                    error = Excepcion('2BP01',"Semántico",tipoColumna.toString()+" fuera de rango",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            elif tipoColumna.tipo == Tipo_Dato.BIGINT:
                if(val < -9223372036854775808 or val > 9223372036854775807):
                    error = Excepcion('2BP01',"Semántico",tipoColumna.toString()+" fuera de rango",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            return True
        elif (tipoColumna.tipo == Tipo_Dato.DATE or tipoColumna.tipo == Tipo_Dato.TIMESTAMP or tipoColumna.tipo == Tipo_Dato.TIME or tipoColumna.tipo == Tipo_Dato.INTERVAL or tipoColumna.tipo == Tipo_Dato.CHAR ) and (tipoValor.tipo == Tipo_Dato.DATE or tipoValor.tipo == Tipo_Dato.TIMESTAMP or tipoValor.tipo == Tipo_Dato.TIME or tipoValor.tipo == Tipo_Dato.INTERVAL or tipoValor.tipo == Tipo_Dato.CHAR):
            return True
        elif (tipoColumna.tipo == Tipo_Dato.BOOLEAN) and (tipoValor.tipo == Tipo_Dato.BOOLEAN):
            return True
        return False

    def getCodigo(self, tabla, arbol):
        #valor, tipo, lcol, lexpre, strGram ,linea, columna
        valor = f"{self.valor}"
        tipo = f"{self.tipo}"
        columnas = f""
        expresiones = f""
        gramatica = f"{self.strGram}"
        linea = f"{self.linea}"
        columna = f"{self.columna}"

        tabla = f"{self.valor}"
        #tipo = f"{self.tipo}"
        campos = f""   
        if (self.lcol is not None):
            for item in self.lcol:
                columnas += f"{item}{', ' if self.lcol.index(item) < len(self.lcol) - 1 else ''}"
            
            for item2 in self.lexpre:
                parametro = item2.toString()
                try:
                    if(str.isdigit(parametro) == False):
                        parametro = f"'{parametro}'"

                    campos += f"{parametro}{', ' if self.lexpre.index(item2) < len(self.lexpre) - 1 else ''}"
                except:
                    print("no se pudo evaluar si el parametro era dígito")
            
            table = f"insert into {tabla} ({columnas}) values ({campos});\t"
        else:  
            # for c in range(0,len(listaColumnas)):
            #     campos += f"\t{self.lexpre[c]}{', ' if self.lexpre.index(c) < len(self.lexpre) - 1 else ''}\n"  

            for item in self.lexpre:
                parametro = item.toString()
                try:
                    # if(str.isdigit(parametro) == False):
                    #     parametro = f"{parametro}"
                    
                    campos += f"{parametro}{', ' if self.lexpre.index(item) < len(self.lexpre) - 1 else ''}"
                except:
                    print("no se pudo evaluar si el parametro era dígito")

        
            table = f"insert into {tabla} values( {campos});"
        
        
        expresiones = campos 

        #----------------------------------------------
        num_params = 1
        
        temp_param1 = arbol.getTemporal()
        temp_tam_func = arbol.getTemporal()
        temp_index_param1 = arbol.getTemporal()
        temp_return = arbol.getTemporal()
        temp_result = arbol.getTemporal()

        codigo = f"\t#INSERT TABLE 3D\n"
        codigo += f"\t{temp_param1} = \"{table}\"\n"
        codigo += f"\t{temp_tam_func} = pointer + {num_params}\n"
        codigo += f"\t{temp_index_param1} = {temp_tam_func} + 1\n"
        codigo += f"\tstack[{temp_index_param1}] = {temp_param1}\n"
        codigo += f"\tpointer = pointer + {num_params}\n"
        codigo += f"\tinter()\n"
        #codigo += f"\t{temp_return} = pointer + 0\n"
        #codigo += f"\t{temp_result} = stack[{temp_return}]\n"
        codigo += f"\tpointer = pointer - {num_params}\n"
        #codigo += f"\tprint({temp_result})\n"
        
        #arbol.consola.append(codigo)
        return codigo

        #-------------------------------------
        # num_params = 7
        
        # temp_param1 = arbol.getTemporal()
        # temp_param2 = arbol.getTemporal()
        # temp_param3 = arbol.getTemporal()
        # temp_param4 = arbol.getTemporal()
        # temp_param5 = arbol.getTemporal()
        # temp_param6 = arbol.getTemporal()
        # temp_param7 = arbol.getTemporal()

        # temp_tam_func = arbol.getTemporal()

        # temp_index_param1 = arbol.getTemporal()
        # temp_index_param2 = arbol.getTemporal()
        # temp_index_param3 = arbol.getTemporal()
        # temp_index_param4 = arbol.getTemporal()
        # temp_index_param5 = arbol.getTemporal()
        # temp_index_param6 = arbol.getTemporal()
        # temp_index_param7 = arbol.getTemporal()

        # temp_return = arbol.getTemporal()
        # temp_result = arbol.getTemporal()
        
        # #valor, tipo, lcol, lexpre, strGram ,linea, columna
        # codigo = f"\t#INSERT TABLE 3D\n"
        # codigo += f"\t{temp_param1} = {valor}\n"
        # codigo += f"\t{temp_param2} = {tipo}\n"
        # codigo += f"\t{temp_param3} = list({columnas})\n"
        # codigo += f"\t{temp_param4} = list({expresiones})\n"
        # codigo += f"\t{temp_param5} = \"\"\n"
        # codigo += f"\t{temp_param6} = {-1}\n"
        # codigo += f"\t{temp_param7} = {-1}\n"

        # codigo += f"\t{temp_tam_func} = pointer + {num_params}\n"

        # codigo += f"\t{temp_index_param1} = {temp_tam_func} + 1\n"
        # codigo += f"\tstack[{temp_index_param1}] = {temp_param1}\n"

        # codigo += f"\t{temp_index_param2} = {temp_tam_func} + 2\n"
        # codigo += f"\tstack[{temp_index_param2}] = {temp_param2}\n"

        # codigo += f"\t{temp_index_param3} = {temp_tam_func} + 3\n"
        # codigo += f"\tstack[{temp_index_param3}] = {temp_param3}\n"
 
        # codigo += f"\t{temp_index_param4} = {temp_tam_func} + 4\n"
        # codigo += f"\tstack[{temp_index_param4}] = {temp_param4}\n"
        
        # codigo += f"\t{temp_index_param5} = {temp_tam_func} + 5\n"
        # codigo += f"\tstack[{temp_index_param5}] = {temp_param5}\n"

        # codigo += f"\t{temp_index_param6} = {temp_tam_func} + 6\n"
        # codigo += f"\tstack[{temp_index_param6}] = {temp_param6}\n"
        
        # codigo += f"\t{temp_index_param7} = {temp_tam_func} + 7\n"
        # codigo += f"\tstack[{temp_index_param7}] = {temp_param7}\n"
        
        # codigo += f"\tpointer = pointer + {num_params}\n"
        # codigo += f"\tinter_insertTable()\n"
        # codigo += f"\t{temp_return} = pointer + 0\n"
        # codigo += f"\t{temp_result} = stack[{temp_return}]\n"
        # codigo += f"\tpointer = pointer - {num_params}\n"
        # codigo += f"\tprint({temp_result})\n"
        
        # arbol.consola.append(codigo)

        