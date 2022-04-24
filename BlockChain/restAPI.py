from flask import Flask, request
import requests

class api:
from BlockChain import Blockchain
app = Flask(__name__)

blockchanin = Blockchain().Blockchain()

@app.route('/chain', methods=['GET'])
