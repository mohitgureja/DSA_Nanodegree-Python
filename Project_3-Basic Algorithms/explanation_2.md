Search in a Rotated Sorted Array:

To find a element in rotated sorted array about a pivot element, i have used a recursive approach. First I have to find mid element of the list. There are two cases:
Case 1: If array before mid number is sorted array
	if number lies in between the sorted first half array recursively call the first half array else if number lies in second half array, recursively call the second array.
Case 2: If second half array is already sorted
	if number lies in between the sorted second half array, recursively call the second half array else if number lies in first half array, recursively call the first half array.
	
Time Complexity : As we are removing one half of the numbers at each recursive call. So time complexity will be O(logn)
Space Complexity: As we are not using any extra data structure with respect to input. So Space complexity will be constant i.e O(1)