import random

def get_min_max(ints):
	size = len(ints)

	if size == 0:
		return -1 

	min = ints[0]
	max = ints[0]

	if size == 1:
		return (min, max)

	elif  size == 2 :
		if (ints[0] <= ints[1]):
			max = ints[1]
		else:
			max = ints[0]
			min = ints[1]
		return (min, max)
	else:

		for i in range (2,size):

			if ints[i] > max:
				max = ints[i]
			if ints[i] < min:
				min = ints[i]
		return (min, max)


#Test Cases

# Test Case 1
## Example Test Case of Ten Integers
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Test case 2
print ("Pass" if ((-1) == get_min_max([])) else "Fail")

# Test Case 3
print ("Pass" if ((1, 1) == get_min_max([1])) else "Fail")

# Test Case 4
print ("Pass" if ((0, 9) == get_min_max([9, 0])) else "Fail")

# Test Case 5
l = [i for i in range(2, 100000)]  # a list containing 2 - 100000
random.shuffle(l)
print ("Pass" if ((2, 99999) == get_min_max(l)) else "Fail")