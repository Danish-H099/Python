# Snake is killed by gun  S>G
# Gun drowns in water     G>W
# Snake can hide in water s<W

def game(c,p):
    if(c=="s" and p=="g"):
        print("You won!")
    elif(c=="g" and p=="s"):
        print("You lost!")
    elif(c=="g" and p=="w"):
        print("You won!")
    elif(c=="w" and p=="g"):
        print("You lost!")
    elif(c=="s" and p=="w"):
        print("You lost")
    elif(c=="w" and p=="s"):
        print("You won!")
    else:
        print("Draw!")
    print("Computer's choice",c)

import random
a=random.randint(1,3) # Generate random number from 1,2,and 3 

while(True):
    a=random.randint(1,3) # Generate random number from 1,2,and 3 
    player=input("Enter Your choice : Snake(s) , Gun(g), and Water(w) :")
    if a==1:
        comp="s"
    elif a==2:
        comp="w"
    else:
        comp="g"
    game(comp,player)
    c=int(input("Do you want to play  again?? 1->Yes and 0->No :"))
    if(c==0):
        break

