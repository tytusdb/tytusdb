# File:         B+ Mode File for EDD
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Virginia Sarai Gutierrez Depaz


import math
import os
from storageManager.Clave import Clave
from storageManager.Pagina import Pagina

class ArbolBmas:
    def __init__(self):
        self.raiz = None
        self.Dato = []
        self.retorno = 1 

    def insertar(self, clave, data):
        if self.estaVacio():
            self.raiz = Pagina([None, Clave(clave, data), None])
        else:
            valorMediana, nuevaPagina, seDividio = self.insertarRecursivo(
                clave, data, self.raiz)
            if seDividio:
                self.raiz = Pagina([self.raiz, valorMediana, nuevaPagina])

    def insertarRecursivo(self, clave, data, paginaTemporal):
        if paginaTemporal.esHoja():
            return paginaTemporal.insertarEnPagina(clave, data)
        else:
            if clave > paginaTemporal.contenido[-2].clave:
                valorMediana, nuevaPagina, seDividio = self.insertarRecursivo(
                    clave, data, paginaTemporal.contenido[-1])
            else:
                i = 1
                while i < len(paginaTemporal.contenido) and clave > paginaTemporal.contenido[i].clave:
                    i += 2
                valorMediana, nuevaPagina, seDividio = self.insertarRecursivo(
                    clave, data, paginaTemporal.contenido[i-1])
            if seDividio:
                return paginaTemporal.insertarEnPagina(valorMediana.clave, valorMediana.data, nuevaPagina)
            else:
                return None, None, False

                #[apuntador, Clave, Apuntador]

    def estaVacio(self):
        return self.raiz == None

    def recorrer(self):
        self.recorrerRecursivo(self.raiz, 0)

    def recorrerRecursivo(self, pagina, level):
        if not pagina.esHoja():
            # [puntero, clave, puntero, clave2, puntero, clave3]
            for x in pagina.contenido[::2]:
                self.recorrerRecursivo(x, level+1)
        #print("Level: "+str(level))
        for x in pagina.contenido[1::2]:
            print(x.data)

    def imprimirLista(self, pagina):
        if pagina.esHoja():
            aux = pagina
            i = 0
            while aux:
                #print("Pagina: " + str(i))
                for x in aux.contenido[1::2]:
                    #print(x.data)
                    ''''''
                aux = aux.paginaSiguiente
                i += 1
        else:
            self.imprimirLista(pagina.contenido[0])

    # contador de F = level + 1
    def graphviz(self):
        self.hojas = []
        archivo = open('archivo.dot', 'w', encoding='utf-8')
        archivo.write('digraph structs {\n')
        archivo.write('node [shape=record];\n')
        self.contPag = 0
        self.graficarEncabezado(self.raiz, 0, archivo)
        self.contPag = 0
        self.graficarEnlace(self.raiz, 0, archivo, None)
        tmp = self.hojas[0]
        ant = tmp
        for x in self.hojas[1::1]:
            ant = tmp
            tmp = x
            archivo.write('{0} -> {1};\n'.format(ant, tmp))
        archivo.write('{rank=same; ')
        for x in self.hojas[::1]: archivo.write('{0}; '.format(x))
        archivo.write('}\n}\n')
        archivo.close()
        os.system('dot -Tpng archivo.dot -o salida.png')
        #os.system('salida.png')

    def graficarEncabezado(self, pagina, level, archivo):
        f = ''
        for x in range(level + 1):
            f += 'f'

        nombre = 'pagina{0}'.format(self.contPag)
        archivo.write('{0} [label="'.format(nombre))
        self.contPag += 1

        pos = 0  # posicion actual del arreglo
        bandera = True
        for x in pagina.contenido[::1]:
            if bandera:
                # puntero
                archivo.write('<{0}{1}> '.format(f, pos))
            else:
                # clave
                archivo.write('|<{0}{1}> {2} |'.format(f, pos, x.data))
            bandera = not bandera
            pos += 1
        archivo.write('"];\n')

        if not pagina.esHoja():
            for x in pagina.contenido[::2]:
                self.graficarEncabezado(x, level+1, archivo)
        else:
            self.hojas += [nombre]

    def graficarEnlace(self, pagina, level, archivo, padre):
        f = ''
        for x in range(level + 1):
            f += 'f'

        if not (padre is None):
            self.contPag += 1
            archivo.write('{0} -> pagina{1};\n'.format(padre, self.contPag))

        pos = 0  # posicion actual del arreglo
        bandera = True
        nombre = 'pagina' + str(self.contPag)
        for x in pagina.contenido[::1]:  # pagina0
            if bandera:
                # puntero
                if not pagina.esHoja():
                    # no es Hoja
                    self.graficarEnlace(x, level+1, archivo,
                                        '{0}:{1}{2}'.format(nombre, f, pos))
            bandera = not bandera
            pos += 1

    def eliminar(self, clave):
        if  self.raiz is None:
            return False
        seElimino, esHoja = self.raiz.eliminar(clave, None, self.raiz)
        if seElimino == True:
            '''print(str(clave) + ' eliminado.')'''
        else:
            '''print('Error: La clave ' + str(clave) + ' no se eliminó.')'''
        return seElimino

    def truncateRoot(self):
        self.raiz = None



