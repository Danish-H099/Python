def greatest(a,b,c):
    if(a<b and b<c):
        print(c," is largest")
    elif(a<b and c<b):
        print(b," is largest")
    else:
        print(a," is largest")
        
a=int(input("Enter the number 1 :"))
b=int(input("Enter the number 2 :"))
c=int(input("Enter the number 3 :"))

greatest(a,b,c)


    