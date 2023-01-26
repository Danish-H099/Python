# A for loop is used to iterate through the sequence like list,tuples,or strings

a=["Apple","Mango","Orange","Banana"]

for item in a:
    print(item) # Apple Mango orange Banana

#for loop with else (optional)
#its used to run code when the for is exhausted i.e run completely

for item in a:
    print(item)
else:
    print("Done!")