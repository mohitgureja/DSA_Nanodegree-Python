def sort_012(input_list):
    zero_index = 0
    two_index = len(input_list)-1
    pointer = 0

    # Sort 0 and 2 for its positions upto when pointer is less than or equal to 2's position 
    while pointer <= two_index :
        # if next number is 0 swap the number at 0's position with it and increase 0's index 
        if input_list[pointer] == 0:
            input_list[pointer] = input_list[zero_index]
            input_list[zero_index] = 0
            zero_index += 1
            pointer += 1
        # if next number is 2 swap the number at 2's position with it and decrease 2's index
        elif input_list[pointer] == 2:
            input_list[pointer] = input_list[two_index]
            input_list[two_index] = 2
            two_index -= 1
        else:
            pointer += 1

    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# Test Cases
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])
test_function([2, 1, 0, 0])
test_function([0, 1, 2])