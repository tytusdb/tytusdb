import hashlib


class Vertex:
    def __init__(self, data):
        self.__data = data
        self.__adjacency_list = list()
        self.__hash = self.__generate__hash(data)

    def set_data(self, data):
        self.__data = data
        self.__hash = self.__generate__hash(data)

    def get_data(self):
        return self.__data

    def set__adjacency_list(self, new_list):
        self.__adjacency_list = new_list

    def get__adjacency_list(self):
        return self.__adjacency_list

    def get_hash(self):
        return self.__hash

    def __generate__hash(self, data):
        return hashlib.md5(str(data).encode()).hexdigest()


class Graph:
    def __init__(self):
        self.__vertex_list = list()
        self.__string = ""

    def add_vertex(self, value):
        data: Vertex = self.__exist(value)
        if data: return 1
        new_vertex = Vertex(value)
        self.__vertex_list.append(new_vertex)
        # print("Se agrego")
        return 0

    def __exist(self, value):
        for vertex in self.__vertex_list:
            if value == vertex.get_data():
                return vertex
        return None

    def join(self, a, b):
        origin: Vertex = self.__exist(a)
        destiny: Vertex = self.__exist(b)
        if origin is None or destiny is None: return 1
        origin.get__adjacency_list().append(destiny)
        # destiny.get__adjacency_list().append(origin)

    # Recorrido por profundiad
    def bfb(self):
        list_aux = list()
        for a in self.__vertex_list:
            if list_aux.__contains__(a) is False:
                list_aux.append(a)

            for b in a.get__adjacency_list():
                if list_aux.__contains__(b) is False:
                    list_aux.append(b)

        while len(list_aux) != 0:
            print(list_aux.pop().get_data())

    def graficar(self):
        list_aux = list()
        self.__string = "digraph G{\n"
        self.__string += "node[shape=\"circle\"]\n"
        for index in range(len(self.__vertex_list)):
            temp: Vertex = self.__vertex_list[index]
            if list_aux.__contains__(temp) is False:
                list_aux.append(temp)
                self.__string += f"node{temp.get_hash()} [label = \"{temp.get_data()}\" ]\n"

            for x in range(len(temp.get__adjacency_list())):
                self.__string += f"node{temp.get_hash()} -> node{temp.get__adjacency_list()[x].get_hash()} \n"
                if list_aux.__contains__(temp.get__adjacency_list()[x]) is False:
                    list_aux.append(temp.get__adjacency_list()[x])
                    self.__string += f"node{temp.get__adjacency_list()[x].get_hash()} [label " \
                                     f"=\"{temp.get__adjacency_list()[x].get_data()}\" ]\n "

        self.__string += "}\n"
        #print(self.__string)
        return self.__string

    def graficar2(self):
        list_aux = list()
        self.__string = "digraph G{\n"
        self.__string += "node[shape=\"circle\"]\n"
        for index in range(len(self.__vertex_list)):
            temp: Vertex = self.__vertex_list[index]
            if list_aux.__contains__(temp) is False:
                list_aux.append(temp)
                self.__string += f"node{temp.get_data()} [label = \"{temp.get_data()}\" ]\n"

            for x in range(len(temp.get__adjacency_list())):
                self.__string += f"node{temp.get_data()} -> node{temp.get__adjacency_list()[x].get_data()} \n"
                if list_aux.__contains__(temp.get__adjacency_list()[x]) is False:
                    list_aux.append(temp.get__adjacency_list()[x])
                    self.__string += f"node{temp.get__adjacency_list()[x].get_data()} [label " \
                                     f"=\"{temp.get__adjacency_list()[x].get_data()}\" ]\n "

        self.__string += "}\n"
        #print(self.__string)
        return self.__string


