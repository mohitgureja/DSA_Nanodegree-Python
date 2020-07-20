class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    head_l1 = llist_1.head
    head_l2 = llist_2.head
    hash_set = set()
    while head_l1:
        hash_set.add(head_l1.value)
        head_l1 = head_l1.next

    while head_l2:
        hash_set.add(head_l2.value)
        head_l2 = head_l2.next

    result_list = LinkedList()
    for item in hash_set:
        result_list.append(item)
    return result_list

def intersection(llist_1, llist_2):
    head_l1 = llist_1.head
    head_l2 = llist_2.head
    hash_map = dict()
    while head_l1:
        hash_map[head_l1.value] = 1
        head_l1 = head_l1.next

    while head_l2:
        if head_l2.value in hash_map.keys():
            hash_map[head_l2.value] += 1
        head_l2 = head_l2.next

    result_list = LinkedList()
    for key in hash_map.keys():
        if (hash_map[key] > 1):
            result_list.append(key)
    return result_list

print (f'**** TestCase 1 ****\n')
# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# Prints: 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 
print (intersection(linked_list_1,linked_list_2))
# Prints: 4 -> 6 -> 21 -> 

print (f'\n**** TestCase 2 ****\n')
# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# Prints: 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
print (intersection(linked_list_3,linked_list_4))
#Prints: nothing as there is no intersecting element

print (f'**** TestCase 3 ****\n')
# Test Case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1,7,8,9,11,21,1]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
# Prints: 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
print (intersection(linked_list_5,linked_list_6))
# Prints: 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->

print (f'\n**** TestCase 4 ****\n')
# Test Case 4

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_7,linked_list_8))
# Prints: Blank string (as list is empty)
print (intersection(linked_list_7,linked_list_8))
# Prints: Blank string (as list is empty)