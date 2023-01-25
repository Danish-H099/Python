
name=input("Enter Your name:")
date=input("Enter Date:")

print("Dear",name,"\nyou are selected\n",date)

#OR

a='''\nDear <name>
Your are Selected
<date>'''
a=a.replace("<name>",name)
a=a.replace("<date>",date)
print(a)