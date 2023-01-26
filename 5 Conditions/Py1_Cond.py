# if-elif-else Ladder
a=11

if (a>13): # Parenthesis are optional
    print("greater than 13") # Indention in this line is important in Python otherwise 
    # you will get error as soon as you run this code
elif(a>9):
    print("greater than 9 but smaller than 14")
else:
    print("Smaller than 10")

# if in if -Multiple indentation
if a<=10:
    if a==9:
        print("Number is 9")
    else:
        print("Number isn't 9")
else:
    print("Number is greater than 10")
