Autocomplete with Tries:

To proceed with autocompletion with the help of trie, i have made recursive function whose job is to find all the suffixes lying beneath a particular node recursively.
As we know Trie eases to find a prefix word by word, so to find the suffixes we need to find the prefix and then for each children of prefix node we need to recursively find the suffix the same way recursively and when suffixes form a valid word add them in the suffixes list.

Time Complexity: As we know, in a Trie data structure to find a prefix complexity is constant i.e O(1). But to find all the suffixes i.e to autocomplete a word in the worst case we may need to traverse each character of all the words which means none of the words overlap, so you end up with one node for each character in every suggestion
If l is the length of longest word suggestion then Time complexity will be O(n*l) where n is number of words in Trie

Space Complexity: same way like time complexity we need to travel all the word character by character in worst case. So space complexity will also be O(n*l)