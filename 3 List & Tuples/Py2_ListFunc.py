a=[2,8,9,3,1,6,5]

# Lenght of the List
l=len(a)
print(l) # op-> 7

# Count frequency of an element
x=a.count(2)
print(x) # op-> 1

# Sorting of List
b=a.sort()
print(a) # op-> [1, 2, 3, 5, 6, 8, 9] so a.sort() sorts the a only
print(b) # op-> returns None

# Reversing of List
a.reverse()
print(a) # op-> [9, 8, 6, 5, 3, 2, 1]

# Append Method -> add element in the end of list
a.append(7)
print(a) #op-> [9, 8, 6, 5, 3, 2, 1, 7]

# Insert Method
a.insert(3,11) # insert 11 at index 3
print(a) # op-> [9, 8, 6, 11, 5, 3, 2, 1, 7]

# Pop Method
a.pop(2) # delete elemeent from index 2
print(a) # op->[9, 8, 11, 5, 3, 2, 1, 7]

# Remove Method 
a.remove(9) # removes 9 from the list 
print(a) # op->[8, 11, 5, 3, 2, 1, 7]
