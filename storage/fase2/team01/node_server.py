from hashlib import sha256
import json
import time

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
    
    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()

class Blockchain:
    difficulty = 2
    
    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []

    def create_genesis_block(self):
        genesis_block = Block(0,[],0,"0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)
    
    @property
    def last_block(self):
        return self.chain[-1]

    def add_block(self, block, proof):
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False
        
        if not Blockchain.is_valid_proof(block, proof):
            return False
        
        block.hash = proof
        self.chain.append(block)
        return True

    @staticmethod
    def proof_of_work(block):
        block.nonce =0 
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0'*Blockchain.difficulty):
            block.nonce +=1
            computed_hash=block.compute_hash()
        return computed_hash
    
    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)
    
    @classmethod
    def is_valid_proof(cls,block, block_hash):
        return (block_hash.startswith('0' * Blockchain.difficulty) and block_hash == block.compute_hash())

    @classmethod
    def chek_main_validity(cls, chain):
        result = True
        previous_hash = "0"

        for block in chain:
            block_hash = block.hash
            delattr(block,"hash")

            if not cls.is_valid_proof(block,block_hash) or previous_hash != block.previous_hash:
                result = True
                break
            block.hash, previous_hash = block_hash,block_hash
        return result
        
    def mine(self):
        if not self.unconfirmed_transactions:
            return False
        last_block = self.last_block
        new_block = Block(index=last_block.index + 1,
            transactions=self.unconfirmed_transactions,
            timestamp=time.time(),
            previous_hash=last_block.hash)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []
        return True

blockchain = Blockchain()
blockchain.create_genesis_block()
peers = set()
def get_chain():
    chain_data =[]
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
        "chain":chain_data,
        "peers":"None"
    }
    )
def consensus():
    global blockchain
    longest_chain = None
    current_len = len(blockchain.chain)
    

def announce_new_block(block):
    for peer in peers:
        url = "{}add_block".format(peer)
        headers = {'Content-Type':"application/json"}
        print(url, json.dumps(block.__dict__,sort_keys=True),headers)

def mine_unconfirmed_transactions():
    result = blockchain.mine()
    if not result:
        return "No transactions to mine"
    else:
        chain_length = len(blockchain.chain)
        if chain_length == len(blockchain.chain):
            announce_new_block(blockchain.last_block)
    return "Block #{} is mined.".format(blockchain.last_block.index)
def get_pending_tx():
    return json.dumps(blockchain.unconfirmed_transactions)


