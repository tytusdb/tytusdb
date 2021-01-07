class Element:
    E_LABEL = 1
    E_GOTO = 2
    E_SCALAR = 3

    def __init__(self):
        self.id = ""
        self.type = -1

    def constructor1(self, id, type) -> None:
        self.id = id
        self.type = type

    def copy(self, copy):
        if copy != None:
            self.id = copy.id
            self.type = copy.type

    def __str__(self):
        if self.id != None:
            return self.id
        return ""