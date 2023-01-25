#String declation and printing
a="danish's"
b='have you not "been" listening.'
c='''not "today" cause i have got so'os much to give you'''
print(a)
print(b,c)

#String Cancatenation
a="Hey "
b="Danish"
c=a+b
print(c)

#String Slicing
a="Danish Hussain"
print(a[4]) #-> gives the 5th letter of string a
# if we want to take a range of elements of string then we use slicing
print(a[2:8])#-> gives the string from index 2 to 7 yes last one gets excluded
print(a[:5]) #-> same as print(a[0:4])
print(a[2:]) #-> takes whole string from index 3 to the end
#To print the string in reverse order, we use negative index
print(a[-6:-1])#-> same is print(a[8:13])
print(a[0:5:2])#->print 0 to 5 and read one and skip one letter