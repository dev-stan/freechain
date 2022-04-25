from hashlib import sha256
import json

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
