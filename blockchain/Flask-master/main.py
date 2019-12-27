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


class BlockChain:
    def __init__(self):
        self.head=None
        self.size=0
    
    def add(self,item):
        if self.size==0:
            self.head=item
        else:
            cur=self.head
            while cur.next != None:
                cur=cur.next
            cur.next=item 
        self.size+=1
    
    def dump_blockchain(self):     
        d=dict()
        cur=self.head
        x=0
        while cur != None:
            result=[]
            t = "block #"+str(x)
            result.append('data: '+str(cur.data))
            result.append('Nonce: '+str(cur.Nonce))
            result.append('previous_block_hash: '+str(cur.previous_block_hash))
            result.append('Hash: '+str(cur.hash))
            d[t]=result
            x+=1
            cur=cur.next
        return d
            
class Block:
    def __init__(self):
        self.data = "" 
        self.previous_block_hash = ""
        self.Nonce = ""
        self.hash=""
        self.next = None
        
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
    block.hash=digest
    
    BLOCKCHAIN.add(block)
    return BLOCKCHAIN.dump_blockchain()


BLOCKCHAIN=BlockChain()
Last_block_hash = 'None'

app.run(port=8080)
