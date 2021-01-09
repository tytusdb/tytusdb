import hashlib
import json
import datetime
import os.path as path
import os


class Block:
    def __init__(self, id_block, data, previous_block, hash):
        self.__id_block = id_block
        self.__data = data
        self.__previous_block = previous_block
        self.__hash = hash
        self.__time = self.__get_time()

    def set_id_block(self, id_block):
        self.__id_block = id_block

    def get_id_block(self):
        return self.__id_block

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_previous_block(self, previous_block):
        self.__previous_block = previous_block

    def get_previous_block(self):
        return self.__previous_block

    def set_hash(self, hash):
        self.__hash = hash

    def get_hash(self):
        return self.__hash

    def __get_time(self):
        return str(datetime.datetime.now())

    def get_time(self):
        return self.__time

    def get(self):
        return {
            "block": self.get_id_block(),
            "timestamp": self.get_time(),
            "data": self.get_data(),
            "previous": self.get_previous_block(),
            "hash": self.get_hash()
        }


class BlockChain:
    def __init__(self, name_table):
        self.__id_block = 1
        self.__block_list = list()
        self.__hash_before = ""
        self.__string = ""
        self.__name_table = name_table
        self.__load_json()
        self.__id_update = -1
        self.__id_delete = -1

    def get_name_table(self):
        return self.__name_table

    def __init_id(self):
        self.__id_update = -1
        self.__id_delete = -1

    def get_block(self, data):
        path_file = f"./blockChain/block-{self.__name_table}.json"
        if path.exists(path_file):
            file = open(path_file, "r")
            block_json = json.loads(file.read())
            file.close()
            hash = self.__hash(data)
            for bloque in block_json:
                if bloque.get("hash") == hash:
                    return bloque.get('block')
            return None
        else:
            return None

    def create_block(self, data):
        hash = self.__hash(data)
        previous_hash = self.__hash_before if self.__id_block != 1 else 0
        new_block = Block(self.__id_block, data, previous_hash, hash)
        self.__block_list.append(new_block)
        self.__write_json()
        self.__id_block += 1
        self.__hash_before = hash

    def __hash(self, data):
        encoded_block = json.dumps(data).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def __write_json(self):
        if path.exists("./blockChain/"):
            file = open(f"./blockChain/block-{self.__name_table}.json", "w+")
            file.write(json.dumps([j.get() for j in self.__block_list]))
            file.close()
        else:
            os.makedirs("./blockChain/")
            return self.__write_json()

    def update(self, data, block):
        path_file = f"./blockChain/block-{self.__name_table}.json"
        if path.exists(path_file):
            file = open(path_file, "r")
            block_json = json.loads(file.read())
            file.close()
            for bloque in block_json:
                if bloque.get("block") == block:
                    bloque.pop("data")
                    bloque.pop("hash")
                    bloque.setdefault('data', data)
                    bloque.setdefault('hash', self.__hash(data))
                    self.__update_list(bloque)
                    self.__id_update = int(block)
                    break
            self.__write_json()
            return 0

    def __update_list(self, block):
        new_block = Block(block.get("block"), block.get("data"), block.get("previous"), block.get("hash"))
        self.__block_list[int(new_block.get_id_block()) - 1] = new_block

    def delete_block(self, id_block):
        for block in self.__block_list:
            if block.get_id_block() == id_block:
                self.__block_list.remove(block)
                self.__id_delete = int(id_block) + 1
                self.__write_json()
                return 0
        return 1

    def mine_all(self):
        bandera = False
        for index in range(len(self.__block_list)):
            block: Block = self.__block_list[index]
            if index != len(self.__block_list) - 1:
                block_next: Block = self.__block_list[index + 1]
                if block.get_hash() != block_next.get_previous_block():
                    block_next.set_previous_block(block.get_hash())
                    bandera = True
                    # break
        if bandera:
            self.__write_json()

    def mine(self, id_block):
        for a in range(len(self.__block_list)):
            pass

    def mostrar(self):
        print([j.get() for j in self.__block_list])

    def delete_json(self):
        path_file = f"./blockChain/block-{self.__name_table}.json"
        if path.exists(path_file):
            os.remove(path_file)
            return 0
        else:
            return 1

    def __load_json(self):
        path_file = f"./blockChain/block-{self.__name_table}.json"
        if path.exists(path_file):
            with open(path_file) as file_json:
                data = json.load(file_json)
                index = 1
                last_hash = ""
                for block in data:
                    new_block = Block(block['block'], block['data'], block['previous'], block['hash'])
                    self.__block_list.append(new_block)
                    index = int(block['block']) + 1
                    last_hash = block['hash']

                self.__id_block = index
                self.__hash_before = last_hash
        else:
            self.__block_list = list()

    def graficar(self):
        flag = False
        self.__string = ""
        self.__string = "digraph G{\n"
        self.__string += "rankdir=\"LR\"\n"
        self.__string += "node[shape=\"record\"]\n"
        id = -1
        index = 0
        while index < len(self.__block_list):
            block: Block = self.__block_list[index]
            if self.__id_delete == block.get_id_block() and self.__id_delete != -1:
                id = block.get_id_block()
                flag = True
            if block.get_id_block() == self.__id_update and self.__id_update != -1:
                id = block.get_id_block()
                flag = True

            if flag:
                if block.get_id_block() >= id:
                    # Rojos
                    self.__string += f"node{block.get_id_block()}[color=\"#E30101\",label=\" " \
                                     f"Block:{block.get_id_block()} \\n anterior:{block.get_previous_block()}" \
                                     f" \\n hash:{block.get_hash()} \" ] \n"
                    if index != len(self.__block_list) - 1:
                        block_next: Block = self.__block_list[index + 1]
                        self.__string += f"node{block_next.get_id_block()}[color=\"#E30101\",label=\" " \
                                         f"Block:{block_next.get_id_block()} \\n anterior:{block_next.get_previous_block()}" \
                                         f" \\n hash:{block_next.get_hash()} \" ] \n"
                        self.__string += f"node{block.get_id_block()}->node{block_next.get_id_block()} " \
                                         f"[arrowhead=\"crow\",color=\"#E30101 \"] \n"
                    # else:
                    # pass
                else:
                    # Verdes
                    self.__string += f"node{block.get_id_block()}[color=\"#5DE345\",label=\" " \
                                     f"Block:{block.get_id_block()}  \\n anterior:{block.get_previous_block()}" \
                                     f" \\n hash:{block.get_hash()} \" ] \n"
                    if index != len(self.__block_list) - 1:
                        block_next: Block = self.__block_list[index + 1]
                        if block_next.get_id_block() < id:
                            self.__string += f"node{block_next.get_id_block()}[color=\"#5DE345\",label=\" " \
                                             f"Block:{block_next.get_id_block()} \\n anterior:{block_next.get_previous_block()}" \
                                             f" \\n hash:{block_next.get_hash()} \" ] \n"

                            self.__string += f"node{block.get_id_block()}->node{block_next.get_id_block()} " \
                                             f"[arrowhead=\"crow\",color=\"#27FF00 \"] \n"
            else:
                self.__string += f"node{block.get_id_block()}[color=\"#5DE345\",label=\" " \
                                 f"Block:{block.get_id_block()}  \\n anterior:{block.get_previous_block()}" \
                                 f" \\n hash:{block.get_hash()} \" ] \n"
                if index != len(self.__block_list) - 1:
                    block_next: Block = self.__block_list[index + 1]
                    self.__string += f"node{block_next.get_id_block()}[color=\"#5DE345\",label=\" " \
                                     f"Block:{block_next.get_id_block()} \\n anterior:{block_next.get_previous_block()}" \
                                     f" \\n hash:{block_next.get_hash()} \" ] \n"
                    self.__string += f"node{block.get_id_block()}->node{block_next.get_id_block()} " \
                                     f"[arrowhead=\"crow\",color=\"#27FF00 \"] \n"

            index += 1
        self.__string += "}\n"
        #print(self.__string)
        self.__init_id()
        return self.__string
