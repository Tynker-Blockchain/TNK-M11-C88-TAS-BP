import hashlib
import json
from time import time

def generateHash(input_string):
    hashObject = hashlib.sha256()
    hashObject.update(input_string.encode('utf-8'))
    hashValue = hashObject.hexdigest()
    return hashValue

class BlockChain():
    def __init__(self):
        self.chain = []

    def length(self):
        return len(self.chain)
        
    def addBlock(self, newBlock):
        if(len(self.chain) == 0):
            self.createGensisBlock()
        newBlock.previousHash = self.chain[-1].currentHash
        newBlock.currentHash = newBlock.calculateHash()
        self.chain.append(newBlock)
    
    def createGensisBlock(self):
        genesisBlock = Block(0, time(), {'sender':'NA', 'receiver':'NA', 'amount':'NA'}, "No Prevoius Hash Present. Since this is the first block.")
        self.chain.append(genesisBlock)
    
    def printChain(self):
        for block in self.chain:
            print("Block Index", block.index)
            print("Timestamp", block.timestamp)
            print("Transaction", block.transaction)
            print( "Previous Hash",block.previousHash)
            print( "Current Hash",block.currentHash)
            print( "Is Valid Block",block.isValid)

            print("*" * 100 , "\n")

    def validateBlock(self, currentBlock):
        previousBlock = self.chain[currentBlock.index - 1]
        if(currentBlock.index != previousBlock.index + 1):
            return False
        
        previousBlockHash = previousBlock.calculateHash()

        # Set previous block hash to a wrong value when current block index become 2, i.e simulate and invalid block for block index 2
        
        
        if(previousBlockHash != currentBlock.previousHash):
            return False
        
        return True
        
class Block:
    def __init__(self, index, timestamp, transaction, previousHash):
        self.index = index
        self.transaction = transaction
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.currentHash = self.calculateHash()
        self.isValid = None
       
    def calculateHash(self, timestamp=None):
        if(timestamp == None):
            timestamp = self.timestamp

        blockString = str(self.index) + str(timestamp) + str(self.previousHash) + json.dumps(self.transaction)
        return generateHash(blockString)

       
