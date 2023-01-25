# Python List are containers which can store values of any data type
a=[1,"Danish",1.55,True,'f']

print(a)# op-> [1,"Danish",1.55,True,'f']

#printing elements at a specific index
print (a[2]) # op->1.55 it basically gives the element at index 2

#Changing the value of elements using index
a[0]="Hi"
print(a)# op->["Hi","Danish",1.55,True,'f']

#List Slicing
print(a[0:3]) # op-> ['Hi', 'Danish', 1.55]
print(a[-3:]) # op-> [1.55, True, 'f']

