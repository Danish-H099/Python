# while renaming we copy content of a file to another file and delete present one
import os 
oldname="demo.txt"
newname="demo1.txt"
with open(oldname) as f:
    content=f.read()
with open(newname,"w")as g:
    g.write(content) # this copies the content to another file 

os.remove(oldname) # way to delete a file in python