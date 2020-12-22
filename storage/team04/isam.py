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

    # Inserta un nuevo nodo con información en la estructura
    def insert(self, new_node):
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