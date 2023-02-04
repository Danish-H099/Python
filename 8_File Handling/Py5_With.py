#The best way to open and close a file automatically is using "WITH" keyword

with open("demo.txt","r") as f:
    a=f.read()
print(a)