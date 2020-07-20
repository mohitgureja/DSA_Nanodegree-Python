LRU_Cache :

Data Structures used in making LRU Cache are Queue, Dictionary

Queue : It is used to have a sneek peek of the cache queue. For each operation of the problem (set / get), i have updated the cache queue so that i can get the least recently used key.

Dictionary: It is used because the average case time complexity of dictionary operations is O(1) and so is best suited for retrieval as well as setting the key, val pair.

For set operations i have checked if total elements equals to 5 then remove the least recently used key from the dictionary and set the key we want to set. For get operations cache dictionary well serves its operation.

For both set and get operations, i have updated the cache queue with recent usage of the key.

Time complexity:

Queue operations put, get have constant time complexity i.e O(1). So function update_cache_queue(key) has constant time complexity.

dictionary operations i.e pop and other take constant time in average cases. So functions set and get for LRU Cache have constant time complexity and it does not changes according to the input
So Time complexity =  O(c) where c is constant or O(1)

Space Complexity:  We are using a dictionary whose max size will be number of items we set say n, but Queue will be of fixed length i.e c (max capacity)
So overall Space complexity: O(n + c) or we can say O(n)