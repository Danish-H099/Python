# WAP to read text from a file poem.txt and check wheather it contains the work twinkle or not
data=True
i=0
f=open("poem.txt")
while data:
    data=f.readline()
    i=i+1
    if "diamond" in data:
        print("Yes it is present in the file in line number ",i)
    
f.close()