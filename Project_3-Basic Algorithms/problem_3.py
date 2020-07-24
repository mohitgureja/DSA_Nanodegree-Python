def rearrange_digits(input_list):
    if len(input_list) == 0 or len(input_list) == 1:
        return input_list
    # Sort the input list first using merge sort in descending order
    input_list = mergesort(input_list)
    result = []
    first_num = ""
    second_num = ""
    # traverse the sorted list and maximum sum will be combination of digits of all even index numbers and all odd index numbers
    for i in range(0,len(input_list)):
    #  append numbers on all even indexes in first number
        if i % 2 == 0:
            first_num += str(input_list[i])
        #  append numbers on all odd indexes in second number
        else:
            second_num += str(input_list[i])
    result.append(int(first_num))
    result.append(int(second_num))
    return result

def mergesort(input_list):

    if len(input_list) <= 1:
        return input_list
    
    mid = len(input_list) // 2
    left = input_list[:mid]
    right = input_list[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    # Merge in descending order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    print (output)
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

#Test Cases 
test_function([[1, 2, 3, 4, 5], [531, 42]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[],[]])
test_function([[1],[1]])
test_function([[1,2],[2,1]])