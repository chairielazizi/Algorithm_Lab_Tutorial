import random

list=[1,2,3,4,5,6,7,8,9]
rand=random.choice(list)

num=input("Guess a number between 1 to 9:")

if num==rand:
    print("You got it right!")
if num<rand:
    print("You guessed too low")
else:
    print("You guessed too high")