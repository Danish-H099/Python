a={1,2,3,4,5,(1,2,3)}

#Add method
a.add(11) 
print(a) #op-> {1, 2, 3, 4, 5, 11, (1, 2, 3)}
#Lenght method
print(len(a)) #op-> 7

#Remove Method
a.remove(1)
print(a) #op->{2, 3, 4, 5, 11, (1, 2, 3)}
#If you remove an element which isn't present in the set then it will throw an error

#Pop Method - Removes an first Element from the set and return the removed element
b=a.pop()
print(a)
print(b)

#Clear Method - Make Your Set Empty 
a.clear()
print(a) #-> set()

#Union Method - returns a new set from which is union of both of the sets
a={1,2,3}
b=a.union({3,4,5})
print(b) #-> {1, 2, 3, 4, 5}

#Intersection Method - returns a new set having intersecting elements of both the sets
c=b.intersection(a)
print(c) #-> {1, 2, 3}


