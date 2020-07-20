from queue import Queue

class LRU_Cache(object):

    def __init__(self, capacity):
    	# Initialize class variables
    	self.q = Queue(maxsize=capacity)
    	self.cache_dict = dict()
    	self.num_elements = 0

    def get(self, key):
    	# Retrieve item from provided key. Return -1 if nonexistent. 
    	if key not in self.cache_dict:
    		return -1
    	self.update_cache_queue(key)
    	return self.cache_dict[key]

    def set(self, key, value):
    	# Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
    	lru_key = self.update_cache_queue(key) 
    	if self.num_elements ==  5:
    		self.cache_dict.pop(lru_key)
    		self.num_elements -= 1
    	self.cache_dict[key] = value
    	self.num_elements += 1

    def update_cache_queue(self,key):
    	lru_key = None
    	if self.q.full():
    		lru_key = self.q.get()
    	self.q.put(key)
    	return lru_key

print (f'**** TestCase 1 ****\n')
#Test Case 1
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print (our_cache.get(1))
# returns 1
print(our_cache.get(2))
# returns 2
print(our_cache.get(9))
# returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)
print(our_cache.get(3))
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print (f'\n**** TestCase 2 ****\n')

# Test Case 2
our_cache = LRU_Cache(5)
print (our_cache.get(1))
# returns -1

print (f'\n**** TestCase 3 ****\n')

# Test Case 3
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

our_cache.get(1)
our_cache.get(2)
our_cache.get(9)

our_cache.set(5, 5) 
our_cache.set(6, 6)
print(our_cache.get(3))
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print (f'\n**** TestCase 4 ****\n')

# Test Case 4
our_cache = LRU_Cache(0)

our_cache.set(1, 1);
print (our_cache.get(1))
# returns 1 as capacity is 0 so number itself will be the least recently used