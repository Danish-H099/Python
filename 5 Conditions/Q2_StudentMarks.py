#WAP to find wheather a student is pass or fail by checking his marks in three subject
#if he requires total 40% and atleast 33% in each subject to pass 

phy=int(input("Enter the Marks in Physics :"))
che=int(input("Enter the Marks in Chemistry :"))
math=int(input("Enter the Marks in maths :"))

total=phy+che+math
per=total/3

if(total>40 and phy>=33 and che>=33 and math>=33):
    print("Your are Pass")
else:
    print("You are Fail")