Rearrange Array Elements:

To find the numbers whose sum will be maximum we first have to sort the numbers.
We have sorted the input list first using merge sort in descending order and then traverse the sorted list and maximum sum will be combination of digits of all even index numbers and all odd index numbers.
So i have appended numbers on all even indexes in first number and appended numbers on all odd indexes in second number.
The sum of this first number and second number will be maximum

Time Complexity: As we are using merge sort so complexity of merge sort will be O(nlogn) then we are traversing each number in input list.
So overall complexity will be : O(nlogn) + O(n) => O(nlogn)  (For very large numbers n can be ignored, it will be order of nlogn)

Space Complexity: During merging we have used list data structure to store merged items. Lets say total elements be n So space complexity will be O(n). For rest all operations space complexity will be constant.
So overall space complexity will be O(n) + O(1) =>  O(n)