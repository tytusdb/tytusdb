# File:         B+ Mode File for EDD
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Virginia Sarai Gutierrez Depaz

import math
import os
from storageManager.Clave import Clave

class Pagina:
    def __init__(self, contenido=[], paginaSiguiente=None, grado=5):
        self.grado = grado
        self.contenido = contenido
        # contenido -> [apuntador, clave1, apuntador, clave2, apuntador....]
        self.paginaSiguiente = paginaSiguiente

    def insertarEnPagina(self, clave, data, pagina=None):
        if self.paginaVacia():
            #posiciones   [0,    1,     2]
            # contenido -> [none, clave, none]
            self.contenido = [None, Clave(clave, data), None]
        elif clave > self.contenido[-2].clave:  # insertar de ultimo
            #posiciones [-3,   -2,    -1]
            #contenido  [none, clave, none]
            # despues
            ##contenido  [none, clave, none, clav2, none]
            self.contenido += [Clave(clave, data), pagina]
        elif clave < self.contenido[1].clave:  # insertar al principio
            #posiciones   [0,    1,     2,    3,      4,    5,      6]
            # contenido -> [none, clave, none, Clave2, none, clave3, none]
            #              [:1]  + ClaveNueva, none + clave, none, Clave2, none, clave3, none
           # contenido -> [none,                      clave, none, Clave2, none, clave3, none]
            self.contenido = self.contenido[:1] + \
                [Clave(clave, data), pagina] + self.contenido[1:]
        else:  # Insertar en medio
            i = 1
            while i < len(self.contenido) and clave > self.contenido[i].clave:
                i += 2
            self.contenido = self.contenido[:i] + \
                [Clave(clave, data), pagina] + self.contenido[i:]
        if len(self.contenido[1::2]) >= self.grado:
            return self.dividir()
        return None, None, False

    def dividir(self):

        valorMediana = self.contenido[self.grado]
        nuevaPagina = Pagina(self.contenido[self.grado+1:])
        if self.esHoja():
            nuevaPagina = Pagina([None]+self.contenido[self.grado:])
            nuevaPagina.paginaSiguiente = self.paginaSiguiente
            self.paginaSiguiente = nuevaPagina
        self.contenido = self.contenido[:self.grado]
        return valorMediana, nuevaPagina, True

    def paginaVacia(self):
        return len(self.contenido) == 0

    def esHoja(self):
        esHoja = True
        i = 0
        while i < len(self.contenido):
            esHoja &= self.contenido[i] == None
            i += 2
        return esHoja

     # paginaPadre => pagina anterior
    # pagina => pagina actual
    # CLAVE -> clave que estamos buscando eliminar
    def eliminar(self, clave, paginaPadre=None, pagina=None):
        if paginaPadre == None:
            self.seElimino = False
#========================================== BLOQUE 1 ===============================================        
# Verifica si la CLAVE es mayor a la ultima clave de la pagina
        if clave > pagina.contenido[-2].clave:  # -> puntador derecha
            if not pagina.esHoja(): # verificamos que no sea una hoja
                # Pagina intermedia
                self.seElimino, esHoja = self.eliminar(clave, pagina, pagina.contenido[-1])  # Recursivo
                der = pagina.contenido[-1]
                izq = pagina.contenido[-3]
                if len(der.contenido[1::2]) < 2: # verificamos que la canitidad de claves sea menor a 2
                  if esHoja: # la pagina de abajo es una hoja
                      # BLOQUE 1.1
                      if len(izq.contenido[1::2]) >= 3: # verificamos que no este llena la pagina 
                          der.contenido = [None, izq.contenido[-2]] + der.contenido
                          izq.contenido = izq.contenido[:-2]
                          pagina.contenido = pagina.contenido[:-2] + [der.contenido[1]] + pagina.contenido[-1:]
                      # BLOQUE 1.2
                      else: # la pagina a la izquierda no esta llena
                        izq.contenido = izq.contenido + [der.contenido[1], None] # Modificado
                        pagina.contenido = pagina.contenido[:-2]
                  else: # la pagina de abajo es una pagina intermedia
                       # BLOQUE 1.3
                    if len(izq.contenido[1::2]) >= 3: # no hay espacio en la izquierda
                        der.contenido =  [izq.contenido[-1]] + [pagina.contenido[-2]] + der.contenido
                        pagina.contenido = pagina.contenido[:-2] + [izq.contenido[-2]] + pagina.contenido[-1:]
                        izq.contenido = izq.contenido[:-2]
                        # BLOQUE 1.4
                    else:
                      izq.contenido = izq.contenido + [pagina.contenido[- 2]] + der.contenido
                      pagina.contenido = pagina.contenido[:-2]
                return self.seElimino, False
            else:
                # Hoja
                # No Existe el valor, NO PUEDE IRSE A LA DERECHA PORQUE ES NULO
                return self.seElimino, True
