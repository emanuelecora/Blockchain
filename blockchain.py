import hashlib
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
import datetime

class Block:
    def __init__(self, prev_hash, index, data, reward):
        self.prev_hash = prev_hash
        self.index = index
        self.data = data
        self.timestamp = datetime.datetime.now()
        self.reward = reward
        self.proof_no = self.proof_of_work()
    
    @property
    def hash(self):
        return hashlib.sha256(str(self).encode()).hexdigest()
    
    def proof_of_work(self):
        proof_no = 1
        while self.verify_proof(self, proof_no) is False:
            proof_no += 1
        print("Verified: The Proof of Work is {}".format(proof_no))
        return proof_no
    
    @staticmethod
    def verify_proof(self, proof_no):
        self.proof_of_work = proof_no
        print("HASH: {}".format(self.hash))
        print(f"Proof of Work: {proof_no}")
        print("-----")
        return self.hash[:4] == "0000"

    def __str__(self):
        return "{} {} {} {} {}".format(self.prev_hash, self.index, self.data, self.timestamp, self.proof_of_work)

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.node = set()
        self.create_genesis()
    
    @property
    def reward(self):
        reward = -1/10 * len(self.chain) + 50
        return reward if reward >= 0 else 0
    
    def last_block(self):
        return self.chain[-1]
    
    def create_genesis(self):
        genesis_block =  Block(0, 0, ["Genesis"], 0)
        self.chain.append(genesis_block)
    
    def mine(self):
        block = Block(self.last_block().hash, len(self.chain), self.current_data, self.reward)
        self.chain.append(block)
        self.current_data = []

