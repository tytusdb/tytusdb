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
        self.height = 0
    
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

    def __right_shift_sp(self, node_id, page):
        if not page.leaf:
            if node_id < page.left_node.node_id:
                code = self.__right_shift_sp(node_id, page.left)
            elif page.right_node != None:
                if node_id >= page.left_node.node_id and node_id < page.right_node.node_id:
                    code = self.__right_shift_sp(node_id, page.mid)
                if node_id >= page.right_node.node_id:
                    code = self.__right_shift_sp(node_id, page.right)
            else:
                code = self.__right_shift_sp(node_id, page.mid)
            self.update_level(page.level)
            return code
        else:
            if page.left_node != None and page.left_node.node_id == node_id:
                if page.right_sister != None:
                    code = self.__right_shift_sp(node_id, page.right_sister)
                    if code == 0:
                        page.left_node = None
                        self.update_level(page.level)
                        return 0
                    else:
                        return 1
                else:
                    return 1
            elif page.left_node != None and page.left_node.node_id != node_id:
                if page.right_sister != None:
                    code = self.__right_shift_sp(node_id, page.right_sister)
                    if code == 0:
                        page.left_node = page.left_sister.left_node
                        return 0
                    else:
                        return 1
                else:
                    return 1
            elif page.empty:
                page.left_node = page.left_sister.left_node
                return 0
            else:
                return 1

    # Mueve una posición a la derecha a la página que contenga el nodo
    # con el node_id indicado
    def right_shift_sp(self, node_id):
        return self.__right_shift_sp(node_id, self.root)

    def __left_shift_sp(self, node_id, page):
        if not page.leaf:
            if node_id < page.left_node.node_id:
                code = self.__left_shift_sp(node_id, page.left)
            elif page.right_node != None:
                if node_id >= page.left_node.node_id and node_id < page.right_node.node_id:
                    code = self.__left_shift_sp(node_id, page.mid)
                if node_id >= page.right_node.node_id:
                    code = self.__left_shift_sp(node_id, page.right)
            else:
                code = self.__left_shift_sp(node_id, page.mid)
            self.update_level(page.level)
            return code
        else:
            is_left_node = page.left_node != None and page.left_node.node_id == node_id
            is_right_node = page.right_node != None and page.right_node.node_id == node_id
            if is_left_node or is_right_node:
                aux = self.leftmost
                count = 1
                shift = False
                while aux != None:
                    if aux.empty:
                        shift = True
                        if aux.right_sister != None and not aux.right_sister.empty:
                            aux.left_node = aux.right_sister.left_node
                            aux.right_sister.left_node = None
                            aux.right_node = aux.right_sister.right_node
                            aux.right_sister.right_node = None
                        elif aux.right_sister != None and aux.right_sister.empty:
                            if count % 3 != 0:
                                aux.left_node = aux.right_sister.right_sister.left_node
                                aux.right_sister.right_sister.left_node = None
                                aux.right_node = aux.right_sister.right_sister.right_node
                                aux.right_sister.right_sister.right_node = None
                    is_left_node = aux.left_node != None and aux.left_node.node_id == node_id
                    is_right_node = aux.right_node != None and aux.right_node.node_id == node_id
                    if is_left_node or is_right_node:
                        return int(not shift)
                    self.update_level(1)
                    self.update_level(0)
                    aux = aux.right_sister
                    count += 1
                return 1
            else:
                return 1

    # Mueve una posición a la izquierda a la página que contenga el nodo
    # con el node_id indicado
    def left_shift_sp(self, node_id):
        return self.__left_shift_sp(node_id, self.root)

    def __right_shift(self, node_id, page):
        if not page.leaf:
            if node_id < page.left_node.node_id:
                code = self.__right_shift(node_id, page.left)
            elif page.right_node != None:
                if node_id >= page.left_node.node_id and node_id < page.right_node.node_id:
                    code = self.__right_shift(node_id, page.mid)
                if node_id >= page.right_node.node_id:
                    code = self.__right_shift(node_id, page.right)
            else:
                code = self.__right_shift(node_id, page.mid)
            self.update_level(page.level)
            return code
        else:
            is_left_node = page.left_node != None and page.left_node.node_id == node_id
            is_right_node = page.right_node != None and page.right_node.node_id == node_id
            if is_left_node or is_right_node:
                if page.right_sister != None:
                    code = self.__right_shift(node_id, page.right_sister)
                    if code == 0:
                        page.right_sister.left_node = page.right_node
                        page.right_node = None
                        if is_left_node:
                            page.right_node = page.left_node
                            page.left_node = None
                        return 0
                    else:
                        pass
                else:
                    return 1
            else:
                if page.full:
                    code = self.__right_shift(node_id, page.right_sister)
                    if code == 0:
                        page.right_sister.left_node = page.right_node
                        page.right_node = page.left_node
                        page.left_node = None
                    return code
                else:
                    page.right_node = page.left_node
                    page.left_node =  None
                    return 0

    # Mueve una posición a la derecha al nodo con el node_id indicado
    def right_shift(self, node_id):
        return self.__right_shift(node_id, self.root)

    def __left_shift(self, node_id, page):
        if not page.leaf:
            if node_id < page.left_node.node_id:
                code = self.__left_shift(node_id, page.left)
            elif page.right_node != None:
                if node_id >= page.left_node.node_id and node_id < page.right_node.node_id:
                    code = self.__left_shift(node_id, page.mid)
                if node_id >= page.right_node.node_id:
                    code = self.__left_shift(node_id, page.right)
            else:
                code = self.__left_shift(node_id, page.mid)
            self.update_level(page.level)
            return code
        else:
            is_left_node = page.left_node != None and page.left_node.node_id == node_id
            is_right_node = page.right_node != None and page.right_node.node_id == node_id
            if is_left_node or is_right_node:
                aux = self.leftmost
                while aux != None:
                    if aux.empty:
                        aux.left_node = aux.right_sister.left_node
                        aux.right_sister.left_node = None
                        if aux.left_node.node_id == node_id:
                            return 0
                    elif aux.full:
                        if aux.left_node.node_id == node_id or aux.right_node.node_id == node_id:
                            return 0
                    else:
                        aux.right_node = aux.right_sister.left_node
                        aux.right_sister.left_node = None
                        if aux.left_node.node_id == node_id or aux.right_node.node_id == node_id:
                            return 0
                    self.update_level(1)
                    self.update_level(0)
                    aux = aux.right_sister
                return 1
            else:
                return 1

    # Mueve una posición a la izquierda al nodo con el node_id indicado
    def left_shift(self, node_id):
        return self.__left_shift(node_id, self.root)

    # Inserta un nuevo nodo con información en la estructura
    def insert(self, new_node):
        if self.root == None:  # Si la raiz es igual a nula
            # Creamos la pagina
            new_page = Page()
            self.root = new_page
            self.leftmost = self.root
            self.root.leaf = True
            self.root.level = 0
            # Insertar Nodo En Página
            full_page = self.root.full
            self.root.insert(new_node, full_page)
        else: # La Raíz No Es Nula

            #trabajar Solo la raiz
            if self.root.leaf:
                if self.root.full:#esta llena
                    self.procreate()
                    self.insert(new_node,new_raiz)
                else: #no esta llena
                    self.root.insert(new_node,new_raiz)


            else: #tiene hijos la raiz

                #la pagina actual no es una hoja
                if new_raiz.leaf == False:
                    #verifico nivel
                    lleno_nivel = self.full_level(new_raiz.level) 

                    if lleno_nivel == 0: #nivel no lleno

                        #Rotaciones Especiales
                        
                        #Verificar Si Página actual Esta Llena
                        #La pagina esta llena
                        if new_raiz.full:   #La Pagina esta Llena
                            full_page = new_raiz.full
                            insert_return = new_raiz.insert(new_node,full_page)

                            if inset_return == 0: #Se inserto correctamente
                                pass
                            elif insert_return == 1: #Ocurrio Un Problema
                                pass
                            elif insert_return == 2: #Ya Existe un Nodo con el # ID:
                                pass
                            elif insert_return == 3: #La Pagina esta llena pero la estructura arborea no (es posible un Corrimiento)
                            
                                lleno_nivel = self.full_level(new_raiz.level) #verifico nivel
                                if lleno_nivel == 0: #nivel no lleno
                                    #error
                                    pass

                                elif lleno_nivel == 1:#nivel lleno

                                    #Se es menor al de la izquierda
                                    if new_node.node_id < new_raiz.left_node.node_id:
                                        if new_node.node_id < new_raiz.left.left_node.node_id:#nodo menor al menor hijo izq
                                            aux = new_node.node_id
                                            new_node.node_id = new_raiz.left.left_node.node_id#el entrante sera el menor del hijo izq
                                            new_raiz.left.left_node.node_id = aux #el menor del hijo izq sera el que iba a entrar antes
                                            corrio = self.left_shift_sp(new_raiz.left.left_node.node_id) # corro y mando la pagina con el menor del hijo izq
                                            if corrio  == 0:#corrio nodos a la izq
                                                new_raiz.left.left_node = new_node #igualo y ya
                                                self.update_level(1)
                                                self.update_level(0)

                                            elif corrio == 1:#no corrio a la izq
                                                if new_node.node_id < new_raiz.left_node.node_id: #manda a correr hijo izq
                                                    corro = self.right_shift_sp(new_raiz.left.left_node.node_id) # corro y mando la pagina con el menor del hijo izq
                                                    if corro == 0:
                                                        new_raiz.left.left_node = new_node #igualo y ya
                                                        self.update_level(1)
                                                        self.update_level(0)                                                        

                                                    elif corro == 1:
                                                        #rotacion ramas
                                                        pass

                                                elif new_node.node_id > new_raiz.left_node.node_id: #manda correr hijo medio
                                                    corro = self.right_shift_sp(new_raiz.mid.left_node.node_id) # corro y mando la pagina con el menor del hijo medio
                                                    if corro == 0:
                                                        new_raiz.mind.left_node = new_node #igualo y ya
                                                        self.update_level(1)
                                                        self.update_level(0)                                                    

                                                    elif corro == 1:
                                                        #rotacion ramas
                                                        pass

                                        elif new_node.node_id > new_raiz.left.left_node.node_id:#es mayor al menor hijo izq
                                            corrio = self.left_shift_sp(new_raiz.left.left_node.node_id) # corro y mando la pagina con el menor del hijo izq
                                            if corrio == 0: #corrio a la izqr
                                                new_raiz.left.left_node = new_node #corro y ya
                                                self.update_level(1)
                                                self.update_level(0)                                                
                                            elif corrio == 1: #no puedo correr a la izqr
                                                aux = new_node.node_id
                                                new_node.node_id = new_raiz.left.left_node.node_id
                                                new_raiz.left.left_node.node_id = aux 
                                                corro = self.right_shift_sp(new_raiz.left.left_node.node_id) 
                                                if corro == 0:
                                                    new_raiz.left.left_node = new_node #corro y ya
                                                    self.update_level(1)
                                                    self.update_level(0)
                                                elif corro == 1:
                                                    #error
                                                    pass                                                                                      

                                    #Se va por el medio
                                    elif new_node.node_id > new_raiz.left_node.node_id and new_node.node_id < new_raiz.right_node.node_id:
                                        corrio = self.left_shift_sp(new_raiz.mid.left_node.node_id) # corro y mando la pagina con el menor del hijo medio
                                        if corrio  == 0:#corrio nodos a la izq
                                            new_raiz.mid.left_node = new_node #corro y ya
                                            self.update_level(1)
                                            self.update_level(0)                                           
                                        elif corrio == 1:#no corrio a la izq
                                            corro = self.right_shift_sp(new_raiz.right.left_node.node_id) # corro y mando la pagina con el menor del hijo izq
                                            if corro == 0:
                                                new_raiz.right.left_node = new_node #corro y ya
                                                self.update_level(1)
                                                self.update_level(0)
                                            elif corro == 1:
                                                #error
                                                pass

                                    #Si es mayor al derecho
                                    elif new_node.node_id > new_raiz.right_node.node_id:
                                        corrio = self.left_shift_sp(new_raiz.right.left_node.node_id) # corro y mando la pagina con el menor del hijo medio
                                        if corrio  == 0:#corrio nodos a la izq
                                            new_raiz.right.left_node = new_node #corro y ya
                                            self.update_level(1)
                                            self.update_level(0)
                                        elif corrio == 1:#no corrio a la izq
                                            corro = self.right_shift_sp(new_raiz.right.right_sister.left_node.node_id) # corro y mando la pagina con el menor del hijo izq
                                            if corro == 0:
                                                new_raiz.right.right_sister.left_node = new_node #corro y ya
                                                self.update_level(1)
                                                self.update_level(0)
                                            elif corro == 1:
                                                #error
                                                pass   
                                  
                            elif insert_return == 4: #si hay posibilidad crear nuevos hijos
                                #DUDA con procreate o desvorde
                                self.root.procreate() #baja los nodos tambien

                                # Busca En Que Página Insetar (Izq o Der)
                                if new_node.node_id < new_raiz.left_node.node_id:
                                    # Se Va Por La izquierda
                                    self.insert(new_node, new_raiz.left)
                                elif new_node.node_id > new_raiz.left_node.node_id:
                                    # Se Va Por La Derecha
                                    self.insert(new_node, new_raiz.right)

                                # Despues De Recursividad Regresa Al Padre Y Actualiza
                                self.update_level(1)
                                self.update_level(0)
                        # La Página No Está Llena
                        else: 
                            if new_raiz.left_node.node_id != None:
                                           
                                if self.full_level(new_raiz.level): # nivel esta lleno, deberia ser si nivel lleno excepto la raiz_actual
                                    #supuesto error
                                    pass
                                else:  # el nivel no esta lleno
                                            
                                    #si es menor 
                                    if new_node.node_id < new_raiz.left_node.node_id:

                                        #Si nodo menor al menor hijo izq
                                        if new_node.node_id < new_raiz.left.left_node.node_id:
                                            aux = new_node.node_id
                                            new_node.node_id = new_raiz.left.left_node.node_id#el entrante sera el menor del hijo izq
                                            new_raiz.left.left_node.node_id = aux #el menor del hijo izq sera el que iba a entrar antes
                                            corrio = self.left_shift_sp(new_raiz.left.left_node.node_id) # corro y mando la pagina con el menor del hijo izq
                                            if corrio  == 0:#corrio nodos a la izq
                                                self.insert(new_node,new_raiz.left)
                                                self.update_level(1)
                                                self.update_level(0)
                                            elif corrio == 1:#no corrio a la izq
                                                #vuelvo nodos como estaban antes , el menor sera el nuevo y el de la izq el valor tenia al principio
                                                aux2 = new_node.node_id
                                                new_node.node_id = new_raiz.left.left_node.node_id
                                                new_raiz.left.left_node.node_id = aux2 #el menor del hijo izq sera el que iba a entrar antes
                                                corro = self.right_shift_sp(new_raiz.left.left_node.node_id) # corro y mando la pagina con el menor del hijo izq
                                                if corro == 0:#inserta 
                                                    self.insert(new_node,new_raiz.left)
                                                    self.update_level(1)
                                                    self.update_level(0)                                                    

                                                elif corro == 1:
                                                    #error
                                                    pass
                                        #es mayor al nodo izq
                                        elif new_node.node_id > new_raiz.left.left_node.node_id:
                                            corrio = self.left_shift_sp(new_raiz.left.left_node.node_id) 
                                            if corrio  == 0:#corrio nodos a la izq
                                                new_raiz.left.left_node = new_node #igualo y ya
                                                self.update_level(1)
                                                self.update_level(0)
                                            elif corrio == 1:#no corrio a la izq
                                                
                                                corro = self.right_shift_sp(new_raiz.mid.left_node.node_id) 
                                                if corro == 0:#inserta 
                                                    new_raiz.mid.left_node = new_node #solo igualo
                                                    self.update_level(1)
                                                    self.update_level(0)
                                                elif corro == 1: #no inserta
                                                    #error
                                                    pass

                                    #si es mayor
                                    elif new_node.node_id > new_raiz.left_node.node_id:
                                        #llamo correr izq, mando rama media
                                        correr = self.left_shift_sp(new_raiz.mid.left_node.node_id)
                                        if correr == 0:
                                            new_raiz.mid.left_node = new_node#igualo y ya
                                            self.update_level(1)
                                            self.update_level(0)
                                        elif correr == 1: #caso este vacio la derecha
                                            new_raiz.right.insert(new_node,False)
                                            self.update_level(1)
                                            self.update_level(0)

                                
                    elif lleno_nivel == 1:#nivel lleno

                        #Si es menor al de la izquierda
                        if new_node.node_id < new_raiz.left_node.node_id:
                            self.insert(new_node,new_raiz.left)
                        #si esta ente los 2 nodos
                        elif new_node.node_id > new_raiz.left_node.node_id and new_node.node_id < new_raiz.right_node.node_id:
                            self.insert(new_node,new_raiz.mid)

                        #si es mayor al nodo derecho
                        elif new_node.node_id > new_raiz.right_node.node_id:
                            self.insert(new_node,new_raiz.right)

                    elif lleno_nivel == 2:#no existe el nivel indicado
                        pass

                #la pagina actual es una hoja
                elif new_raiz.leaf == True:
                    lleno_nivel = self.full_level(new_raiz.level) 
                    if lleno_nivel == 0: #nivel no lleno
                        if new_raiz.full: # la pagina esta llena

                            #nuevo nodo menor a izq
                            if new_node.node_id < new_raiz.left_node.node_id:
                                corrio = self.right_shift(new_raiz.left_node.node_id) # corro 
                                if corrio  == 0:#corrio nodos a la der
                                    new_raiz.left_node = new_node#solo corro
                                    self.update_level(1)
                                    self.update_level(0)
                                elif corrio == 1:
                                    #error
                                    pass
                                       
                            #nuevo nodo esta entre los nodos
                            elif new_node.node_id > new_raiz.left_node.node_id and new_node.node_id < new_raiz.right_node.node_id:
                                corrio = self.right_shift(new_raiz.right_node.node_id) # corro
                                if corrio  == 0:#corrio nodos a la der
                                    new_raiz.right_node = new_node #corro y ya
                                    self.update_level(1)
                                    self.update_level(0)
                                elif corrio == 1: 
                                    #error
                                    pass   

                            #nuevo nodo mayor a der
                            elif  new_node.node_id > new_raiz.right_node.node_id:
                                aux = new_node.node_id
                                new_node.node_id = new_raiz.right_node.node_id#el entrante sera el menor del hijo izq
                                new_raiz.right_node.node_id = aux #el menor del hijo izq sera el que iba a entrar antes
                                corrio = self.right_shift(new_raiz.right_node.node_id)
                                if corrio == 0:
                                    new_raiz.right_node = new_node #corro y ya
                                    self.update_level(1)
                                    self.update_level(0)
                                elif corrio == 1:
                                    #error
                                    pass    

                        else: # la pagina no esta llena, debe tener minimo 1 nodo 
                            if new_node.node_id < new_raiz.left_node.node_id:
                                aux = new_node.node_id
                                new_node.node_id = new_raiz.left_node.node_id
                                new_raiz.left_node.node_id = aux 
                                corrio = self.left_shift(new_raiz.left_node.node_id)
                                if corrio == 0:
                                    new_raiz.left_node = new_node #corro y ya
                                    self.update_level(1)
                                    self.update_level(0)
                                elif corrio == 1:
                                    aux = new_node.node_id
                                    new_node.node_id = new_raiz.left_node.node_id
                                    new_raiz.left_node.node_id = aux
                                    #se corre a la derecha
                                    corro = self.right_shift(new_raiz.left_node.node_id) 
                                    if corro == 0:
                                        new_raiz.left_node = new_node#corro y ya
                                        self.update_level(1)
                                        self.update_level(0)
                                    elif corro == 1:
                                        pass
                            #si el actual es mayor
                            elif new_node.node_id > new_raiz.left_node.node_id:
                                corrio = self.left_shift(new_raiz.left_node.node_id)
                                if corrio == 0:
                                    new_raiz.left_node = new_node
                                    self.update_level(1)
                                    self.update_level(0)
                                elif corrio == 1:
                                    #cambio indices nodo actual.izq y nuevo nodo
                                    aux = new_node.node_id
                                    new_node.node_id = new_raiz.left_node.node_id
                                    new_raiz.left_node.node_id = aux
                                    corro = self.right_shift(new_raiz.left_node.node_id)
                                    if corro == 0:
                                        new_raiz.left_node = new_node
                                        self.update_level(1)
                                        self.update_level(0)
                                    elif corro == 1:
                                        pass  

                    elif lleno_nivel == 1: #nivel lleno
                        #procreate o
                        #desvorde
                        if raiz_actual.level == 2:
                            #desvorde
                            pass
                        else:
                            #procreate
                            pass
                    elif lleno_nivel == 2: #no existe el nivel indicado
                        pass

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
