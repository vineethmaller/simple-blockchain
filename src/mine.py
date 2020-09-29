import hashlib
import json
from blockchain import BlockChain
from election import Election


class Miner:

	def __init__(self):
		self.blockChain = Blockchain()
		self.election = Election()


	def setBlockChain(self, blockChain):
		if self.blockChain.isValid(blockChain):
			self.blockChain.set(blockChain)

	def getBlockChain(self):
		self.blockChain.get();



	#Creates a new block
	#input	string		votes		Votes to be contained in the new block
	#output void	
	def createBlock(self, votes):
		blockChain = self.getBlockChain()
		block = {'index': len(blockChain)+1,
					'timestamp': str(datetime.datetime.now()),
					'votes': votes}
		
		if len(blockChain) == 0:
			block['previousHash'] = '0'
		else:
			block['previousHash'] = blockChain[block['index']-2]['hash']

		block = self.mineBlock(block)
		
		blockChain.append(block);
		self.setBlockChain(blockChain)


	#Mines a block
	#input 	dictionary	partialblock 	A block without nonce and hash 
	#output dictionary
	def mineBlock(self, partialBlock):
		nonce = 1
		checkProofOfWork = False

		while checkProofOfWork is False:
			partialBlock['nonce'] = str(nonce)
			newHash = hashlib.sha256(json.dumps(partialBlock, sort_keys = True).encode()).hexdigest()
			if newHash[:1] == partialBlock['previousHash'][:1]:
				checkProofOfWork = True
				partialBlock['hash'] = newHash
			else:
				nonce += 1

		return partialBlock