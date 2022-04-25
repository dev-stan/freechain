import time
from flask import Flask, request
import requests


from hashlib import sha256
import json

{   
    "author": "author_name",
    "timestamp": "transaction_time", 
    "data": "transaction_data"
}

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):

        # Register variables
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
    
    def compute_hash(self):
        
        # Read json
        block_string = json.dumps(self.__dict__, sort_keys=True)
        # Hash data
        return sha256(block_string.encode()).hexdigest()


class BlockChain:

    # Initialize class
    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()

    # Create block and add to chain
    def create_genesis_block(self):
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash() # don't know why this is needed
        self.chain.append(genesis_block) # Add block to chain

    difficulty = 2
    def proof_of_work(self, block): # Verify if block is valid
        block.nonce = 0 # Amount of zero bits when it's hashed
        computed_hash = block.compute_hash()
        while not computed_hash.startswith("0" * BlockChain.difficulty): # Check if hash starts with 0's
            block.nonce += 1 
            computed_hash = block.compute_hash()
        return computed_hash

    def add_block(self, block, proof):
        previous_hash = self.chain[-1].hash
        if previous_hash != block.previous_hash:
            return False
        if not self.is_valid_proof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True
    
    def is_valid_proof(self, block, block_hash):
        return (block_hash.startswith('0' * BlockChain.difficulty) and block_hash == block.compute_hash())

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)
    
    def mine(self):
        if not self.unconfirmed_transactions:
            return False
        last_block = self.chain[-1]
        new_block = Block(index=last_block.index + 1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time.time(),
                          previous_hash=last_block.hash)
        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []
        return new_block.index

    @property
    def last_block(self):
        return self.chain[-1]


class app:
    app = Flask(__name__)

    blockchain = BlockChain()

    @app.route('/chain', methods=['GET'])
    def get_chain():
        chain_data = []
            
        for block in BlockChain().chain:
            chain_data.append(block.__dict__)
        return json.dumps({"length": len(chain_data),
                        "chain": chain_data})

    app.run(debug=True, port=5000)

