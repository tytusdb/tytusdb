
# Linked List implementada para almacenar informacion, pueden usarla o usar un array xD 

class Nodo():
    def __init__(self, Value):
        self.data = Value
        self.next = None

    def get_value(self):
        return self.data


class SingleLinkedList():
    def __init__(self):
        self.head_value = None
        self.count = 0

    def insert_end(self, value):
        new_node = Nodo(value)
        if self.head_value is None:
            self.head_value = new_node
            self.count += 1
            return
        last_value = self.head_value
        while last_value.next:
            last_value = last_value.next
        last_value.next = new_node
        self.count += 1

    def insert_begin(self, value):
        new_node = Nodo(value)
        new_node.next = self.head_value
        self.head_value = new_node
        self.count += 1

    def __len__(self):
        return self.count

    def __getitem__(self, i):
        if i >= len(self):
            raise IndexError('Index out of range')

        current = self.head_value
        for _ in range(i):
            current = current.next
        return current

    def __iter__(self):
        current = self.head_value

        while current:
            yield current
            current = current.next

    def remove_all(self):
        self.head_value = None
        self.count = 0

    def list_print(self):
        print_value = self.head_value.data
        while print_value is not None:
            print(print_value, end='\n')
            print_value = print_value.next
