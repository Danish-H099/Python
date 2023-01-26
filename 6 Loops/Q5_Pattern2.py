''' print pattern                 *
                                 * *
                                * * *                   '''
n=int(input("Enter the number of rows you want :"))
for i in range(n):
    print(" "*(n-i-1), end="")
    print("*" *(2*i+1), end="")
    print(" "*(n-i-1))
