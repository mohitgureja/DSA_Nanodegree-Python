def sqrt(number):
	# if number is 1 return 1 as the number 1 is square of itself 
    if (number == 1):
    	return 1

    # set globally max perfect square value and max Floor value to 0 
    global maxSquareValue
    maxSquareValue = 0
    global maxFloorValue
    maxFloorValue = 0

    def findSqrt(number,start,end):
    	#  if only one number remains return the maxFloorValue
    	if start == end:
    		return

    	global maxSquareValue
    	global maxFloorValue

    	# find average of two boundary numbers
    	mid = (end + start)//2
    	midSquare = mid*mid

    	"""
    	Case 1:
    	if square of average number itself is square root set maxFloorValue and return

    	Case 2:
    	if average number is greater than the number recurse to the first half of the numbers

    	Case 3:
    	if average number is less than the number set maxFloor value with average number and maxPerfectSquare with average square.
    	Here we have to recurse to the second half whether any number exist whose square is greater than earlier set average square.  
    	"""
        # Case 1
    	if midSquare == number:
    		maxFloorValue = mid
    		return
        # Case 2
    	elif midSquare > number:
    		findSqrt(number,start,mid)
        # Case 3
    	else:
    		if midSquare > maxSquareValue:
    			maxSquareValue = midSquare
    			maxFloorValue = mid
    		findSqrt(number,mid+1,end)

    findSqrt(number,0,number)
    return maxFloorValue

# Tese Cases

print ("Pass" if  (3 == sqrt(9)) else "Fail")
# Perfect square of 3
print ("Pass" if  (0 == sqrt(0)) else "Fail")
# Prints 0
print ("Pass" if  (4 == sqrt(16)) else "Fail")
# Perfect square of 4
print ("Pass" if  (1 == sqrt(1)) else "Fail")
# Square of 1 is 1
print ("Pass" if  (26 == sqrt(676)) else "Fail")
# Perfect square of 26
print ("Pass" if (26 == sqrt(700)) else "Fail" )
# Floored square root of 700 is also 26
print ("Pass" if (100000 == sqrt(10000000008)) else "Fail" )
# Floored square root of 10000000008 will be 100000
