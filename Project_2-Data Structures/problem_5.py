import hashlib
from datetime import datetime

class Block:

	def __init__(self, timestamp, data, previous_hash):
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.calc_hash()
		self.next = None

	def calc_hash(self):
		sha = hashlib.sha256()
		hash_str = self.data.encode('utf-8')
		sha.update(hash_str)
		return sha.hexdigest()

	def __repr__(self):
		return f'data -> {self.data} \nhash -> {self.hash} \nprevious_hash -> {self.previous_hash}\n'

class Blockchain(object):
	
	def __init__(self):
		self.head = None
		self.tail = None

	def append(self, data):
		now = datetime.utcnow()
		timestamp = datetime.timestamp(now)
		block = Block(timestamp,data,0)

		if self.head is None:
			self.head = block
			self.tail = self.head
			return self.head

		self.tail.next = block
		block.previous_hash = self.tail.hash
		self.tail = block

print (f'**** TestCase 1 ****\n')

# Test Case 1
blockchain = Blockchain()
blockchain.append("Hey its Mohit")
blockchain.append("Hey its vishu")

while blockchain.head :
	print (blockchain.head)
	blockchain.head = blockchain.head.next
# Prints: 2 Blocks with data, hash and their previous hash
# data -> Hey its Mohit 
# hash -> 6bcfa1ace0502613a7a2d55f1c8c6d824f18f692c008d43e8a4a09d059edfd3f 
# previous_hash -> 0

# data -> Hey its vishu 
# hash -> 2c6d8431446008077da746c2b935f9af87973d85c80003afd94e93289ee12c6f 
# previous_hash -> 6bcfa1ace0502613a7a2d55f1c8c6d824f18f692c008d43e8a4a09d059edfd3f

print (f'**** TestCase 2 ****\n')
#TestCase 2
blockchain = Blockchain()
blockchain.append("Apple")
blockchain.append("Banana")
blockchain.append("Orange")
blockchain.append("Mango")

while blockchain.head :
	print (blockchain.head)
	blockchain.head = blockchain.head.next

# Prints: 4 Blocks of a chain with data, hash and their previous hash

print (f'**** TestCase 3 ****\n')
#TestCase 3
blockchain = Blockchain()

print (blockchain.head)
# Prints : None (as there is no block in blockchain)

print (f'\n**** TestCase 4 ****\n')

#TestCase 4
blockchain = Blockchain()
blockchain.append("")
print (blockchain.head)
# Prints : block with data equal to blank string
# data ->  
# hash -> e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 
# previous_hash -> 0

print (f'\n**** TestCase 5 ****\n')
#TestCase 5
blockchain = Blockchain()
blockchain.append("Apple")
blockchain.append("Apple")
while blockchain.head :
	print (blockchain.head)
	blockchain.head = blockchain.head.next
# Both blocks have same data but still they are differnt blocks in a chain
# Prints: 
# data -> Apple 
# hash -> f223faa96f22916294922b171a2696d868fd1f9129302eb41a45b2a2ea2ebbfd 
# previous_hash -> 0

# data -> Apple 
# hash -> f223faa96f22916294922b171a2696d868fd1f9129302eb41a45b2a2ea2ebbfd 
# previous_hash -> f223faa96f22916294922b171a2696d868fd1f9129302eb41a45b2a2ea2ebbfd