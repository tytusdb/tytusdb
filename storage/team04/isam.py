# Clase que contiene la definición de los nodos que almacenarán
# la información dentro de la estructura.
class Node:
    def __init__(self, info):
        self.node_id = str(info[0])
        self.secret_pk = "0"
        self.primary_keys = []
        self.columns = len(info)
        self.info = info
    
    def draw(self, name="graph", show=False):
        pass

class Page:
    def __init__(self):
        self.level = 0
        self.leaf = False
        self.overflow = False
        self.left = None
        self.mid = None
        self.right = None
        self.left_node = None
        self.right_node = None
        self.next_page = None
        self.left_sister = None
        self.right_sister = None
        self.overflow_page = None

    # Indica si la página está vacía o no
    @property
    def empty(self):
        if self.left_node == None and self.right_node == None:
            return True
        else:
            return False

    # Indica si una página tiene ocupados ambos slots
    @property
    def full(self):
        if self.left_node == None or self.right_node == None:
            return False
        else:
            return True

    # Devuelve la página hijo más a la derecha de una página
    # si la página no tiene hijos, devuelve la página misma
    def rightmost(self):
        if self.right != None:
            return self.right.rightmost()
        else:
            return self

    # Devuelve la página hijo más a la izquierda de una página
    # si la página no tiene hijos, devuelve la página misma
    def leftmost(self):
        if self.left != None:
            return self.left.leftmost()
        else:
            return self

    # Inserta un nodo en la página
    def insert(self, new_node, full_tree):
        same_left_node = self.left_node != None and self.left_node.node_id == new_node.node_id
        same_right_node = self.right_node != None and self.right_node.node_id == new_node.node_id
        if same_left_node or same_right_node:
            # Ya está almacenado un nodo con ese id
            return 2
        elif self.left_node == None:
            # Si el slot izquierdo de la página está vacío
            self.left_node = new_node
            return 0
        elif self.right_node == None:
            # Si el slot derecho de la página está vacío
            if new_node.node_id > self.left_node.node_id:
                self.right_node = new_node
            else:
                self.right_node = self.left_node
                self.left_node = new_node
            return 0
        elif self.level < 2:
            # La página está llena pero aún queda espacio
            if not full_tree:
                return 3
            else:
                return 4
        elif not full_tree:
            return 3
        elif self.level == 2 and (new_node.node_id > self.right_node.node_id or new_node.node_id < self.left_node.node_id):
            if new_node.node_id > self.right_node.node_id:
                aux = self.right_node
                self.right_node = new_node
                self.insert(aux, full_tree)
            elif new_node.node_id < self.left_node.node_id:
                aux = self.left_node
                self.left_node = new_node
                self.insert(aux, full_tree)
        elif self.overflow_page == None:
            # Si la página ya está llena y no tiene página de overflow
            new_page = Page()
            new_page.level = self.level + 1
            new_page.overflow = True
            new_page.insert(new_node, full_tree)
            new_page.next_page = self.next_page
            self.next_page = new_page
            self.overflow_page = new_page
            return 0
        elif self.overflow_page != None:
            # Si la página ya está llena y tiene una página de overflow
            return self.overflow_page.insert(new_node, full_tree)

    # Devuelve el nodo con el id más bajo de entre la página y sus
    # páginas de desborde (en caso de tenerlas)
    def lowest(self):
        aux = self
        temp = self.left_node if self.left_node != None else self.right_node
        while aux != None:
            if aux.left_node != None and aux.left_node.node_id < temp.node_id:
                temp = aux.left_node
            if aux.right_node != None and aux.right_node.node_id < temp.node_id:
                temp = aux.right_node
            aux = aux.overflow_page
        return temp

    # Devuelve el nodo con el id más alto de entre la página y sus
    # páginas de desborde (en caso de tenerlas)
    def highest(self):
        aux = self
        temp = self.left_node if self.left_node != None else self.right_node
        while aux != None:
            if aux.left_node != None and aux.left_node.node_id > temp.node_id:
                temp = aux.left_node
            if aux.right_node != None and aux.right_node.node_id > temp.node_id:
                temp = aux.right_node
            aux = aux.overflow_page
        return temp

    # Extrae uno de los nodos de la página dándole prioridad al de la izquierda
    def __extract(self):
        if self.left_node != None:
            # Devolver el nodo izquierdo
            aux = self.left_node
            self.left_node = self.right_node
            self.right_node = aux
            self.delete(self.right_node.node_id)
            return aux
        elif self.right_node != None:
            # Devolver el nodo derecho
            aux = self.right_node
            self.delete(self.right_node.node_id)
            return aux

    # Elimina la página de desborde en caso de estar vacía
    def __clean_overflow(self):
        if self.overflow_page != None and self.overflow_page.empty:
            self.next_page = self.overflow_page.next_page
            self.overflow_page = None

    # Busca el nodo con el id especificado entre la página y sus
    # páginas de desborde (en caso de tenerlas) y lo elimina de la
    # estructura
    def delete(self, node_id):
        if self.left_node != None and self.left_node.node_id == node_id:
            if self.leaf:
                # Eliminar nodo de página hoja
                self.left_node = None
                # Obtener el nodo con el id más bajo
                temp = self.lowest()
                if temp != None and temp.node_id == self.right_node.node_id:
                    # El nodo con el id más pequeño es el derecho de la página hoja
                    self.left_node = self.right_node
                    if self.overflow_page != None:
                        self.right_node = self.overflow_page.highest()
                        self.overflow_page.delete(self.right_node.node_id)
                    else:
                        self.right_node = None
                else:
                    # El nodo con el id más pequeño es de una página de desborde
                    if self.overflow_page != None:
                        self.overflow_page.delete(temp.node_id)
                    self.left_node = temp
            else:
                # Eliminar nodo de página de desborde
                # Eliminar nodo izquierdo de la página
                self.left_node = self.right_node
                if self.overflow_page != None:
                    # Sustituir nodo eliminado
                    self.right_node = self.overflow_page.__extract()
                    if self.right_node.node_id < self.left_node.node_id:
                        aux = self.left_node
                        self.left_node = self.right_node
                        self.right_node = aux
                else:
                    # Dejar espacio vacío
                    self.right_node = None
            self.__clean_overflow()
            return 0
        elif self.right_node != None and self.right_node.node_id == node_id:
            if self.leaf:
                # Eliminar nodo de página hoja
                self.right_node = None
                # Obtener el nodo con el id más alto
                temp = self.highest()
                if temp != None and temp.node_id == self.left_node.node_id:
                    # El nodo con el id más alto es el izquierdo de la página hoja
                    if self.overflow_page != None:
                        self.right_node = self.left_node
                        self.left_node = self.overflow_page.lowest()
                    else:
                        self.right_node = None
                else:
                    # El nodo con el id más alto es de una página de desborde
                    if self.overflow_page != None:
                        self.overflow_page.delete(temp.node_id)
                    self.right_node = temp
            else:
                # Eliminar nodo de página de desborde
                # Eliminar nodo derecho de la página
                if self.overflow_page != None:
                    # Sustituir nodo eliminado
                    self.right_node = self.overflow_page.__extract()
                    if self.right_node.node_id < self.left_node.node_id:
                        aux = self.left_node
                        self.left_node = self.right_node
                        self.right_node = aux
                else:
                    # Dejar espacio vacío
                    self.right_node = None
            self.__clean_overflow()
            return 0
        elif self.overflow_page != None:
            # Eliminar nodo de la página de desborde
            code = self.overflow_page.delete(node_id)
            self.__clean_overflow()
            return code
        else:
            # No se encontró ningún nodo con ese id
            return 2

    # Busca el nodo con el id especificado
    def search(self, node_id):
        pass

    # Busca el nodo con el id del nodo especificado y lo sustituye
    def modify(self, edited_node):
        pass

    # Procrea un nuevo nivel de páginas hijo
    def procreate(self):
        code = 1
        if self.leaf and self.left == self.mid == self.right == None:
            self.leaf = False
            self.left = Page()
            self.mid = Page()
            self.right = Page()
            self.left.leaf = True
            self.mid.leaf = True
            self.right.leaf = True
            self.left.level = self.level + 1
            self.mid.level = self.level + 1
            self.right.level = self.level + 1
            self.left.left_node = self.left_node
            self.mid.left_node = self.right_node
            self.left_node = self.right_node
            self.right_node = None
            self.left.next_page = self.mid
            self.mid.next_page = self.right
            self.next_page = None
            self.left.right_sister = self.mid
            self.mid.right_sister = self.right
            self.right.left_sister = self.mid
            self.mid.left_sister = self.left
            code = 0
        else:
            self.left.procreate()
            self.mid.procreate()
            self.right.procreate()
            lft_rightmost = self.left.rightmost()
            mid_rightmost = self.mid.rightmost()
            rgt_leftmost = self.right.leftmost()
            mid_leftmost = self.mid.leftmost()
            lft_rightmost.next_page = mid_leftmost
            mid_rightmost.next_page = rgt_leftmost
            lft_rightmost.right_sister = mid_leftmost
            mid_rightmost.right_sister = rgt_leftmost
            rgt_leftmost.left_sister = mid_rightmost
            mid_leftmost.left_sister =  lft_rightmost
            code = 0
        return code

