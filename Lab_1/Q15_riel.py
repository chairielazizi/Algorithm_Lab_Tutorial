import string
import random

letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation

def get_length():
    length = input("How long do you want for your password?")
    return int(length)

def password_generator(length):

    pw = f"{letters}{digits}{punctuation}"

    # convert to list and shuffle
    pw = list(pw)
    random.shuffle(pw)

    random_pass = random.choices(pw,k=length)
    random_pass = ''.join(random_pass)
    return random_pass

# option = 0

while True:
    length = get_length()
    if(length == 0):
        break
    print(password_generator(length))
