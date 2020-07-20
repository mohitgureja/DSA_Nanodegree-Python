Active Directory

To complete the method is_user_in_group, i have used recursive approach.
Base case will be if user exists in that particular group's users return True.

For each group in list of groups, call recursively for the same method and returns the approach

Time Complexity : 
Worst case complexity for searching an element in list is number of users i.e u
for each group we need to search in its users list so total iterations will be number of groups i.e n
So Worst case complexity : O(n*u)

Space Complexity: 
Let total number of groups be g.
Let max number of users in each group be u.
So total space complexity will be O(u*g)