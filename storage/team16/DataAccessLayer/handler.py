import pickle
import os

class Handler:

    #Databases
    @staticmethod
    def actualizarArchivoDB(databases):
        f = open('data/root.dat','wb')
        pickle.dump(databases, f)
        f.close()
    
    @staticmethod
    def leerArchivoDB() -> list:
        if not os.path.exists('data'):
            os.makedirs('data')
        if not os.path.exists('data/root.dat'):
            f = open('data/root.dat','wb')
            f.close()
        if os.path.getsize('data/root.dat') > 0:
            with open('data/root.dat', 'rb') as f:
                return pickle.load(f)
        return []


    #Tables
    @staticmethod
    def actualizarArchivoTB(tabletrees, database: str, tableName: str):
        f = open('data/'+str(tableName)+'-'+str(database)+'.tbl','wb')
        pickle.dump(tabletrees, f)
        f.close()

    @staticmethod
    def siExiste(database: str, tableName: str):
        return os.path.isfile('data/'+str(tableName)+'-'+str(database)+'.tbl')

    @staticmethod
    def leerArchivoTB(database: str, tableName: str):
        if os.path.getsize('data/'+str(tableName)+'-'+str(database)+'.tbl') > 0:
            with open('data/'+str(tableName)+'-'+str(database)+'.tbl', 'rb') as f:
                return pickle.load(f)
        else:
            return None
    
    @staticmethod
    def borrarArchivo(filename):
        try:
            os.remove('data/'+filename)
        except:
            print("No se encontró el archivo")

    @staticmethod
    def renombrarArchivo(oldName, newName):
        try:
            os.rename('data/'+oldName, 'data/'+newName)
        except:
            print("No se pudo renombrar")

    @staticmethod
    def findCoincidences(database, tablesName):
        tmp = []
        for i in tablesName:
            try:
                if os.path.isfile('data/'+str(i)+'-'+str(database)+'.tbl'):
                    tmp.append(str(i))
            except:
                continue
        return tmp