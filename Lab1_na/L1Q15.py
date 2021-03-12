import string
from random import *

def generate():
    pwd=string.ascii_letters+string.digits+string.punctuation
    strong_pwd ="".join(choice(pwd) for x in range(randint(8, 12)))
    print ("Your password: %s\n"%strong_pwd)

while True:
    opt=input("Do you want to generate new password?\n1-Yes\n2-No\n")
    if opt==1:
        generate()
    else:
        break