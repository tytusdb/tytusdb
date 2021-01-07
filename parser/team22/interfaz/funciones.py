from tkinter import ttk,scrolledtext,simpledialog,filedialog,messagebox,END,INSERT
import sys

path = sys.path[0].replace('interfaz','') or sys.path[0]
sys.path.append(path)

import principal as principal
import parser_asc as parser_asc

class Funciones_:

    def __init__(self):
        self.reservadas = ['create','databases',  'database', 'current_user','session_user','table','insert','inherits','smallint','integer','bigint',
                    'decimal','numeric','real','double','precision','money','character','varying','varchar','bytea','char','text','now',
                    'date_part','current_date','current_time','extract','timestamp','without','time','zone','date','interval','month','day',
                    'hour','minute','second','boolean','year','datetime','drop','alter','delete','not','null','foreign','key','primary',
                    'references','use','select','distinct','as','enum','type','from','left','join','right','on','any','count','sum','like',
                    'avg','abs','cbrt','ceil','ceiling','degrees','div','exp','factorial','floor','gcd','ln','log','mod','pi','power','radians',
                    'round','acos','asin','atan','atan2','cos','cot','sin','tan','acosd','asind','atand','atan2d','cosd','cotd','sind',
                    'tand','sinh','cosh','tanh','asinh','acosh','atanh','max','min','order','where','if','owner','mode','and','or','between','in',
                    'inner','full','self','case','union','group','having','exists','intersect','except','offset','limit','all','into','some',
                    'backup','to','disk','constraint','rename','add','check','default','modify','column','set','unique','index','auto_increment',
                    'values','identity','by','with','replace',    'desc','outer','is','top','truncate','update','asc','show','when','then','greatest',
                    'least','end','else','least','true','false','unknown','isnull','notnull','length','substring','trim','md5','sha256','substr',
                    'get_byte','set_byte','convert','encode','decode','sign','sqrt','width_bucket','trunc','random','exp']
        self.archivo = ""

    def nuevo(self,editor):
        editor.delete(1.0, END)
        self.archivo = ""

    def abrir(self,editor):
        self.archivo = filedialog.askopenfilename(title = "Abrir Archivo", initialdir = sys.path[0])

        entrada = open(self.archivo)
        content = entrada.read()

        editor.delete(1.0, END)
        editor.insert(INSERT, content)
        entrada.close()

    def guardarComo(self,editor):
        guardar = filedialog.asksaveasfilename(title = "Guardar Archivo", initialdir = sys.path[0])
        fguardar = open(guardar, "w+")
        fguardar.write(editor.get(1.0, END))
        fguardar.close()
        self.archivo = guardar

    def guardarArchivo(self,editor):
        if self.archivo == "":
            self.guardarComo(editor)
        else:
            guardarc = open(self.archivo, "w")
            guardarc.write(editor.get(1.0, END))
            guardarc.close()

    def analizar(self,objetos):
        editor = objetos[0]
        consola = objetos[1]
        tabla_lexico = objetos[2]
        tabla_sintactico = objetos[3]
        tabla_semantico = objetos[4]
        tabla_simbolos = objetos[5]
        frame_salida = objetos[6]

        countLex = 0
        countSin = 0
        countSem = 0

        if editor.get(1.0,END) != "\n":
            entrada = editor.get(1.0,END)
            self.pintarPalabras(editor,entrada)
            
            contenido = principal.parse(entrada)
            result_consola = contenido[0]
            result_tabla_simbolos = contenido[1]
            result_errores = contenido[2]
            result_salida = contenido[3]

            #'**************** Consola: ****************'
            consola.delete(1.0,END)
            dataConsola = ">>> \n"
            for element in result_consola:
                dataConsola += element + '\n'
            consola.insert(INSERT,dataConsola)
            
            #'*************** Tabla Simbolos ******************'
            self.limpiarTabla(tabla_simbolos)
            for element in result_tabla_simbolos.simbolos:
                aux = result_tabla_simbolos.simbolos[element].imprimir()
                tabla_simbolos.insert('', 0, text = aux[3], values = (aux[0], aux[1], aux[2]))

            #'*************** Errores ******************'
            self.limpiarTabla(tabla_lexico)
            self.limpiarTabla(tabla_sintactico)
            self.limpiarTabla(tabla_semantico)
            for element in result_errores.errores:
                aux = element.imprimir()
                if aux[0] == "Léxico":
                    countLex += 1
                    tabla_lexico.insert('', 0, text = str(countLex), values = (aux[2], aux[0], aux[1]))
                elif aux[0] == "Sintáctico":
                    countSin += 1
                    tabla_sintactico.insert('', 0, text = str(countSin), values = (aux[2], aux[0], aux[1]))
                else:
                    countSem += 1
                    tabla_semantico.insert('', 0, text = str(countSem), values = (aux[2], aux[0], aux[1]))

            #'*************** Salida ******************'
            if len(result_salida) > 0:
                result_salida = result_salida[len(result_salida) - 1]
                num_columns = len(result_salida[0])
                ancho = int(651/num_columns)
                columns = []
                aux_name_col = []
                index_column = []
                union_column = []
                for index in range(1,num_columns):
                    indice = "#" + str(index)
                    columns.append(indice)
                for index in range(0,num_columns):
                    aux_name_col.append(result_salida[0][index])
                for col in columns:
                    index_column.append(col)
                if len(columns) == 0:
                    columns.append("#0")
                for i in range(0,len(columns)):
                    if i == 0:
                        union_column.append(["#0",aux_name_col[i]])
                        if (i + 1) < len(columns):
                            union_column.append([columns[i],aux_name_col[i + 1]])
                    else:
                        union_column.append([columns[i],aux_name_col[i + 1]])

                tabla_salida = ttk.Treeview(frame_salida, columns = index_column, height = 23)
                tabla_salida.grid(row = 3, column = 2)

                for element in union_column:
                    print(element)
                    tabla_salida.heading(element[0], text = element[1])
                    tabla_salida.column(element[0], width = ancho, minwidth = ancho, stretch = "no", anchor = "center")
                table_scrol_salida = ttk.Scrollbar(frame_salida, orient = "vertical", command  = tabla_salida.yview)
                table_scrol_salida.grid(row = 3, column = 3, sticky = "ns")
                table_scrolx_salida = ttk.Scrollbar(frame_salida, orient = "horizontal", command  = tabla_salida.xview)
                table_scrolx_salida.grid(row = 4, column = 2, columnspan = 2, sticky = "we")
                tabla_salida.configure(yscrollcommand = table_scrol_salida.set, xscrollcommand = table_scrolx_salida.set)

                self.limpiarTabla(tabla_salida)
                for i in range(1,len(result_salida)):
                    aux = result_salida[i][0]
                    result_salida[i].remove(aux)
                    tabla_salida.insert('', 0, text = aux, values = result_salida[i])
        else:
            messagebox.showerror(message="Ingrese datos a analizar",title="TytusDB")

    def reporte(self,reporte):
        if reporte == "gr":
            parser_asc.gramatical.obtenerGramatical()
        else:
            parser_asc.dot.view()

    def limpiarTabla(self,table):
        data = table.get_children()
        for dato in data:
            table.delete(dato)

    def info(self):
        messagebox.showinfo(message="OLC2 sección A\nKIMBERLY MIREYA ELIAS DIAZ - 201700507\nJUAN PABLO ALVARADO VELASQUEZ - 201700511\nDANIEL ARTURO ALFARO GAITAN - 201700857\nCRISTOFHER ANTONIO SAQUILMER RODAS - 201700686",title="TytusDB")

    def pintarPalabras(self,editor,entrada):
        editor.delete(1.0,END)
        fila = 0
        columna = 0
        palabra = ""
        for linea in entrada:
            fila += 1
            if linea == '\n':
                columna = 0
                self.juntarPalabra(palabra,columna,fila,editor)
                palabra = ""
                palabra += linea
            elif linea == '\t' or linea == ' ':
                columna += 1
                self.juntarPalabra(palabra,columna,fila,editor)
                palabra = ""
                palabra += linea
            else:
                palabra += linea
                columna += 1

    def juntarPalabra(self,lexema,columna,fila,editor):
        bandera = False
        pos = str(fila) + '.' + str(columna)
        aux = lexema.replace('\n','') or lexema
        aux = aux.replace('\t','') or aux
        aux = aux.replace(' ','') or aux
        for reservada in self.reservadas:
            if reservada in aux:
                pos = str(fila) + '.' + str(columna)
                bandera = True
            elif reservada in aux.lower():
                pos = str(fila) + '.' + str(columna)
                bandera = True
        if bandera :
            editor.insert(pos,lexema,aux)
            editor.tag_config(aux,foreground = "blue")
        else:
            editor.insert(pos,lexema)

    def salir(self,raiz):
        value = messagebox.askokcancel("Salir", "¿Está seguro que desea salir?")
        if value :
            raiz.destroy()

    def analiza2(self,editor):
        if editor.get(1.0,END) != "\n":
            entrada = editor.get(1.0,END)
            '**************** Para reporte gramatical y ast: ****************'
            parser_asc.parse(entrada)
        else:
            messagebox.showerror(message="Ingrese datos a analizar",title="TytusDB")