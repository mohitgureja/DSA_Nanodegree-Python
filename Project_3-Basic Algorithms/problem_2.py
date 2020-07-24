def search(input_list, lower, higher, number):
    mid = (lower + higher)//2
    # if mid element is the number
    if input_list[mid] == number: 
        return mid
    
    if lower == higher :
        return -1

    # if array before mid number is sorted array
    if input_list[mid] >= input_list[lower]:

        # if number lies in between the sorted first half array recursively call the first half array
        if number < input_list[mid] and number >= input_list[lower]:
            return search(input_list, lower, mid-1, number)
        # else number lies in second half array, recursively call the second array 
        else:
            return search(input_list, mid+1, higher, number)
    # else second half array is already sorted
    else:
        # if number lies in between the sorted second half array, recursively call the second half array
        if number > input_list[mid] and number <= input_list[higher]:
            return search(input_list, mid+1, higher, number)
        # else number lies in first half array, recursively call the first half array 
        else:
            return search(input_list, lower, mid-1, number)

def rotated_array_search(input_list, number):
    if len(input_list) == 0:
        return -1
    return search(input_list, 0, len(input_list)-1, number)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    print (linear_search(input_list, number))
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

#Test Cases

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[ 2, 3, 4, 6, 7, 8, 1], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], 1])
test_function([[2], 1])