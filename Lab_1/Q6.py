def palindrome(str):
    #loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        # if(str[i] != int(len(str)-i-1)):
        if(str[i] != str[len(str)-i-1]):
            return False
        return True

def check(str):
    word = str
    str = palindrome(str)
    if(str):
        print("Yes,"+word+" is a palindrome")
    else:
        print("No,"+word+" is not a palindrome")

string = input("Enter a word: ")

check(string)
