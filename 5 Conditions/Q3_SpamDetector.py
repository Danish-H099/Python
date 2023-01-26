#WAP to detect spam msgs entered by the user
msg=input("Enter Your msg :")

spam=False

if("idiot" in msg):
    spam=True
elif("buy" in msg):
    spam=True
elif("shit" in msg):
    spam=True

if(spam):
    print("This is spam msg")
else:
    print("This isn't spam")
