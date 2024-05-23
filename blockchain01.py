import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data) + str(self.nonce)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def mine_block(self, difficulty):
        required_prefix = '0' * difficulty
        while self.hash[:difficulty] != required_prefix:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self, difficulty):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

# Uso del Blockchain
blockchain = Blockchain(difficulty=4)

# Agregar bloques
blockchain.add_block(Block(1, blockchain.get_latest_block().hash, time.time(), "Block 1 Data"))
blockchain.add_block(Block(2, blockchain.get_latest_block().hash, time.time(), "Block 2 Data"))

# Verificar la cadena
print("Blockchain es válida:", blockchain.is_chain_valid())

# Imprimir la cadena
for block in blockchain.chain:
    print("Index:", block.index)
    print("Hash:", block.hash)
    print("Previous Hash:", block.previous_hash)
    print("Data:", block.data)
    print("Nonce:", block.nonce)
    print("Timestamp:", block.timestamp)
    print("-" * 30)
