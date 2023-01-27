# Factorial using recursive function

def FactRecursion(n):
    if n==1 or n==0:
        return 1
    return FactRecursion(n-1)*n
n=int(input("Enter the Number :"))
fact=FactRecursion(n)
print(fact)