# Clase que contiene la definicón de la estructura de datos ISAM
class Isam:
    def __init__(self):
        self.root = None
        self.leftmost = None
        self.height = None
    
    # Indica si la parte arborea de la estructura ya está llena
    # (Se encuentra llena cuando todas las páginas están llenas)
    @property
    def full(self):
        children = self.root.count_children()
        expected_children = (3**self.height)*2
        return True if children == expected_children else False

    def __full_level(self, level, page):
        if page.level == level:
            result = page.full
            aux = page
            while aux != None:
                result = result and aux.full
                aux = aux.right_sister
            return int(result)
        else:
            if page.left != None:
                return self.__full_level(level, page.left)
            else:
                return 2

    # Indica si un nivel determinado de la estructura arborea está lleno
    def full_level(self, level):
        return self.__full_level(level, self.root)

    def __update_level(self, level, page):
        if page.level == level:
            aux = page
            while aux != None:
                if aux.mid != None and aux.right != None:
                    aux.left_node = aux.mid.leftmost().left_node
                    aux.right_node = aux.right.leftmost().left_node
                aux = aux.right_sister
            return 0
        else:
            if page.left != None:
                return self.__update_level(level, page.left)
            else:
                return 1

    # Crea un nuevo nivel de páginas hijo para todas las páginas
    # en el último nivel. Aplica sólo cuando el árbol tiene menos de
    # 3 niveles.
    def procreate(self):
        if self.full and self.height < 2:
            if self.root.procreate() == 0:
                self.height += 1
                self.leftmost = self.root.leftmost()
                return 0
            else:
                return 1

    # Actualiza los nodos en todas las páginas del nivel
    def update_level(self, level):
        return self.__update_level(level, self.root)

    # Mueve una posición a la derecha a la página que contenga el nodo
    # con el node_id indicado
    def right_shift_sp(self, node_id):
        pass

    # Mueve una posición a la izquierda a la página que contenga el nodo
    # con el node_id indicado
    def left_shift_sp(self, node_id):
        pass

    # Mueve una posición a la derecha al nodo con el node_id indicado
    def right_shift(self, node_id):
        pass

    # Mueve una posición a la izquierda al nodo con el node_id indicado
    def left_shift(self, node_id):
        pass

    # Inserta un nuevo nodo con información en la estructura
    def insert(self, new_node):
        if self.root == None:  # Si la raiz es igual a nula
            #POR CREAR
        else: # La Raíz No Es Nula

            # Verificar Si Página actual Esta Llena
             #La pagina esta llena
            if new_raiz.full:
                full_page = new_raiz.full
                insert_return = new_raiz.insert(new_node,full_page)

                if inset_return == 0: #Se inserto correctamente
                    pass
                elif insert_return == 1: #Ocurrio Un Problema
                    pass
                elif insert_return == 2: #Ya Existe un Nodo con el # IDEA:
                    pass
                elif insert_return == 3: #La Pagina esta llena pero la estructura arborea no (es posible un Corrimiento)
                    
                    if new_raiz.leaf: # es hoja //FALTA HACER ESTA PARTE
                        code = self.full_level(new_raiz.level) #verifico si el nivel esta lleno
                        if code == 0: #no lleno
                            #Se va por la izquierda
                            if new_node.node_id < new_raiz.node_izq.node_id:
                                self.insert(new_node,new_raiz.left)
                            #Se va por el medio
                            elif new_node.node_id > new_raiz.node_izq.node_id and new_node.node_id < new_raiz.node_der.node_id:
                                self.insert(new_node,new_raiz.mid)
                            #Se va por la Derecha
                            elif new_node.node_id > new_raiz.node_der.node_id:
                                self.insert(new_node, new_raiz.der)

                        elif code == 1: #corrimiento especial , si el nivel esta lleno
                         # rotaciones de hojas

                    else: #la raiz no es una hoja

                       lleno_nivel = self.full_level(new_raiz.level) #verifico nivel
                        if lleno_nivel == 0: #nivel no lleno


                        elif lleno_nivel = 1:#nivel lleno

                            #Se es menor al de la izquierda
                            if new_node.node_id < new_raiz.node_izq.node_id:
                                if new_node.node_id < new_raiz.left.node_izq.node_id:#nodo menor al menor hijo izq
                                    aux = new_node.node_id
                                    new_node.node_id = new_raiz.left.node_izq.node_id#el entrante sera el menor del hijo izq
                                    new_raiz.left.node_izq.node_id = aux #el menor del hijo izq sera el que iba a entrar antes
                                    corrio = left_shift_sp(new_raiz.left.node_izq.node_id) # corro y mando la pagina con el menor del hijo izq
                                    if corrio  == 0:#corrio nodos a la izq
                                        self.insert(new_node,new_raiz.left)
                                        self.update_level(new_raiz.level) #update mando la raiz
                                    elif corrio == 1:#no corrio a la izq
                                        if new_node.node_id < new_raiz.node_izq.node_id: #manda a correr hijo izq
                                            corro = right_shift_sp(new_raiz.left.node_izq.node_id) # corro y mando la pagina con el menor del hijo izq
                                            if corro == 0:
                                                self.insert(new_node,new_raiz.left)
                                                self.update_level(new_raiz.level) #update mando la raiz

                                            elif corro == 1:
                                                #rotacion ramas

                                        elif new_node.node_id > new_raiz.node_izq.node_id: #manda correr hijo medio
                                            corro = right_shift_sp(new_raiz.mid.node_izq.node_id) # corro y mando la pagina con el menor del hijo medio
                                            if corro == 0:
                                                self.insert(new_node,new_raiz.mid)
                                                self.update_level(new_raiz.level) #update mando la raiz

                                            elif corro == 1:
                                                #rotacion ramas

                                elif new_node.node_id > new_raiz.left.node_izq.node_id:
                                    corrio = left_shift_sp(new_raiz.left.node_izq.node_id) # corro y mando la pagina con el menor del hijo izq
                                    self.insert(new_node,new_raiz.left)       
                                    #FALTA CODIGO

                            #Se va por el medio
                            elif new_node.node_id > new_raiz.node_izq.node_id and new_node.node_id < new_raiz.node_der.node_id:
                                corrio = left_shift_sp(new_raiz.mid.node_izq.node_id) # corro y mando la pagina con el menor del hijo medio
                                    if corrio  == 0:#corrio nodos a la izq
                                        self.insert(new_node,new_raiz.mid)
                                        self.update_level(new_raiz.level) #update mando la raiz
                                    elif corrio == 1:#no corrio a la izq
                                        corro = right_shift_sp(new_raiz.right.node_izq.node_id) # corro y mando la pagina con el menor del hijo izq
                                            if corro == 0:
                                                self.insert(new_node,new_raiz.right)
                                                self.update_level(new_raiz.level) #update mando la raiz
                                            elif corro == 1:
                                                #rotacion ramas

                            #Si es mayor al derecho
                            elif new_node.node_id > new_raiz.node_der.node_id:
                                corrio = left_shift_sp(new_raiz.right.node_izq.node_id) # corro y mando la pagina con el menor del hijo medio
                                    if corrio  == 0:#corrio nodos a la izq
                                        self.insert(new_node,new_raiz.right)
                                        self.update_level(new_raiz.level) #update mando la raiz
                                    elif corrio == 1:#no corrio a la izq
                                        corro = right_shift_sp(new_raiz.right.right_sister.node_izq.node_id) # corro y mando la pagina con el menor del hijo izq
                                            if corro == 0:
                                                self.insert(new_node,new_raiz.right.right_sister)
                                                self.update_level(new_raiz.level) #update mando la raiz
                                            elif corro == 1:
                                                #rotacion ramas    
                      
                elif insert_return == 4: #si hay posibilidad crear nuevos hijos
                    #print("insert_return = 4")
                    self.root.procreate() #baja los nodos tambien

                    # Busca En Que Página Insetar (Izq o Der)
                    if new_node.node_id < new_raiz.left_node.node_id:
                        # Se Va Por La izquierda
                        self.insert(new_node, new_raiz.left)
                    elif new_node.node_id > new_raiz.left_node.node_id:
                        # Se Va Por La Derecha
                        self.insert(new_node, new_raiz.right)

                    # Despues De Recursividad Regresa Al Padre Y Actualiza
                    self.update_level(new_raiz.level)
            # La Página No Está Llena TRABAJANDO ACTUALMENTE
            else: 
                if new_raiz.left_node.node_id != None:
                    if new_raiz.leaf: # es una hoja
                                
                    else: #no es una hoja
                        if full_level(new_raiz.level): # nivel esta lleno, deberia ser si nivel lleno excepto la raiz_actual
                            #supuesto error
                        else:  # el nivel no esta lleno
                                    
                                #si es menor 
                            if new_node.node_id < new_raiz.node_izq.node_id:

                                #Si nodo menor al menor hijo izq
                                if new_node.node_id < new_raiz.left.node_izq.node_id:
                                    aux = new_node.node_id
                                    new_node.node_id = new_raiz.left.node_izq.node_id#el entrante sera el menor del hijo izq
                                    new_raiz.left.node_izq.node_id = aux #el menor del hijo izq sera el que iba a entrar antes
                                    corrio = left_shift_sp(new_raiz.left.node_izq.node_id) # corro y mando la pagina con el menor del hijo izq
                                    if corrio  == 0:#corrio nodos a la izq
                                        self.insert(new_node,new_raiz.left)
                                        self.update_level(new_raiz.level) #update mando la raiz
                                    elif corrio == 1:#no corrio a la izq
                                        #vuelvo nodos como estaban antes , el menor sera el nuevo y el de la izq el valor tenia al principio
                                        aux2 = new_node.node_id
                                        new_node.node_id = new_raiz.left.node_izq.node_id
                                        new_raiz.left.node_izq.node_id = aux2 #el menor del hijo izq sera el que iba a entrar antes
                                        corro = right_shift_sp(new_raiz.left.node_izq.node_id) # corro y mando la pagina con el menor del hijo izq
                                        if corro == 0:#inserta 
                                            self.insert(new_node,new_raiz.left)
                                            self.update_level(new_raiz.level) #update mando la raiz

                                        elif corro == 1:
                                            #error
                                            
                                elif new_node.node_id > new_raiz.left.node_izq.node_id:
                                    


                                #si es mayor
                                #si es mayor
                            elif new_node.node_id > new_raiz.node_der.node_id:
                                #llamo correr izq, mando rama media
                                correr = left_shift_sp(new_raiz.mid.node_izq.node_id)
                                if correr == 0:
                                    self.insert(new_node,new.raiz.mid)
                                    self.update_level(new_raiz.level)
                                elif correr == 1:
                                    corro = right_shift_sp(new_raiz.right.node_izq.node_id)
                                    if corro == 0:
                                        self.insert(new_node,new_raiz.right)
                                        self.update_level(new_raiz.level)
                                    elif corro == 1:
                                        #error


    # Retorna el nodo con el id especificado
    def search(self, node_id):
    	pass

    # Busca y elimina el nodo con el id especificado
    def delete(self, node_id):
        pass

    # Busca un nodo dentro de la estructura y lo sustituye con el
    # nodo especificado. Para la búsqueda utiliza el id del nodo
    # especificado en los parametros
    def modify(self, edited_node):
    	pass

    # Muestra la estructura de forma gráfica
    def draw(self, name="graph", show=False):
        pass

    # Devuelve una lista con todos los nodos de la estructura
    def get_all(self):
        pass
