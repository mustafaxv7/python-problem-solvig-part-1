#programm of guessing game you have to guess the right number to get points
from random import randint
numberR = randint(1,30)
points = 0
count = 0
while count < 5:
    numberG = int(input("Guess The Right Number>>: ")) 
    if (numberG == numberR):
        print("\nGot It")
        print("\t\t\t+1p\n")
        points+=1
    else:
        print("\nOps Try Again!")
        if(numberG > numberR):
            print("\nmuch bigger")
        else:print("\nmuch lower")
        print("\t\t\t+0p\n")
    count+=1
print(f"\nYou Got {points} point\n")
print(f"The number was: {numberR}\n")