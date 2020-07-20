BlockChain

I have made a Block class with variables data, timestamp, hash, previous hash and next to store next block.
To make a simple block chain, we have initialised first block with head block and for each append method call tail of blockchain will link the next block to its own block and stores block's hash value in next block's previous_hash variable's value

Time Complexity:
Time complexity of given method will be O(1) for each append method so if there are n blocks in a block chain total time taken will be equal to n.
So Time Complexity will be O(n)
Since space for all the variables will be constant so total complexity will depend on number of blocks of a blockchain
Space Complexity : O(n)