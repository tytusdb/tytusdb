#Método para insertar un registro en una tabla específica
def insert(database, table, register):
    #El método BuscarBase(), Pendiente de definirlo
    BaseDatos = BuscarBase(database)
    if BaseDatos == None:
        #La base de datos no se encontró
        return 2
    else:
        existe = False
        for i in range(BaseDatos.getTotalTablas()):
            if BaseDatos.Tablas[i].getNombre() == table:
                existe = True
                if BaseDatos.Tablas[i].getColumnas() != len(register):
                    #El numero de columnas a insertar no coincide con el numero de columnas de la tabla
                    return 5
                repetidas = VerificarLLavesDuplicadas(BaseDatos.Tablas[i].getPK(),BaseDatos.Tablas[i].VerTabla(),register)
                if repetidas[0] == True:
                    return 4
                BaseDatos.Tablas[i].agregarRegistro(register)
                #Operación exitosa
                return 0
        if existe == False:
            #La tabla no existe
            return 3
    return 1

#Método para cambiar los valores de un registro y una tabla en específco
def update(database, table, register, columns):
    BaseDatos = BuscarBase(database)
    if BaseDatos == None:
        #La base de datos no se encontró
        return 2
    else:
        existe = False
        for i in range(BaseDatos.getTotalTablas()):
            if BaseDatos.Tablas[i].getNombre() == table:
                existe = True
                repetidas = VerificarLLavesDuplicadas(BaseDatos.Tablas[i].getPK(),BaseDatos.Tablas[i].VerTabla(),columns)
                if repetidas[0] == False:
                    #La llave no se ha encontrado
                    return 4
                for key in register:
                    BaseDatos.Tablas[i].actualizarRegistro(repetidas[1],key,register[key])
                #Operacion exitosa
                return 0
        if existe == False:
            #La tabla no existe
            return 3
    return 1

#Método para eliminar un registro en la tabla de una base de datos
def delete(database, table, columns):
    BaseDatos = BuscarBase(database)
    if BaseDatos == None:
        #La base de datos no se encontró
        return 2
    else:
        existe = False
        for i in range(BaseDatos.getTotalTablas()):
            if BaseDatos.Tablas[i].getNombre() == table:
                existe = True
                repetidas = VerificarLLavesDuplicadas(BaseDatos.Tablas[i].getPK(),BaseDatos.Tablas[i].VerTabla(),columns)
                if repetidas[0] == False:
                    #La llave no se ha encontrado
                    return 4
                BaseDatos.Tablas[i].eliminarRegistro(repetidas[1])
                #Operacion exitosa
                return 0
        if existe == False:
            #La tabla no existe
            return 3
    return 1

#def truncate(database: str, table str) -> int:
def truncate(database, table):
    BaseDatos = BuscarBase(database)
    if BaseDatos == None:
        #La base de datos no se encontró
        return 2
    else:
        existe = False
        for i in range(BaseDatos.getTotalTablas()):
            if BaseDatos.Tablas[i].getNombre() == table:
                existe = True
                BaseDatos.Tablas[i].vaciarTabla()
                #Operacion exitosa
                return 0
        #No se encontro la tabla
        return 3
    #Algún problema en ejecucion
    return 1

#def extractRow(database: str, table: str, columns: list) -> list:
def extractRow(database, table, columns):
    BaseDatos = BuscarBase(database)
    if BaseDatos == None:
        #La base de datos no se encontró
        return []
    else:
        existe = False
        for i in range(BaseDatos.getTotalTablas()):
            if BaseDatos.Tablas[i].getNombre() == table:
                existe = True
                repetidas = VerificarLLavesDuplicadas(BaseDatos.Tablas[i].getPK(),BaseDatos.Tablas[i].VerTabla(),columns)
                if repetidas[0] == False:
                    #La llave no se ha encontrado
                    return []
                #Operacion exitosa
                return BaseDatos.Tablas[i].extraerRegistro(repetidas[1])
        if existe == False:
            #La tabla no existe
            return []
    return []

#Método para verificar si hay llaves duplicadas en el registro enviado
def VerificarLLavesDuplicadas(llaves,arreglo,registro):
    Repetidos = []
    Comparar = []
    for i in range(len(arreglo)):
        #print(type(llaves))
        if type(llaves) == int and type(registro)==int:
            #print("Se compara "+str(arreglo[i][llaves])+" con "+str(registro)+" comparacion 1")
            if str(arreglo[i][llaves]) == str(registro):
                # La llave primaria está duplicada
                return [True,i]
        elif type(llaves) == int:
            #print("Se compara "+str(arreglo[i][llaves])+" con "+str(registro[llaves])+" comparacion 2")
            if str(arreglo[i][llaves]) == str(registro[llaves]):
                # La llave primaria está duplicada
                return [True,i]
        else:
            for j in range(len(llaves)):
                #print("Comparacion 3")
                if str(arreglo[i][llaves[j]]) == str(registro[j]):
                    # La llave primaria está duplicada
                    Repetidos.append(True)
                    Comparar.append(True)
                else:
                    Repetidos.append(False)
                    Comparar.append(True)
        if Repetidos == Comparar and Repetidos!=[]:
            return [True,i]
        Repetidos=[]
        Comparar=[]
    return [False,0]