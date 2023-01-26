# WAP to print Multiplication Table of a number
a=int(input("Enter the number whose table you want :"))
for i in range(10):
    print(a,"*",i+1,"=",a*(i+1))

# we use f string to do the same in simple way 
# we put a variable in curly braces 
# print(f"{a}*{i}={a*i}) gives the same table 