# and,or & not are the logical operators in python

age=int(input("Enter Your age :"))
if(age>22 and age<58):
    print("You can drive")
else:
    print("You can't drive")

if(age<=22 or age>=58):
    print("You aren't suitable for this")

if not(age!=22):
    print("age is 22")



