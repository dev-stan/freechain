## Free chain, explaining block chain technology
**To-do:**
- Build as Django app

## Building a block

In the `Block` class we register variables as shown below:

```python
self.index = index
self.transactions = transactions
self.timestamp = timestamp
self.previous_hash = previous_hash
self.nonce = nonce
```

We define the block as a json of the class contents `self.__dict__` with `sort_keys=True`. In the `compute_hash` function we return the encoded Block string.

---
## Building the blockchain and confirming data

### Creating the first block
First we have to create the genesis block which we started in the `Block` class. We'll fill in all the already defined variables:

```python
def create_genesis_block(self):
    genesis_block = Block(0, [], time.time(), "0") # Fill in variables
    genesis_block.hash = genesis_block.compute_hash() # Compute the hash
    self.chain.append(genesis_block) # Add block to chain
```

### Proof of work

Define a difficulty of 2 which is the number of leading zero bits in front of each block, this number will grow each time a new block is mined. You will also need to define the `nonce` value. From my understanding difficulty applies to non hashed blocks while the nonce is the hashed number of zero bits that has to be found. 

> The nonce is the number that blockchain miners are solving for, in order to receive cryptocurrency.

The nonce and difficulty concepts are yet to be fully understood by myself. Now let's move on to proof of work. If the non computed hash starts with zeros we add to the nonce value and compute (and return) the new hash with the new nonce value.

```python3
while not computed_hash.startswith("0" * BlockChain.difficulty): 
    block.nonce += 1 
    computed_hash = block.compute_hash()
return computed_hash
```

```python3
# Valid proof function for what's below
def is_valid_proof(self, block, block_hash):
    return (block_hash.startswith('0' * BlockChain.difficulty) and block_hash == block.compute_hash())
```
### Add block
Define the previous hash, and verify it, if the previous hash is the same as `block.previous_hash` and `self.is_valid_proof` then `block.hash = proof` and append the block. That's it!

### Mining a block

> Blockchain mining is used to secure and verify bitcoin transactions.

Each transaction has a different hash which has to be "mined", mining a single bitcoin block (**not a bitcoin!**) takes around 10 minutes.

First we have to define the last block `self.chain[-1]`. Then make a new_block like this:

```python3
new_block = Block(index=last_block.index + 1,
        transactions=self
        unconfirmed_transactions,
        timestamp=time.time(),
        previous_hash=last_block.hash)
```

The we have to add the block and the proof:
```python3
proof = self.proof_of_work(new_block)
self.add_block(new_block, proof)
```
At the end let's return the `new_block.index` and that's it for our mining function.

## Veryfing our blockchain
Extremely simple Flask application, copy and paste.
```python3
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

```
