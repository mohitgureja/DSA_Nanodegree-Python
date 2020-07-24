HTTPRouter using a Trie:

To make a Router using Trie data structure, I have created a new RouteTrie for holding our routes and to act as a wrapper for RouteTrieNode.
Each RouteTrieNode consists a dictionary of RouteTrieNodes (children) and a handler. As a wrapper RouteTrie does the job of a trie keeping the RouteTrieNode abstracted from the Router.

On initialisation of a Router we have set root trie node with "root handler" and also a default "not found handler".
To add a handler in Router, we first split the router into a list of path according to delimiter "/" and then for each path string add node to the RouteTrie.
For the lookup method, we first check if it is a root handler else split the path string into list of paths with delimiter "/". For each path string we try to find the handler in RouteTrie. If any handler is found for complete path we return the corresponding handler associated with that path otherwise if its None we return default not found hanler.

Time Complexity: For addition of a handler, we first have to split the path string of length "n" into list of path with delimiter "/" which can be done in O(n). Let k be the length of path list. So total time complexity for adding k items in RouteTrie is O(k). 
Same way lookup will also have time complexity : O(n) + O(k)
So overall time complexity will be: O(n) + O(k). Here k can be considered very less than n So, Time complexity = O(n)
(If we consider input as only 1 string then overall time complexity will be O(1))

Space Complexity: For string of length n. We are splitting it into input list of length k. For each k we are using a dictionary, so space complexity will be O(k).
For string length n, k can be considered as very small. So overall space complexity will be O(c), where c is constant or we can say O(1)
 