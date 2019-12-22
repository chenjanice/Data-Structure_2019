import flask
from flask import request, render_template
import hashlib
import random
import binascii
import Crypto
import Crypto.Random
from Crypto.Hash import SHA


app = flask.Flask(__name__)
app.config["DEBUG"] = True


class Block:
    def __init__(self):
        self.data = ""
        self.previous_block_hash = ""
        self.Nonce = ""
        
    def dump_blockchain (self,BlockChain,HASH):
        d=dict()
        for x in range (len(BlockChain)):
            block_temp = BlockChain[x]
            result=[]
            t = "block #"+str(x)
            result.append('data: '+str(block_temp.data))
            result.append('Nonce: '+str(block_temp.Nonce))
            result.append('previous_block_hash: '+str(block_temp.previous_block_hash))
            result.append('Hash: '+str(HASH[x]))
            d[t]=result
        return d
            
    def sha256(self,message):
        return hashlib.sha256(message.encode('ascii')).hexdigest()
    
    def mine(self,message):
        difficulty = 2
        prefix = '1' * difficulty
        for i in range(1000):
            digest = self.sha256(str(hash(message)) + str(i))
            if digest.startswith(prefix):
                return digest

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit():
    global Last_block_hash
    number = request.form.get('number')

    block = Block()
    block.data = number
    block.previous_block_hash = Last_block_hash
    block.Nonce = Block().mine(block)
    
    digest = hash(block)
    Last_block_hash = digest
    HASH.append(digest)
    BlockChain.append (block)
    
    return Block().dump_blockchain(BlockChain,HASH)


BlockChain =[]
HASH=[]
Last_block_hash = 'None'

app.run(port=8080)
