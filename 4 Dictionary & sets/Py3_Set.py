# set is the collection of non repetitive items
# Sets are unordered and unindexable
a={1,3,7,4,"3","a"}
print(a) #op-> {'3', 1, 3, 4, 7, 'a'} even if some element are repeating then also it prints the dincinct ones
print(type(a)) #op-><class 'set'>

#Syntax to create an empty set
b=set() #b={} creates an empty dictionary

#Add Method
b.add(44)
b.add(33)
b.add(33.0) #33.0 value is considered as 33 so till now only 2 elements are in the set
b.add((1,2,3))# Tuple can be added to set but list n dictionary, nope
print(b) # op-> {33, (1, 2, 3), 44}


