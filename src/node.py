import json
from blockchain import Blockchain
from mine import Miner
from flask import Flask, jsonify, request
from urllib.parse import urlparse


app = Flask(__name__)

blockChainObj = Blockchain()
minerObj = Miner()


class Node:

	def __init__(self):
		nodes = ();

	def add(self, address):
		parsedURL = urlparse(address)
		self.nodes.add(parsedURL.netloc)

#Mine a new block
#requestmethod	POST
#responsebody ContentType	JSON
@app.route('/blockchain/mine', methods=['POST'])
def mineBlock():
	transactions = request.form['data']
	miner.createBlock(transactions)
	response = {'newBlock': minerObj.getBlockChain()[-1],
					'length': len(minerObj.getBlockChain())}
	return jsonify(response), 200


#Get blockchain
#requestmethod	GET
#responsebody ContentType	JSON
@app.route('/blockchain/get', methods=['GET'])
def getBlockChain():
	response = {'blockchain': minerObj.getBlockChain(),
					'length': len(minerObj.getBlockChain())}
	return jsonify(response), 200


#Set blockchain
#requestmethod	POST
#requestbody	
#responsebody ContentType	JSON
@app.route('/blockchain/set', methods=['POST'])
def setBlockChain():
	blockChain = request.form['blockChain']
	minerObj.setBlockChain(json.loads(blockChain))
	response = {"message": "Blockchain inserted"}
	return jsonify(response), 200


#Validate blockchain
#requestmethod	GET/ POST
#requestbody	
#response	ContentType		JSON
@app.route('/blockchain/validate/', methods=['GET', 'POST'])
def validateBlockChain():
	savedBlockChain = minerObj.getBlockChain()
	if request.method == 'POST':
		blockChain = json.loads(request.form['blockChain'])
		minerObj.setBlockChain(blockChain)

	if blockChainObj.isValid(minerObj.getBlockChain()):
		response = {'status': True}
	else:
		response = {'status': False}

	minerObj.setBlockChain(savedBlockChain)
	return jsonify(response), 200



app.run(host='0.0.0.0', port='8080')