import json
from uuid import uuid4
from blockchain import Blockchain

class Election:

	def __init__(self, election_id, block_chain):
		self.election_id = election_id
		self.votes = [];
		self.parties = [];
		if block_chain.is_valid():
			self.block_chain = block_chain

	def vote(self, election_id, voter_id, party_id):
		self.votes.append({'electionID': election_id,
									'voterID': str(voter_id),
									'partyID': str(party_id)})

	def get_parties():
		

	def get_election_result(self):
		vote_count = {}
		try:
			for block in block_chain:
				votes = block['votes']
				for vote in votes:
					party_id = vote['partyID']
					if vote['electionID'] == self.election_id and party_id in self.parties]:
						vote_count[party_id] = 1 if vote_count[party_id] == None else vote_count[party_id]+1
			return vote_count
		except:
			print("Unable to get election result")


