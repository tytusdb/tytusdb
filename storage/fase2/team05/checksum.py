import hashlib
import os
from pathlib import Path

import storageManager as u

hashmodes=['MD5','SHA256']


class Checksum:
    def __init__(self):
        self.chksum_db={}
        self.chksum_tables={}
        self.chksum_test={}
        self.default_dir='data/'

    def checksumDatabase(self,database: str, mode: str) -> str: #retorno checksum string
        chksum=None
        encoded_as=u.getCodificacionDatabase(database)
        #print(database,'encoded as:',encoded_as)
        paths=self.setDirectory(database,None)
        string2chksum=''
        try:
            if paths is not None:
                for p in paths:
                    with open(str(p),'r',encoding=encoded_as) as f:
                        string2chksum=string2chksum+str(f.read())
                if mode in hashmodes:
                    if mode=='MD5':
                        chksum=str(self.md5(string2chksum))
                        self.chksum_db[str(database+';md5')]=str(chksum+';md5')
                    if mode=='SHA256':
                        chksum=str(self.sha256(string2chksum))
                        self.chksum_db[str(database+';sha256')]=str(chksum+';sha256')
                else:
                    return None
        except:
            return None
        
        return chksum
            

    def checksumTable(self, database: str, table:str, mode: str) -> str: #retorno checksum string
        chksum=None
        encoded_as=u.getCodificacionDatabase(database)
        #print(database,'encoded as:',encoded_as)
        paths=self.setDirectory(database,table)
        try:
            if paths is not None:
                string2chksum=''
                for p in paths:
                    with open(str(p),'r',encoding=encoded_as) as f:
                        string2chksum=string2chksum+str(f.read())+'\n'
                if mode in hashmodes:
                    if mode=='MD5':
                        chksum=str(self.md5(string2chksum))
                        self.chksum_tables[str(database+'-'+table+';md5')]=str(chksum+';md5')
                    if mode=='SHA256':
                        chksum=str(self.sha256(string2chksum))
                        self.chksum_tables[str(database+'-'+table+';sha256')]=str(chksum+';sha256')
                else:
                    return None
        except:
            return None
        return chksum

    def md5(self, cadena:str) -> str:
        string_md5=''
        m=hashlib.md5()
        m.update(cadena.encode())
        string_md5=m.digest()
        del m
        return string_md5

    def sha256(self, cadena:str) -> str:
        string_sha256=''
        m=hashlib.sha256()
        m.update(cadena.encode())
        string_sha256=m.digest()
        del m
        return string_sha256
        
    def stringtest(self, cadena:str, mode:str) -> str:
        print('CHECKSUM')
        chksum=''
        if mode in hashmodes:
            if mode=='MD5':
                chksum=str(self.md5(cadena))
                self.chksum_test[str(cadena+';md5')]=str(chksum+';md5')
            if mode=='SHA256':
                chksum=str(self.sha256(cadena))
                self.chksum_test[str(cadena+';sha256')]=str(chksum+';sha256')
            else:
                return None
        else:
            return None
        return chksum

    def printDict(self, dic:dict):
        print('DICCIONARIO: ')
        for t in dic:
            print(t)

    def setDirectory(self,database:str,table:str):
        modo=u.getModoBaseDatos(database)
        if modo !=None:
            #print('Modo DB:',database,'|',modo)
            self.default_dir=''
            paths=[]
            if modo=='avl':
                self.default_dir='data/avlMode/'
                with os.scandir(self.default_dir) as ficheros:
                    for f in ficheros:
                        
                        if table==None:
                            if f.name.startswith(str(database)):
                                paths.append(f.path)
                        else:
                            if f.name.endswith(str(table)+'.tbl') and f.name.startswith(str(database)):
                                paths.append(f.path)
            if modo=='b':
                self.default_dir='data/b/'
                with os.scandir(self.default_dir) as ficheros:
                    for f in ficheros:
                        if f.name.startswith(str(database)):
                            if table==None:
                                paths.append(f.path)
                            else:
                                if f.name.endswith(str(table)+'-b.bin'):
                                    paths.append(f.path)
            if modo=='bplus':
                self.default_dir='data/BPlusMode/'+str(database)+'/'
            
                if table==None:
                    with os.scandir(self.default_dir) as ficheros:
                        for f in ficheros:    
                            if f.name.startswith(database):
                                paths.append(f.path)
                else:
                    lista=u.showTables(database)
                    for l in lista:
                        with os.scandir(self.default_dir+str(l)+'/') as folders:
                            for c in folders:
                                paths.append(c.path)

            if modo=='dict':
                self.default_dir='data/dictMode/'+str(database)+'/'
                if table==None:
                    with os.scandir(self.default_dir) as ficheros:
                        for f in ficheros:
                            paths.append(f.path)
                else:
                    with os.scandir(self.default_dir) as ficheros:
                        for f in ficheros:
                            if f.name.startswith(str(table)):
                                paths.append(f.path)

            if modo=='isam':
                self.default_dir='data/ISAMMode/tables/'
                with os.scandir(self.default_dir) as ficheros:
                    for f in ficheros:
                        if f.name.startswith(str(database)):
                            if table==None:
                                paths.append(f.path)
                            else:
                                if f.name.endswith(str(table)+'.bin'):
                                    paths.append(f.path)
            if modo=='json':
                self.default_dir='data/json/'
                with os.scandir(self.default_dir) as ficheros:
                    for f in ficheros:
                        if f.name.startswith(str(database)):
                            if table==None:
                                paths.append(f.path)
                            else:
                                if f.name.endswith(str(table)):
                                    paths.append(f.path)

            if modo=='hash':
                self.default_dir='data/hash/'+str(database)+'/'
                with os.scandir(self.default_dir) as ficheros:
                    for f in ficheros:
                        if table==None:
                            paths.append(f.path)
                        else:
                            if f.name.endswith(str(table)+'.bin'):
                                paths.append(f.path)
   
            return paths
        else:
            return None


chk=Checksum()

print(chk.checksumDatabase('BD5','MD5'))
print(chk.checksumTable('BD5','Year','MD5'))
print('--------------')
#print('BD1')
##print('MD5',chk.checksumDatabase('BD1','MD5'))
#print('SHA256',chk.checksumDatabase('BD1','SHA256'))
#print('--------------')
#print('BD3')
#print('MD5',chk.checksumDatabase('BD3','MD5'))
#print('SHA256',chk.checksumDatabase('BD3','SHA256'))
#print('--------------')
#print('BD4')
#print('MD5',chk.checksumDatabase('BD4','MD5'))
#print('SHA256',chk.checksumDatabase('BD4','SHA256'))
#print('--------------')
#print('BD5')
#print('MD5',chk.checksumDatabase('BD5','MD5'))
#print('SHA256',chk.checksumDatabase('BD5','SHA256'))
#print('--------------')
#print('BD6')
#print('MD5',chk.checksumDatabase('BD6','MD5'))
#print('SHA256',chk.checksumDatabase('BD6','SHA256'))
#print('--------------')
#print('BD7')
#print('MD5',chk.checksumDatabase('BD7','MD5'))
#print('SHA256',chk.checksumDatabase('BD7','SHA256'))
#print('--------------')
#print('BD8')
#print('MD5',chk.checksumDatabase('BD8','MD5'))
#print('SHA256',chk.checksumDatabase('BD8','SHA256'))

#print(chk.checksumTable('BD6','Cliente','MD5'))
