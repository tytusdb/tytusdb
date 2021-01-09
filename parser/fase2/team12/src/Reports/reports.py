from prettytable import PrettyTable
import webbrowser
import json
def generar_img(temp : str):
    if temp != "" and temp is not None:
        from graphviz import Source
        s = Source(temp, filename="src\\Reports\\tree_report", format="png")
        s.view()

def reporte_ts(arbol):
    if arbol is not None:
        cadena = "\t\t\t\t\t\tTABLA DE SIMBOLOS \n"
        with open('src\\typeChecker\\estructura.json') as file:
            data = json.load(file)

            for db in data:
                cadena += "DATABASE: "+db +"\n"
                dbactual = data[db]["tables"]
                indexes = data[db]["indexes"]
                procedimientos = data[db]["procedures"]
                cadena += "\t\t\t\t"+"LISTA DE INDICES:\n"
                for indx in indexes:
                    cadena += "\t"+"INDICE: "+str(indx["name"])+"\n"
                    cadena += "\t\t"+"table: "+str(indx["table"])+"\n"
                    cadena += "\t\t"+"Method: "+str(indx["method"])+"\n"
                    for columns in indx['listaAtribb']:
                        cadena += "\t\t\t"+"Column: "+str(columns["column"])+"\n"
                        cadena += "\t\t\t"+"Order: "+str(columns["order"])+"\n"
                        cadena += "\t\t\t"+"Nulls: "+str(columns["nulls"])+"\n"

                cadena += "\t\t\t\t"+"LISTA DE PROCEDIMIENTOS\n"
                for proce in procedimientos:
                    cadena += "\t"+"PROCEDIMIENTO: "+str(proce["nombre"])+"\n"
                    cadena += "\t\t"+"Parametros: "+str(proce["parametros"])+"\n\n"
                cadena += "\t\t\t\t"+"LISTA DE TABLAS:\n"                        
                for table in dbactual:
                    cadena += "\t"+"TABLA: "+table+"\n"
                    columnas = data[db]["tables"][table]["columnas"]
                    for column in columnas:
                        cadena += "\t"+"\t"+"COLUMNA:"+"\n"
                        cadena += "\t"+"\t"+"\t"+"Index: "+ str(column["index"])+"\n"
                        cadena += "\t"+"\t"+"\t"+"Name: "+ str(column["name"])+"\n"
                        cadena += "\t"+"\t"+"\t"+"type: "+ str(column["type"])+"\n"
                        cadena += "\t"+"\t"+"\t"+"specificType: "+ str(column["specificType"])+"\n"
                        cadena += "\t"+"\t"+"\t"+"default: "+ str(column["default"])+"\n"
                        cadena += "\t"+"\t"+"\t"+"isNull: "+ str(column["isNull"])+"\n"
                        cadena += "\t"+"\t"+"\t"+"isUnique: "+str(column["isUnique"])+"\n"
                        cadena += "\t"+"\t"+"\t"+"uniqueName: "+ str(column["uniqueName"])+"\n"
                        cadena += "\t"+"\t"+"\t"+"size: "+ str(column["index"])+"\n"
                        cadena += "\t"+"\t"+"\t"+"isPrimary: "+ str(column["index"])+"\n"
                        cadena += "\t"+"\t"+"\t"+"referencesTable: "+ str(column["referencesTable"])+"\n"
                        cadena += "\t"+"\t"+"\t"+"isCheck: "+ str(column["isCheck"])+"\n"
                        cadena += "\t"+"\t"+"\t"+"referenceColumn: "+ str(column["referenceColumn"])+"\n"
        f = open("src\\Reports\\TS.txt", "w")
        f.write(cadena)
        f.close()
        webbrowser.open("src\\Reports\\TS.txt")

def reportar_bnf(reportebnf):
    cadena = "REPORTE BNF"
    for i in reportebnf:
        cadena += i
    reportebnf.clear()
    f = open("src\\Reports\\GramaticaDinamica.txt", "w")
    f.write(cadena)
    f.close()
    webbrowser.open("src\\Reports\\GramaticaDinamica.txt")
    return reportebnf
