File Recursion:

Data Structure used in this problem is list() since it is easier and efficient to use basic operations in list.
As shown in the code i have tried to traverse each file in directory or subdirectory recursively and if file matches with the suffix it is to be appended in the output list and return the output if depth of the directory is traversed.

Complexity:

Since all the operations in get_files method are of constant time, even replace and join method will be constant because of constant string length. and we are recursively traversing to the depth of the directory. Lets say depth of directory be n. So Time complexity will be order of n (taking rest of operations as constant)

Time Complexity: O(n)

Space complexity will also be O(n) as list can store values upto depth of directory