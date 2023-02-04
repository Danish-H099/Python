# opening and displaying content of a file 

f=open('demo.txt','r') #Even if you don't specify the mode it takes read mode bydefault
data=f.read()
#data=f.read(5) -> reads first 5 characters from file
print(data)
f.close()


