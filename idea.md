# Blockchain Concept

*Implementation of a simple blockchain in Python 3 with a proof of concept.*

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


