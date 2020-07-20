Huffman Encoding and Decoding:

I have used dictionary to make the frequency distribution table for occurence of each character
For better results i have made priority queue with customised min Heap using list data structure to get the Node with minimum value
Then we have traversed recursively to form Huffman tree and get the encoded string.

To decode the encoded string we have traversed from the root_node of huffman tree whenever 0 occurs we follow left node and with occurence of 1 we follow right node.

Time Complexity:
The time complexity of Huffman encoding and decoding is O(nlogn)
We have used a min Heap to store the value of each tree, each iteration requires O(logn) time to determine the minimum value and insert the new value.
There are total O(n) iterations, one for each element.
So overall Time Complexity : O(nlogn)
Space Complexity: We have used 2 dictionaries one for frequency distribution and one for encoded distribution, space complexity of both nodes will be n, where n is number of nodes or distinct characters.
					For minimum heap we have used space with max length of 2* n + 2. 
					So overall Space complexity will be O(n)