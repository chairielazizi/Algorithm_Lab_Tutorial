
def check_odd(num):
    if (num % 2 == 0):
        print(str(num)+ " is an even number")
    else:
        print(str(num) + " is an odd number")


number = input("Enter a number: ")

check_odd(int(number))