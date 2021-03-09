number = input("Enter a number: ")

def prime(n):
    if(n>1):
        for i in range(2, int(n/2)+1):
            if(n %i == 0):
                return False
            return True

def check(n):
    res = prime(n)
    if(res):
        print(str(n)+" is a prime number")
    else:
        print(str(n)+" is not a prime number")

# prime(int(number))
check(int(number))