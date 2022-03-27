#Snake water gun game
import random
print("Welcome to Snake-Water-Gun Game: ")
user=int(0)
comp=int(0)
chances=int(10)
print("s: Snake\t w:Water\t g:Gun\n")
lst=['s','w','g']
while chances>0:
    cch=random.choice(lst)
    uch=input("Enter your choice from: s,w or g")
    if cch=='s' and uch=='g':
        user+=1
        print("You win")
    elif cch=='g' and uch=='s':
        comp+=1
        print("Computer wins")
    elif cch=='s' and uch=='w':
        comp+=1
        print("Computer wins")
    elif cch=='w' and uch=='s':
        user+=1
        print("you won")
    elif cch=='w' and uch=='g':
        comp+=1
        print("Computer won")
    elif cch=='g' and uch=='w':
        user+=1
        print("User won")
    elif cch==uch:
        print("Draw round: no score given")
    else:
        print("Invalid choices")
    chances-=1
if chances==0:
    print("Game over:\n Results:\t")
    if comp>5:
        print("Computer has won", comp," rounds:\t Hence computer winner")
    elif user>5:
        print("User has won", user," rounds:\t Hence user is the winner")
    else:
        print("Match tied")
print("Thank you for playing Snake water gun game :)")

    

    

