from analizer_pl import grammar


class BackFill:
    true_list = list()
    false_list = list()

    def __init__(self):
        self.new_lists()

    def new_lists(self):
        v = list()
        f = list()
        self.true_list.append(v)
        self.false_list.append(f)

    def merge_lists(self):
        true_cap, false_cap = list()
        if len(self.true_list) > 1:
            true_cap = list(self.true_list.pop())
            true_cap.extend(list(self.true_list.pop()))
            self.true_list.append(true_cap)
        if len(self.false_list) > 1:
            false_cap = list(self.false_list.pop())
            false_cap.extend(list(self.false_list.pop()))
            self.false_list.append(false_cap)

    def invert(self):
        aux_list = self.true_list
        self.true_list = self.false_list
        self.false_list = aux_list

    def insert_true(self, etiq):
        index = len(self.true_list) - 1
        self.true_list[index].append(etiq)

    def insert_false(self, etiq):
        index = len(self.false_list) - 1
        self.false_list[index].append(etiq)

    def take_out_true_list(self, row):
        ret = ""
        index = len(self.true_list) - 1
        aux = list(self.true_list[index])
        iterator = iter(aux)
        while True:
            try:
                element = next(iterator)
                ret += "\tlabel .etiv" + str(element) + "\n"
                grammar.optimizer_.addLabel(str("etiv" + str(element)), row, True)
            except StopIteration:
                break
        if index == 0:
            self.true_list[index].clear()
        else:
            del self.true_list[index]
        return ret

    def take_out_false_list(self, row):
        ret = ""
        index = len(self.false_list) - 1
        aux = list(self.false_list[index])
        iterator = iter(aux)
        while True:
            try:
                element = next(iterator)
                ret += "\tlabel .etif" + str(element) + "\n"
                grammar.optimizer_.addLabel(str("etif" + str(element)), row, True)
            except StopIteration:
                break
        if index == 0:
            self.false_list[index].clear()
        else:
            del self.false_list[index]
        return ret