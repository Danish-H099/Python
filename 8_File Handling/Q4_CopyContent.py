with open('demo.txt') as f:
    content=f.read()
with open("copy.txt","w") as g:
    g.write(content)