#========================================== BLOQUE 2 =============================================== 
        # Verifica que la ultima clave de la pagina sea igual a la CLAVE
        elif pagina.contenido[-2].clave == clave:
            self.seElimino = True
            if not pagina.esHoja():
                # Pagina intermedia
                self.seElimino, esHoja = self.eliminar(clave, pagina, pagina.contenido[-1])  # RECURSIVIDAD
                der = pagina.contenido[-1]
                izq = pagina.contenido[-3]
                if len(der.contenido[1::2]) < 2:
                  if esHoja: # La pagina derecha es una hoja
                      # BLOQUE 1.1 == BLOQUE 2.1
                      if len(izq.contenido[1::2]) >= 3: #********************* Probando...
                          der.contenido = [None, izq.contenido[-2]] + der.contenido
                          izq.contenido = izq.contenido[:-2]
                          pagina.contenido = pagina.contenido[:-2] + [der.contenido[1]] + pagina.contenido[-1:]
                      # BLOQUE 1.2 == BLOQUE 2.2
                      else:
                        izq.contenido = izq.contenido + [der.contenido[1], None] # Modificado
                        pagina.contenido = pagina.contenido[:-2]
                  else: # La pagina derecha es una pagina intermedio
                    # BLOQUE 2.3
                    if len(izq.contenido[1::2]) >= 3: # no hay espacio en la izquierda
                        tmp = der
                        ant = tmp
                        while tmp != None:
                            ant = tmp
                            tmp = tmp.contenido[0]
                        der.contenido = [izq.contenido[-1]] + [ant.contenido[1]] + der.contenido 
                        pagina.contenido = pagina.contenido[:-2] + [izq.contenido[-2]] + pagina.contenido[-1:]
                        izq.contenido = izq.contenido[:-2]
                    # BLOQUE 2.4
                    else:
                        tmp = der
                        ant = tmp
                        while tmp != None:
                            ant = tmp
                            tmp = tmp.contenido[0]
                        izq.contenido = izq.contenido + [ant.contenido[1]] + der.contenido
                        pagina.contenido = pagina.contenido[:-2]
                else:
                    if esHoja:
                        pagina.contenido = pagina.contenido[:-2] + [der.contenido[1]] + pagina.contenido[-1:]
                    else:
                        tmp = pagina.contenido[-1]
                        ant = tmp
                        while tmp != None:
                            ant = tmp
                            tmp = tmp.contenido[0]
                        pagina.contenido = pagina.contenido[:-2] + [ant.contenido[1]] + pagina.contenido[-1:]
                return self.seElimino, False
            else:
                # Hoja
                pagina.contenido = pagina.contenido[:-2]  # Eliminó LA CLAVE
                return self.seElimino, True
