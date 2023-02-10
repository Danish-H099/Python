# game is function which lets a user to play a game and returns his score
# if score of user is highest then we update the file which stores highest score
def game():
    return 533

Myscore=game()
with open("Gamescore.txt") as f:
    hscore=int(f.read())
# hscore=int(hscore)
if Myscore>hscore:
    with open("Gamescore.txt","w") as f:
        f.write(str(Myscore))
    print("Congrats! This is highest score of this game ",Myscore)
else:
    print("Better luck next time and your score is ",Myscore)
