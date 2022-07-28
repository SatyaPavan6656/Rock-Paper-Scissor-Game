print("\t\t\t\tWELCOME TO ROCK,PAPER and SCISSOR GAME")
print("\t\t\t\t--------------------------------------")
print("Enter Your Choice(in lowercase letters only):")
print("Rock or Paper or Scissor")
a=str(input())
b=a.lower()
k=["rock","paper","scissor"]
score=0
import random
j=random.choice(k)
if k==b:
    print(f"{k} and {b} are same.")
    print("It's a Tie")
elif a=="rock":
    if j=="scissor":
        score+=5
        print("Rock Smashes Scissor.!!!YOU WON!!!")
        print("Score:",score)
    else:
        print("Paper can Wrap a Rock.!!!YOU LOSE!!!")
        print("Score:",score)
elif a=="paper":
    if j=="rock":
        score+=5
        print("Paper Can wrap a Rock.!!!YOU WON!!!")
        print("Score:",score)
    else:
        print("Scissor can cut a paper.!!!YOU LOSE!!!")
        print("Score:",score)
elif a=="scissor":
    if j=="paper":
        score+=5
        print("Scissor can cut a paper.!!!YOU WON!!!")
        print("Score:",score)
    else:
        print("Rock Smashes a Scissor.!!!YOU LOSE!!!")
        print("Score:",score)
