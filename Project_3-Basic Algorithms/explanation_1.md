Square root of an integer:

To find the floored square root i have used recursive approach, First i have to find average of two boundary numbers, then there will be 3 cases:
Case 1:
    if square of average number itself is square root set maxFloorValue and return
Case 2:
    if average number is greater than the number recurse to the first half of the numbers
Case 3:
    if average number is less than the number set maxFloor value with average number and maxPerfectSquare with average square.
    Here we have to recurse to the second half whether any number exist whose square is greater than earlier set average square.

Time Complexity: As we are removing one half of the numbers at each recursive call. So time complexity will be O(logn)
Space Complexity: As we are not using any extra data structure with respect to input. So Space complexity will be constant i.e O(1)