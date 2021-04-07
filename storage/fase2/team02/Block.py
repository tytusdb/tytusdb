#----block
import hashlib

class Block:
    def __init__(self, previos_hash, transaction):
        self.transaction = transaction
        self.previos_hash = previos_hash
        string_to_hash = "".join(transaction) + previos_hash
        self.block_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()