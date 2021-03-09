import random

print("Can you guess the number that I'm thinkking right now?")

secret_number = random.randint(1,10)

for i in range(6):
    your_guess = input("Enter your guess:")
    # print(secret_number)
    if(i == 5):
        print("Nope, the secret number is "+str(secret_number))
    else:
        if(int(your_guess) < secret_number):
            print("It is too low")
        elif(int(your_guess) > secret_number):
            print("It is too high")
        elif(int(your_guess) == secret_number):
            print("You are correct!")
            break