from flask import Flask, request
import chain.Blockchain
import json

class app:
    app = Flask(__name__)

    blockchain = chain.Blockchain.BlockChain()

    @app.route('/chain', methods=['GET'])
    def get_chain():

        chain_data = []
        for block in chain.Blockchain.BlockChain().chain:
            chain_data.append(block.__dict__)
        return json.dumps({"length": len(chain_data),
                        "chain": chain_data})

    app.run(debug=True, port=5000)