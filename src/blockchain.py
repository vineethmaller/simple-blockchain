import datetime
import hashlib
import json
from transaction import Transaction 


class Blockchain:

	#No argument constructor
	def __init__(self):
		self.chain = []
		self.createBlock(transactions = '')	#Creates a genesis block


	#Set a blockchain
	#input	list	blockChain
	def set(self, blockChain):
		self.chain = blockChain


	#Get a blockchain
	#output	list
	def get(self):
		return self.chain


	#Check if blockchain is valid
	#input	list		blockChain 		A list of blocks
	#output boolean
	def isValid(self, blockChain):
		index = 1

		while index<=len(blockChain):
			block = blockChain[index-1]

			if block['index'] == index:
				if block['index'] != 1:
					prevBlock = blockChain[index-2];
					if block['previousHash'] != prevBlock['hash']:
						return False
				else:
					if block['previousHash'] != '0':
						return False
				newBlock = {'index': block['index'],
								'timestamp': block['timestamp'],
								'transactions': block['transactions'],
								'previousHash': block['previousHash'],
								'nonce': block['nonce']}
				calculatedHash = hashlib.sha256(json.dumps(newBlock, sort_keys = True).encode()).hexdigest()
				if (block['hash'] == calculatedHash) and (calculatedHash[:1] == block['previousHash'][:1]):
					index += 1
				else:
					return False
			else:
				return False
		return True
