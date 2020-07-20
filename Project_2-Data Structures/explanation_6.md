Union and Intersection:

For Union method, i have used set() data structure and started adding all the nodes of both first and second linked list. Due to hashing property set only stores one element with same value, So At last set will have union of both lists.
Let's say n be total number of elements including both lists.
So Time Complexity for Union will be : O(n)

Space Complexity : Since we are using set() so Space complexity of using set can be length of list 1 + length of list 2. Let's say n be total number of elements including both lists. In the same way to form a union linked list 
Space complexity will be length of list 1 + length of list 2
So Overall Space complexity will be order of n : O(n)

For Intersection method, i have used dictionary data structure to store linked list element as key and its occurence count as value
First, We will iterate for each element of list 1 and add them in dictionary with value count 1, next we will iterate over second list and check if the list item is already there in dictionary then we will increase its count.
For all the items in dictionary whose count will be more than 1 will be the intersection list, Let's say n be total number of elements including both lists.
So Time Complexity for intersection will be: O(n)

Space complexity : We have used one dictionary for which total items can go upto length of list 1 + length of list 2,. Let's say n be total number of elements including both lists. Next we have made Linked list for intersection which will be the maximum of length of both list's length.
So Overall Complexity will be order of n: O(n)