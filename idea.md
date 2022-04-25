

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

First we have to create the genesis block which we started in the `Block` class. We'll fill in all the already defined variables:

```python
def create_genesis_block(self):
    genesis_block = Block(0, [], time.time(), "0") # Fill in variables
    genesis_block.hash = genesis_block.compute_hash() # Compute the hash
    self.chain.append(genesis_block) # Add block to chain
```

Define a difficulty of 2 which is the number of leading zero bits in front of each block, this number will grow each time a new block is mined. You will also need to define the `nonce` value. From my understanding difficulty applies to non hashed blocks while the nonce is the hashed number of zero bits that has to be found. 

> The nonce is the number that blockchain miners are solving for, in order to receive cryptocurrency.

The nonce and difficulty concepts are yet to be fully understood by myself. Now let's move on to proof of work. If the non computed hash starts with zeros we add to the nonce value and compute (and return) the new hash with the new nonce value.

```python3
while not computed_hash.startswith("0" * BlockChain.difficulty): 
    block.nonce += 1 
    computed_hash = block.compute_hash()
return computed_hash
```