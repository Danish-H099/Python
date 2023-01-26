#WAP to find the greatest of four numbers

a1=int(input("Enter the number1 :"))
a2=int(input("Enter the number2 :"))
a3=int(input("Enter the number3 :"))
a4=int(input("Enter the number4 :"))

if(a1>a2):
    s1=a1
else:
    s1=a2

if(a3>a4):
    s2=a3
else:
    s2=a4

if s1>s2:
    print(s1," is the largest Number")
else:
    print(s2," is the largest number")