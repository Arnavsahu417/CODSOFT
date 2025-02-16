import random

choice=["rock","paper","scissors"]
a=input("choose rock ,paper, or scissors ")
comp=random.choice(choice)

print("computer chose ",comp)

if (a=="rock" and comp=="rock"):
    print("draw")
elif(a=="rock" and comp=="paper"):
    print("you lose")
elif(a=="rock" and comp=="scissors"):
    print("you win")
 

if (a=="paper" and comp=="paper"):
    print("draw")
elif(a=="paper" and comp=="scissors"):
    print("you lose")
elif(a=="paper" and comp=="rock"):
    print("you win")

if (a=="scissors" and comp=="scissors"):
    print("draw")
elif(a=="scissors" and comp=="rock"):
    print("you lose")
elif(a=="scissors" and comp=="paper"):
    print("you win")

if a not in choice:
    print("you lose as you chose nothing")
   