#========================================== BLOQUE 3 =============================================== 
        # Verificamos que la CLAVE este al inicio o en medio de la pagina                   
        else:
            indice = 1
            for x in pagina.contenido[1::2]:
                if clave < x.clave:  # apuntador izq
                    if not self.esHoja():
                        # Pagina intemedia
                        
                        self.seElimino, esHoja = self.eliminar(clave, pagina, pagina.contenido[indice - 1])  # R
                        
                        # |izq | 10 | der | 12 | |
                        izq = pagina.contenido[indice - 1]
                        der = pagina.contenido[indice + 1]
                        if len(izq.contenido[1::2]) < 2:
                            # || 8 || 10 || 11 ||
                            if esHoja:
                                #BLOQUE 3.1 Si la clave está al principio
                                if indice == 1:
                                    #BLOQUE 3.1.1
                                    if len(der.contenido[1::2]) >= 3: # no hay espacio en la derecha (hoja)
                                        izq.contenido = izq.contenido + [der.contenido[1], None]
                                        der.contenido = der.contenido[2:]
                                        pagina.contenido = pagina.contenido[:1] + [der.contenido[1]] + pagina.contenido[2:]
                                    #BLOQUE 3.1.2
                                    else:
                                        der.contenido = izq.contenido[:2] + der.contenido
                                        pagina.contenido = pagina.contenido[indice+1:]
                                #BLOQUE 3.2 si la clave está en medio   
                                else: # el indice no es igual a 1
                                    izq2 = pagina.contenido[indice - 3]
                                    # BLOQUE 3.2.1 Presto el derecho
                                    if len(der.contenido[1::2]) >= 3: # hay espacio en la derecha (hoja)
                                        izq.contenido = izq.contenido + [der.contenido[1], None]
                                        der.contenido = [None] + der.contenido[3:]
                                        pagina.contenido = pagina.contenido[:indice-2] + [izq.contenido[1], pagina.contenido[indice - 1], der.contenido[1]] + pagina.contenido[indice+1:]
                                    # BLOQUE 3.2.2 presta el izquierdo
                                    elif len(izq.contenido[1::2]) >= 3: # hay espacio en la izquierda (hoja) **
                                        izq.contenido = [None, izq2.contenido[-2]] + izq.contenido
                                        izq2.contenido = izq2.contenido[:-2]
                                        pagina.contenido = pagina.contenido[:indice-2] + [izq.contenido[1]] + pagina.contenido[indice-1:]
                                    # BLOQUE 3.2.3 se une a la izquierda
                                    else:
                                        izq2.contenido = izq2.contenido +  [izq.contenido[1], None] # Modificado
                                        pagina.contenido = pagina.contenido[:indice - 2] + pagina.contenido[indice:]           
                            else: #si es Pagina intermedia
                                #Bloque 3.3 
                                if indice == 1: # Si esta al principio
                                    #Bloque 3.3.1
                                    if len(der.contenido[1::2]) >= 3: # hay espacio en la derecha
                                        izq.contenido = izq.contenido + [pagina.contenido[indice]] + [der.contenido[0]]
                                        pagina.contenido = pagina.contenido[:indice] + [der.contenido[1]] + pagina.contenido[indice+1:]
                                        der.contenido = der.contenido[2:]
                                    #Bloque 3.3.2 #Se une
                                    else:
                                        der.contenido = izq.contenido + [pagina.contenido[1]] + der.contenido
                                        pagina.contenido = pagina.contenido[indice+1:]
                                #Bloque 3.4 #Si está en medio
                                else:   
                                    izq2 = pagina.contenido[indice - 3]
                                    # BLQUE 3.4.1 Le presta el de la derecha
                                    if len(der.contenido[1::2]) >= 3: # hay espacio en la derecha
                                        izq.contenido = izq.contenido + [pagina.contenido[indice]] + [der.contenido[0]]
                                        pagina.contenido = pagina.contenido[:indice] + [der.contenido[1]] + pagina.contenido[indice+1:]
                                        der.contenido = der.contenido[2:]
                                    #BLOQUE 3.4.2 Le presta el de la izquierda
                                    elif len(izq2.contenido[1::2]) >= 3: # hay espacio en la izquierda
                                        izq.contenido = [izq2.contenido[-1]] + [pagina.contenido[indice-2]] +  izq.contenido
                                        pagina.contenido = pagina.contenido[:indice-2] + [izq2.contenido[-2]] + pagina.contenido[indice-1:]
                                        izq2.contenido = izq2.contenido[:-2]
                                    #BLOQUE 3.4.3 se une a la izquierda
                                    else: # si hay espacio en la izq
                                        izq2.contenido = izq2.contenido + [pagina.contenido[indice - 2]] + izq.contenido
                                        pagina.contenido = pagina.contenido[:indice - 2] + pagina.contenido[indice:]
                        return self.seElimino, False
                    else:
                        # Hoja
                        # No Existe el valor
                        return self.seElimino, True

               #BLOQUE 3.5 es cuando la CLAVE es igual a la clave de la posicion actual
                elif clave == x.clave:  # apuntador der
                    self.seElimino = True
                    if not pagina.esHoja():
                        # Pagina intemedia
                        self.seElimino, esHoja = self.eliminar(clave, pagina, pagina.contenido[indice + 1])  # R
                        der = pagina.contenido[indice + 1]
                        izq = pagina.contenido[indice - 1]

                        if len(der.contenido[1::2]) < 2: #Si la pagina tiene menos de dos claves
                          if esHoja: #La pagina derecha es una hoja
                            der2 = pagina.contenido[indice + 3] 
                            #BLOQUE 3.5.1 La derecha presta
                            if len(der2.contenido[1::2]) >= 3: #hay espacio en la derecha (hoja)
                                der.contenido = der.contenido + [der2.contenido[1], None]
                                der2.contenido = der2.contenido[2:]
                                pagina.contenido = pagina.contenido[:indice] + [der.contenido[1], pagina.contenido[indice+1], der2.contenido[1]] + pagina.contenido[indice+3:]
                            #BLOQUE 3.5.2 La izquierda presta
                            elif len(izq.contenido[1::2]) >= 3: # hay espacio en la izquierda (hoja) **
                                der.contenido = [None, izq.contenido[-2]] + der.contenido
                                izq.contenido = izq.contenido[:-2]
                                pagina.contenido = pagina.contenido[:indice] + [der.contenido[1]] + pagina.contenido[indice+1:]
                            #BLOQUE 3.5.3 se unio a la izquierda
                            else:
                                izq.contenido = izq.contenido + [der.contenido[1], None] # Modificado
                                pagina.contenido = pagina.contenido[:indice] + pagina.contenido[indice+2:]
                          else:# Si es Pagina intermedia
                            der2 = pagina.contenido[indice + 3]
                            #BLOQUE 3.5.4 La derecha presta
                            if len(der2.contenido[1::2]) >= 3:
                                #**********************************
                                tmp = pagina.contenido[indice + 1] # der
                                ant = tmp
                                while tmp != None:
                                    ant = tmp
                                    tmp = tmp.contenido[0]

                                tmp1 = pagina.contenido[indice + 3] # der2
                                ant1 = tmp1
                                while tmp1 != None:
                                    ant1 = tmp1
                                    tmp1 = tmp1.contenido[0]
                                #**********************************
                                der.contenido = der.contenido + [ant1.contenido[1]] + [der2.contenido[0]]
                                pagina.contenido = pagina.contenido[:indice] + [ant.contenido[1], pagina.contenido[indice + 1], der2.contenido[1]] + pagina.contenido[indice+3:]
                                der2.contenido = der2.contenido[2:]
                            # BLOQUE 3.5.5 La derecha presta
                            elif len(izq.contenido[1::2]) >= 3: # hay espacio en la izquierda
                                #**********************************
                                tmp = pagina.contenido[indice + 1]
                                ant = tmp
                                while tmp != None:
                                    ant = tmp
                                    tmp = tmp.contenido[0]
                                #**********************************
                                der.contenido = [izq.contenido[-1]] + [ant.contenido[1]] + der.contenido 
                                pagina.contenido = pagina.contenido[:indice] + [izq.contenido[-2]] + pagina.contenido[indice+1:]
                                izq.contenido = izq.contenido[:-2]
                            #BLOQUE 3.5.6 se une a la izquierda
                            else:
                                #**********************************
                                tmp = pagina.contenido[indice + 1]
                                ant = tmp
                                while tmp != None:
                                    ant = tmp
                                    tmp = tmp.contenido[0]
                                #**********************************
                                izq.contenido = izq.contenido + [ant.contenido[1]] + der.contenido
                                pagina.contenido = pagina.contenido[:indice] + pagina.contenido[indice+2:]
                        else:
                            # entendemos que encontramos una referencia a la clave que queremos eliminar
                            # BLOQUE 3.5.7 modificar referencia de lado derecho en la pagina
                            if esHoja:
                                pagina.contenido = pagina.contenido[:indice] + [der.contenido[1]] + pagina.contenido[indice + 1:]
                            # BLOQUE 3.5.8 modificar referencia de lado derecho más izquierda en la pagina
                            else:
                                tmp = pagina.contenido[indice + 1]
                                ant = tmp
                                while tmp != None:
                                    ant = tmp
                                    tmp = tmp.contenido[0]
                                pagina.contenido = pagina.contenido[:indice] + [ant.contenido[1]] + pagina.contenido[indice + 1:]
                        return self.seElimino, False
                    else:
                        #Bloque 3.5.9
                        # Hoja
                        pagina.contenido = pagina.contenido[:indice] + pagina.contenido[indice+2:] # Eliminó
                        return self.seElimino, True
                indice += 2
        return self.seElimino, False