################################################################################################################
################################################################################################################

    #METODO DE BUSQUEDA DENTRO DEL ARBOL  ---------------------------------------------------------
    def Busqueda(self,valor):
        if self.raiz is None:
            return []
        else:
            self.Dato =[] 
            self._Busqueda(self.raiz,valor)
            return  self.Dato
    def _Busqueda(self, pagina,valor):
        if pagina is None:
            return []
    
        # se busca el valor en el nodo
        for x in pagina.contenido[1::2]:
            if valor == x.clave:
                self.Dato.append(x.data)
                break
        cont=1
        #i= len(pagina.contenido)      
        for x in pagina.contenido[1::2]:
            if cont==1:
                if len(pagina.contenido)==3:
                    if valor < x.clave: 
                        self._Busqueda(pagina.contenido[0], valor)
                        cont+=2
                        break
                    else:
                        self._Busqueda(pagina.contenido[2], valor)
                        cont+=2
                        break
                else:
                    if valor >= x.clave and valor < pagina.contenido[cont+2].clave: 
                        self._Busqueda(pagina.contenido[cont+1], valor)
                        cont+=2
                        break
                           
                    elif valor < x.clave: 
                        self._Busqueda(pagina.contenido[0], valor)
                        cont+=2
                        break
                           
            elif cont == len(pagina.contenido)-2:
                if valor >= x.clave: 
                    self._Busqueda(pagina.contenido[cont+1], valor)
                    cont+=2
                    break
                        
            elif valor >= x.clave and valor < pagina.contenido[cont+2].clave:
                self._Busqueda(pagina.contenido[cont+1], valor)
                cont+=2
                break   
            
    def VerHoja(self, pag):
        if pag == None:
            return []
        esHoja = True
        i = 0      
        while i < len(pag.contenido):
            esHoja &= pag.contenido[i] == None 
            i += 2 
        return esHoja       

    def Update(self,diccionario, val ):
        if self.raiz is None:
            return 4
        else:
            self._Upadate(diccionario,self.raiz,val )
            return self.retorno

    def _Upadate(self,diccionario,pagina,valor):
        if pagina is None:
            self.retorno = 4
            return self.retorno
         #ES LA ULTIMA PAGINA 
        try:
            if self.VerHoja(pagina):
                for val in pagina.contenido[1::2]:
                    if val.clave ==valor:
                        try:
                            # CAMBIO DE DATOS DENTRO DEL REGISTRO
                            for x in diccionario:
                                val.data[x]=diccionario[x]
                            self.retorno = 0
                            return self.retorno
                        except ( IndexError):
                            self.retorno = 1
                            return self.retorno
                self.retorno = 4
                return self.retorno
            # CORROBORAR  SI ES POR LA IZQUIERDA
            else:
                cont=1
                #i= len(pagina.contenido)      
                for x in pagina.contenido[1::2]:
                    if cont==1:
                        if len(pagina.contenido)==3:
                            if valor < x.clave: 
                                self._Upadate(diccionario,pagina.contenido[0], valor)
                                break
                            else:
                                self._Upadate(diccionario,pagina.contenido[2], valor)
                                break
                        else:
                            if valor >= x.clave and valor < pagina.contenido[cont+2].clave: 
                                self._Upadate(diccionario,pagina.contenido[cont+1], valor)
                                break
                            elif valor < x.clave: 
                                self._Upadate(diccionario,pagina.contenido[0], valor)
                                break
                    elif cont == len(pagina.contenido)-2:
                        if valor >= x.clave: 
                            self._Upadate(diccionario,pagina.contenido[cont+1], valor)
                            break
                    
                    elif valor >= x.clave and valor < pagina.contenido[cont+2].clave:
                        self._Upadate(diccionario,pagina.contenido[cont+1], valor)
                        break
                    cont+=2
        except:
            return 1

    # ACCEDER A LA LISTA ENLAZADA DE LAS HOJAS AL FINAL DEL ARBOL 
    def ListaEnlazada(self,columns,lower,upper):
        if self.raiz is None:
            return  []
        registro=[]
        self._ListaEnlazada(self.raiz,registro,columns,lower,upper)
        return registro  
    
    def _ListaEnlazada(self,pagina,lista,column,lower,upper):
        try: 
            if self.VerHoja(pagina):
                #  PARA LA FUNCION DE EXTRAER TODOS LOS VALORES DE LA TABLA EXTRACT TABLE
                if column ==None and lower == None and upper == None:
                    lista.clear()
                    while pagina !=None:
                        for val in pagina.contenido[1::2]: 
                            lista.append(val.data)          
                        
                        pagina = pagina.paginaSiguiente
                    return lista
                #  PARA LA FUNCION DE EXTRAER TODOS LOS VALORES DE LA TABLA EXTRACT CON RANGO EXTRAC RANGE
                else: 
                    lista.clear()
                    try:
                        contador = 0 
                        while pagina !=None:

                            for val in pagina.contenido[1::2]:
                                if contador >= lower :
                                    lista.append(val.data[column])
                                if contador == upper:
                                    break
                                else: 
                                    contador += 1
                                        
                            pagina = pagina.paginaSiguiente
                            if contador == upper:
                                break
                        return lista
                    except(IndexError):
                        return None
            else: 
                self._ListaEnlazada(pagina.contenido[0],lista,column,lower,upper)
        except:
            return []

    def AlterCol(self,function, column): 
        if self.raiz is None:
            return 1
        val= self._AlterCol(self.raiz,  function, column)
        return val 
    
    def _AlterCol(self, pagina,  function , column) -> int:
        retorno = 0
        try:
            if self.VerHoja(pagina):      # se comprueba que es el ultimo nivel del arbol 
                # FUNCION PARA AGREGAR 
                if function == "Add":
                    while pagina != None:
                        for val in pagina.contenido[1::2]:
                            val.data.append(column)
                        pagina = pagina.paginaSiguiente
                # FUNCION PARA ELIMINAR COLUMNA
                elif function == "Drop":
                    while pagina != None:
                        for val in pagina.contenido[1::2]:
                            val.data.pop(column)
                        pagina = pagina.paginaSiguiente
                    
            #    CUANDO NO ES HOJA Y ES UNA PAGINA CON HIJOS 
            else: 
                self._AlterCol(pagina.contenido[0],function,column)
            return retorno
        except(IndexError, TypeError):
            return 1

    # RETORNA LOS NODOS DEL ARBOL
    # ACCEDER A LA LISTA ENLAZADA DE LAS HOJAS AL FINAL DEL ARBOL 
    def Claves_Hojas(self,):
        if self.raiz is None:
            return []
        registro=[]
        self._Claves_Hojas(self.raiz,registro)
        return registro  
    
    def _Claves_Hojas(self,pagina,lista):
        try: 
            if self.VerHoja(pagina):
                #  PARA LA FUNCION DE EXTRAER TODOS LOS VALORES DE LA TABLA EXTRACT TABLE
                lista.clear()
                while pagina !=None:
                    for val in pagina.contenido[1::2]:
                        lista.append(val)
                        
                    pagina = pagina.paginaSiguiente
                return lista
                #  PARA LA FUNCION DE EXTRAER TODOS LOS VALORES DE LA TABLA EXTRACT CON RANGO EXTRAC RANGE
            elif self.VerHoja(pagina) ==[]:
                return []
            else: 
                self._Claves_Hojas(pagina.contenido[0],lista)
        except( IOError):
            return []