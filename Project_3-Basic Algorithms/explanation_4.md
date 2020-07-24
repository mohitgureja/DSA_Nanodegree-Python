Dutch National Flag Problem:

To sort 0, 1 and 2 in single traversal, we need to sort only 0's and 2's to their positions, it will automatically sort the list of 0,1 and 2's.
We will sort 0 and 2 for its positions upto when pointer is less than or equal to 2's position.
Start the pointer, if next number is 0 swap the number at 0's position with it and increase 0's index and if next number is 2 swap the number at 2's position with it and decrease 2's index.
We will have sorted list at the last iteration.

Time Complexity: Since we are having only one complete traversal so in the worst case complexity can go upto total items in the list i.e n.
So overall time complexity will be O(n)

Space complexity: Since we are not using any other data structure in our method other than input list. So our space complexity will be constant.
So Overall space complexity will be O(n)