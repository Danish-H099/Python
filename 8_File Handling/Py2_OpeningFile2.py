f=open('demo.txt','r')
data=f.readline() # reads first line of file
print(data)
data=f.readline() # reads second line of file
print(data)
f.close()