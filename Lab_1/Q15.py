import random
import string


def main():
    charlow=string.ascii_lowercase
    charhigh=string.ascii_uppercase
    dig=string.digits
    punc=string.punctuation
    a=""

    for i in range(4):
        a += random.choice(charlow)
        a += random.choice(charhigh)
        a += random.choice(dig)
        a += random.choice(punc)

    return a






if __name__ == "__main__":
    pas = main()
    print("Your password is ",pas)