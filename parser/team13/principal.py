import gramaticaASC as g
from sentencias import *


def interpretar_sentencias(arbol):
   
    for nodo in arbol:
        if isinstance(nodo, SCrearBase):
            print("Creando Base-----")
            print(nodo.id)
            print("Es con replace?")
            print(nodo.replace)
            print("Es con if not exists?")
            print(nodo.exists)
            # aqui va el metodo para ejecutar crear base
        elif isinstance(nodo, SShowBase):
            print("Mostrando Base-----")
            print(nodo.like)
            # aqui va el metodo para ejecutar show base
        elif isinstance(nodo, SAlterBase):
            print("Alterando Base-----")
            print(nodo.id)
            # aqui va el metodo para ejecutar alter base
        elif isinstance(nodo, SDropBase):
            print("Drop Base-----")
            print(nodo.exists)
            print(nodo.id)
            # aqui va el metodo para ejecutar drop base
        elif isinstance(nodo, STypeEnum):
            print("Enum Type------")
            print(nodo.id)
            for val in nodo.lista:
                print(val.valor)
        elif isinstance(nodo, SUpdateBase):
            print("Update Table-----------")
            print(nodo.id)
            for val in nodo.listaSet:
                print("columna------")
                print(val.columna)
                print("------------")
                if isinstance(val.valor, SOperacion):
                    val2 = val.valor
                    print(val2.opIzq.valor)
                    print(val2.operador)
                    print(val2.opDer.valor)
                else:
                    val2 = val.valor
                    print(val2.valor)
            print(nodo.listaWhere)
        elif isinstance(nodo, SDeleteBase):
            print("Delete Table-------------")
            print(nodo.id)
            print("Tiene where?")
            print(nodo.listaWhere)
        elif isinstance(nodo, STruncateBase):
            print("Truncate Table------------")

            for id in nodo.listaIds:
                print(id)
        elif isinstance(nodo, SInsertBase):
            print("Insert Table-------------")
            print("nombre tabla")
            print(nodo.id)
            print("valores")
            for val in nodo.listValores:
                if isinstance(val, SExpresion):
                    print(val.valor)
        elif isinstance(nodo, SShowTable):
            print("Mostrando tablas----------")
        elif isinstance(nodo, SDropTable):
            print("Drop table-----------")
            print(nodo.id)
        elif isinstance(nodo, SAlterTableRename):
            print("Cambiando nombre columna---")
            print(nodo.idtabla)
            print(nodo.idcolumna)
            print(nodo.idnuevo)
        elif isinstance(nodo, SAlterTableAddColumn):
            print("Agregando Columna-----")
            print(nodo.idtabla)
            print(nodo.idcolumna)
            print(nodo.tipo.dato)
        elif isinstance(nodo, SAlterTableCheck):
            print("Agregando check--------")
            print(nodo.idtabla)
            print(nodo.expresion)
        elif isinstance(nodo, SAlterTableAddUnique):
            print("Agregando unique-------")
            print(nodo.idtabla)
            print(nodo.idcolumna)
            print(nodo.idconstraint)
        elif isinstance(nodo, SAlterTableAddFK):
            print("Agregando llave foranea--------")
            print(nodo.idtabla)
            print(nodo.idcolumna)
            print(nodo.idtpadre)
        elif isinstance(nodo, SAlterTable_AlterColumn):
            print("Alter column--------------")
            print(nodo.idtabla)
            for col in nodo.columnas:
                print(col.idcolumna)
        elif isinstance(nodo, SAlterTableDrop):
            print("Alter drop----------")
            print(nodo.idtabla)
            print("Es un constraint?")
            print(nodo.idco)
        elif isinstance(nodo, SCrearTabla):
            print("Creando tabla")
            print(nodo.id)
            print("Hereda?")
            print(nodo.herencia)
            print(nodo.nodopadre)
            print("Columnas")
            for col in nodo.columnas:
                if isinstance(col,SColumna):
                    print(col.id)
                    print(col.tipo.dato)
                    if col.opcionales!=None:
                        print(col.opcionales)
                elif isinstance(col,SColumnaUnique):
                    print("columna unique")
                    print(col.id)

                elif isinstance(col,SColumnaPk):
                    print(col.id)
                elif isinstance(col,SColumnaCheck):
                    print(col.id)
                elif isinstance(col,SColumnaFk):
<<<<<<< Updated upstream
                    print(col.id)
=======
                    print(col.id)


f = open("./entrada.sql", "r")
input = f.read()
arbol = g.parse(input)
interpretar_sentencias(arbol)
>>>>>>> Stashed changes
