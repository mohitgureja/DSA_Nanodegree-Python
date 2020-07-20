import sys

class  Node(object):
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None	

	def __repr__(self):
		return f' key -> {self.key} value -> {self.value}'

class MinHeap(object):

	def __init__(self, maxsize):
		self.maxsize = maxsize
		self.heap = [Node(None,sys.maxsize) for _ in range(maxsize)]
		self.heap[0].value = -1*sys.maxsize
		self.size = 0

	# Returns the index of parent node
	def parent(self, index):
		return index//2

	# Returns left child index of a node
	def left_child(self, index):
		return 2*index

	# Returns right child index of a node
	def right_child(self, index):
		return 2*index + 1

	# Returns true if node is leaf node
	def is_leaf_node(self, index):
		if index > self.size//2 and index <= self.size:
			return True
		return False

    # Swaps two nodes
	def swap_nodes(self, first_index, second_index):
		self.heap[first_index], self.heap[second_index] = self.heap[second_index], self.heap[first_index]

	# It heapifies the node for minimum value
	def heapify(self, index):
		boolean = self.is_leaf_node(index)
		if not boolean:

			if self.heap[self.left_child(index)].value < self.heap[index].value or self.heap[self.right_child(index)].value < self.heap[index].value:

				if self.heap[self.left_child(index)].value <= self.heap[self.right_child(index)].value:
					self.swap_nodes(self.left_child(index), index)
					self.heapify(self.left_child(index))
				else:
					self.swap_nodes(self.right_child(index), index)
					self.heapify(self.right_child(index))

	# Insert an node
	def insert(self, node):
		if self.size >= self.maxsize:
			return
		self.size += 1
		self.heap[self.size] = node

		current_index = self.size
		while self.heap[current_index].value < self.heap[self.parent(current_index)].value:
			self.swap_nodes(current_index, self.parent(current_index))
			current_index = self.parent(current_index)
		
	# Pops min node from Heap
	def remove(self):
		node = self.heap[1]
		self.heap[1] = self.heap[self.size]
		# self.heap[self.size] = Node(None,0)
		self.size -= 1
		self.heapify(1)
		return node

	def print_heap(self):
		for i in range(1,self.size//2+1):
			print (f'index : {i} {self.heap[i]} left_child ->{self.heap[self.left_child(i)]} right_child -> {self.heap[self.right_child(i)]}')
	
	#Function to build min Heap
	def build_min_heap(self):
		for index in range(self.size//2,0,-1):
			self.heapify(index)


def get_frequency_distribution(data):
	distribution = {}
	for char in data:
		if char in distribution:
			distribution[char] += 1
		else:
			distribution[char] = 1
	return distribution

def get_huffman_tree(heap):
	if heap.size == 0:
		return None
	elif heap.size == 1:
		return heap.remove()
	else:
		first_node = heap.remove()
		second_node = heap.remove()
		root_node = Node("parent",first_node.value + second_node.value)
		root_node.left = first_node
		root_node.right = second_node
		heap.insert(root_node)
		return get_huffman_tree(heap)

def get_encoded_distribution(root_node):
	if root_node is None:
		return
	encoded_dict = {}
	encoded_string = ""

	def traverse(root_node, encoded_string):
		if root_node.left is None and root_node.right is None and root_node.key != "parent":
			encoded_dict[root_node.key] = encoded_string
			return

		traverse(root_node.left, encoded_string + "0")
		traverse(root_node.right, encoded_string + "1")

	traverse(root_node, encoded_string)
	return encoded_dict

def get_min_heap(frequency_distribution, maxsize):
	heap = MinHeap(maxsize)
	for key in frequency_distribution.keys():
		heap.insert(Node(key,frequency_distribution[key]))
		heap.build_min_heap()
	return heap

def huffman_encoding(data):
	frequency_distribution = get_frequency_distribution(data)
	priority_queue = get_min_heap(frequency_distribution, len(frequency_distribution)*2 + 2)
	root_node = get_huffman_tree(priority_queue)
	encoded_dict = get_encoded_distribution(root_node)
	encoded_string = ""
	for i in range(0,len(data)):
		encoded_string = encoded_string + encoded_dict[data[i]]
	return encoded_string, root_node

def huffman_decoding(encoded_string, root_node):
	decoded_string = ""
	node = root_node
	for i in range(len(encoded_string)):

		if encoded_string[i] == '0':
			node = node.left
		else:
			node = node.right

		if node.left is None and node.right is None:
			decoded_string = decoded_string +node.key
			node = root_node
	return decoded_string

if __name__ == "__main__":
    codes = {}

    # Test Case 1
    print (f'**** Test Case 1 ****\n')

    a_great_sentence = "The bird is the word"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Prints : 45
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # Prints : The bird is the word
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Prints : 22 
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Prints : 1010111001011010111111100000110111101111100010111001011001100011100000
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Prints : 45
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # Prints : The bird is the word

    print (f'\n**** Test Case 2 ****\n\n')

    # Test Case 2
    a_great_sentence = "Th"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Prints : 28
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # Prints : The
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base = 2))))
    # Prints : 14
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Prints : 10011
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Prints : 28
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # Prints : The

    print (f'\n**** Test Case 3 ****\n\n')

    # Test Case 3
    a_great_sentence = "aaaaaaaaannnnnnnnnnnn"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Prints : 46
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # Prints : aaaaaaaaannnnnnnnnnnn
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Prints : 14
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Prints : 000000000111111111111
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Prints : 46
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # Prints : aaaaaaaaannnnnnnnnnnn

    print (f'\n**** Test Case 4 ****\n\n')
    #Test Case 4

    empty_string = ""
    print ("The size of the data is: {}\n".format(sys.getsizeof(empty_string)))
    # Prints : 25
    print ("The content of the data is: {}\n".format(empty_string))
    # Prints : Blank String
    encoded_data, tree = huffman_encoding(empty_string)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(encoded_data)))
    # Prints : 25
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Prints : Blank String
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Prints : 25
    print ("The content of the decoded_data data is: {}\n".format(decoded_data))
	# Prints : Blank String